# Class: CastMethodDataSerialization

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[Extension]`

```csharp
public static class CastMethodDataSerialization
```

## Methods (2)

::: details `ReadWriteCastMethodData(NetworkReader)`

```csharp
public static CastMethodData ReadWriteCastMethodData(this NetworkReader reader)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `reader` | `Mirror.NetworkReader` |  |

**Returns:** `CastMethodData`

:::

::: details `WriteCastMethodData(NetworkWriter, CastMethodData)`

```csharp
public static void WriteCastMethodData(this NetworkWriter writer, CastMethodData value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `writer` | `Mirror.NetworkWriter` |  |
| `value` | [`CastMethodData`](/api/Global.CastMethodData) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `CastMethodDataSerialization`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [DewPlayer](/api/Global.DewPlayer) · `Mirror.GeneratedNetworkCode`

### Dependencies (1)

*Types and components that `CastMethodDataSerialization` references or depends upon:*

[CastMethodData](/api/Global.CastMethodData)

:::
