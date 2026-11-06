# Class: Treasure

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public abstract class Treasure : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`basePrice`** | `[BoxGroup("Treasure Settings", true, false, 0)] public int basePrice` |  |
| **`chanceWeight`** | `[HideIf("@excludeFromPool", true)] [BoxGroup("Treasure Settings", true, false, 0)] public float chanceWeight` |  |
| **`excludeFromPool`** | `[BoxGroup("Treasure Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`icon`** | `[BoxGroup("Treasure Settings", true, false, 0)] public Sprite icon` |  |
| **`maxUse`** | `[BoxGroup("Treasure Settings", true, false, 0)] public int maxUse` |  |

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`customData`** | `public string customData { get; set; }` |  |
| **`hero`** | `public Hero hero { get; set; }` |  |
| **`merchant`** | `public PropEnt_Merchant_Base merchant { get; set; }` |  |
| **`player`** | `public DewPlayer player { get; set; }` |  |
| **`price`** | `public int price { get; set; }` |  |

:::

## Methods (5)

::: details `CanBePurchased()`

This is checked on server upon purchase. If this returns false, purchase will not be made. You should show some kind of message to the user if this returns false.This is invoked on a prefab, and before being invoked, relevant fields like hero / player will be populated.

```csharp
public virtual bool CanBePurchased()
```

**Returns:** `bool`

:::

::: details `GetCustomDescription()`

```csharp
public virtual string GetCustomDescription()
```

**Returns:** `string`

:::

::: details `GetCustomName()`

```csharp
public virtual string GetCustomName()
```

**Returns:** `string`

:::

::: details `OnAddMerchandise(out Cost, out string)`

```csharp
public virtual void OnAddMerchandise(out Cost mercPrice, out string customData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `mercPrice` | [`Cost`](/api/Global.Cost) |  |
| `customData` | `string` |  |

:::

::: details `ShouldBeIncludedInPool()`

This is checked on server when populating for each player. If this returns false, this treasure will not be included in the pool.

```csharp
public virtual bool ShouldBeIncludedInPool()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (18)

*Classes and systems that invoke, reference, or depend on `Treasure`:*

`NextZoneOverrideTreasure` · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · `Treasure_BlueElixir` · `Treasure_Clairvoyance` · `Treasure_CloakOfGuidance` · `Treasure_CrimsonElixir` · `Treasure_DreamingStarfish` · `Treasure_FragmentOfDetermination` · `Treasure_InvitationToSecretMeetingOfJonas` · `Treasure_SparklingElixir` · `Treasure_StarSeekersJournal` · `Treasure_StrayMemory` · `Treasure_SuspiciousHat` · `Treasure_TokenOfGuidance` · `Treasure_TotallyGenuineTreasureMap` · `Treasure_TreasureMap` · `UI_TooltipManager`

### Dependencies (8)

*Types and components that `Treasure` references or depends upon:*

[Actor](/api/Global.Actor) · [Cost](/api/Global.Cost) · [DewPlayer](/api/Global.DewPlayer) · [GameManager](/api/Global.GameManager) · [Hero](/api/Global.Hero) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base)

:::
