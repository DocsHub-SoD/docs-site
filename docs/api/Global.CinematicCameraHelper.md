# Class: CinematicCameraHelper

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(500)]
public class CinematicCameraHelper : LogicBehaviour, ILogicUpdate
```

## Fields (18)

::: details Click to expand Fields (18)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castIndicatorObject`** | `public GameObject castIndicatorObject` |  |
| **`cinematicCameras`** | `public GameObject[] cinematicCameras` |  |
| **`entireUICanvasGroup`** | `public CanvasGroup entireUICanvasGroup` |  |
| **`freeCamFastSpeed`** | `public float freeCamFastSpeed` |  |
| **`freeCamIndex`** | `public int freeCamIndex` |  |
| **`freeCamMouseSensitivity`** | `public float freeCamMouseSensitivity` |  |
| **`freeCamRotSmoothTime`** | `public float freeCamRotSmoothTime` |  |
| **`freeCamSlowSpeed`** | `public float freeCamSlowSpeed` |  |
| **`freeCamSmoothTime`** | `public float freeCamSmoothTime` |  |
| **`freeCamSpeed`** | `public float freeCamSpeed` |  |
| **`freeCamTargetTransform`** | `public Transform freeCamTargetTransform` |  |
| **`freeCamTransform`** | `public Transform freeCamTransform` |  |
| **`groupAllHeroes`** | `public CinemachineTargetGroup groupAllHeroes` |  |
| **`groupHeroesAndMonsters`** | `public CinemachineTargetGroup groupHeroesAndMonsters` |  |
| **`groupMyHero`** | `public CinemachineTargetGroup groupMyHero` |  |
| **`maxTargets`** | `public int maxTargets` |  |
| **`radius`** | `public float radius` |  |
| **`weightGainPerSecond`** | `public float weightGainPerSecond` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isCinematicHelperEnabled`** | `public bool isCinematicHelperEnabled { get; set; }` |  |

:::

## Methods (2)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `CinematicCameraHelper`:*

`DewConsoleCommands`

### Dependencies (9)

*Types and components that `CinematicCameraHelper` references or depends upon:*

[ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual) · [Hero](/api/Global.Hero) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1)

:::
