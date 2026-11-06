# Class: PropEnt_Merchant_Jonas

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity) → [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) → [PropEnt_Merchant_Unmanned](/api/Global.PropEnt_Merchant_Unmanned)

```csharp
public class PropEnt_Merchant_Jonas : PropEnt_Merchant_Base, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp, IInteractable
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gemQuantity`** | `public Vector2 gemQuantity` |  |
| **`gemTypeCount`** | `public int gemTypeCount` |  |
| **`skillQuantity`** | `public Vector2 skillQuantity` |  |
| **`skillTypeCount`** | `public int skillTypeCount` |  |

:::

## Methods (5)

::: details `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

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

::: details `OnPopulateMerchandises(DewPlayer)`

```csharp
protected override void OnPopulateMerchandises(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `OnRefresh(DewPlayer)`

```csharp
protected override void OnRefresh(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `PropEnt_Merchant_Jonas`:*

[PropEnt_Merchant_Unmanned](/api/Global.PropEnt_Merchant_Unmanned) · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Husk_I_ShopIntimidation` · `Shrine_CookingPot`

### Dependencies (14)

*Types and components that `PropEnt_Merchant_Jonas` references or depends upon:*

[Cost](/api/Global.Cost) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityStatus](/api/Global.EntityStatus) · [Gem](/api/Global.Gem) · [LootManager](/api/Global.LootManager) · [MerchandiseData](/api/Global.MerchandiseData) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [SafeAction`1](/api/Global.SafeAction`1) · [SkillTrigger](/api/Global.SkillTrigger) · [ZoneManager](/api/Global.ZoneManager)

:::
