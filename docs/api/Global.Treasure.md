# Class: Treasure

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public abstract class Treasure : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`basePrice`** | `[BoxGroup("Treasure Settings", true, false, 0)]
public int basePrice` |  |
| **`chanceWeight`** | `[HideIf("@excludeFromPool", true)]
[BoxGroup("Treasure Settings", true, false, 0)]
public float chanceWeight` |  |
| **`excludeFromPool`** | `[BoxGroup("Treasure Settings", true, false, 0)]
public bool excludeFromPool` |  |
| **`icon`** | `[BoxGroup("Treasure Settings", true, false, 0)]
public Sprite icon` |  |
| **`maxUse`** | `[BoxGroup("Treasure Settings", true, false, 0)]
public int maxUse` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`customData`** | `public string customData { get; set; }` |  |
| **`hero`** | `public Hero hero { get; set; }` |  |
| **`merchant`** | `public PropEnt_Merchant_Base merchant { get; set; }` |  |
| **`player`** | `public DewPlayer player { get; set; }` |  |
| **`price`** | `public int price { get; set; }` |  |

## Methods

### `CanBePurchased()`

This is checked on server upon purchase. If this returns false, purchase will not be made. You should show some kind of message to the user if this returns false.This is invoked on a prefab, and before being invoked, relevant fields like hero / player will be populated.

```csharp
public virtual bool CanBePurchased()
```

**Returns:** `bool`

### `GetCustomDescription()`

```csharp
public virtual string GetCustomDescription()
```

**Returns:** `string`

### `GetCustomName()`

```csharp
public virtual string GetCustomName()
```

**Returns:** `string`

### `OnAddMerchandise(out Cost, out string)`

```csharp
public virtual void OnAddMerchandise(out Cost mercPrice, out string customData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `mercPrice` | [Cost](/api/Global.Cost) |  |
| `customData` | `string` |  |

### `ShouldBeIncludedInPool()`

This is checked on server when populating for each player. If this returns false, this treasure will not be included in the pool.

```csharp
public virtual bool ShouldBeIncludedInPool()
```

**Returns:** `bool`
