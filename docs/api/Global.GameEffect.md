# Class: GameEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [DewQuest](/api/Global.DewQuest) → [GameModifierBase](/api/Global.GameModifierBase) → [LucidDream](/api/Global.LucidDream)

```csharp
[SaveActor(true)]
public class GameEffect : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`endEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject endEffect` |  |
| **`loopEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject loopEffect` |  |
| **`startEffect`** | `[BoxGroup("Effects", true, false, 0)] public GameObject startEffect` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

## Methods

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`
