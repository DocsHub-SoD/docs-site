# Class: DewPlayer

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public class DewPlayer : DewNetworkBehaviour, ILogicUpdate, ISettingsChangedCallback
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allHumanPlayers`** | `public static List&lt;DewPlayer&gt; allHumanPlayers` | All human players that are connected to the server. |
| **`allies`** | `public readonly SyncList&lt;DewPlayer&gt; allies` |  |
| **`availableLucidDreams`** | `[NonSerialized]
public List&lt;string&gt; availableLucidDreams` | Available on server. |
| **`ClientEvent_OnDreamDustChanged`** | `public SafeAction&lt;int, int&gt; ClientEvent_OnDreamDustChanged` |  |
| **`ClientEvent_OnEarnDreamDust`** | `public SafeAction&lt;int&gt; ClientEvent_OnEarnDreamDust` |  |
| **`ClientEvent_OnEarnGold`** | `public SafeAction&lt;int&gt; ClientEvent_OnEarnGold` |  |
| **`ClientEvent_OnEarnStardust`** | `public SafeAction&lt;int&gt; ClientEvent_OnEarnStardust` |  |
| **`ClientEvent_OnEquippedNametagChanged`** | `public SafeAction&lt;string, string&gt; ClientEvent_OnEquippedNametagChanged` |  |
| **`ClientEvent_OnGiveCurrency`** | `public SafeAction&lt;int, int, DewPlayer&gt; ClientEvent_OnGiveCurrency` | Arguments are as follows: Gold, DreamDust, Target |
| **`ClientEvent_OnGoldChanged`** | `public SafeAction&lt;int, int&gt; ClientEvent_OnGoldChanged` |  |
| **`ClientEvent_OnHeroChanged`** | `public SafeAction&lt;Hero, Hero&gt; ClientEvent_OnHeroChanged` |  |
| **`ClientEvent_OnIsReadyChanged`** | `public SafeAction&lt;bool&gt; ClientEvent_OnIsReadyChanged` |  |
| **`ClientEvent_OnPlatinumCoinChanged`** | `public SafeAction&lt;int, int&gt; ClientEvent_OnPlatinumCoinChanged` |  |
| **`ClientEvent_OnSelectedAccessoriesChanged`** | `public SafeAction ClientEvent_OnSelectedAccessoriesChanged` |  |
| **`ClientEvent_OnSelectedDejavuItemChanged`** | `public SafeAction&lt;string&gt; ClientEvent_OnSelectedDejavuItemChanged` |  |
| **`ClientEvent_OnSelectedHeroTypeChanged`** | `public SafeAction&lt;string&gt; ClientEvent_OnSelectedHeroTypeChanged` |  |
| **`ClientEvent_OnSelectedLoadoutChanged`** | `public SafeAction&lt;HeroLoadoutData&gt; ClientEvent_OnSelectedLoadoutChanged` |  |
| **`ClientEvent_OnSelectedSkinChanged`** | `public SafeAction&lt;string&gt; ClientEvent_OnSelectedSkinChanged` |  |
| **`ClientEvent_OnSpendDreamDust`** | `public SafeAction&lt;int&gt; ClientEvent_OnSpendDreamDust` |  |
| **`ClientEvent_OnSpendGold`** | `public SafeAction&lt;int&gt; ClientEvent_OnSpendGold` |  |
| **`ClientEvent_OnSpendStardust`** | `public SafeAction&lt;int&gt; ClientEvent_OnSpendStardust` |  |
| **`ClientEvent_OnStateChanged`** | `public SafeAction ClientEvent_OnStateChanged` |  |
| **`enemies`** | `public readonly SyncList&lt;DewPlayer&gt; enemies` |  |
| **`friendSteamIds`** | `[NonSerialized]
public List&lt;string&gt; friendSteamIds` |  |
| **`gamePlayers`** | `public static List&lt;DewPlayer&gt; gamePlayers` | Human players that are playing the game. |
| **`lobbyPlayers`** | `public static List&lt;DewPlayer&gt; lobbyPlayers` | Human players that are in the lobby. Note: players can be in the lobby even after the game has been started, if they joined mid-game. |
| **`neutrals`** | `public readonly SyncList&lt;DewPlayer&gt; neutrals` |  |
| **`onGamePlayerAdded`** | `public static SafeAction&lt;DewPlayer&gt; onGamePlayerAdded` |  |
| **`onGamePlayerRemoved`** | `public static SafeAction&lt;DewPlayer&gt; onGamePlayerRemoved` |  |
| **`onHumanPlayerAdded`** | `public static SafeAction&lt;DewPlayer&gt; onHumanPlayerAdded` |  |
| **`onHumanPlayerRemoved`** | `public static SafeAction&lt;DewPlayer&gt; onHumanPlayerRemoved` |  |
| **`onLobbyPlayerAdded`** | `public static SafeAction&lt;DewPlayer&gt; onLobbyPlayerAdded` |  |
| **`onLobbyPlayerRemoved`** | `public static SafeAction&lt;DewPlayer&gt; onLobbyPlayerRemoved` |  |
| **`onSpectatorAdded`** | `public static SafeAction&lt;DewPlayer&gt; onSpectatorAdded` |  |
| **`onSpectatorRemoved`** | `public static SafeAction&lt;DewPlayer&gt; onSpectatorRemoved` |  |
| **`ownedItems`** | `[NonSerialized]
public List&lt;string&gt; ownedItems` |  |
| **`ownershipKeys`** | `public readonly SyncList&lt;string&gt; ownershipKeys` |  |
| **`selectedAccessories`** | `public readonly SyncList&lt;string&gt; selectedAccessories` |  |
| **`spectators`** | `public static List&lt;DewPlayer&gt; spectators` | Human players that are in the game spectating. Note: this does not include game players with dead heroes. |
| **`steamId`** | `public CSteamID steamId` |  |
| **`unlockedGameItems`** | `public readonly SyncList&lt;string&gt; unlockedGameItems` |  |

## Properties

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
| **`dreamDust`** | `[SaveVar(SaveVarFlags.Default)]
public int dreamDust { get; set; }` |  |
| **`environment`** | `public static DewPlayer environment { get; }` | Environment player. Owner of server entities will default to this. |
| **`equippedNametag`** | `public string equippedNametag { get; }` |  |
| **`gamepadTargetEnemy`** | `public Entity gamepadTargetEnemy { get; }` | Available on server and local client in-game. |
| **`gold`** | `[SaveVar(SaveVarFlags.Default)]
public int gold { get; set; }` |  |
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
| **`platinumCoin`** | `[SaveVar(SaveVarFlags.Default)]
public int platinumCoin { get; set; }` |  |
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
| **`state`** | `[ShowInInspector]
[ReadOnly]
public PlayerState state { get; set; }` |  |
| **`totalMasteryLevel`** | `public int totalMasteryLevel { get; }` |  |

## Methods

### `AddDreamDust(int)`

```csharp
public void AddDreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `AddGold(int)`

```csharp
public void AddGold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `CheckEnemyOrNeutral(Entity)`

```csharp
public bool CheckEnemyOrNeutral(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`

### `CmdAuthorizeForUse(string)`

```csharp
public void CmdAuthorizeForUse(string ownershipKey)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ownershipKey` | `string` |  |

### `CmdGiveCurrency(int, int, DewPlayer)`

```csharp
public void CmdGiveCurrency(int goldAmount, int dreamDustAmount, DewPlayer target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `goldAmount` | `int` |  |
| `dreamDustAmount` | `int` |  |
| `target` | [DewPlayer](/api/Global.DewPlayer) |  |

### `CmdNotifyEveryInfoSet()`

```csharp
public void CmdNotifyEveryInfoSet()
```

### `CmdNotifyMidJoinReady(string)`

```csharp
public void CmdNotifyMidJoinReady(string sceneName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sceneName` | `string` |  |

### `CmdPing()`

```csharp
public void CmdPing()
```

### `CmdRequestMidJoin()`

```csharp
public void CmdRequestMidJoin()
```

### `CmdRequestOverrides()`

```csharp
public void CmdRequestOverrides()
```

### `CmdRequestStardust(int)`

```csharp
public void CmdRequestStardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `CmdRequestToJoinCurrentLobby()`

```csharp
public void CmdRequestToJoinCurrentLobby()
```

### `CmdSetAccessories(List&lt;string&gt;)`

```csharp
public void CmdSetAccessories(List<string> accessories)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `accessories` | `System.Collections.Generic.List&lt;T&gt;&lt;string&gt;` |  |

### `CmdSetDejavuItem(string)`

```csharp
public void CmdSetDejavuItem(string item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | `string` |  |

### `CmdSetHeroLoadoutData(HeroLoadoutData)`

```csharp
public void CmdSetHeroLoadoutData(HeroLoadoutData newData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newData` | [HeroLoadoutData](/api/Global.HeroLoadoutData) |  |

### `CmdSetHeroType(string)`

Set local player's hero type. Can only be called in local machine of this DewPlayer.

```csharp
public void CmdSetHeroType(string newType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newType` | `string` |  |

### `CmdSetIsReady(bool)`

```csharp
public void CmdSetIsReady(bool newReady)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newReady` | `bool` |  |

### `CmdSetNametag(string)`

```csharp
public void CmdSetNametag(string ntName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ntName` | `string` |  |

### `CmdSetProfileStats(DewProfileStats)`

```csharp
public void CmdSetProfileStats(DewProfileStats stats)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `stats` | [DewProfileStats](/api/Global.DewProfileStats) |  |

### `CmdSetSkin(string)`

```csharp
public void CmdSetSkin(string skin)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skin` | `string` |  |

### `CmdSetUnlockedGameItems()`

```csharp
public void CmdSetUnlockedGameItems()
```

### `EarnDreamDust(int)`

```csharp
public void EarnDreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `EarnGold(int)`

```csharp
public void EarnGold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `GetLocalUnlockedGameItems()`

```csharp
public static string[] GetLocalUnlockedGameItems()
```

**Returns:** `string[]`

### `GetTeamRelation(DewPlayer)`

```csharp
public TeamRelation GetTeamRelation(DewPlayer other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [DewPlayer](/api/Global.DewPlayer) |  |

**Returns:** `TeamRelation`

### `GetTeamRelation(Entity)`

```csharp
public TeamRelation GetTeamRelation(Entity other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [Entity](/api/Global.Entity) |  |

**Returns:** `TeamRelation`

### `GiveStardust(int)`

```csharp
public void GiveStardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `HideOnScreenTimer(NetworkedOnScreenTimerHandle)`

```csharp
public void HideOnScreenTimer(NetworkedOnScreenTimerHandle handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [NetworkedOnScreenTimerHandle](/api/Global.NetworkedOnScreenTimerHandle) |  |

### `IsAllowedToUseItem(string)`

```csharp
public bool IsAllowedToUseItem(string itemName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `itemName` | `string` |  |

**Returns:** `bool`

### `Kick()`

```csharp
public void Kick()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStop()`

```csharp
public override void OnStop()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `PurgeRelationsList()`

Purge any despawned / null entries in player relation lists.

```csharp
public void PurgeRelationsList()
```

### `RevalidateAllItems()`

```csharp
public void RevalidateAllItems()
```

### `RpcInvokeOnSpendStardust(int)`

```csharp
public void RpcInvokeOnSpendStardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `SendLog(string)`

```csharp
public void SendLog(string message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` |  |

### `SendLogError(string)`

```csharp
public void SendLogError(string message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` |  |

### `SendLogWarning(string)`

```csharp
public void SendLogWarning(string message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | `string` |  |

### `ShowOnScreenTimer(NetworkedOnScreenTimerHandle)`

```csharp
public void ShowOnScreenTimer(NetworkedOnScreenTimerHandle handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [NetworkedOnScreenTimerHandle](/api/Global.NetworkedOnScreenTimerHandle) |  |

### `Spend(Cost)`

Note this will not work for stardusts.

```csharp
public void Spend(Cost cost)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cost` | [Cost](/api/Global.Cost) |  |

### `SpendDreamDust(int)`

```csharp
public void SpendDreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `SpendGold(int)`

```csharp
public void SpendGold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

### `TpcMakePlayerChangeLobby(string)`

```csharp
public void TpcMakePlayerChangeLobby(string lobbyId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobbyId` | `string` |  |

### `TpcNotifyDejavuUse()`

```csharp
public void TpcNotifyDejavuUse()
```

### `TpcShowCenterMessage(CenterMessageType, string, string[])`

```csharp
public void TpcShowCenterMessage(CenterMessageType type, string key, string[] localizedFormatArgs)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [CenterMessageType](/api/Global.CenterMessageType) |  |
| `key` | `string` |  |
| `localizedFormatArgs` | `string[]` |  |

### `TpcShowCenterMessage(CenterMessageType, string)`

```csharp
public void TpcShowCenterMessage(CenterMessageType type, string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [CenterMessageType](/api/Global.CenterMessageType) |  |
| `key` | `string` |  |

### `TpcShowWorldPopMessage(WorldMessageSetting)`

```csharp
public void TpcShowWorldPopMessage(WorldMessageSetting message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [WorldMessageSetting](/api/Global.WorldMessageSetting) |  |
