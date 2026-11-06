# Class: CameraManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [CameraManager](/api/Global.CameraManager)

```csharp
public class CameraManager : ManagerBase<CameraManager>, ILogicUpdate
```

## Fields (33)

::: details Click to expand Fields (33)

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

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentCutsceneDirector`** | `public DewCutsceneDirector currentCutsceneDirector { get; }` |  |
| **`currentZoomIndex`** | `public int currentZoomIndex { get; }` |  |
| **`entityCamAngle`** | `public float entityCamAngle { get; set; }` |  |
| **`focusedEntity`** | `public Entity focusedEntity { get; }` |  |
| **`isPlayingCutscene`** | `public bool isPlayingCutscene { get; }` | Is cutscene being played locally? |
| **`isSpectating`** | `public bool isSpectating { get; }` |  |

:::

## Methods (19)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `DoCutsceneFadeIn()`

```csharp
public void DoCutsceneFadeIn()
```

:::

::: details `DoCutsceneFadeOut()`

```csharp
public void DoCutsceneFadeOut()
```

:::

::: details `DoGenericFadeIn(bool)`

```csharp
public void DoGenericFadeIn(bool immediately = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediately` | `bool` |  |

:::

::: details `DoGenericFadeOut(bool)`

```csharp
public void DoGenericFadeOut(bool immediately = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `immediately` | `bool` |  |

:::

::: details `DoLetterBoxFadeIn()`

```csharp
public void DoLetterBoxFadeIn()
```

:::

::: details `DoLetterBoxFadeOut()`

```csharp
public void DoLetterBoxFadeOut()
```

:::

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

::: details `ResetLetterBoxPositions()`

```csharp
public void ResetLetterBoxPositions()
```

:::

::: details `SetActiveEntityVCam(bool)`

```csharp
public void SetActiveEntityVCam(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `SetCameraPosition(Vector3)`

```csharp
public void SetCameraPosition(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

:::

::: details `SetFocusedEntity(Entity)`

```csharp
public void SetFocusedEntity(Entity newValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newValue` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `SetZoomLevel(int)`

```csharp
public void SetZoomLevel(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

:::

::: details `SkipCurrentCutscene()`

```csharp
public void SkipCurrentCutscene()
```

:::

::: details `SnapCameraToFocusedEntity()`

```csharp
public void SnapCameraToFocusedEntity()
```

:::

::: details `SpectateImmediatelyIfDead()`

```csharp
public void SpectateImmediatelyIfDead()
```

:::

::: details `ZoomIn()`

```csharp
public void ZoomIn()
```

:::

::: details `ZoomOut()`

```csharp
public void ZoomOut()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (58)

*Classes and systems that invoke, reference, or depend on `CameraManager`:*

`Ai_Curse_AnchorOfMind_Anchor` · `Ai_Curse_DreamAfflictionInductive_Smite` · `At_Mon_Forest_BossDemon_Spawn` · `At_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `At_Mon_Special_BossMaw_Purgatory` · `At_Mon_Special_BossObliviax_Artillery` · `At_Mon_Special_BossObliviax_NeedleAtk` · `At_Mon_Special_BossPolaris_Holy_SelfCleanse` · [AttachToHero](/api/Global.AttachToHero) · [CameraModifierBase](/api/Global.CameraModifierBase) · [ControlManager](/api/Global.ControlManager) · `Despair_FogPositionController` · `DewConsoleCommands` · [DewCutsceneDirector](/api/Global.DewCutsceneDirector) · `DewDamageNumberRenderer` · [DewEffect](/api/Global.DewEffect) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillManager](/api/Global.EditSkillManager) · [EntityControl](/api/Global.EntityControl) · [FxCameraShake](/api/Global.FxCameraShake) · [FxDoFDynamicFocusDistance](/api/Global.FxDoFDynamicFocusDistance) · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · `Ge_Obliviax_InterruptTravelAndKidnap` · `Ink_GhostBehavior` · `ItemWorldModel` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_BossPolaris` · [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager) · `PlayTutorialManager` · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_Intro` · [Room](/api/Global.Room) · `RoomMod_StardustEverywhere` · [RoomMonsters](/api/Global.RoomMonsters) · `Se_Curse_AnchorOfMind` · `Se_Curse_IntermittentExplosion` · `Se_D_PrismaticEyes` · `Se_E_VileStrike` · `Se_Gem_E_Insensitivity_BombSpawner` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_ObliviaxKidnap` · `Se_Star_Bismuth_D_SkillHasteAndAutoCast` · `Se_UsingShortcut` · [ShaderManager](/api/Global.ShaderManager) · `Shrine_TheConsortOfNight` · `SnowMountain_RotateFogVolume` · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `UI_InGame_Conversations_Instance` · `UI_InGame_FollowAndFaceHero_Base` · `UI_InGame_Map` · `UI_InGame_SkillButtonsBottomBar` · `UI_InGame_SpectateIndicator` · `UI_InGame_TimerDisplay` · `UI_InGame_VisibilityOnSpectate` · `UI_World_FollowAndFaceCamera`

### Dependencies (36)

*Types and components that `CameraManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [ArrayReturnHandle`1](/api/Global.ArrayReturnHandle`1) · [CameraModifierBase](/api/Global.CameraModifierBase) · [ComponentCache`2](/api/Global.ComponentCache`2) · [ConsoleManager](/api/Global.ConsoleManager) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · `DOTweenVolumeExtension` · [DewCutsceneDirector](/api/Global.DewCutsceneDirector) · [DewEffect](/api/Global.DewEffect) · [DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoDamage](/api/Global.EventInfoDamage) · [FinalDamageData](/api/Global.FinalDamageData) · [GameManager](/api/Global.GameManager) · [Hero](/api/Global.Hero) · [IInteractable](/api/Global.IInteractable) · [InGameUIManager](/api/Global.InGameUIManager) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [ShaderManager](/api/Global.ShaderManager) · [TransitionManager](/api/Global.TransitionManager) · [UIManager](/api/Global.UIManager) · `Vector3FlattenExtension`

:::
