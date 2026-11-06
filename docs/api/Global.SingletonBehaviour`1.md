# Class: SingletonBehaviour&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DevCanvas](/api/Global.DevCanvas) → [Room_BossArena](/api/Global.Room_BossArena) → [Special_RoomAnnouncer](/api/Global.Special_RoomAnnouncer) → [UI_BindingWindow](/api/Global.UI_BindingWindow) → [UI_EmoteWheel](/api/Global.UI_EmoteWheel) → [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput)

```csharp
public class SingletonBehaviour<T> : MonoBehaviour where T : MonoBehaviour
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static T instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static T softInstance { get; }` |  |

:::

## Methods (1)

::: details `Awake()`

```csharp
protected virtual void Awake()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (100)

*Classes and systems that invoke, reference, or depend on `SingletonBehaviour<T>`:*

`Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Ink_BossDarkMoon_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Sky_BossNyx_Swipe` · `Ai_Mon_Special_BossErebos_Teleport` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `At_Mon_Special_BossMaw_Purgatory` · [ControlManager](/api/Global.ControlManager) · `DarkCave_BossRoomCenter` · [DevCanvas](/api/Global.DevCanvas) · [DewInput](/api/Global.DewInput) · `Erebos_BossRoomCenter` · `GameArea` · `Ge_Shrine_PotOfGreed` · `Ge_TheConsortOfNight` · `IShowTooltip` · `Ink_BossRoomCenter` · `Ink_BossTeleportPosition` · `LavaLand_InfernusPillarPosition` · `Mon_Special_BossPolaris` · `Obliviax_BossRoomCenter` · `Primus_Pizza0` · [Room_BossArena](/api/Global.Room_BossArena) · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `Sky_BossRoomCenter` · `Sky_LightFog` · `Sky_LightFogDamager` · [Special_RoomAnnouncer](/api/Global.Special_RoomAnnouncer) · `UI_AccList` · `UI_AccList_Item` · `UI_AccList_PreviewWindow` · [UI_BindItem](/api/Global.UI_BindItem) · [UI_BindingWindow](/api/Global.UI_BindingWindow) · `UI_Common_MenuView` · `UI_Constellations` · `UI_Constellations_StarDetails` · `UI_Constellations_StarEdge` · `UI_Constellations_StarItem` · `UI_Constellations_UnselectButton` · `UI_DamageNumberGroup` · `UI_EmoteList` · `UI_EmoteList_EditEmote` · `UI_EmoteList_EditEmoteWheel_FloatingEmote` · `UI_EmoteList_Item` · `UI_EmoteList_PreviewWindow` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · [UI_GamepadInputField](/api/Global.UI_GamepadInputField) · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_InGame_CurrentArtifact` · `UI_InGame_GemSlot` · `UI_InGame_MouseInputReceiver` · `UI_InGame_QuestDisplay_Item` · `UI_InGame_RoomModDisplay` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButtons` · `UI_InGame_SkillNotifications` · `UI_InGame_VoteDisplay` · `UI_InGame_WorldMap` · `UI_InGame_World_NodeItem` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_AlphaStar` · `UI_Lobby_Constellations_FloatingStar` · `UI_Lobby_Constellations_HeroConstellation` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_Skills_ContextMenu` · `UI_Lobby_Constellations_Skills_ContextMenu_Item` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_Constellations_StarDetails` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_Emotes_Back` · `UI_Lobby_Loadout_AvailableSkills_Item` · `UI_Lobby_LucidDreamsWindow` · `UI_Lobby_NametagList` · `UI_Lobby_ObliterationView` · `UI_Lobby_SendChatMessage` · `UI_ModManager` · `UI_NametagList` · `UI_NametagList_PreviewWindow` · `UI_PlayRewardAnnouncer` · `UI_PlayerStardust` · `UI_ProfileStatistics` · `UI_ProfileStatistics_ItemBase` · `UI_RegisterTooltipCallbacks` · `UI_SelectControlPresetWindow` · `UI_SkinList` · `UI_SkinList_Item` · `UI_SkinList_PreviewWindow` · `UI_TitleDescTooltip` · `UI_Title_ProfileSelection_LinkEnterCodeWindow` · `UI_TooltipManager` · `UI_TooltipSection` · `UI_Tooltip_ObjEditSkillActions` · `UI_Tooltip_SkillStarDescriber` · `UI_TravelerStory_HeroNode`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
