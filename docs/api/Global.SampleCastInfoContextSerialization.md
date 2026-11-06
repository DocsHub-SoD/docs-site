# Class: SampleCastInfoContextSerialization

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class SampleCastInfoContextSerialization
```

## Methods (2)

::: details `ReadSampleCastInfoContext(NetworkReader)`

```csharp
public static SampleCastInfoContext? ReadSampleCastInfoContext(this NetworkReader reader)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reader` | `Mirror.NetworkReader` |  |

**Returns:** `SampleCastInfoContext?`

:::

::: details `WriteSampleCastInfoContext(NetworkWriter, SampleCastInfoContext?)`

```csharp
public static void WriteSampleCastInfoContext(this NetworkWriter writer, SampleCastInfoContext? value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Mirror.NetworkWriter` |  |
| `value` | [`SampleCastInfoContext?`](/api/Global.SampleCastInfoContext) |  |

:::
