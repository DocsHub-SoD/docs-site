# Class: EntityComponent

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityAbility](/api/Global.EntityAbility) → [EntityAI](/api/Global.EntityAI) → [EntityAnimation](/api/Global.EntityAnimation) → [EntityControl](/api/Global.EntityControl) → [EntitySound](/api/Global.EntitySound) → [EntityStatus](/api/Global.EntityStatus) → [EntityVisual](/api/Global.EntityVisual) → [HeroComponent](/api/Global.HeroComponent)

```csharp
[LogicUpdatePriority(-300)]
public abstract class EntityComponent : DewNetworkBehaviour, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`entity`** | `public Entity entity { get; }` |  |

## Methods

### `OnDisable()`

```csharp
protected virtual void OnDisable()
```
