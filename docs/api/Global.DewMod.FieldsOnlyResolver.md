# Class: DewMod.FieldsOnlyResolver

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
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
