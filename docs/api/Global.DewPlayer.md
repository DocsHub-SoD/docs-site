# Class: DewPlayer

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public class DewPlayer : DewNetworkBehaviour, ILogicUpdate, ISettingsChangedCallback
```

## Fields (41)

::: details Click to expand Fields (41)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allHumanPlayers`** | `public static List<DewPlayer> allHumanPlayers` | All human players that are connected to the server. |
| **`allies`** | `public readonly SyncList<DewPlayer> allies` |  |
| **`availableLucidDreams`** | `[NonSerialized] public List<string> availableLucidDreams` | Available on server. |
| **`ClientEvent_OnDreamDustChanged`** | `public SafeAction<int, int> ClientEvent_OnDreamDustChanged` |  |
| **`ClientEvent_OnEarnDreamDust`** | `public SafeAction<int> ClientEvent_OnEarnDreamDust` |  |
| **`ClientEvent_OnEarnGold`** | `public SafeAction<int> ClientEvent_OnEarnGold` |  |
| **`ClientEvent_OnEarnStardust`** | `public SafeAction<int> ClientEvent_OnEarnStardust` |  |
| **`ClientEvent_OnEquippedNametagChanged`** | `public SafeAction<string, string> ClientEvent_OnEquippedNametagChanged` |  |
| **`ClientEvent_OnGiveCurrency`** | `public SafeAction<int, int, DewPlayer> ClientEvent_OnGiveCurrency` | Arguments are as follows: Gold, DreamDust, Target |
| **`ClientEvent_OnGoldChanged`** | `public SafeAction<int, int> ClientEvent_OnGoldChanged` |  |
| **`ClientEvent_OnHeroChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnHeroChanged` |  |
| **`ClientEvent_OnIsReadyChanged`** | `public SafeAction<bool> ClientEvent_OnIsReadyChanged` |  |
| **`ClientEvent_OnPlatinumCoinChanged`** | `public SafeAction<int, int> ClientEvent_OnPlatinumCoinChanged` |  |
| **`ClientEvent_OnSelectedAccessoriesChanged`** | `public SafeAction ClientEvent_OnSelectedAccessoriesChanged` |  |
| **`ClientEvent_OnSelectedDejavuItemChanged`** | `public SafeAction<string> ClientEvent_OnSelectedDejavuItemChanged` |  |
| **`ClientEvent_OnSelectedHeroTypeChanged`** | `public SafeAction<string> ClientEvent_OnSelectedHeroTypeChanged` |  |
| **`ClientEvent_OnSelectedLoadoutChanged`** | `public SafeAction<HeroLoadoutData> ClientEvent_OnSelectedLoadoutChanged` |  |
| **`ClientEvent_OnSelectedSkinChanged`** | `public SafeAction<string> ClientEvent_OnSelectedSkinChanged` |  |
| **`ClientEvent_OnSpendDreamDust`** | `public SafeAction<int> ClientEvent_OnSpendDreamDust` |  |
| **`ClientEvent_OnSpendGold`** | `public SafeAction<int> ClientEvent_OnSpendGold` |  |
| **`ClientEvent_OnSpendStardust`** | `public SafeAction<int> ClientEvent_OnSpendStardust` |  |
| **`ClientEvent_OnStateChanged`** | `public SafeAction ClientEvent_OnStateChanged` |  |
| **`enemies`** | `public readonly SyncList<DewPlayer> enemies` |  |
| **`friendSteamIds`** | `[NonSerialized] public List<string> friendSteamIds` |  |
| **`gamePlayers`** | `public static List<DewPlayer> gamePlayers` | Human players that are playing the game. |
| **`lobbyPlayers`** | `public static List<DewPlayer> lobbyPlayers` | Human players that are in the lobby. Note: players can be in the lobby even after the game has been started, if they joined mid-game. |
| **`neutrals`** | `public readonly SyncList<DewPlayer> neutrals` |  |
| **`onGamePlayerAdded`** | `public static SafeAction<DewPlayer> onGamePlayerAdded` |  |
| **`onGamePlayerRemoved`** | `public static SafeAction<DewPlayer> onGamePlayerRemoved` |  |
| **`onHumanPlayerAdded`** | `public static SafeAction<DewPlayer> onHumanPlayerAdded` |  |
| **`onHumanPlayerRemoved`** | `public static SafeAction<DewPlayer> onHumanPlayerRemoved` |  |
| **`onLobbyPlayerAdded`** | `public static SafeAction<DewPlayer> onLobbyPlayerAdded` |  |
| **`onLobbyPlayerRemoved`** | `public static SafeAction<DewPlayer> onLobbyPlayerRemoved` |  |
| **`onSpectatorAdded`** | `public static SafeAction<DewPlayer> onSpectatorAdded` |  |
| **`onSpectatorRemoved`** | `public static SafeAction<DewPlayer> onSpectatorRemoved` |  |
| **`ownedItems`** | `[NonSerialized] public List<string> ownedItems` |  |
| **`ownershipKeys`** | `public readonly SyncList<string> ownershipKeys` |  |
| **`selectedAccessories`** | `public readonly SyncList<string> selectedAccessories` |  |
| **`spectators`** | `public static List<DewPlayer> spectators` | Human players that are in the game spectating. Note: this does not include game players with dead heroes. |
| **`steamId`** | `[SyncVar] public CSteamID steamId` |  |
| **`unlockedGameItems`** | `public readonly SyncList<string> unlockedGameItems` |  |

:::

## Properties (46)

::: details Click to expand Properties (46)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`avatar`** | `public Texture2D avatar { get; }` |  |
| **`buyPriceMultiplier`** | `public float buyPriceMultiplier { get; set; }` |  |
| **`cleanseRefundMultiplier`** | `public float cleanseRefundMultiplier { get; set; }` |  |
| **`controllingEntity`** | `public Entity controllingEntity { get; set; }` |  |
| **`creep`** | `public static DewPlayer creep { get; }` |  |
| **`cursorWorldPos`** | `public Vector3 cursorWorldPos { get; }` | Cursor world position of this player. Available on server and local client in-game. |
| **`dismantleDreamDustMultiplier`** | `public float dismantleDreamDustMultiplier { get; set; }` |  |
| **`dismantleGemDreamDustMultiplier`** | `public float dismantleGemDreamDustMultiplier { get; set; }` |  |
| **`dismantleSkillDreamDustMultiplier`** | `public float dismantleSkillDreamDustMultiplier { get; set; }` |  |
| **`doubleChaosChance`** | `public float doubleChaosChance { get; set; }` |  |
| **`dreamDust`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int dreamDust { get; set; }` |  |
| **`environment`** | `public static DewPlayer environment { get; }` | Environment player. Owner of server entities will default to this. |
| **`equippedNametag`** | `public string equippedNametag { get; }` |  |
| **`gamepadTargetEnemy`** | `public Entity gamepadTargetEnemy { get; }` | Available on server and local client in-game. |
| **`gold`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int gold { get; set; }` |  |
| **`guid`** | `public string guid { get; set; }` | This is given for each profile. |
| **`hero`** | `public Hero hero { get; set; }` |  |
| **`inputMode`** | `public InputMode inputMode { get; }` | Available on server and local client in-game. |
| **`isCreepPlayer`** | `public bool isCreepPlayer { get; }` |  |
| **`isEnvironmentPlayer`** | `public bool isEnvironmentPlayer { get; }` |  |
| **`isEveryInfoSet`** | `public bool isEveryInfoSet { get; }` |  |
| **`isGamepadExplicitAim`** | `public bool isGamepadExplicitAim { get; }` | Available on server and local client in-game. |
| **`isHostPlayer`** | `public bool isHostPlayer { get; }` |  |
| **`isHumanPlayer`** | `public bool isHumanPlayer { get; }` |  |
| **`isKicked`** | `public bool isKicked { get; }` | Available on server. |
| **`isLoadingForMidJoin`** | `public bool isLoadingForMidJoin { get; set; }` |  |
| **`isPlayingCutscene`** | `public bool isPlayingCutscene { get; }` | Is this player in a cutscene? Available on server. |
| **`isReadingArtifactStory`** | `public bool isReadingArtifactStory { get; }` |  |
| **`isReady`** | `public bool isReady { get; set; }` | Is ready to start the game (lobby) / travel to next node (ingame) / end the game (end result screen) ? |
| **`isSamplingCastInfo`** | `public bool isSamplingCastInfo { get; }` |  |
| **`isWaitingForContinueMidJoin`** | `public bool isWaitingForContinueMidJoin { get; set; }` |  |
| **`local`** | `public static DewPlayer local { get; }` |  |
| **`monsterKillGoldMultiplier`** | `public float monsterKillGoldMultiplier { get; set; }` | Available on server. |
| **`platinumCoin`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int platinumCoin { get; set; }` |  |
| **`playerName`** | `public string playerName { get; }` |  |
| **`playerNameRaw`** | `public string playerNameRaw { get; set; }` |  |
| **`potionDropChanceMultiplier`** | `public float potionDropChanceMultiplier { get; set; }` |  |
| **`profileStats`** | `public DewProfileStats profileStats { get; }` |  |
| **`selectedDejavuItem`** | `public string selectedDejavuItem { get; }` |  |
| **`selectedHeroType`** | `public string selectedHeroType { get; }` |  |
| **`selectedLoadout`** | `public HeroLoadoutData selectedLoadout { get; }` |  |
| **`selectedSkin`** | `public string selectedSkin { get; }` |  |
| **`sellPriceMultiplier`** | `public float sellPriceMultiplier { get; set; }` |  |
| **`shopAddedItems`** | `public int shopAddedItems { get; set; }` |  |
| **`state`** | `[ShowInInspector] [ReadOnly] public PlayerState state { get; set; }` |  |
| **`totalMasteryLevel`** | `public int totalMasteryLevel { get; }` |  |

:::

## Methods (53)

::: details `AddDreamDust(int)`

```csharp
public void AddDreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `AddGold(int)`

```csharp
public void AddGold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CheckEnemyOrNeutral(Entity)`

```csharp
public bool CheckEnemyOrNeutral(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `CmdAuthorizeForUse(string)`

```csharp
public void CmdAuthorizeForUse(string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ownershipKey` | `string` |  |

:::

::: details `CmdGiveCurrency(int, int, DewPlayer)`

```csharp
public void CmdGiveCurrency(int goldAmount, int dreamDustAmount, DewPlayer target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `goldAmount` | `int` |  |
| `dreamDustAmount` | `int` |  |
| `target` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `CmdNotifyEveryInfoSet()`

```csharp
public void CmdNotifyEveryInfoSet()
```

:::

::: details `CmdNotifyMidJoinReady(string)`

```csharp
public void CmdNotifyMidJoinReady(string sceneName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sceneName` | `string` |  |

:::

::: details `CmdPing()`

```csharp
public void CmdPing()
```

:::

::: details `CmdRequestMidJoin()`

```csharp
public void CmdRequestMidJoin()
```

:::

::: details `CmdRequestOverrides()`

```csharp
public void CmdRequestOverrides()
```

:::

::: details `CmdRequestStardust(int)`

```csharp
public void CmdRequestStardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `CmdRequestToJoinCurrentLobby()`

```csharp
public void CmdRequestToJoinCurrentLobby()
```

:::

::: details `CmdSetAccessories(List&lt;string&gt;)`

```csharp
public void CmdSetAccessories(List<string> accessories)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `accessories` | `System.Collections.Generic.List<T><string>` |  |

:::

::: details `CmdSetDejavuItem(string)`

```csharp
public void CmdSetDejavuItem(string item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | `string` |  |

:::

::: details `CmdSetHeroLoadoutData(HeroLoadoutData)`

```csharp
public void CmdSetHeroLoadoutData(HeroLoadoutData newData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newData` | [`HeroLoadoutData`](/api/Global.HeroLoadoutData) |  |

:::

::: details `CmdSetHeroType(string)`

Set local player's hero type. Can only be called in local machine of this DewPlayer.

```csharp
public void CmdSetHeroType(string newType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newType` | `string` |  |

:::

::: details `CmdSetIsReady(bool)`

```csharp
public void CmdSetIsReady(bool newReady)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newReady` | `bool` |  |

:::

::: details `CmdSetNametag(string)`

```csharp
public void CmdSetNametag(string ntName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |

:::

::: details `CmdSetProfileStats(DewProfileStats)`

```csharp
public void CmdSetProfileStats(DewProfileStats stats)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `stats` | [`DewProfileStats`](/api/Global.DewProfileStats) |  |

:::

::: details `CmdSetSkin(string)`

```csharp
public void CmdSetSkin(string skin)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skin` | `string` |  |

:::

::: details `CmdSetUnlockedGameItems()`

```csharp
public void CmdSetUnlockedGameItems()
```

:::

::: details `EarnDreamDust(int)`

```csharp
public void EarnDreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `EarnGold(int)`

```csharp
public void EarnGold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `GetLocalUnlockedGameItems()`

```csharp
public static string[] GetLocalUnlockedGameItems()
```

**Returns:** `string[]`

:::

::: details `GetTeamRelation(DewPlayer)`

```csharp
public TeamRelation GetTeamRelation(DewPlayer other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `TeamRelation`

:::

::: details `GetTeamRelation(Entity)`

```csharp
public TeamRelation GetTeamRelation(Entity other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `TeamRelation`

:::

::: details `GiveStardust(int)`

```csharp
public void GiveStardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `HideOnScreenTimer(NetworkedOnScreenTimerHandle)`

```csharp
public void HideOnScreenTimer(NetworkedOnScreenTimerHandle handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [`NetworkedOnScreenTimerHandle`](/api/Global.NetworkedOnScreenTimerHandle) |  |

:::

::: details `IsAllowedToUseItem(string)`

```csharp
public bool IsAllowedToUseItem(string itemName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `itemName` | `string` |  |

**Returns:** `bool`

:::

::: details `Kick()`

```csharp
public void Kick()
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

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStop()`

```csharp
public override void OnStop()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `PurgeRelationsList()`

Purge any despawned / null entries in player relation lists.

```csharp
public void PurgeRelationsList()
```

:::

::: details `RevalidateAllItems()`

```csharp
public void RevalidateAllItems()
```

:::

::: details `RpcInvokeOnSpendStardust(int)`

```csharp
public void RpcInvokeOnSpendStardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `SendLog(string)`

```csharp
public void SendLog(string message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` |  |

:::

::: details `SendLogError(string)`

```csharp
public void SendLogError(string message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` |  |

:::

::: details `SendLogWarning(string)`

```csharp
public void SendLogWarning(string message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` |  |

:::

::: details `ShowOnScreenTimer(NetworkedOnScreenTimerHandle)`

```csharp
public void ShowOnScreenTimer(NetworkedOnScreenTimerHandle handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [`NetworkedOnScreenTimerHandle`](/api/Global.NetworkedOnScreenTimerHandle) |  |

:::

::: details `Spend(Cost)`

Note this will not work for stardusts.

```csharp
public void Spend(Cost cost)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cost` | [`Cost`](/api/Global.Cost) |  |

:::

::: details `SpendDreamDust(int)`

```csharp
public void SpendDreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `SpendGold(int)`

```csharp
public void SpendGold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::

::: details `TpcMakePlayerChangeLobby(string)`

```csharp
public void TpcMakePlayerChangeLobby(string lobbyId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobbyId` | `string` |  |

:::

::: details `TpcNotifyDejavuUse()`

```csharp
public void TpcNotifyDejavuUse()
```

:::

::: details `TpcShowCenterMessage(CenterMessageType, string, string[])`

```csharp
public void TpcShowCenterMessage(CenterMessageType type, string key, string[] localizedFormatArgs)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#centermessagetype" class="enum-link" data-tooltip="General=0 · Error=1">CenterMessageType</a> |  |
| `key` | `string` |  |
| `localizedFormatArgs` | `string[]` |  |

:::

::: details `TpcShowCenterMessage(CenterMessageType, string)`

```csharp
public void TpcShowCenterMessage(CenterMessageType type, string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#centermessagetype" class="enum-link" data-tooltip="General=0 · Error=1">CenterMessageType</a> |  |
| `key` | `string` |  |

:::

::: details `TpcShowWorldPopMessage(WorldMessageSetting)`

```csharp
public void TpcShowWorldPopMessage(WorldMessageSetting message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [`WorldMessageSetting`](/api/Global.WorldMessageSetting) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (335)

*Classes and systems that invoke, reference, or depend on `DewPlayer`:*

`ACH_ANGER_MANAGEMENT_PROFESSIONAL` · `ACH_BFR_9000` · `ACH_DECEIVING_LOOKS` · `ACH_DOLL_OF_MANA` · `ACH_DOUBLE_VISION` · `ACH_GO_WITH_THE_FLOW` · `ACH_HOTTER_FIRE_WINS` · `ACH_IMMORTALITY_ACHIEVED` · `ACH_I_AM_SHELL` · `ACH_JUST_LIKE_THE_OLD_DAYS` · `ACH_KING_OF_THE_ELEMENTALS` · `ACH_LIKE_A_BREEZE` · `ACH_LOOK_RAINBOW` · `ACH_MASTER_OF_HAMMER` · `ACH_NIGHT_OF_COUNTING_THE_STARS` · `ACH_ODE_TO_THE_STARS` · `ACH_OMEGA_POINT` · `ACH_OVERFLOWING_HEALS` · `ACH_PEACE_AMID_THE_STORM` · `ACH_PEAK_PERFORMANCE` · `ACH_PRAISE_THE_SUN` · `ACH_PURE_IMAGINATION` · `ACH_REAP_WHAT_YOU_SOW` · `ACH_SUSPICIOUSLY_WEALTHY_TRAVELER` · `ACH_ULTRA_RAPID_FIRE` · `ACH_UNTOUCHABLE` · `ACH_VINE_IN_CREVICES` · [AchievementManager](/api/Global.AchievementManager) · [Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `Ai_ArcticTerritory` · `Ai_E_FlameJet` · `Ai_L_CoinExplosion_Coin` · `Ai_L_SoulKiller_Soul` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Special_AmbushSpawner_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_QR_ValiantHeart` · `Ai_R_ChainReaction` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · `At_Mon_DarkCave_BossSeeker_GreenChaserOrb` · [AttackTrigger](/api/Global.AttackTrigger) · [CameraManager](/api/Global.CameraManager) · [ChargingChannel](/api/Global.ChargingChannel) · [ChatManager](/api/Global.ChatManager) · [ChoiceShrine](/api/Global.ChoiceShrine) · [CinematicCameraHelper](/api/Global.CinematicCameraHelper) · [ClientEventManager](/api/Global.ClientEventManager) · [ConsoleManager](/api/Global.ConsoleManager) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · [Cost](/api/Global.Cost) · `CostDisplay` · `CostExtensions` · [DevGameManager](/api/Global.DevGameManager) · [Dew](/api/Global.Dew) · [DewAdvText](/api/Global.DewAdvText) · `DewConsoleCommands` · [DewConversationSettings](/api/Global.DewConversationSettings) · [DewEffect](/api/Global.DewEffect) · [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewInterestManagement](/api/Global.DewInterestManagement) · `DewLocalDitherFade` · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) · [DewSave](/api/Global.DewSave) · `DewStarItemOld` · [EditSkillManager](/api/Global.EditSkillManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntityHighlightProvider](/api/Global.EntityHighlightProvider) · [EntitySound](/api/Global.EntitySound) · [EntityVisual](/api/Global.EntityVisual) · [FeedbackManager](/api/Global.FeedbackManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [FxEffect](/api/Global.FxEffect) · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · [GameManager](/api/Global.GameManager) · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameResultManager](/api/Global.GameResultManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Gem](/api/Global.Gem) · `Gem_E_Might` · `Gem_L_DivineFaith` · `Gem_L_HeartOfGold` · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · [IItem](/api/Global.IItem) · `InGameAnalyticsManager` · [InGameCrashReportManager](/api/Global.InGameCrashReportManager) · [InGameReverieManager](/api/Global.InGameReverieManager) · [InGameTutorialManager](/api/Global.InGameTutorialManager) · [InGameUIManager](/api/Global.InGameUIManager) · `Ink_BossRoomDamageGround` · [LobbyUIManager](/api/Global.LobbyUIManager) · [LootManager](/api/Global.LootManager) · `LucidDream_TheDarkestUrge` · `LucidDream_WILD` · `Mon_Despair_AzurakMonsterSpawner` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Ink_BossWhiteNight` · `Mon_Polaris` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · [Monster](/api/Global.Monster) · `NetworkConnectionToClientExtension` · `NextZoneOverrideTreasure` · [PickupInstance](/api/Global.PickupInstance) · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseExpOrb](/api/Global.Pickup_BaseExpOrb) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [PingManager](/api/Global.PingManager) · [PingUIInstance](/api/Global.PingUIInstance) · [PlayGameManager](/api/Global.PlayGameManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · [PlayLobby_CharacterCamera](/api/Global.PlayLobby_CharacterCamera) · [PlayLobby_RotateCharacterTutorial](/api/Global.PlayLobby_RotateCharacterTutorial) · `PlayTutorialManager` · `PlayTutorial_Tutorial` · `PlayTutorial_Tutorial_SkillsAndEssences` · `PrimusCutsceneEntityVisualOff` · `Primus_Ending` · `Primus_PureWhiteOpenEffect` · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · [QuestManager](/api/Global.QuestManager) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · [Room](/api/Global.Room) · `RoomMod_Ambush` · `RoomMod_DistantMemories` · `RoomMod_GoldEverywhere` · `RoomMod_HeroSoul` · `RoomMod_PureDream` · [RoomMonsters](/api/Global.RoomMonsters) · [RoomProps](/api/Global.RoomProps) · [RoomRewards](/api/Global.RoomRewards) · [Room_Shortcut](/api/Global.Room_Shortcut) · `Se_Curse_DarkUrge` · `Se_Curse_FateOfGreed` · `Se_Curse_VainDream` · `Se_DarkCondensationZone` · `Se_HeroKnockedOut` · `Se_L_PyranasFireball` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_RoomMod_WarpingField_Unstable` · `Se_Star_Aurena_I_GoldEveryZone` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Bismuth_D_AtkSpdFromDismantle` · `Se_Star_Bismuth_I_DismantleMemoryDreamDust` · `Se_Star_Bismuth_I_ShopDiscount` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Husk_I_BossKillPlatinumCoin` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_I_AdditionalChaosChance` · `Se_Star_I_DismantleBonus` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_KillGoldBonus` · `Se_Star_I_MawDiscountAndProtection` · `Se_Star_I_MoreShopItems` · `Se_Star_I_MoreShrineItems` · `Se_Star_I_ShopDiscount` · `Se_Star_I_StartGold` · `Se_Star_L_PotionChance` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_Lacerta_I_ShopDiscount` · `Se_Star_Lacerta_I_ShopMoreItemsWithPenalty` · `Se_Star_Mist_I_StartGoldWithPenalty` · `Se_Star_Nachia_I_ForestShopDiscount` · `Se_Star_Vesper_I_ShopDiscount` · `Se_Star_Vesper_I_StartGold` · `Se_U_Hysteria` · `Se_UsingShortcut` · `Se_WaypointTeleport` · [Shrine](/api/Global.Shrine) · `Shrine_AltarOfCleansing` · `Shrine_ArtifactGiver` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_Destiny` · `Shrine_Enlightenment` · `Shrine_Entanglement` · `Shrine_FallenStar` · `Shrine_Guidance` · `Shrine_Hatred_Reward` · `Shrine_HiddenStash` · `Shrine_InvitationOfJonasMeeting` · `Shrine_Luck` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_MawOfDoom` · `Shrine_MirrorOfRemorse` · `Shrine_Paradox` · `Shrine_Retrospection` · `Shrine_ScaredMaw` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · `Shrine_Stardust` · `Shrine_TheConsortOfNight_Rift` · `Shrine_UpgradeWell` · `Shrine_WagesOfResolve` · [SkillTrigger](/api/Global.SkillTrigger) · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `St_L_CoinExplosion` · [StarEffect](/api/Global.StarEffect) · `Star_Global_Cleanse` · `Star_Global_DismantleDreamDustBonus` · `Star_Global_IncreasePotionDrop` · `Star_Global_KillGoldBonus` · `Star_Global_ShopDiscount` · `Star_Global_ShopMoreItems` · `Star_Global_StartGold` · `StarlessPath_BossPolarisManager` · `Sum_R_AnnoyingBanner` · [TransitionManager](/api/Global.TransitionManager) · `TravelerStoryPresenter` · [Treasure](/api/Global.Treasure) · `Treasure_Clairvoyance` · `Treasure_InvitationToSecretMeetingOfJonas` · `TutorialNetworkManager` · `UI_AccList_Item` · `UI_Constellations` · `UI_Constellations_CategoryGroup` · `UI_ControllerDisconnectedIndicator` · `UI_EndingBlackScreenText` · `UI_EntityDreamDust` · `UI_EntityGold` · `UI_EntityHealthBarGroup` · `UI_EntityName` · `UI_EntityPlatinumCoin` · `UI_EntityProvider_LocalHero` · `UI_HealthBar_Simple` · `UI_InGame_Conversations_Instance` · `UI_InGame_CurrentArtifact` · `UI_InGame_CurseNotifications` · `UI_InGame_EmoteCanvas` · `UI_InGame_FloatingWindow_Chaos` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_FloatingWindow_CorruptedChaos` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_InGame_GemSlot` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_GiveCurrencyView` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroDetailWindow_StatItem` · `UI_InGame_HeroInfoBar` · `UI_InGame_Interact_Base` · `UI_InGame_Interact_Gem` · `UI_InGame_Interact_Shrine` · `UI_InGame_Interact_Skill` · `UI_InGame_Map_Item_Entity` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_OffscreenIndicator_Item_Entity` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_PickupNumbers` · `UI_InGame_PickupNumbers_Number` · `UI_InGame_ResultView` · `UI_InGame_RoomModDisplay` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButton_GemGroup` · `UI_InGame_SkillNotifications` · `UI_InGame_SpectateIndicator` · `UI_InGame_VisibilityOnCoop` · `UI_InGame_VoteDisplay` · `UI_InGame_VoteDisplay_PlayerItem` · `UI_InGame_WorldMap` · `UI_Lobby_AccList` · `UI_Lobby_CharacterRotator` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_AlphaStar` · `UI_Lobby_Constellations_HeroConstellationBase` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_MasteryLevels` · `UI_Lobby_Constellations_MiniAlphaStar` · `UI_Lobby_Constellations_MiniHeroConstellation` · `UI_Lobby_Constellations_QuickLoadoutSwitch` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_Constellations_StarCount` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_Constellations_TitleAndEmblem` · `UI_Lobby_DejavuButton` · `UI_Lobby_DejavuWindow` · `UI_Lobby_DejavuWindow_Item` · `UI_Lobby_EmoteCanvas` · `UI_Lobby_ExpandableStory` · `UI_Lobby_HeroList_Item` · `UI_Lobby_HideIfReady` · `UI_Lobby_Loadout_AvailableSkills` · `UI_Lobby_Loadout_ComponentBase` · `UI_Lobby_MidJoinWaitObject` · `UI_Lobby_NametagList` · `UI_Lobby_PlayerInfoBase` · `UI_Lobby_PlayerListItem` · `UI_Lobby_PlayerNametag` · `UI_Lobby_SelectedHeroInfo_Base` · `UI_Lobby_SelectedHeroInfo_StarDecoration` · `UI_Lobby_SkinList` · `UI_Lobby_StartButtonController` · `UI_Lobby_StartButtonDejavuCost` · `UI_Lobby_WaitingForContinueMidJoin_Loading` · `UI_PlayRewardAnnouncer` · `UI_PlayerPlatinumCoinToggler` · `UI_TooltipManager` · `UI_Tooltip_EditSkillShrineTooltip` · `UI_Tooltip_EquippedGemDescriber` · `UI_Tooltip_GemDescription` · `UI_Tooltip_ObjEditSkillActions` · `UI_Tooltip_SkillDescription` · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_SkillTitle` · `UI_Tooltip_TreasureDescription` · `UI_TravelerHeroTitle` · `UI_TravelerStory` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (50)

*Types and components that `DewPlayer` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · [CameraManager](/api/Global.CameraManager) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [CastMethodDataSerialization](/api/Global.CastMethodDataSerialization) · [ControlManager](/api/Global.ControlManager) · [Cost](/api/Global.Cost) · `DateTimeExtensions` · `DecryptedItemData` · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewInput](/api/Global.DewInput) · `DewItem` · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewProfileStats](/api/Global.DewProfileStats) · [DewResources](/api/Global.DewResources) · [DewSafety](/api/Global.DewSafety) · [DewSave](/api/Global.DewSave) · [DewSteam](/api/Global.DewSteam) · [Entity](/api/Global.Entity) · [GameManager](/api/Global.GameManager) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · [HeroLoadoutData](/api/Global.HeroLoadoutData) · [HeroSkill](/api/Global.HeroSkill) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [InGameUIManager](/api/Global.InGameUIManager) · [LobbyManager](/api/Global.LobbyManager) · [LobbyServiceProvider](/api/Global.LobbyServiceProvider) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [NetworkedOnScreenTimerHandle](/api/Global.NetworkedOnScreenTimerHandle) · [PickupManager](/api/Global.PickupManager) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · [SampleCastInfoContext](/api/Global.SampleCastInfoContext) · [SampleCastInfoContextSerialization](/api/Global.SampleCastInfoContextSerialization) · [SkillTrigger](/api/Global.SkillTrigger) · [Skin](/api/Global.Skin) · `TestMapGameManager` · [WorldMessageSetting](/api/Global.WorldMessageSetting) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Related Enums (5)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#centermessagetype" class="enum-link" data-tooltip="General=0 · Error=1">CenterMessageType</a> · <a href="/enums#inputmode" class="enum-link" data-tooltip="KeyboardAndMouse=0 · Gamepad=1">InputMode</a> · <a href="/enums#playerstate" class="enum-link" data-tooltip="None=0 · InLobby=1 · Playing=2 · Spectating=3">PlayerState</a> · <a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a> · <a href="/enums#teamrelation" class="enum-link" data-tooltip="Own=1 · Neutral=2 · Enemy=4 · Ally=8">TeamRelation</a>

:::
