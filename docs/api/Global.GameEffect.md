# Class: GameEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [DewQuest](/api/Global.DewQuest) → [GameModifierBase](/api/Global.GameModifierBase) → [LucidDream](/api/Global.LucidDream)

```csharp
[SaveActor(true)]
public class GameEffect : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`endEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject endEffect` |  |
| **`loopEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject loopEffect` |  |
| **`startEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject startEffect` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

:::

## Methods (3)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::
