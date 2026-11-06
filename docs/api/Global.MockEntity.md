# Class: MockEntity

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity)

```csharp
public class MockEntity : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`conversationNameUIKey`** | `[SyncVar] public string conversationNameUIKey` |  |

:::

## Methods (1)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `MockEntity`:*

`ConversationShrineBase` · `Shrine_ArtifactGiver`

### Dependencies (3)

*Types and components that `MockEntity` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [InvisibleEffect](/api/Global.InvisibleEffect)

:::
