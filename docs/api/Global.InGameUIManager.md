# Class: InGameUIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [UIManager](/api/Global.UIManager)

```csharp
public class InGameUIManager : UIManager, ILogicUpdate
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cmsgContainer`** | `public Transform cmsgContainer` |  |
| **`cmsgErrorPrefab`** | `public GameObject cmsgErrorPrefab` |  |
| **`cmsgGeneralPrefab`** | `public GameObject cmsgGeneralPrefab` |  |
| **`cmsgStartPivot`** | `public Transform cmsgStartPivot` |  |
| **`currentMockExit`** | `public Rift_MockExit currentMockExit` |  |
| **`disableOnEndingObjects`** | `public GameObject[] disableOnEndingObjects` |  |
| **`fullWorldMapNodeItems`** | `[NonSerialized] public List<RectTransform> fullWorldMapNodeItems` |  |
| **`miniWorldMapNodeItems`** | `[NonSerialized] public List<RectTransform> miniWorldMapNodeItems` |  |
| **`onHasWorldNodePingChanged`** | `public Action<bool> onHasWorldNodePingChanged` |  |
| **`onScoreboardDisplayedChanged`** | `public Action<bool> onScoreboardDisplayedChanged` |  |
| **`onShowWorldMessage`** | `public Action<WorldMessageSetting> onShowWorldMessage` |  |
| **`onWorldDisplayedChanged`** | `public Action<WorldDisplayStatus> onWorldDisplayedChanged` |  |
| **`whiteFadeCg`** | `public CanvasGroup whiteFadeCg` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disablePlayingInput`** | `public bool disablePlayingInput { get; }` |  |
| **`hasWorldNodePing`** | `public bool hasWorldNodePing { get; }` | Do we need mini world map instead of party display right now? |
| **`instance`** | `public static InGameUIManager instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`isDoingEnding`** | `public bool isDoingEnding { get; }` |  |
| **`isScoreboardDisplayed`** | `public bool isScoreboardDisplayed { get; set; }` |  |
| **`isWorldDisplayed`** | `public WorldDisplayStatus isWorldDisplayed { get; set; }` |  |
| **`lastWorldDisplayUnscaledTime`** | `public float lastWorldDisplayUnscaledTime { get; }` |  |
| **`softInstance`** | `public static InGameUIManager softInstance { get; }` |  |

:::

## Methods (15)

::: details `DecrementWorldNodePingCounter()`

This decrements internal counter. You must pair this with equivalent number EnableMiniWorldMap calls.

```csharp
public void DecrementWorldNodePingCounter()
```

:::

::: details `DisablePlayingInput()`

```csharp
public void DisablePlayingInput()
```

:::

::: details `EnablePlayingInput()`

```csharp
public void EnablePlayingInput()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetContinueRelatedDescription()`

```csharp
public string GetContinueRelatedDescription()
```

**Returns:** `string`

:::

::: details `GetWorldNodeUIPos(int)`

```csharp
public Vector2 GetWorldNodeUIPos(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `IncrementWorldNodePingCounter()`

```csharp
public void IncrementWorldNodePingCounter()
```

:::

::: details `OnStateChanged(string, string)`

```csharp
protected override void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

:::

::: details `SetIsDoingEnding(bool)`

```csharp
public void SetIsDoingEnding(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `SetWhiteFade(bool)`

```csharp
public void SetWhiteFade(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `ShouldDoAutoFocus()`

```csharp
public override bool ShouldDoAutoFocus()
```

**Returns:** `bool`

:::

::: details `ShowCenterMessage(CenterMessageType, string, object[])`

```csharp
public void ShowCenterMessage(CenterMessageType type, string key, object[] formatArgs = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`CenterMessageType`](/api/Global.CenterMessageType) |  |
| `key` | `string` |  |
| `formatArgs` | `object[]` |  |

:::

::: details `ShowCenterMessageRaw(CenterMessageType, string)`

```csharp
public void ShowCenterMessageRaw(CenterMessageType type, string raw)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`CenterMessageType`](/api/Global.CenterMessageType) |  |
| `raw` | `string` |  |

:::

::: details `ShowWorldPopMessage(WorldMessageSetting)`

```csharp
public void ShowWorldPopMessage(WorldMessageSetting message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [`WorldMessageSetting`](/api/Global.WorldMessageSetting) |  |

:::

::: details `ValidateInGameActionMessage(bool)`

```csharp
public static bool ValidateInGameActionMessage(bool requireAliveHero = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `requireAliveHero` | `bool` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (68)

*Classes and systems that invoke, reference, or depend on `InGameUIManager`:*

[Artifact](/api/Global.Artifact) · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [CursorManager](/api/Global.CursorManager) · [DevGameManager](/api/Global.DevGameManager) · [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) · `DewConsoleCommands` · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillManager](/api/Global.EditSkillManager) · [FPSManager](/api/Global.FPSManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [GameResultManager](/api/Global.GameResultManager) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · `Mon_GoldenLizard_ElusiveLizard` · [ObjectHighlightManager](/api/Global.ObjectHighlightManager) · [PingUIInstance](/api/Global.PingUIInstance) · `PlayTutorialManager` · `Primus_Ending` · [QuestManager](/api/Global.QuestManager) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · `Se_GenericStealth` · `Se_MirageSkin_Delusion_Delusional` · `Se_Mon_Special_BossPolaris_Holy_ShortInvul` · `Se_OntologicalShield` · `Se_Star_Husk_I_ShopIntimidation` · `Se_VeilOfDark` · `Shrine_Chaos` · `Shrine_PrimusEndingLightPillar` · `Shrine_StarCookie` · `Shrine_StarlessPath_EndingRift` · [SkillTrigger](/api/Global.SkillTrigger) · `St_D_CircleOfLife` · `StarlessPath_BossPolarisManager` · [TimescaleManager](/api/Global.TimescaleManager) · `Tut_World` · `Tut_WorldHunt` · `UI_Common_MenuView` · `UI_DamageNumberGroup` · `UI_InGame_ArtifactStoryView` · `UI_InGame_CenterMessage` · `UI_InGame_EmoteCanvas` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_HasWorldNodePingFlasher` · `UI_InGame_InteractGroup` · `UI_InGame_InvertedControlsCursor` · `UI_InGame_MouseInputReceiver` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_ScoreboardView` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SpectateIndicator` · `UI_InGame_TimerDisplay` · `UI_InGame_VisibilityOnWorldView` · `UI_InGame_VoteDisplay` · `UI_InGame_WorldMap` · `UI_InGame_WorldView` · `UI_InGame_World_Edge` · `UI_InGame_World_NodeItem` · `UI_PlayTutorial_TutorialCanvas` · `UI_TooltipManager` · `UI_Tooltip_WorldNode_CanTravelObject` · `UI_Tooltip_WorldNode_Description` · [View](/api/Global.View) · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (29)

*Types and components that `InGameUIManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewInputTrigger](/api/Global.DewInputTrigger) · [DewLocalization](/api/Global.DewLocalization) · [DewPersistence](/api/Global.DewPersistence) · [DewPlayer](/api/Global.DewPlayer) · [EntityCheck](/api/Global.EntityCheck) · [FPSManager](/api/Global.FPSManager) · [GameManager](/api/Global.GameManager) · `GameObjectExtensions` · [GameSettingsManager](/api/Global.GameSettingsManager) · [Gem](/api/Global.Gem) · [GlobalUIManager](/api/Global.GlobalUIManager) · [IItem](/api/Global.IItem) · [IMenuView](/api/Global.IMenuView) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Rift_MockExit](/api/Global.Rift_MockExit) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SkillTrigger](/api/Global.SkillTrigger) · [UIManager](/api/Global.UIManager) · [View](/api/Global.View) · [WorldMessageSetting](/api/Global.WorldMessageSetting) · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`CenterMessageType`](/enums#centermessagetype) · [`WorldDisplayStatus`](/enums#worlddisplaystatus)

:::
