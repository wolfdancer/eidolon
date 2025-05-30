---
title: APIAgent
description: Description of the APIAgent component
---

**Description:** An Agent that can call rest endpoints documented via OpenAPI (Swagger).

| Property                                         | Pattern | Type    | Deprecated | Definition | Title/Description    |
| ------------------------------------------------ | ------- | ------- | ---------- | ---------- | -------------------- |
| + [implementation](#implementation )             | No      | const   | No         | -          | Implementation       |
| + [title](#title )                               | No      | string  | No         | -          | Title                |
| + [root_call_url](#root_call_url )               | No      | string  | No         | -          | Root Call Url        |
| + [open_api_location](#open_api_location )       | No      | string  | No         | -          | Open Api Location    |
| + [operations_to_expose](#operations_to_expose ) | No      | array   | No         | -          | Operations To Expose |
| - [extra_header_params](#extra_header_params )   | No      | object  | No         | -          | Extra Header Params  |
| - [extra_query_params](#extra_query_params )     | No      | object  | No         | -          | Extra Query Params   |
| - [max_response_size](#max_response_size )       | No      | integer | No         | -          | Max Response Size    |

## <a name="implementation"></a>1. Property `implementation`

**Title:** Implementation

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"APIAgent"`

## <a name="title"></a>2. Property `title`

**Title:** Title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Title of the API

## <a name="root_call_url"></a>3. Property `root_call_url`

**Title:** Root Call Url

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Root URL of the API to call

## <a name="open_api_location"></a>4. Property `open_api_location`

**Title:** Open Api Location

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Location of the OpenAPI schema

## <a name="operations_to_expose"></a>5. Property `operations_to_expose`

**Title:** Operations To Expose

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | Yes     |

**Description:** Operations to expose

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [Operation](#operations_to_expose_items) | -           |

### <a name="autogenerated_heading_1"></a>5.1. Operation

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/$defs/Operation                                                         |

| Property                                                        | Pattern | Type            | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| + [name](#operations_to_expose_items_name )                     | No      | string          | No         | -          | Name              |
| - [description](#operations_to_expose_items_description )       | No      | string          | No         | -          | Description       |
| + [path](#operations_to_expose_items_path )                     | No      | string          | No         | -          | Path              |
| + [method](#operations_to_expose_items_method )                 | No      | string          | No         | -          | Method            |
| - [result_filters](#operations_to_expose_items_result_filters ) | No      | array of string | No         | -          | Result Filters    |

#### <a name="operations_to_expose_items_name"></a>5.1.1. Property `name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Name of the operation

#### <a name="operations_to_expose_items_description"></a>5.1.2. Property `description`

**Title:** Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `null`   |

**Description:** Description of the operation

#### <a name="operations_to_expose_items_path"></a>5.1.3. Property `path`

**Title:** Path

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Path of the operation. Must match exactly including path parameters

#### <a name="operations_to_expose_items_method"></a>5.1.4. Property `method`

**Title:** Method

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** HTTP method of the operation.  get and post are supported

#### <a name="operations_to_expose_items_result_filters"></a>5.1.5. Property `result_filters`

**Title:** Result Filters

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |
| **Default**  | `null`            |

**Description:** Filters to apply to the result of the operation per json ref spec

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                          | Description |
| ------------------------------------------------------------------------ | ----------- |
| [result_filters items](#operations_to_expose_items_result_filters_items) | -           |

##### <a name="autogenerated_heading_2"></a>5.1.5.1. result_filters items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="extra_header_params"></a>6. Property `extra_header_params`

**Title:** Extra Header Params

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |

**Description:** Extra header parameters to add to every call. This can be a jinja template where the variables in the template are ENV variables (matching case)

## <a name="extra_query_params"></a>7. Property `extra_query_params`

**Title:** Extra Query Params

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |

**Description:** Extra query parameters to add to every call. This can be a jinja template where the variables in the template are ENV variables (matching case)

## <a name="max_response_size"></a>8. Property `max_response_size`

**Title:** Max Response Size

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `51200`   |

**Description:** Maximum size of response content to allow. If the response is larger than this, an error will be raised. Default is 50k

----------------------------------------------------------------------------------------------------------------------------
