# Interface: ICleanup

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ICleanup
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canDestroy`** | `bool canDestroy { get; }` | If anyICleanupreports false, destroy call will be delayed. |

:::

## Methods (1)

::: details `OnCleanup()`

Called on server to ready itself before getting destroyed.

```csharp
void OnCleanup()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `ICleanup`:*

[Actor](/api/Global.Actor) · [Dew](/api/Global.Dew) · [EntityAbility](/api/Global.EntityAbility) · [EntityControl](/api/Global.EntityControl) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [HeroSkill](/api/Global.HeroSkill)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
