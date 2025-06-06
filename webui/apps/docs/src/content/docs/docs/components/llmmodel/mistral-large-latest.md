---
title: mistral-large-latest
description: Description of the mistral-large-latest component
---

| Property                                         | Pattern | Type    | Deprecated | Definition | Title/Description    |
| ------------------------------------------------ | ------- | ------- | ---------- | ---------- | -------------------- |
| + [implementation](#implementation )             | No      | const   | No         | -          | Implementation       |
| + [human_name](#human_name )                     | No      | string  | No         | -          | Human Name           |
| + [name](#name )                                 | No      | string  | No         | -          | Name                 |
| + [input_context_limit](#input_context_limit )   | No      | integer | No         | -          | Input Context Limit  |
| + [output_context_limit](#output_context_limit ) | No      | integer | No         | -          | Output Context Limit |
| + [supports_tools](#supports_tools )             | No      | boolean | No         | -          | Supports Tools       |
| + [supports_image_input](#supports_image_input ) | No      | boolean | No         | -          | Supports Image Input |
| + [supports_audio_input](#supports_audio_input ) | No      | boolean | No         | -          | Supports Audio Input |

## <a name="implementation"></a>1. Property `implementation`

**Title:** Implementation

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"mistral-large-latest"`

## <a name="human_name"></a>2. Property `human_name`

**Title:** Human Name

|              |                   |
| ------------ | ----------------- |
| **Type**     | `string`          |
| **Required** | Yes               |
| **Default**  | `"Mistral Large"` |

## <a name="name"></a>3. Property `name`

**Title:** Name

|              |                          |
| ------------ | ------------------------ |
| **Type**     | `string`                 |
| **Required** | Yes                      |
| **Default**  | `"mistral-large-latest"` |

## <a name="input_context_limit"></a>4. Property `input_context_limit`

**Title:** Input Context Limit

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |
| **Default**  | `32000`   |

## <a name="output_context_limit"></a>5. Property `output_context_limit`

**Title:** Output Context Limit

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |
| **Default**  | `4096`    |

## <a name="supports_tools"></a>6. Property `supports_tools`

**Title:** Supports Tools

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | Yes       |
| **Default**  | `true`    |

## <a name="supports_image_input"></a>7. Property `supports_image_input`

**Title:** Supports Image Input

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | Yes       |
| **Default**  | `false`   |

## <a name="supports_audio_input"></a>8. Property `supports_audio_input`

**Title:** Supports Audio Input

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | Yes       |
| **Default**  | `false`   |

----------------------------------------------------------------------------------------------------------------------------
