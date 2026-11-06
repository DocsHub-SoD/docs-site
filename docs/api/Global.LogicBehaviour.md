# Class: LogicBehaviour

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [CharacterModelDisplay](/api/Global.CharacterModelDisplay) → [CinematicCameraHelper](/api/Global.CinematicCameraHelper) → [CustomLogicBehavior](/api/Global.CustomLogicBehavior) → [DewBeamRenderer](/api/Global.DewBeamRenderer) → [DewCanvas](/api/Global.DewCanvas) → [FxAttachToEntity](/api/Global.FxAttachToEntity) → [FxCastTelegraph](/api/Global.FxCastTelegraph) → [FxRepeatedEffect](/api/Global.FxRepeatedEffect) → [HighlightProvider](/api/Global.HighlightProvider) → `ManagerBase<T>` → [PlayLobby_Character](/api/Global.PlayLobby_Character) → [PlayLobby_Fireplace](/api/Global.PlayLobby_Fireplace) → [RoomSection](/api/Global.RoomSection) → [RoomSectionComponent](/api/Global.RoomSectionComponent) → [Title_LastGameCharacters](/api/Global.Title_LastGameCharacters) → [UI_BindItem](/api/Global.UI_BindItem) → [UI_GamepadBindButton](/api/Global.UI_GamepadBindButton)

```csharp
public class LogicBehaviour : MonoBehaviour, ILogicUpdate
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public virtual bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (5)

::: details `FrameUpdate()`

```csharp
public virtual void FrameUpdate()
```

:::

::: details `GetComponent&lt;T&gt;(out T)`

```csharp
protected void GetComponent<T>(out T comp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `comp` | `T` |  |
| `` | `T` |  |

:::

::: details `LogicUpdate(float)`

```csharp
public virtual void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected virtual void OnEnable()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (135)

*Classes and systems that invoke, reference, or depend on `LogicBehaviour`:*

[CameraManager](/api/Global.CameraManager) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CharacterModelDisplay](/api/Global.CharacterModelDisplay) · [CinematicCameraHelper](/api/Global.CinematicCameraHelper) · `ContextMenu` · [ControlManager](/api/Global.ControlManager) · [CursorManager](/api/Global.CursorManager) · [CustomLogicBehavior](/api/Global.CustomLogicBehavior) · [DewBeamRenderer](/api/Global.DewBeamRenderer) · [DewCanvas](/api/Global.DewCanvas) · [EditSkillManager](/api/Global.EditSkillManager) · [FeedbackManager](/api/Global.FeedbackManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [FxAttachToEntity](/api/Global.FxAttachToEntity) · [FxCastTelegraph](/api/Global.FxCastTelegraph) · [FxRepeatedEffect](/api/Global.FxRepeatedEffect) · [GlobalUIManager](/api/Global.GlobalUIManager) · `GraphicsManager` · [HighlightProvider](/api/Global.HighlightProvider) · `IMG_AnimatedImage` · [InGameTutorialManager](/api/Global.InGameTutorialManager) · [InGameUIManager](/api/Global.InGameUIManager) · `Ink_ScrollingInkAnimation` · [InputManager](/api/Global.InputManager) · [LobbyUIManager](/api/Global.LobbyUIManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MaterialHighlightProvider](/api/Global.MaterialHighlightProvider) · [MeshHighlightProvider](/api/Global.MeshHighlightProvider) · [MessageManager](/api/Global.MessageManager) · [MusicManager](/api/Global.MusicManager) · [ObjectHighlightManager](/api/Global.ObjectHighlightManager) · [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · [RoomSection](/api/Global.RoomSection) · [RoomSectionComponent](/api/Global.RoomSectionComponent) · [ShaderManager](/api/Global.ShaderManager) · `ShakyLight` · `Shrine_CorruptedChaos_PetalAnimator` · `Shrine_FallenStar_Visual` · [TitleManager](/api/Global.TitleManager) · [Title_LastGameCharacters](/api/Global.Title_LastGameCharacters) · [TransitionManager](/api/Global.TransitionManager) · `TutorialArrow` · `UI_AnimatedValueText` · [UI_BindItem](/api/Global.UI_BindItem) · `UI_Common_ChatBox` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_DropdownControls` · `UI_EntityCrowdControl` · `UI_EntityDestroyOnDeath` · `UI_EntityElementals` · `UI_EntityGenericStackIndicator` · `UI_EntityLevel` · `UI_EntityName` · `UI_EntityPrimaryStats` · `UI_EntityProtected` · `UI_EntitySummonDuration` · `UI_EntityTalk` · `UI_EntityUnstoppable` · [UI_GamepadBindButton](/api/Global.UI_GamepadBindButton) · `UI_GenericBar` · `UI_HealthBar_Simple` · `UI_InGame_AchievementNotifications` · `UI_InGame_BossBars_Item` · `UI_InGame_CooldownTimeNotification` · `UI_InGame_CurseNotifications` · `UI_InGame_EditSkillShrineText` · `UI_InGame_FloatingWindow_Base` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_GameTimer` · `UI_InGame_GemSlot` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroInfoBar` · `UI_InGame_InteractGroup` · `UI_InGame_Interact_Base` · `UI_InGame_Interact_Custom` · `UI_InGame_Interact_Gem` · `UI_InGame_Interact_Rift` · `UI_InGame_Interact_Shrine` · `UI_InGame_Interact_Skill` · `UI_InGame_InvertedControlsCursor` · `UI_InGame_KnockedOutIndicator` · `UI_InGame_Map` · `UI_InGame_Map_Item` · `UI_InGame_OffscreenIndicator_Item` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_PickupNumbers_Number` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_Scoreboard_PlayerItem_Skill_Gem` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButton_GemGroup` · `UI_InGame_SkillButtons` · `UI_InGame_SkillNotifications` · `UI_InGame_SpectateIndicator` · `UI_InGame_StardustGroup` · `UI_InGame_StatusEffectIcons_Item` · `UI_InGame_TimerDisplay_Item` · `UI_InGame_VoteDisplay` · `UI_InGame_VoteDisplay_PlayerItem` · `UI_InGame_WorldMap` · `UI_LimboDepthIcon` · `UI_Lobby_AllowDejavu` · `UI_Lobby_AllowMidJoins` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_DejavuButton_ActivationManager` · `UI_Lobby_DifficultyGroup` · `UI_Lobby_DifficultyItem` · `UI_Lobby_EnableVotes` · `UI_Lobby_HeroList_Item` · `UI_Lobby_HideIfReady` · `UI_Lobby_InviteButtonController` · `UI_Lobby_Loadout_ComponentBase` · `UI_Lobby_Loadout_SkillSlot` · `UI_Lobby_MidJoinWaitObject` · `UI_Lobby_PlayerInfoBase` · `UI_Lobby_ReadyStatusText` · `UI_Lobby_ReverieButton` · `UI_Lobby_StartButtonController` · `UI_Lobby_WaitingForContinueMidJoin_Loading` · `UI_PlayerPlatinumCoinToggler` · `UI_Reveries` · `UI_Reveries_CompletedReveries` · `UI_Reveries_RemainingRerolls` · `UI_Reveries_SlotBase` · `UI_Reveries_SpecialSlot` · `UI_TickedBar` · `UI_Title_CoopButtonManager` · `UI_Title_FindLobby_LobbyItem` · `UI_Title_LizardSmoothie` · `UI_Title_ProfileButton`

### Dependencies (2)

*Types and components that `LogicBehaviour` references or depends upon:*

[ILogicUpdate](/api/Global.ILogicUpdate) · [LogicUpdateManager](/api/Global.LogicUpdateManager)

:::
