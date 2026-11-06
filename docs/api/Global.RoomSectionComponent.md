# Class: RoomSectionComponent

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority] [RequireComponent]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [Section_Monsters](/api/Global.Section_Monsters) → [Section_Props](/api/Global.Section_Props)

```csharp
[LogicUpdatePriority(200)]
[RequireComponent(typeof(RoomSection))]
public class RoomSectionComponent : LogicBehaviour, ILogicUpdate
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`section`** | `public RoomSection section { get; }` |  |

:::

## Methods (1)

::: details `Awake()`

```csharp
protected virtual void Awake()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `RoomSectionComponent`:*

[Section_Monsters](/api/Global.Section_Monsters) · [Section_Props](/api/Global.Section_Props)

### Dependencies (2)

*Types and components that `RoomSectionComponent` references or depends upon:*

[LogicBehaviour](/api/Global.LogicBehaviour) · [RoomSection](/api/Global.RoomSection)

:::
