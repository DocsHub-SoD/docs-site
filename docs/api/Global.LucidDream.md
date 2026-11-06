# Class: LucidDream

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect)

```csharp
public class LucidDream : GameEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ChaoticColor`** | `public static readonly Color ChaoticColor` |  |
| **`EvilColor`** | `public static readonly Color EvilColor` |  |
| **`GoodColor`** | `public static readonly Color GoodColor` |  |
| **`icon`** | `[BoxGroup("Lucid Dream Settings", true, false, 0)] public Sprite icon` |  |
| **`type`** | `[BoxGroup("Lucid Dream Settings", true, false, 0)] public LucidDreamType type` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`color`** | `public Color color { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |

## Methods

### `GetCustomInGameTooltip()`

```csharp
public virtual string GetCustomInGameTooltip()
```

**Returns:** `string`
