# Class: PlayLobby_Fireplace

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(2000)]
public class PlayLobby_Fireplace : LogicBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`intensityDeviation`** | `public float intensityDeviation` |  |
| **`intensityNewTargetTime`** | `public float intensityNewTargetTime` |  |
| **`intensitySmoothTime`** | `public float intensitySmoothTime` |  |
| **`positionDeviation`** | `public float positionDeviation` |  |
| **`positionNewTargetTime`** | `public float positionNewTargetTime` |  |
| **`positionSmoothTime`** | `public float positionSmoothTime` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```
