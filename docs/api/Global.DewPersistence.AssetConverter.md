# Class: DewPersistence.AssetConverter

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.AssetConverter : JsonConverter
```

## Methods (3)

::: details `CanConvert(Type)`

```csharp
public override bool CanConvert(Type objectType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `objectType` | `System.Type` |  |

**Returns:** `bool`

:::

::: details `ReadJson(JsonReader, Type, object, JsonSerializer)`

```csharp
public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reader` | `Newtonsoft.Json.JsonReader` |  |
| `objectType` | `System.Type` |  |
| `existingValue` | `object` |  |
| `serializer` | `Newtonsoft.Json.JsonSerializer` |  |

**Returns:** `object`

:::

::: details `WriteJson(JsonWriter, object, JsonSerializer)`

```csharp
public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Newtonsoft.Json.JsonWriter` |  |
| `value` | `object` |  |
| `serializer` | `Newtonsoft.Json.JsonSerializer` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
