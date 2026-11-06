# Interface: IAttachableToEntity

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IAttachableToEntity
```

## Methods (1)

::: details `OnAttachToEntity(Entity)`

```csharp
void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (17)

*Classes and systems that invoke, reference, or depend on `IAttachableToEntity`:*

[DewEffect](/api/Global.DewEffect) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · `FxAnimatorBoneOffset` · [FxAnimatorSetFloat](/api/Global.FxAnimatorSetFloat) · [FxAnimatorSetTrigger](/api/Global.FxAnimatorSetTrigger) · [FxAttachToEntity](/api/Global.FxAttachToEntity) · [FxEntityAnimation](/api/Global.FxEntityAnimation) · [FxEntityColor](/api/Global.FxEntityColor) · [FxEntityDisableRenderer](/api/Global.FxEntityDisableRenderer) · `FxEntityInvoke` · [FxEntityModelTransform](/api/Global.FxEntityModelTransform) · [FxEntityShake](/api/Global.FxEntityShake) · [FxEntityShell](/api/Global.FxEntityShell) · [FxEntityTransform](/api/Global.FxEntityTransform) · [FxFindEntity](/api/Global.FxFindEntity) · [FxMeshTrail](/api/Global.FxMeshTrail) · [FxRepeatedEffect](/api/Global.FxRepeatedEffect)

### Dependencies (1)

*Types and components that `IAttachableToEntity` references or depends upon:*

[Entity](/api/Global.Entity)

:::
