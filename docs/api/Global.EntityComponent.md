# Class: EntityComponent

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityAbility](/api/Global.EntityAbility) → [EntityAI](/api/Global.EntityAI) → [EntityAnimation](/api/Global.EntityAnimation) → [EntityControl](/api/Global.EntityControl) → [EntitySound](/api/Global.EntitySound) → [EntityStatus](/api/Global.EntityStatus) → [EntityVisual](/api/Global.EntityVisual) → [HeroComponent](/api/Global.HeroComponent)

```csharp
[LogicUpdatePriority(-300)]
public abstract class EntityComponent : DewNetworkBehaviour, ILogicUpdate
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entity`** | `public Entity entity { get; }` |  |

:::

## Methods (1)

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (13)

*Classes and systems that invoke, reference, or depend on `EntityComponent`:*

[DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityControl](/api/Global.EntityControl) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [Hero](/api/Global.Hero) · [HeroComponent](/api/Global.HeroComponent) · [HeroSkill](/api/Global.HeroSkill) · `Se_HeroKnockedOut`

### Dependencies (3)

*Types and components that `EntityComponent` references or depends upon:*

[DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity)

:::
