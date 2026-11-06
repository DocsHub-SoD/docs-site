# Class: CameraManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [CameraManager](/api/Global.CameraManager)

```csharp
public class CameraManager : ManagerBase<CameraManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bigDamageAlpha`** | `public float bigDamageAlpha` |  |
| **`bigDamageShake`** | `[Title("Damage", null, TitleAlignments.Left, true, true)] public GameObject bigDamageShake` |  |
| **`bigDamageThreshold`** | `public float bigDamageThreshold` |  |
| **`closeZoomBody`** | `public Vector3 closeZoomBody` |  |
| **`cutsceneBottomLetterBox`** | `public RectTransform cutsceneBottomLetterBox` |  |
| **`cutsceneFadeTime`** | `public float cutsceneFadeTime` |  |
| **`cutsceneSkipButtonObject`** | `public GameObject cutsceneSkipButtonObject` |  |
| **`cutsceneTopLetterBox`** | `public RectTransform cutsceneTopLetterBox` |  |
| **`cutsceneTransitionFade`** | `public CanvasGroup cutsceneTransitionFade` |  |
| **`damageOverlay`** | `public CanvasGroup damageOverlay` |  |
| **`damageOverlayDecaySpeed`** | `public float damageOverlayDecaySpeed` |  |
| **`defaultZoomLevel`** | `public int defaultZoomLevel` |  |
| **`disableSeeThrough`** | `[NonSerialized] public bool disableSeeThrough` |  |
| **`entityCamAngleRotation`** | `[NonSerialized] public Quaternion entityCamAngleRotation` | Flat Y-Axis rotation of current camera rotation. |
| **`fadeOutVolume`** | `public Volume fadeOutVolume` |  |
| **`farZoomBody`** | `[Title("Zoom", null, TitleAlignments.Left, true, true)] public Vector3 farZoomBody` |  |
| **`followSmoothTime`** | `[Title("General", null, TitleAlignments.Left, true, true)] public float followSmoothTime` |  |
| **`genericFadeTime`** | `public float genericFadeTime` |  |
| **`maxAlpha`** | `public float maxAlpha` |  |
| **`maxAlphaHealthThreshold`** | `public float maxAlphaHealthThreshold` |  |
| **`midZoombody`** | `public Vector3 midZoombody` |  |
| **`minAlphaHealthThreshold`** | `public float minAlphaHealthThreshold` |  |
| **`nextSpectateTargetTime`** | `public float nextSpectateTargetTime` |  |
| **`occlusionTestRadius`** | `[Title("Extra", null, TitleAlignments.Left, true, true)] public float occlusionTestRadius` |  |
| **`onFocusedEntityChanged`** | `public Action<Entity, Entity> onFocusedEntityChanged` |  |
| **`onIsSpectatingChanged`** | `public Action<bool> onIsSpectatingChanged` |  |
| **`selectedEntityCamera`** | `public CinemachineVirtualCamera selectedEntityCamera` |  |
| **`smallDamageAlpha`** | `public float smallDamageAlpha` |  |
| **`smallDamageShake`** | `public GameObject smallDamageShake` |  |
| **`smallDamageThreshold`** | `public float smallDamageThreshold` |  |
| **`startSpectatingTime`** | `public float startSpectatingTime` |  |
| **`zoomSmoothTime`** | `public float zoomSmoothTime` |  |
| **`zoomSteps`** | `public int zoomSteps` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentCutsceneDirector`** | `public DewCutsceneDirector currentCutsceneDirector { get; }` |  |
| **`currentZoomIndex`** | `public int currentZoomIndex { get; }` |  |
| **`entityCamAngle`** | `public float entityCamAngle { get; set; }` |  |
| **`focusedEntity`** | `public Entity focusedEntity { get; }` |  |
| **`isPlayingCutscene`** | `public bool isPlayingCutscene { get; }` | Is cutscene being played locally? |
| **`isSpectating`** | `public bool isSpectating { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `DoCutsceneFadeIn()`

```csharp
public void DoCutsceneFadeIn()
```

### `DoCutsceneFadeOut()`

```csharp
public void DoCutsceneFadeOut()
```

### `DoGenericFadeIn(bool)`

```csharp
public void DoGenericFadeIn(bool immediately = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediately` | `bool` |  |

### `DoGenericFadeOut(bool)`

```csharp
public void DoGenericFadeOut(bool immediately = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediately` | `bool` |  |

### `DoLetterBoxFadeIn()`

```csharp
public void DoLetterBoxFadeIn()
```

### `DoLetterBoxFadeOut()`

```csharp
public void DoLetterBoxFadeOut()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `ResetLetterBoxPositions()`

```csharp
public void ResetLetterBoxPositions()
```

### `SetActiveEntityVCam(bool)`

```csharp
public void SetActiveEntityVCam(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

### `SetCameraPosition(Vector3)`

```csharp
public void SetCameraPosition(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

### `SetFocusedEntity(Entity)`

```csharp
public void SetFocusedEntity(Entity newValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newValue` | [`Entity`](/api/Global.Entity) |  |

### `SetZoomLevel(int)`

```csharp
public void SetZoomLevel(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

### `SkipCurrentCutscene()`

```csharp
public void SkipCurrentCutscene()
```

### `SnapCameraToFocusedEntity()`

```csharp
public void SnapCameraToFocusedEntity()
```

### `SpectateImmediatelyIfDead()`

```csharp
public void SpectateImmediatelyIfDead()
```

### `ZoomIn()`

```csharp
public void ZoomIn()
```

### `ZoomOut()`

```csharp
public void ZoomOut()
```
