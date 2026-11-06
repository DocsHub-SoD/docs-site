# Class: PropEnt_Merchant_Smoothie

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity) → [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base)

```csharp
public class PropEnt_Merchant_Smoothie : PropEnt_Merchant_Base, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp, IInteractable, IEnableWandering
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`souvenirsCount`** | `public int souvenirsCount` |  |
| **`treasuresCount`** | `public int treasuresCount` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldWanderAround`** | `public bool shouldWanderAround { get; }` |  |

:::

## Methods (4)

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnInteract(Entity, bool)`

```csharp
public override void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

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

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (16)

*Types and components that `PropEnt_Merchant_Smoothie` references or depends upon:*

[Actor](/api/Global.Actor) · [AssetRef`1](/api/Global.AssetRef`1) · [Cost](/api/Global.Cost) · [Dew](/api/Global.Dew) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [IEnableWandering](/api/Global.IEnableWandering) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [ResourceLoadSettings](/api/Global.ResourceLoadSettings) · [Treasure](/api/Global.Treasure) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

:::
