# Enums & Constants

Comprehensive reference of all **118 enumerations** and **609 constant values** extracted directly from *Shape of Dreams* game assemblies (`Dew.Core.dll`, `Dew.UI.dll`).

> [!TIP]
> Use these exact integer and hexadecimal values when crafting mods, intercepting network RPCs (`[Server]`/`[ClientRpc]`), reading save variables (`[SaveVar]`), or invoking hero skill triggers. Click any enum in the index to jump to its members.

## Quick Index

| Enum Name | Assembly | Kind | Constants Count |
| :--- | :--- | :--- | :--- |
| [`AccAttachPointType`](#accattachpointtype) | `Dew.Core.dll` | `enum` | 9 |
| [`AccType`](#acctype) | `Dew.Core.dll` | `enum` | 2 |
| [`AffordType`](#affordtype) | `Dew.Core.dll` | `enum` | 6 |
| [`AimAssistType`](#aimassisttype) | `Dew.Core.dll` | `enum` | 4 |
| [`AllowMidJoinType`](#allowmidjointype) | `Dew.Core.dll` | `enum` | 3 |
| [`ArrowFollowMode`](#arrowfollowmode) | `Dew.Core.dll` | `enum` | 3 |
| [`AttackEffectType`](#attackeffecttype) | `Dew.Core.dll` | `enum` | 3 |
| [`AudioSpaceType`](#audiospacetype) | `Dew.Core.dll` | `enum` | 2 |
| [`AudioType`](#audiotype) | `Dew.Core.dll` | `enum` | 8 |
| [`BackgroundAudioBehavior`](#backgroundaudiobehavior) | `Dew.Core.dll` | `enum` | 3 |
| [`BasicEffectMask`](#basiceffectmask) | `Dew.Core.dll` | `[Flags]` | 24 |
| [`BindingType`](#bindingtype) | `Dew.Core.dll` | `[Flags]` | 4 |
| [`BoxPlacementMode`](#boxplacementmode) | `Dew.Core.dll` | `enum` | 3 |
| [`BoxTelegraphAnimType`](#boxtelegraphanimtype) | `Dew.Core.dll` | `enum` | 4 |
| [`BuildFeatureTag`](#buildfeaturetag) | `Dew.Core.dll` | `enum` | 4 |
| [`BuildType`](#buildtype) | `Dew.Core.dll` | `enum` | 4 |
| [`CastConfirmType`](#castconfirmtype) | `Dew.Core.dll` | `enum` | 3 |
| [`CastMethodType`](#castmethodtype) | `Dew.Core.dll` | `enum` | 5 |
| [`CenterMessageType`](#centermessagetype) | `Dew.Core.dll` | `enum` | 2 |
| [`ChaosRewardType`](#chaosrewardtype) | `Dew.Core.dll` | `enum` | 8 |
| [`ClientTransportChoice`](#clienttransportchoice) | `Dew.Core.dll` | `enum` | 2 |
| [`CombatAreaActivateCondition`](#combatareaactivatecondition) | `Dew.Core.dll` | `enum` | 2 |
| [`ConfirmMemoryEditBehavior`](#confirmmemoryeditbehavior) | `Dew.Core.dll` | `enum` | 3 |
| [`ConsoleBindItemType`](#consolebinditemtype) | `Dew.Core.dll` | `enum` | 2 |
| [`ControllerButtonType`](#controllerbuttontype) | `Dew.Core.dll` | `enum` | 3 |
| [`ConversationVisibility`](#conversationvisibility) | `Dew.Core.dll` | `enum` | 2 |
| [`CorruptedChaosRewardType`](#corruptedchaosrewardtype) | `Dew.Core.dll` | `enum` | 12 |
| [`CosmeticPurchasePrerequisite`](#cosmeticpurchaseprerequisite) | `Dew.Core.dll` | `enum` | 7 |
| [`CurrencyType`](#currencytype) | `Dew.Core.dll` | `enum` | 5 |
| [`DamageAttribute`](#damageattribute) | `Dew.Core.dll` | `[Flags]` | 10 |
| [`DamageNumberVisibility`](#damagenumbervisibility) | `Dew.Core.dll` | `enum` | 3 |
| [`DashDirection`](#dashdirection) | `Dew.Core.dll` | `enum` | 3 |
| [`DescriptionTags`](#descriptiontags) | `Dew.Core.dll` | `[Flags]` | 12 |
| [`DevelopmentBuildMode`](#developmentbuildmode) | `Dew.Core.dll` | `enum` | 3 |
| [`DewAudioRollOffType`](#dewaudiorollofftype) | `Dew.Core.dll` | `enum` | 3 |
| [`DewEase`](#dewease) | `Dew.Core.dll` | `enum` | 32 |
| [`DewExceptionType`](#dewexceptiontype) | `Dew.Core.dll` | `enum` | 44 |
| [`DewLobbyType`](#dewlobbytype) | `Dew.Core.dll` | `enum` | 2 |
| [`DewNetworkMode`](#dewnetworkmode) | `Dew.Core.dll` | `enum` | 5 |
| [`DewProfileState`](#dewprofilestate) | `Dew.Core.dll` | `enum` | 5 |
| [`DewSubProfileState`](#dewsubprofilestate) | `Dew.Core.dll` | `enum` | 3 |
| [`DewTransportPreference`](#dewtransportpreference) | `Dew.Core.dll` | `enum` | 3 |
| [`DoCommandType`](#docommandtype) | `Dew.Core.dll` | `enum` | 2 |
| [`DuplicateEffectBehavior`](#duplicateeffectbehavior) | `Dew.Core.dll` | `enum` | 3 |
| [`EditSkillTargetType`](#editskilltargettype) | `Dew.Core.dll` | `[Flags]` | 5 |
| [`EffectBindEntityType`](#effectbindentitytype) | `Dew.Core.dll` | `enum` | 3 |
| [`EffectOwnerContext`](#effectownercontext) | `Dew.Core.dll` | `enum` | 5 |
| [`EffectVisibility`](#effectvisibility) | `Dew.Core.dll` | `enum` | 5 |
| [`ElementalType`](#elementaltype) | `Dew.Core.dll` | `enum` | 4 |
| [`EnterGroupBehavior`](#entergroupbehavior) | `Dew.Core.dll` | `enum` | 11 |
| [`EntityRelation`](#entityrelation) | `Dew.Core.dll` | `[Flags]` | 4 |
| [`EntityVisualPointType`](#entityvisualpointtype) | `Dew.Core.dll` | `enum` | 8 |
| [`ExpressionChildNodeType`](#expressionchildnodetype) | `Dew.Core.dll` | `enum` | 2 |
| [`FailReason`](#failreason) | `Dew.Core.dll` | `enum` | 3 |
| [`FocusableBehavior`](#focusablebehavior) | `Dew.Core.dll` | `enum` | 2 |
| [`GameState`](#gamestate) | `Dew.Core.dll` | `enum` | 3 |
| [`GamepadButtonEx`](#gamepadbuttonex) | `Dew.Core.dll` | `enum` | 32 |
| [`GamepadNavigation`](#gamepadnavigation) | `Dew.Core.dll` | `enum` | 7 |
| [`HatredStrengthType`](#hatredstrengthtype) | `Dew.Core.dll` | `[Flags]` | 4 |
| [`HeroSkillLocation`](#heroskilllocation) | `Dew.Core.dll` | `enum` | 6 |
| [`HunterStatus`](#hunterstatus) | `Dew.Core.dll` | `enum` | 5 |
| [`InputMode`](#inputmode) | `Dew.Core.dll` | `enum` | 2 |
| [`InteractableStatus`](#interactablestatus) | `Dew.Core.dll` | `enum` | 4 |
| [`JoystickClickAction`](#joystickclickaction) | `Dew.Core.dll` | `enum` | 3 |
| [`KnockUpStrength`](#knockupstrength) | `Dew.Core.dll` | `enum` | 3 |
| [`LevelScaling`](#levelscaling) | `Dew.Core.dll` | `enum` | 3 |
| [`LimboDepthState`](#limbodepthstate) | `Dew.Core.dll` | `enum` | 3 |
| [`LineType`](#linetype) | `Dew.Core.dll` | `enum` | 3 |
| [`LoadingStatus`](#loadingstatus) | `Dew.Core.dll` | `enum` | 16 |
| [`LobbyConnectionQuality`](#lobbyconnectionquality) | `Dew.Core.dll` | `enum` | 5 |
| [`LobbyMessageType`](#lobbymessagetype) | `Dew.Core.dll` | `enum` | 1 |
| [`LocaleNodeType`](#localenodetype) | `Dew.Core.dll` | `enum` | 3 |
| [`LucidDreamType`](#luciddreamtype) | `Dew.Core.dll` | `enum` | 3 |
| [`MapCellType`](#mapcelltype) | `Dew.Core.dll` | `enum` | 3 |
| [`MapItemOrder`](#mapitemorder) | `Dew.UI.dll` | `enum` | 7 |
| [`MapItemVisibility`](#mapitemvisibility) | `Dew.Core.dll` | `enum` | 4 |
| [`MerchandiseType`](#merchandisetype) | `Dew.Core.dll` | `enum` | 5 |
| [`MidJoinBanType`](#midjoinbantype) | `Dew.Core.dll` | `enum` | 3 |
| [`MidJoinWaitType`](#midjoinwaittype) | `Dew.Core.dll` | `enum` | 5 |
| [`ModItemState`](#moditemstate) | `Dew.Core.dll` | `enum` | 3 |
| [`ModSourceType`](#modsourcetype) | `Dew.Core.dll` | `enum` | 2 |
| [`ModifierSpawnType`](#modifierspawntype) | `Dew.Core.dll` | `enum` | 3 |
| [`MonsterSpawnConditionType`](#monsterspawnconditiontype) | `Dew.Core.dll` | `enum` | 3 |
| [`MouseButton`](#mousebutton) | `Dew.Core.dll` | `enum` | 8 |
| [`NodeModifierVisibility`](#nodemodifiervisibility) | `Dew.Core.dll` | `enum` | 4 |
| [`OverpopulationBehavior`](#overpopulationbehavior) | `Dew.Core.dll` | `enum` | 3 |
| [`PlatformType`](#platformtype) | `Dew.Core.dll` | `enum` | 3 |
| [`PlayerState`](#playerstate) | `Dew.Core.dll` | `enum` | 4 |
| [`Quality3Levels`](#quality3levels) | `Dew.Core.dll` | `enum` | 3 |
| [`Quality4Levels`](#quality4levels) | `Dew.Core.dll` | `enum` | 4 |
| [`QualityOff3Levels`](#qualityoff3levels) | `Dew.Core.dll` | `enum` | 4 |
| [`QualityOff4Levels`](#qualityoff4levels) | `Dew.Core.dll` | `enum` | 5 |
| [`QuestProgressType`](#questprogresstype) | `Dew.Core.dll` | `enum` | 5 |
| [`QuestState`](#queststate) | `Dew.Core.dll` | `enum` | 3 |
| [`QuestType`](#questtype) | `Dew.Core.dll` | `enum` | 4 |
| [`Rarity`](#rarity) | `Dew.Core.dll` | `enum` | 7 |
| [`ReduceOtherPlayerEffectsStrength`](#reduceotherplayereffectsstrength) | `Dew.Core.dll` | `enum` | 5 |
| [`ResourceLinkBy`](#resourcelinkby) | `Dew.Core.dll` | `enum` | 4 |
| [`RoomRewardFlowItemType`](#roomrewardflowitemtype) | `Dew.Core.dll` | `enum` | 5 |
| [`SaveVarFlags`](#savevarflags) | `Dew.Core.dll` | `[Flags]` | 3 |
| [`ScaleWithDifficultyMode`](#scalewithdifficultymode) | `Dew.Core.dll` | `enum` | 3 |
| [`SectionCombatAreaType`](#sectioncombatareatype) | `Dew.Core.dll` | `enum` | 3 |
| [`SelectionDisplayType`](#selectiondisplaytype) | `Dew.Core.dll` | `enum` | 3 |
| [`ServiceStatus`](#servicestatus) | `Dew.Core.dll` | `enum` | 3 |
| [`SkillType`](#skilltype) | `Dew.Core.dll` | `enum` | 2 |
| [`SkinRarity`](#skinrarity) | `Dew.Core.dll` | `enum` | 4 |
| [`StarType`](#startype) | `Dew.Core.dll` | `enum` | 4 |
| [`StoryChunkState`](#storychunkstate) | `Dew.UI.dll` | `enum` | 3 |
| [`StoryNodeState`](#storynodestate) | `Dew.UI.dll` | `enum` | 3 |
| [`SyncTransformChannel`](#synctransformchannel) | `Dew.Core.dll` | `[Flags]` | 4 |
| [`TeamRelation`](#teamrelation) | `Dew.Core.dll` | `[Flags]` | 4 |
| [`TooltipPositionMode`](#tooltippositionmode) | `Dew.UI.dll` | `enum` | 2 |
| [`TutorialHighlightTextPlacement`](#tutorialhighlighttextplacement) | `Dew.Core.dll` | `enum` | 4 |
| [`UnlockStatus`](#unlockstatus) | `Dew.Core.dll` | `enum` | 3 |
| [`VoteType`](#votetype) | `Dew.Core.dll` | `enum` | 5 |
| [`WorldDisplayStatus`](#worlddisplaystatus) | `Dew.Core.dll` | `enum` | 3 |
| [`WorldNodeStatus`](#worldnodestatus) | `Dew.Core.dll` | `enum` | 4 |
| [`WorldNodeType`](#worldnodetype) | `Dew.Core.dll` | `enum` | 7 |

---

## Enumeration Details

### `AccAttachPointType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`HatGlasses`** | `0` | `0x0` |
| **`HatCigar`** | `1` | `0x1` |
| **`HatTopper`** | `2` | `0x2` |
| **`HatAliveTopper`** | `3` | `0x3` |
| **`HatHeadCover`** | `4` | `0x4` |
| **`HatHalo`** | `5` | `0x5` |
| **`HatCustom`** | `100` | `0x64` |
| **`HipSideBelt`** | `200` | `0xC8` |
| **`HipCustom`** | `300` | `0x12C` |

### `AccType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Hat`** | `0` | `0x0` |
| **`Hip`** | `1` | `0x1` |

### `AffordType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Yes`** | `0` | `0x0` |
| **`NoGold`** | `1` | `0x1` |
| **`NoDreamDust`** | `2` | `0x2` |
| **`NoStardust`** | `3` | `0x3` |
| **`NoHealth`** | `4` | `0x4` |
| **`NoPlatinumCoin`** | `5` | `0x5` |

### `AimAssistType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Medium`** | `1` | `0x1` |
| **`High`** | `2` | `0x2` |
| **`VeryHigh`** | `3` | `0x3` |

### `AllowMidJoinType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`AllowAll`** | `0` | `0x0` |
| **`RejoinOnly`** | `1` | `0x1` |
| **`Disallow`** | `2` | `0x2` |

### `ArrowFollowMode`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`World`** | `1` | `0x1` |
| **`Screen`** | `2` | `0x2` |

### `AttackEffectType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`BasicAttackMain`** | `0` | `0x0` |
| **`BasicAttackSub`** | `1` | `0x1` |
| **`Others`** | `2` | `0x2` |

### `AudioSpaceType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Normal`** | `0` | `0x0` |
| **`Global`** | `1` | `0x1` |

### `AudioType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`UI`** | `0` | `0x0` |
| **`Music`** | `1` | `0x1` |
| **`SFX`** | `2` | `0x2` |
| **`GameBoss`** | `3` | `0x3` |
| **`GameSelf`** | `4` | `0x4` |
| **`GameOtherPlayers`** | `7` | `0x7` |
| **`GameOthers`** | `5` | `0x5` |
| **`GameEnvironment`** | `6` | `0x6` |

### `BackgroundAudioBehavior`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Mute`** | `0` | `0x0` |
| **`MuteMusic`** | `1` | `0x1` |
| **`Full`** | `2` | `0x2` |

### `BasicEffectMask`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Slow`** | `1` | `0x1` |
| **`Speed`** | `2` | `0x2` |
| **`Haste`** | `4` | `0x4` |
| **`Cripple`** | `8` | `0x8` |
| **`Root`** | `16` | `0x10` |
| **`Silence`** | `32` | `0x20` |
| **`Stun`** | `64` | `0x40` |
| **`Blind`** | `128` | `0x80` |
| **`AttackCritical`** | `256` | `0x100` |
| **`AttackOverride`** | `512` | `0x200` |
| **`AttackEmpower`** | `1024` | `0x400` |
| **`Invulnerable`** | `2048` | `0x800` |
| **`Unstoppable`** | `4096` | `0x1000` |
| **`Protected`** | `8192` | `0x2000` |
| **`Uncollidable`** | `16384` | `0x4000` |
| **`Untargetable`** | `32768` | `0x8000` |
| **`ArmorBoost`** | `65536` | `0x10000` |
| **`ArmorReduction`** | `131072` | `0x20000` |
| **`DeathInterrupt`** | `262144` | `0x40000` |
| **`Shield`** | `524288` | `0x80000` |
| **`HealReduction`** | `1048576` | `0x100000` |
| **`FakeMaxHealth`** | `2097152` | `0x200000` |
| **`Invisible`** | `4194304` | `0x400000` |
| **`Reveal`** | `8388608` | `0x800000` |

### `BindingType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Keyboard`** | `1` | `0x1` |
| **`Mouse`** | `2` | `0x2` |
| **`Gamepad`** | `4` | `0x4` |

### `BoxPlacementMode`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`TowardsCenter`** | `0` | `0x0` |
| **`AwayFromCenter`** | `1` | `0x1` |
| **`Below`** | `2` | `0x2` |

### `BoxTelegraphAnimType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Center`** | `1` | `0x1` |
| **`FromStart`** | `2` | `0x2` |
| **`FromEnd`** | `3` | `0x3` |

### `BuildFeatureTag`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Booth`** | `0` | `0x0` |
| **`Prologue`** | `1` | `0x1` |
| **`UnlockEverything`** | `2` | `0x2` |
| **`TravelerStory`** | `3` | `0x3` |

### `BuildType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Indev`** | `0` | `0x0` |
| **`DemoLite`** | `1` | `0x1` |
| **`DemoPrivate`** | `2` | `0x2` |
| **`Release`** | `3` | `0x3` |

### `CastConfirmType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Normal`** | `0` | `0x0` |
| **`Immediately`** | `1` | `0x1` |
| **`OnRelease`** | `2` | `0x2` |

### `CastMethodType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Cone`** | `1` | `0x1` |
| **`Arrow`** | `2` | `0x2` |
| **`Target`** | `3` | `0x3` |
| **`Point`** | `4` | `0x4` |

### `CenterMessageType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`General`** | `0` | `0x0` |
| **`Error`** | `1` | `0x1` |

### `ChaosRewardType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`MaxHealth`** | `0` | `0x0` |
| **`AttackDamage`** | `1` | `0x1` |
| **`AttackSpeed`** | `2` | `0x2` |
| **`AbilityPower`** | `3` | `0x3` |
| **`AbilityHaste`** | `4` | `0x4` |
| **`UpgradeGem`** | `5` | `0x5` |
| **`UpgradeSkill`** | `6` | `0x6` |
| **`Armor`** | `7` | `0x7` |

### `ClientTransportChoice`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Eos`** | `0` | `0x0` |
| **`Steam`** | `1` | `0x1` |

### `CombatAreaActivateCondition`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`OnEnterFirstTime`** | `0` | `0x0` |
| **`OnEveryonePresent`** | `1` | `0x1` |

### `ConfirmMemoryEditBehavior`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`All`** | `0` | `0x0` |
| **`SellOnly`** | `1` | `0x1` |
| **`Off`** | `2` | `0x2` |

### `ConsoleBindItemType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Down`** | `0` | `0x0` |
| **`Up`** | `1` | `0x1` |

### `ControllerButtonType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Xbox`** | `1` | `0x1` |
| **`PlayStation`** | `2` | `0x2` |
| **`Generic`** | `3` | `0x3` |

### `ConversationVisibility`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Everyone`** | `0` | `0x0` |
| **`OnlyToPlayer`** | `1` | `0x1` |

### `CorruptedChaosRewardType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`AddedEssenceSlot`** | `0` | `0x0` |
| **`EveryFourAttackBonus`** | `1` | `0x1` |
| **`DodgeCooldown`** | `2` | `0x2` |
| **`DodgeCharge`** | `3` | `0x3` |
| **`AttackRange`** | `4` | `0x4` |
| **`CritChance`** | `5` | `0x5` |
| **`FireAmp`** | `6` | `0x6` |
| **`DarkMaxStack`** | `7` | `0x7` |
| **`LightMaxStack`** | `8` | `0x8` |
| **`ColdAmp`** | `9` | `0x9` |
| **`MaxLevel`** | `10` | `0xA` |
| **`MovSpdSkillHaste`** | `11` | `0xB` |

### `CosmeticPurchasePrerequisite`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`NightmareKillCount`** | `1` | `0x1` |
| **`ReachZone`** | `2` | `0x2` |
| **`HeroMastery`** | `3` | `0x3` |
| **`NightmareWin`** | `4` | `0x4` |
| **`LimboMaxDepth`** | `5` | `0x5` |
| **`WayOfStars`** | `6` | `0x6` |

### `CurrencyType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Gold`** | `0` | `0x0` |
| **`DreamDust`** | `1` | `0x1` |
| **`Stardust`** | `2` | `0x2` |
| **`Health`** | `3` | `0x3` |
| **`PlatinumCoin`** | `4` | `0x4` |

### `DamageAttribute`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`IsCrit`** | `1` | `0x1` |
| **`IgnoreArmor`** | `2` | `0x2` |
| **`IgnoreShield`** | `4` | `0x4` |
| **`IgnoreDamageImmunity`** | `8` | `0x8` |
| **`AreaOfEffect`** | `16` | `0x10` |
| **`DamageOverTime`** | `32` | `0x20` |
| **`ForceMergeNumber`** | `64` | `0x40` |
| **`DamageShieldOnly`** | `128` | `0x80` |
| **`NoTracking`** | `256` | `0x100` |

### `DamageNumberVisibility`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Off`** | `0` | `0x0` |
| **`MineOnly`** | `1` | `0x1` |
| **`All`** | `2` | `0x2` |

### `DashDirection`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`CurrentMovement`** | `0` | `0x0` |
| **`CurrentMovementOnlyDodge`** | `1` | `0x1` |
| **`AllTowardsCursor`** | `2` | `0x2` |

### `DescriptionTags`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Fire`** | `1` | `0x1` |
| **`Cold`** | `2` | `0x2` |
| **`Dark`** | `4` | `0x4` |
| **`Light`** | `8` | `0x8` |
| **`Melee`** | `16` | `0x10` |
| **`HardCC`** | `32` | `0x20` |
| **`Heal`** | `64` | `0x40` |
| **`Shield`** | `128` | `0x80` |
| **`Attack`** | `256` | `0x100` |
| **`Mobility`** | `512` | `0x200` |
| **`Summon`** | `1024` | `0x400` |

### `DevelopmentBuildMode`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Full`** | `1` | `0x1` |
| **`LeanProfiling`** | `2` | `0x2` |

### `DewAudioRollOffType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Default`** | `0` | `0x0` |
| **`Loud`** | `1` | `0x1` |
| **`Unity`** | `2` | `0x2` |

### `DewEase`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Linear`** | `0` | `0x0` |
| **`EaseInQuad`** | `1` | `0x1` |
| **`EaseOutQuad`** | `2` | `0x2` |
| **`EaseInOutQuad`** | `3` | `0x3` |
| **`EaseInCubic`** | `4` | `0x4` |
| **`EaseOutCubic`** | `5` | `0x5` |
| **`EaseInOutCubic`** | `6` | `0x6` |
| **`EaseInQuart`** | `7` | `0x7` |
| **`EaseOutQuart`** | `8` | `0x8` |
| **`EaseInOutQuart`** | `9` | `0x9` |
| **`EaseInQuint`** | `10` | `0xA` |
| **`EaseOutQuint`** | `11` | `0xB` |
| **`EaseInOutQuint`** | `12` | `0xC` |
| **`EaseInSine`** | `13` | `0xD` |
| **`EaseOutSine`** | `14` | `0xE` |
| **`EaseInOutSine`** | `15` | `0xF` |
| **`EaseInExpo`** | `16` | `0x10` |
| **`EaseOutExpo`** | `17` | `0x11` |
| **`EaseInOutExpo`** | `18` | `0x12` |
| **`EaseInCirc`** | `19` | `0x13` |
| **`EaseOutCirc`** | `20` | `0x14` |
| **`EaseInOutCirc`** | `21` | `0x15` |
| **`Spring`** | `22` | `0x16` |
| **`EaseInBounce`** | `23` | `0x17` |
| **`EaseOutBounce`** | `24` | `0x18` |
| **`EaseInOutBounce`** | `25` | `0x19` |
| **`EaseInBack`** | `26` | `0x1A` |
| **`EaseOutBack`** | `27` | `0x1B` |
| **`EaseInOutBack`** | `28` | `0x1C` |
| **`EaseInElastic`** | `29` | `0x1D` |
| **`EaseOutElastic`** | `30` | `0x1E` |
| **`EaseInOutElastic`** | `31` | `0x1F` |

### `DewExceptionType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`GameAlreadyStarted`** | `0` | `0x0` |
| **`VersionMismatch`** | `1` | `0x1` |
| **`LobbyTimeout`** | `2` | `0x2` |
| **`UnknownLobby`** | `3` | `0x3` |
| **`Disconnected`** | `4` | `0x4` |
| **`LobbyNotFound`** | `5` | `0x5` |
| **`TooLateToMidJoin`** | `6` | `0x6` |
| **`TooManyRequests`** | `7` | `0x7` |
| **`Timeout`** | `8` | `0x8` |
| **`CannotResolveDestinationHost`** | `9` | `0x9` |
| **`NoInternetConnection`** | `10` | `0xA` |
| **`SaveLoadFailed_SaveCorrupt`** | `11` | `0xB` |
| **`SaveLoadFailed_NewSaveFailed`** | `12` | `0xC` |
| **`SteamAuthGetTicketFailed`** | `13` | `0xD` |
| **`SteamAuthFailed`** | `14` | `0xE` |
| **`SteamNotAvailable`** | `15` | `0xF` |
| **`UnknownItem`** | `16` | `0x10` |
| **`InvalidResponseFromItemServer`** | `17` | `0x11` |
| **`FailedToGetItemGeneric`** | `18` | `0x12` |
| **`ItemNotEligible`** | `19` | `0x13` |
| **`InvalidGiftCode`** | `20` | `0x14` |
| **`UsedCode`** | `21` | `0x15` |
| **`AlreadyHaveThisGift`** | `22` | `0x16` |
| **`CorruptGameFiles`** | `23` | `0x17` |
| **`MidJoinBlockedBeforeBossFight`** | `24` | `0x18` |
| **`MidJoinBlockedFightingBoss`** | `25` | `0x19` |
| **`MidJoinBlockedAfterBossFight`** | `26` | `0x1A` |
| **`GameHasEnded`** | `27` | `0x1B` |
| **`UnknownError`** | `28` | `0x1C` |
| **`DuplicatePlayerInGame`** | `29` | `0x1D` |
| **`MidJoinOnlyRejoinAllowed`** | `30` | `0x1E` |
| **`CrossPlayMismatch`** | `31` | `0x1F` |
| **`LobbyFull`** | `32` | `0x20` |
| **`LobbyConnectionFailed`** | `33` | `0x21` |
| **`ModdedLobbyBlocked`** | `34` | `0x22` |
| **`AccountLinkNotAvailable`** | `35` | `0x23` |
| **`AccountLinkInvalidIdToken`** | `36` | `0x24` |
| **`AccountLinkCodeInvalid`** | `37` | `0x25` |
| **`AccountLinkFailed`** | `38` | `0x26` |
| **`CloudSaveUnavailable`** | `39` | `0x27` |
| **`CloudSaveFailed`** | `40` | `0x28` |
| **`CloudSaveVersionUnsupported`** | `41` | `0x29` |
| **`CloudSaveFileNotFound`** | `42` | `0x2A` |
| **`CloudSaveOwnedElsewhere`** | `43` | `0x2B` |

### `DewLobbyType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Public`** | `0` | `0x0` |
| **`InviteOnly`** | `1` | `0x1` |

### `DewNetworkMode`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Singleplayer`** | `0` | `0x0` |
| **`MultiplayerHost`** | `1` | `0x1` |
| **`MultiplayerJoinLobby`** | `2` | `0x2` |
| **`MultiplayerHostRestart`** | `3` | `0x3` |
| **`MultiplayerJoinRestart`** | `4` | `0x4` |

### `DewProfileState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Normal`** | `0` | `0x0` |
| **`Convertible`** | `1` | `0x1` |
| **`UnsupportedEdition`** | `2` | `0x2` |
| **`UnsupportedVersion`** | `3` | `0x3` |
| **`Corrupted`** | `4` | `0x4` |

### `DewSubProfileState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Normal`** | `0` | `0x0` |
| **`Corrupted`** | `1` | `0x1` |
| **`NonExistent`** | `2` | `0x2` |

### `DewTransportPreference`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Auto`** | `0` | `0x0` |
| **`ForceEOS`** | `1` | `0x1` |
| **`ForceSteam`** | `2` | `0x2` |

### `DoCommandType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Default`** | `0` | `0x0` |
| **`PostponeBasicCommand`** | `1` | `0x1` |

### `DuplicateEffectBehavior`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`UsePrevious`** | `0` | `0x0` |
| **`ReplacePrevious`** | `1` | `0x1` |
| **`DoNothing`** | `2` | `0x2` |

### `EditSkillTargetType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Skill`** | `1` | `0x1` |
| **`SkillEmptySlot`** | `2` | `0x2` |
| **`Gem`** | `4` | `0x4` |
| **`GemEmptySlot`** | `8` | `0x8` |

### `EffectBindEntityType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`FindType`** | `1` | `0x1` |
| **`LocalHero`** | `2` | `0x2` |

### `EffectOwnerContext`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Self`** | `1` | `0x1` |
| **`Boss`** | `2` | `0x2` |
| **`OtherPlayers`** | `3` | `0x3` |
| **`Others`** | `4` | `0x4` |

### `EffectVisibility`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Everyone`** | `0` | `0x0` |
| **`Caster`** | `1` | `0x1` |
| **`Target`** | `2` | `0x2` |
| **`Victim`** | `3` | `0x3` |
| **`Owner`** | `4` | `0x4` |

### `ElementalType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Fire`** | `0` | `0x0` |
| **`Cold`** | `1` | `0x1` |
| **`Light`** | `2` | `0x2` |
| **`Dark`** | `3` | `0x3` |

### `EnterGroupBehavior`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`UseDistanceFromPrevious`** | `0` | `0x0` |
| **`PrioritizeLT`** | `1` | `0x1` |
| **`PrioritizeRT`** | `2` | `0x2` |
| **`PrioritizeLB`** | `3` | `0x3` |
| **`PrioritizeRB`** | `4` | `0x4` |
| **`PrioritizeTop`** | `5` | `0x5` |
| **`PrioritizeLeft`** | `6` | `0x6` |
| **`PrioritizeRight`** | `7` | `0x7` |
| **`PrioritizeBottom`** | `8` | `0x8` |
| **`UseEnterDirection`** | `9` | `0x9` |
| **`Custom`** | `20` | `0x14` |

### `EntityRelation`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Self`** | `1` | `0x1` |
| **`Neutral`** | `2` | `0x2` |
| **`Enemy`** | `4` | `0x4` |
| **`Ally`** | `8` | `0x8` |

### `EntityVisualPointType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Head`** | `3` | `0x3` |
| **`LeftHand`** | `4` | `0x4` |
| **`RightHand`** | `5` | `0x5` |
| **`LeftFoot`** | `6` | `0x6` |
| **`RightFoot`** | `7` | `0x7` |
| **`Weapon`** | `8` | `0x8` |
| **`Muzzle`** | `9` | `0x9` |
| **`Center`** | `10` | `0xA` |

### `ExpressionChildNodeType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `DewInternal`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`FieldName`** | `0` | `0x0` |
| **`Expression`** | `1` | `0x1` |

### `FailReason`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`NotSpecified`** | `0` | `0x0` |
| **`HunterOccupied`** | `1` | `0x1` |
| **`MissedDestination`** | `2` | `0x2` |

### `FocusableBehavior`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Normal`** | `0` | `0x0` |
| **`BottomBar`** | `1` | `0x1` |

### `GameState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`InLobby`** | `0` | `0x0` |
| **`Starting`** | `1` | `0x1` |
| **`InGame`** | `2` | `0x2` |

### `GamepadButtonEx`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`DpadUp`** | `0` | `0x0` |
| **`DpadDown`** | `1` | `0x1` |
| **`DpadLeft`** | `2` | `0x2` |
| **`DpadRight`** | `3` | `0x3` |
| **`North`** | `4` | `0x4` |
| **`Triangle`** | `4` | `0x4` |
| **`Y`** | `4` | `0x4` |
| **`B`** | `5` | `0x5` |
| **`Circle`** | `5` | `0x5` |
| **`East`** | `5` | `0x5` |
| **`A`** | `6` | `0x6` |
| **`Cross`** | `6` | `0x6` |
| **`South`** | `6` | `0x6` |
| **`Square`** | `7` | `0x7` |
| **`West`** | `7` | `0x7` |
| **`X`** | `7` | `0x7` |
| **`LeftStick`** | `8` | `0x8` |
| **`RightStick`** | `9` | `0x9` |
| **`LeftShoulder`** | `10` | `0xA` |
| **`RightShoulder`** | `11` | `0xB` |
| **`Start`** | `12` | `0xC` |
| **`Select`** | `13` | `0xD` |
| **`LeftTrigger`** | `32` | `0x20` |
| **`RightTrigger`** | `33` | `0x21` |
| **`LeftStickUp`** | `1000` | `0x3E8` |
| **`LeftStickDown`** | `1001` | `0x3E9` |
| **`LeftStickLeft`** | `1002` | `0x3EA` |
| **`LeftStickRight`** | `1003` | `0x3EB` |
| **`RightStickUp`** | `1010` | `0x3F2` |
| **`RightStickDown`** | `1011` | `0x3F3` |
| **`RightStickLeft`** | `1012` | `0x3F4` |
| **`RightStickRight`** | `1013` | `0x3F5` |

### `GamepadNavigation`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Generic`** | `0` | `0x0` |
| **`Grid`** | `10` | `0xA` |
| **`GridWrapAround`** | `11` | `0xB` |
| **`GridLong`** | `12` | `0xC` |
| **`Wide`** | `20` | `0x14` |
| **`HeroInfoBar`** | `100` | `0x64` |
| **`Custom`** | `255` | `0xFF` |

### `HatredStrengthType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Mild`** | `1` | `0x1` |
| **`Potent`** | `2` | `0x2` |
| **`Powerful`** | `4` | `0x4` |

### `HeroSkillLocation`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Q`** | `0` | `0x0` |
| **`W`** | `1` | `0x1` |
| **`E`** | `2` | `0x2` |
| **`R`** | `3` | `0x3` |
| **`Identity`** | `4` | `0x4` |
| **`Movement`** | `5` | `0x5` |

### `HunterStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`AboutToBeTaken`** | `1` | `0x1` |
| **`Level1`** | `100` | `0x64` |
| **`Level2`** | `101` | `0x65` |
| **`Level3`** | `102` | `0x66` |

### `InputMode`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`KeyboardAndMouse`** | `0` | `0x0` |
| **`Gamepad`** | `1` | `0x1` |

### `InteractableStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`No`** | `0` | `0x0` |
| **`Yes`** | `1` | `0x1` |
| **`YesWithAlt`** | `2` | `0x2` |
| **`YesWithHoldAlt`** | `3` | `0x3` |

### `JoystickClickAction`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Dodge`** | `1` | `0x1` |
| **`PingAndEmotes`** | `2` | `0x2` |

### `KnockUpStrength`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Small`** | `0` | `0x0` |
| **`Normal`** | `1` | `0x1` |
| **`Big`** | `2` | `0x2` |

### `LevelScaling`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`NoScaling`** | `0` | `0x0` |
| **`SkillDefault`** | `1` | `0x1` |
| **`GemDefault`** | `2` | `0x2` |

### `LimboDepthState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Available`** | `0` | `0x0` |
| **`Completed`** | `1` | `0x1` |
| **`Locked`** | `2` | `0x2` |

### `LineType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `DewInternal`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Say`** | `0` | `0x0` |
| **`Choice`** | `1` | `0x1` |
| **`Action`** | `2` | `0x2` |

### `LoadingStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Empty`** | `0` | `0x0` |
| **`WaitingForService`** | `1` | `0x1` |
| **`CheckingLobbyStatus`** | `2` | `0x2` |
| **`CleaningUpPreviousLobby`** | `3` | `0x3` |
| **`LeavingPreviousLobby`** | `4` | `0x4` |
| **`CreatingLobby`** | `5` | `0x5` |
| **`PreparingLobby`** | `6` | `0x6` |
| **`PreparingLobbyClient`** | `7` | `0x7` |
| **`WaitingForHostPlayer`** | `8` | `0x8` |
| **`ConnectingToGame`** | `9` | `0x9` |
| **`ConnectingToLobby`** | `10` | `0xA` |
| **`CreatingGame`** | `11` | `0xB` |
| **`GettingLobbyInformation`** | `12` | `0xC` |
| **`WaitingForSteam`** | `13` | `0xD` |
| **`WaitingForOtherPlayers`** | `14` | `0xE` |
| **`RequestingItemFromServer`** | `15` | `0xF` |

### `LobbyConnectionQuality`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Unknown`** | `0` | `0x0` |
| **`Bad`** | `1` | `0x1` |
| **`Okay`** | `2` | `0x2` |
| **`Good`** | `3` | `0x3` |
| **`Best`** | `4` | `0x4` |

### `LobbyMessageType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`GameServerAddress`** | `0` | `0x0` |

### `LocaleNodeType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `DewInternal`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Text`** | `0` | `0x0` |
| **`Expression`** | `1` | `0x1` |
| **`Tag`** | `2` | `0x2` |

### `LucidDreamType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Good`** | `0` | `0x0` |
| **`Evil`** | `1` | `0x1` |
| **`Chaotic`** | `2` | `0x2` |

### `MapCellType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Playable`** | `1` | `0x1` |
| **`Wall`** | `2` | `0x2` |

### `MapItemOrder`

- **Assembly:** `Dew.UI.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Default`** | `0` | `0x0` |
| **`Shrines`** | `0` | `0x0` |
| **`Waypoints`** | `0` | `0x0` |
| **`NonImportantEntities`** | `1` | `0x1` |
| **`HeroicAllies`** | `3` | `0x3` |
| **`HeroicEnemies`** | `4` | `0x4` |
| **`LocalHero`** | `5` | `0x5` |

### `MapItemVisibility`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Always`** | `0` | `0x0` |
| **`NeedsToBeDiscovered`** | `1` | `0x1` |
| **`NeedsToBeVisible`** | `2` | `0x2` |
| **`Hidden`** | `10` | `0xA` |

### `MerchandiseType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Empty`** | `0` | `0x0` |
| **`Skill`** | `1` | `0x1` |
| **`Gem`** | `2` | `0x2` |
| **`Souvenir`** | `3` | `0x3` |
| **`Treasure`** | `4` | `0x4` |

### `MidJoinBanType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`GameHasEnded`** | `1` | `0x1` |
| **`TooLateToJoin`** | `2` | `0x2` |

### `MidJoinWaitType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`BeforeBossFight`** | `10` | `0xA` |
| **`FightingBoss`** | `11` | `0xB` |
| **`AfterBossFight`** | `12` | `0xC` |
| **`HostLoadingGame`** | `20` | `0x14` |

### `ModItemState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Ok`** | `0` | `0x0` |
| **`InvalidMetadata`** | `1` | `0x1` |
| **`IdConflict`** | `2` | `0x2` |

### `ModSourceType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Local`** | `0` | `0x0` |
| **`Steam`** | `1` | `0x1` |

### `ModifierSpawnType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Chance`** | `0` | `0x0` |
| **`Ratio`** | `1` | `0x1` |
| **`Count`** | `2` | `0x2` |

### `MonsterSpawnConditionType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`CurrentZoneClearedNodes`** | `0` | `0x0` |
| **`GlobalRoomIndex`** | `1` | `0x1` |
| **`ActivatedCombatAreas`** | `2` | `0x2` |

### `MouseButton`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Left`** | `1` | `0x1` |
| **`Right`** | `2` | `0x2` |
| **`Middle`** | `3` | `0x3` |
| **`Forward`** | `4` | `0x4` |
| **`Back`** | `5` | `0x5` |
| **`ScrollUp`** | `6` | `0x6` |
| **`ScrollDown`** | `7` | `0x7` |

### `NodeModifierVisibility`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`OnRevealed`** | `0` | `0x0` |
| **`OnRevealedFull`** | `1` | `0x1` |
| **`Hidden`** | `2` | `0x2` |
| **`Always`** | `3` | `0x3` |

### `OverpopulationBehavior`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Stall`** | `0` | `0x0` |
| **`Cancel`** | `1` | `0x1` |
| **`Ignore`** | `2` | `0x2` |

### `PlatformType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`DRMFREE`** | `0` | `0x0` |
| **`STEAM`** | `1` | `0x1` |
| **`STOVE`** | `2` | `0x2` |

### `PlayerState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`InLobby`** | `1` | `0x1` |
| **`Playing`** | `2` | `0x2` |
| **`Spectating`** | `3` | `0x3` |

### `Quality3Levels`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Low`** | `1` | `0x1` |
| **`Medium`** | `2` | `0x2` |
| **`High`** | `3` | `0x3` |

### `Quality4Levels`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Low`** | `1` | `0x1` |
| **`Medium`** | `2` | `0x2` |
| **`High`** | `3` | `0x3` |
| **`Ultra`** | `4` | `0x4` |

### `QualityOff3Levels`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Off`** | `0` | `0x0` |
| **`Low`** | `1` | `0x1` |
| **`Medium`** | `2` | `0x2` |
| **`High`** | `3` | `0x3` |

### `QualityOff4Levels`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Off`** | `0` | `0x0` |
| **`Low`** | `1` | `0x1` |
| **`Medium`** | `2` | `0x2` |
| **`High`** | `3` | `0x3` |
| **`Ultra`** | `4` | `0x4` |

### `QuestProgressType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Hidden`** | `0` | `0x0` |
| **`Kills`** | `1` | `0x1` |
| **`Travel`** | `2` | `0x2` |
| **`Collect`** | `3` | `0x3` |
| **`TravelZone`** | `4` | `0x4` |

### `QuestState`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Ongoing`** | `0` | `0x0` |
| **`Completed`** | `1` | `0x1` |
| **`Failed`** | `2` | `0x2` |

### `QuestType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Goal`** | `0` | `0x0` |
| **`Curse`** | `1` | `0x1` |
| **`Tutorial`** | `2` | `0x2` |
| **`Quest`** | `3` | `0x3` |

### `Rarity`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Common`** | `0` | `0x0` |
| **`Rare`** | `1` | `0x1` |
| **`Epic`** | `2` | `0x2` |
| **`Legendary`** | `3` | `0x3` |
| **`Character`** | `4` | `0x4` |
| **`Identity`** | `5` | `0x5` |
| **`Unique`** | `10` | `0xA` |

### `ReduceOtherPlayerEffectsStrength`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Low`** | `0` | `0x0` |
| **`Medium`** | `1` | `0x1` |
| **`High`** | `2` | `0x2` |
| **`VeryHigh`** | `3` | `0x3` |
| **`Hide`** | `4` | `0x4` |

### `ResourceLinkBy`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Type`** | `1` | `0x1` |
| **`Guid`** | `2` | `0x2` |
| **`Name`** | `3` | `0x3` |

### `RoomRewardFlowItemType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Skill`** | `1` | `0x1` |
| **`Gem`** | `2` | `0x2` |
| **`Any`** | `3` | `0x3` |
| **`Luck`** | `4` | `0x4` |

### `SaveVarFlags`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Default`** | `0` | `0x0` |
| **`ApplyAfterCreation`** | `1` | `0x1` |
| **`ApplyAfterFrameDelay`** | `2` | `0x2` |

### `ScaleWithDifficultyMode`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Beneficial`** | `1` | `0x1` |
| **`Harmful`** | `2` | `0x2` |

### `SectionCombatAreaType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Random`** | `0` | `0x0` |
| **`Yes`** | `1` | `0x1` |
| **`No`** | `2` | `0x2` |

### `SelectionDisplayType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Dont`** | `0` | `0x0` |
| **`Box`** | `1` | `0x1` |
| **`Circle`** | `2` | `0x2` |

### `ServiceStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Loading`** | `0` | `0x0` |
| **`Ready`** | `1` | `0x1` |
| **`Error`** | `2` | `0x2` |

### `SkillType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Normal`** | `0` | `0x0` |
| **`Ultimate`** | `1` | `0x1` |

### `SkinRarity`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Default`** | `0` | `0x0` |
| **`Rare`** | `1` | `0x1` |
| **`Epic`** | `2` | `0x2` |
| **`Legendary`** | `3` | `0x3` |

### `StarType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Destruction`** | `0` | `0x0` |
| **`Life`** | `1` | `0x1` |
| **`Imagination`** | `2` | `0x2` |
| **`Flexible`** | `3` | `0x3` |

### `StoryChunkState`

- **Assembly:** `Dew.UI.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Locked`** | `0` | `0x0` |
| **`ReadyToUnlock`** | `1` | `0x1` |
| **`Unlocked`** | `2` | `0x2` |

### `StoryNodeState`

- **Assembly:** `Dew.UI.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Locked`** | `0` | `0x0` |
| **`ReadyToUnlock`** | `1` | `0x1` |
| **`Unlocked`** | `2` | `0x2` |

### `SyncTransformChannel`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`Position`** | `1` | `0x1` |
| **`Rotation`** | `2` | `0x2` |
| **`Scale`** | `4` | `0x4` |

### `TeamRelation`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `[Flags] Bitfield`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Own`** | `1` | `0x1` |
| **`Neutral`** | `2` | `0x2` |
| **`Enemy`** | `4` | `0x4` |
| **`Ally`** | `8` | `0x8` |

### `TooltipPositionMode`

- **Assembly:** `Dew.UI.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`RawValue`** | `0` | `0x0` |
| **`Getter`** | `1` | `0x1` |

### `TutorialHighlightTextPlacement`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Left`** | `0` | `0x0` |
| **`Right`** | `1` | `0x1` |
| **`Top`** | `2` | `0x2` |
| **`Bottom`** | `3` | `0x3` |

### `UnlockStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Locked`** | `0` | `0x0` |
| **`NotDiscovered`** | `1` | `0x1` |
| **`Complete`** | `2` | `0x2` |

### `VoteType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`NextNode`** | `1` | `0x1` |
| **`NextZone`** | `2` | `0x2` |
| **`Sidetrack`** | `3` | `0x3` |
| **`TheDream`** | `4` | `0x4` |

### `WorldDisplayStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`None`** | `0` | `0x0` |
| **`ShownNoMove`** | `1` | `0x1` |
| **`Shown`** | `2` | `0x2` |

### `WorldNodeStatus`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Unexplored`** | `0` | `0x0` |
| **`Revealed`** | `1` | `0x1` |
| **`RevealedFull`** | `2` | `0x2` |
| **`HasVisited`** | `3` | `0x3` |

### `WorldNodeType`

- **Assembly:** `Dew.Core.dll`
- **Namespace:** `Global`
- **Type:** `Sequential Enum`

| Constant Name | Value (Dec) | Value (Hex) |
| :--- | :--- | :--- |
| **`Start`** | `0` | `0x0` |
| **`Combat`** | `1` | `0x1` |
| **`Event`** | `2` | `0x2` |
| **`Merchant`** | `100` | `0x64` |
| **`Quest`** | `101` | `0x65` |
| **`Special`** | `200` | `0xC8` |
| **`ExitBoss`** | `1000` | `0x3E8` |
