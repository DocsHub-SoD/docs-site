# Class: PropEnt_Merchant_Smoothie

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity) → [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base)

```csharp
public class PropEnt_Merchant_Smoothie : PropEnt_Merchant_Base, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp, IInteractable, IEnableWandering
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`souvenirsCount`** | `public int souvenirsCount` |  |
| **`treasuresCount`** | `public int treasuresCount` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldWanderAround`** | `public bool shouldWanderAround { get; }` |  |

## Methods

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnInteract(Entity, bool)`

```csharp
public override void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [Entity](/api/Global.Entity) |  |
| `alt` | `bool` |  |

### `OnPopulateMerchandises(DewPlayer)`

```csharp
protected override void OnPopulateMerchandises(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

### `OnRefresh(DewPlayer)`

```csharp
protected override void OnRefresh(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |
