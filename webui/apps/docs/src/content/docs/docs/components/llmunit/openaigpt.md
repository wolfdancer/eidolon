---
title: OpenAIGPT
description: Description of the OpenAIGPT component
---

| Property                                                 | Pattern | Type                               | Deprecated | Definition | Title/Description        |
| -------------------------------------------------------- | ------- | ---------------------------------- | ---------- | ---------- | ------------------------ |
| + [implementation](#implementation )                     | No      | const                              | No         | -          | Implementation           |
| - [model](#model )                                       | No      | [Reference[LLMModel]](/docs/components/llmmodel/overview)                | No         | -          | -                        |
| - [temperature](#temperature )                           | No      | number                             | No         | -          | Temperature              |
| - [force_json](#force_json )                             | No      | boolean                            | No         | -          | Force Json               |
| - [max_tokens](#max_tokens )                             | No      | integer                            | No         | -          | Max Tokens               |
| - [supports_system_messages](#supports_system_messages ) | No      | boolean                            | No         | -          | Supports System Messages |
| - [can_stream](#can_stream )                             | No      | boolean                            | No         | -          | Can Stream               |
| - [client_args](#client_args )                           | No      | object                             | No         | -          | Client Args              |
| - [connection_handler](#connection_handler )             | No      | [Reference[OpenAIConnectionHandler]](/docs/components/openaiconnectionhandler/overview) | No         | -          | -                        |

## <a name="implementation"></a>1. Property `implementation`

**Title:** Implementation

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"OpenAIGPT"`

## <a name="model"></a>2. Property `model`

|              |                                                              |
| ------------ | ------------------------------------------------------------ |
| **Type**     | [`Reference[LLMModel]`](/docs/components/llmmodel/overview)                                        |
| **Required** | No                                                           |
| **Default**  | `{"implementation": "eidolon_ai_sdk.apu.llm_unit.LLMModel"}` |

## <a name="temperature"></a>3. Property `temperature`

**Title:** Temperature

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0.3`    |

## <a name="force_json"></a>4. Property `force_json`

**Title:** Force Json

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

## <a name="max_tokens"></a>5. Property `max_tokens`

**Title:** Max Tokens

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `null`    |

## <a name="supports_system_messages"></a>6. Property `supports_system_messages`

**Title:** Supports System Messages

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

## <a name="can_stream"></a>7. Property `can_stream`

**Title:** Can Stream

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

## <a name="client_args"></a>8. Property `client_args`

**Title:** Client Args

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |

## <a name="connection_handler"></a>9. Property `connection_handler`

|              |                                      |
| ------------ | ------------------------------------ |
| **Type**     | [`Reference[OpenAIConnectionHandler]`](/docs/components/openaiconnectionhandler/overview) |
| **Required** | No                                   |
| **Default**  | `null`                               |

----------------------------------------------------------------------------------------------------------------------------
