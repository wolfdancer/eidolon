from __future__ import annotations

import copy
import typing
from abc import ABC, ABCMeta
from dataclasses import dataclass

import jsonref
from jsonschema.validators import validate
from pydantic import BaseModel, TypeAdapter
from typing import Dict, List, AsyncIterator, Coroutine

from eidolon_ai_sdk.apu.call_context import CallContext
from eidolon_ai_sdk.apu.llm_unit import LLMCallFunction
from eidolon_ai_sdk.apu.processing_unit import ProcessingUnit
from eidolon_ai_client.events import (
    ObjectOutputEvent,
    BaseStreamEvent,
    StringOutputEvent,
    ToolCall,
)
from eidolon_ai_sdk.system.fn_handler import register_handler, FnHandler, get_handlers
from eidolon_ai_client.util.logger import logger
from eidolon_ai_sdk.system.tool_builder import ToolBuilder


@dataclass
class LLMToolWrapper:
    logic_unit: LogicUnit
    llm_message: LLMCallFunction
    eidolon_handler: FnHandler
    input_model: typing.Type[BaseModel]

    async def execute(self, tool_call: ToolCall) -> AsyncIterator[BaseStreamEvent]:
        logger.info("calling tool " + self.eidolon_handler.name)
        logger.debug("args: " + str(tool_call.arguments) + " | fn: " + str(self.eidolon_handler.fn))

        # if this is a sync tool call just call execute, if it is not we need to store the state of the conversation and call in memory
        input_model = self.eidolon_handler.input_model_fn(self.logic_unit, self.eidolon_handler)
        if isinstance(input_model, type) and issubclass(input_model, BaseModel):
            kwargs = dict(input_model.model_validate(tool_call.arguments))
        elif isinstance(input_model, dict):
            validate(tool_call.arguments, input_model)
            kwargs = copy.deepcopy(tool_call.arguments)
        else:
            raise ValueError("input_model must be a BaseModel or a dict")
        # passing in self is workaround for legacy logic units.
        result = self.eidolon_handler.fn(self.logic_unit, **kwargs)
        if isinstance(result, Coroutine):
            result = await result

        if isinstance(result, typing.AsyncIterable):
            async for event in result:
                yield event
        else:
            model = TypeAdapter(type(result))
            result = model.dump_python(result)
            if isinstance(result, str):
                yield StringOutputEvent(content=result)
            else:
                yield ObjectOutputEvent(content=result)

    @classmethod
    async def from_logic_units(
        cls, call_context: CallContext, logic_units: List[LogicUnit]
    ) -> Dict[str, LLMToolWrapper]:
        acc = {}
        for logic_unit in logic_units:
            for handler in await logic_unit.build_tools(call_context):
                new_name = logic_unit.__class__.__name__ + "_" + handler.name
                i = 0
                while new_name in acc:
                    new_name = logic_unit.__class__.__name__ + "_" + handler.name + "_" + str(i)
                    i += 1
                input_model = handler.input_model_fn(logic_unit, handler)
                if isinstance(input_model, type) and issubclass(input_model, BaseModel):
                    schema = copy.deepcopy(
                        jsonref.replace_refs(
                            input_model.model_json_schema(),
                            jsonschema=True,
                        )
                    )
                    del schema["title"]
                elif isinstance(input_model, dict):
                    schema = input_model
                else:
                    raise ValueError("input_model must be a BaseModel or a dict", input_model)
                acc[new_name] = LLMToolWrapper(
                    logic_unit=logic_unit,
                    llm_message=LLMCallFunction(
                        name=new_name,
                        description=handler.description(logic_unit, handler),
                        parameters=schema,
                    ),
                    eidolon_handler=handler,
                    input_model=input_model,
                )
        return acc


def llm_function(
    name: str = None,
    title: str = None,
    sub_title: str = None,
    description: typing.Optional[typing.Callable[[object, FnHandler], str]] = None,
    input_model: typing.Optional[typing.Callable[[object, FnHandler], BaseModel]] = None,
    output_model: typing.Optional[typing.Callable[[object, FnHandler], typing.Any]] = None,
):
    extra = {}
    if title:
        extra["title"] = title
    if sub_title:
        extra["sub_title"] = sub_title
    return register_handler(
        name=name, description=description, input_model=input_model, output_model=output_model, **extra
    )


class LogicUnitMeta(ABCMeta):
    def __subclasscheck__(cls, subclass):
        if issubclass(subclass, ToolBuilder) and cls is LogicUnit:
            return True
        return super().__subclasscheck__(subclass)


class LogicUnit(ProcessingUnit, ABC, metaclass=LogicUnitMeta):
    async def build_tools(self, call_context: CallContext) -> List[FnHandler]:
        handlers = get_handlers(self)
        for handler in handlers:
            if "title" not in handler.extra:
                handler.extra["title"] = self.__class__.__name__
            if "sub_title" not in handler.extra:
                handler.extra["sub_title"] = handler.fn.__name__
            handler.extra["agent_call"] = False

            return handlers
