# Class: DewMod.FieldsOnlyResolver

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewMod.FieldsOnlyResolver : DefaultContractResolver
```

## Methods

### `CreateProperty(MemberInfo, MemberSerialization)`

```csharp
protected override JsonProperty CreateProperty(MemberInfo member, MemberSerialization memberSerialization)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `member` | `System.Reflection.MemberInfo` |  |
| `memberSerialization` | `Newtonsoft.Json.MemberSerialization` |  |

**Returns:** `Newtonsoft.Json.Serialization.JsonProperty`
