# Class: PickupManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [PickupManager](/api/Global.PickupManager)

```csharp
public class PickupManager : NetworkedManagerBase<PickupManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dreamDustMaxCount`** | `public int dreamDustMaxCount` |  |
| **`dreamDustMinAmount`** | `public int dreamDustMinAmount` |  |
| **`expOrbMaxCount`** | `public int expOrbMaxCount` |  |
| **`goldOrbMaxCount`** | `public int goldOrbMaxCount` |  |
| **`isStardustDropDisabled`** | `public bool isStardustDropDisabled` |  |
| **`largeExpOrbAmount`** | `public int largeExpOrbAmount` |  |
| **`largeGoldOrbAmount`** | `public int largeGoldOrbAmount` |  |
| **`mediumExpOrbAmount`** | `public int mediumExpOrbAmount` |  |
| **`mediumGoldOrbAmount`** | `public int mediumGoldOrbAmount` |  |
| **`smallExpOrbAmount`** | `public int smallExpOrbAmount` |  |
| **`smallGoldOrbAmount`** | `public int smallGoldOrbAmount` |  |

## Methods

### `DropDreamDust(bool, int, Vector3, Hero)`

```csharp
public void DropDreamDust(bool isGivenByOtherPlayer, int amount, Vector3 position, Hero target = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isGivenByOtherPlayer` | `bool` |  |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |
| `target` | [Hero](/api/Global.Hero) |  |

### `DropExp(int, Vector3)`

```csharp
public void DropExp(int amount, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |

### `DropGold(bool, bool, int, Vector3, Hero)`

```csharp
public void DropGold(bool isKillGold, bool isGivenByOtherPlayer, int amount, Vector3 position, Hero target = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isKillGold` | `bool` |  |
| `isGivenByOtherPlayer` | `bool` |  |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |
| `target` | [Hero](/api/Global.Hero) |  |

### `DropStarDust(int, Vector3)`

```csharp
public void DropStarDust(int amount, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |

### `OnStartServer()`

```csharp
public override void OnStartServer()
```
