# Interface: IEffectWithOwnerContext

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IEffectWithOwnerContext
```

## Methods (1)

::: details `SetOwnerContext(EffectOwnerContext)`

```csharp
void SetOwnerContext(EffectOwnerContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EffectOwnerContext`](/api/Global.EffectOwnerContext) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `IEffectWithOwnerContext`:*

[DewAudioSource](/api/Global.DewAudioSource) · [DewEffect](/api/Global.DewEffect) · [FxCameraShake](/api/Global.FxCameraShake) · [FxVolume](/api/Global.FxVolume)

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`EffectOwnerContext`](/enums#effectownercontext)

:::
