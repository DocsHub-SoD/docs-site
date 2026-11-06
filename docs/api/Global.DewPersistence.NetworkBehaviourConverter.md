# Class: DewPersistence.NetworkBehaviourConverter

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.NetworkBehaviourConverter : JsonConverter
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`prevNetIdMap`** | `public readonly Dictionary<uint, NetworkIdentity> prevNetIdMap` | Previous netId to current NetworkIdentity |

:::

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
