# Class: PickupManager

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [PickupManager](/api/Global.PickupManager)

```csharp
public class PickupManager : NetworkedManagerBase<PickupManager>, ILogicUpdate
```

## Fields (11)

::: details Click to expand Fields (11)

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

:::

## Methods (5)

::: details `DropDreamDust(bool, int, Vector3, Hero)`

```csharp
public void DropDreamDust(bool isGivenByOtherPlayer, int amount, Vector3 position, Hero target = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isGivenByOtherPlayer` | `bool` |  |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |
| `target` | [`Hero`](/api/Global.Hero) |  |

:::

::: details `DropExp(int, Vector3)`

```csharp
public void DropExp(int amount, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `DropGold(bool, bool, int, Vector3, Hero)`

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
| `target` | [`Hero`](/api/Global.Hero) |  |

:::

::: details `DropStarDust(int, Vector3)`

```csharp
public void DropStarDust(int amount, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::
