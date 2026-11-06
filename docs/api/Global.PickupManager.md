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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (30)

*Classes and systems that invoke, reference, or depend on `PickupManager`:*

[DewPlayer](/api/Global.DewPlayer) · [Gem](/api/Global.Gem) · `Mon_GoldenLizard_ElusiveLizard` · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) · `Se_E_LizardlyBlessing` · `Se_GoldEverywhere` · `Se_PureDream` · `Se_Star_Aurena_F_CR_EarnGold` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_I_GoldOnMerchantDamage` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_GoldPerCrit` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_SummonKillGold` · `Shrine_AltarOfCleansing` · `Shrine_CookingPot` · `Shrine_DreamdustBit` · `Shrine_DreamdustBox` · `Shrine_GoldBit` · `Shrine_GoldBox` · `Shrine_MarshOfDestiny_SeedOfTorment` · [SkillTrigger](/api/Global.SkillTrigger) · `Treasure_DreamingStarfish`

### Dependencies (19)

*Types and components that `PickupManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [ActorManager](/api/Global.ActorManager) · [Dew](/api/Global.Dew) · [DewBuildProfile](/api/Global.DewBuildProfile) · [DewMath](/api/Global.DewMath) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoKill](/api/Global.EventInfoKill) · [GameManager](/api/Global.GameManager) · `GraphicsManager` · [Hero](/api/Global.Hero) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PerMonsterTypeData`1](/api/Global.PerMonsterTypeData`1) · [Pickup_BaseExpOrb](/api/Global.Pickup_BaseExpOrb) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [SafeAction`1](/api/Global.SafeAction`1)

:::
