# Class: GameMod_Limbo

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect) → [GameModifierBase](/api/Global.GameModifierBase)

```csharp
public class GameMod_Limbo : GameModifierBase, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (14)

::: details Click to expand Fields (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`atkMovSpdPerDepth`** | `public float atkMovSpdPerDepth` |  |
| **`atkMovSpdPerDepthMax`** | `public float atkMovSpdPerDepthMax` |  |
| **`d1HuntSpeedAmp`** | `public float d1HuntSpeedAmp` |  |
| **`d1SkillHaste`** | `public float d1SkillHaste` |  |
| **`d2Armor`** | `public float d2Armor` |  |
| **`d2DamageAmp`** | `public float d2DamageAmp` |  |
| **`d3ExpReduction`** | `public float d3ExpReduction` |  |
| **`d3GoldPriceAmp`** | `public float d3GoldPriceAmp` |  |
| **`d3ShieldReduction`** | `public float d3ShieldReduction` |  |
| **`d4ElementalDurationAmp`** | `public float d4ElementalDurationAmp` |  |
| **`d4MirageSkinChance`** | `public float d4MirageSkinChance` |  |
| **`d5BossAtkSpd`** | `public float d5BossAtkSpd` |  |
| **`d5BossMovSpd`** | `public float d5BossMovSpd` |  |
| **`depth`** | `[SyncVar] [SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public int depth` |  |

:::

## Methods (17)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `GetCurrentUnlockedEvilLucidDreams()`

```csharp
public static int GetCurrentUnlockedEvilLucidDreams()
```

**Returns:** `int`

:::

::: details `GetDepthLocalized(int)`

```csharp
public static string GetDepthLocalized(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

**Returns:** `string`

:::

::: details `GetInsufficientRequirementMessage()`

```csharp
public static string GetInsufficientRequirementMessage()
```

**Returns:** `string`

:::

::: details `GetMaxDepths()`

```csharp
public static int GetMaxDepths()
```

**Returns:** `int`

:::

::: details `GetRequiredUnlockedEvilLucidDreams()`

```csharp
public static int GetRequiredUnlockedEvilLucidDreams()
```

**Returns:** `int`

:::

::: details `IsLimboUnlocked()`

```csharp
public static bool IsLimboUnlocked()
```

**Returns:** `bool`

:::

::: details `Lobby_GetDepth()`

```csharp
public static int Lobby_GetDepth()
```

**Returns:** `int`

:::

::: details `Lobby_GetDepth(LobbyInstance)`

```csharp
public static int Lobby_GetDepth(LobbyInstance lobby)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobby` | [`LobbyInstance`](/api/Global.LobbyInstance) |  |

**Returns:** `int`

:::

::: details `Lobby_GetLimboDepthState(int)`

```csharp
public static LimboDepthState Lobby_GetLimboDepthState(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

**Returns:** `LimboDepthState`

:::

::: details `Lobby_GetLimboDepthUnavailableReason(int)`

```csharp
public static string Lobby_GetLimboDepthUnavailableReason(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

**Returns:** `string`

:::

::: details `Lobby_SetDepth(int)`

```csharp
public static void Lobby_SetDepth(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::

::: details `OnStartClientLobby()`

```csharp
public override void OnStartClientLobby()
```

:::

::: details `OnStartServerLobby()`

```csharp
public override void OnStartServerLobby()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (12)

*Classes and systems that invoke, reference, or depend on `GameMod_Limbo`:*

`InGameAnalyticsManager` · [TitleManager](/api/Global.TitleManager) · `UI_InGame_AchievementNotifications` · `UI_LimboDepthIcon` · `UI_Lobby_Limbo_DepthSelect` · `UI_Lobby_Limbo_DepthSelect_Item` · `UI_Lobby_PlayerNametag` · `UI_Lobby_SelectedHeroInfo_LimboProgress` · `UI_Title_CreateLobbyView` · `UI_Title_FindLobbyView` · `UI_Title_FindLobby_LobbyItem` · `UI_Title_TitleView`

### Dependencies (40)

*Types and components that `GameMod_Limbo` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [ChatManager](/api/Global.ChatManager) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [Dew](/api/Global.Dew) · [DewGameResult](/api/Global.DewGameResult) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [DewProfileStats](/api/Global.DewProfileStats) · [DewResources](/api/Global.DewResources) · [DewSave](/api/Global.DewSave) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoLoadRoom](/api/Global.EventInfoLoadRoom) · [GameEffect](/api/Global.GameEffect) · [GameManager](/api/Global.GameManager) · [GameModifierBase](/api/Global.GameModifierBase) · [GameSettingsManager](/api/Global.GameSettingsManager) · [ILimboNotifyReceiver](/api/Global.ILimboNotifyReceiver) · [LobbyInstance](/api/Global.LobbyInstance) · [LobbyManager](/api/Global.LobbyManager) · [LobbyServiceProvider](/api/Global.LobbyServiceProvider) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [Monster](/api/Global.Monster) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [QuestManager](/api/Global.QuestManager) · [ResourceLoadSettings](/api/Global.ResourceLoadSettings) · `ResultTypeExtensions` · [Room](/api/Global.Room) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [StatBonus](/api/Global.StatBonus) · [WorldNodeData](/api/Global.WorldNodeData) · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#limbodepthstate" class="enum-link" data-tooltip="Available=0 · Completed=1 · Locked=2">LimboDepthState</a> · <a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
