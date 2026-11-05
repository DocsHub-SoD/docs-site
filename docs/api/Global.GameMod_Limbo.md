# Class: GameMod_Limbo

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect) → [GameModifierBase](/api/Global.GameModifierBase)

```csharp
public class GameMod_Limbo : GameModifierBase, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields

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
| **`depth`** | `[SaveVar(SaveVarFlags.Default)]
[NonSerialized]
public int depth` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `GetCurrentUnlockedEvilLucidDreams()`

```csharp
public static int GetCurrentUnlockedEvilLucidDreams()
```

**Returns:** `int`

### `GetDepthLocalized(int)`

```csharp
public static string GetDepthLocalized(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

**Returns:** `string`

### `GetInsufficientRequirementMessage()`

```csharp
public static string GetInsufficientRequirementMessage()
```

**Returns:** `string`

### `GetMaxDepths()`

```csharp
public static int GetMaxDepths()
```

**Returns:** `int`

### `GetRequiredUnlockedEvilLucidDreams()`

```csharp
public static int GetRequiredUnlockedEvilLucidDreams()
```

**Returns:** `int`

### `IsLimboUnlocked()`

```csharp
public static bool IsLimboUnlocked()
```

**Returns:** `bool`

### `Lobby_GetDepth()`

```csharp
public static int Lobby_GetDepth()
```

**Returns:** `int`

### `Lobby_GetDepth(LobbyInstance)`

```csharp
public static int Lobby_GetDepth(LobbyInstance lobby)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobby` | [LobbyInstance](/api/Global.LobbyInstance) |  |

**Returns:** `int`

### `Lobby_GetLimboDepthState(int)`

```csharp
public static LimboDepthState Lobby_GetLimboDepthState(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

**Returns:** `LimboDepthState`

### `Lobby_GetLimboDepthUnavailableReason(int)`

```csharp
public static string Lobby_GetLimboDepthUnavailableReason(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

**Returns:** `string`

### `Lobby_SetDepth(int)`

```csharp
public static void Lobby_SetDepth(int depth)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `depth` | `int` |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnPrepare()`

```csharp
protected override void OnPrepare()
```

### `OnStartClientLobby()`

```csharp
public override void OnStartClientLobby()
```

### `OnStartServerLobby()`

```csharp
public override void OnStartServerLobby()
```
