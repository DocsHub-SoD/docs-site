# Class: DewPersistence.NetworkBehaviourConverter

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.NetworkBehaviourConverter : JsonConverter
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`prevNetIdMap`** | `public readonly Dictionary&lt;uint, NetworkIdentity&gt; prevNetIdMap` | Previous netId to current NetworkIdentity |

## Methods

### `CanConvert(Type)`

```csharp
public override bool CanConvert(Type objectType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `objectType` | `System.Type` |  |

**Returns:** `bool`

### `ReadJson(JsonReader, Type, object, JsonSerializer)`

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

### `WriteJson(JsonWriter, object, JsonSerializer)`

```csharp
public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Newtonsoft.Json.JsonWriter` |  |
| `value` | `object` |  |
| `serializer` | `Newtonsoft.Json.JsonSerializer` |  |
