# Class: PropEnt_Merchant_Jonas

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity) → [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) → [PropEnt_Merchant_Unmanned](/api/Global.PropEnt_Merchant_Unmanned)

```csharp
public class PropEnt_Merchant_Jonas : PropEnt_Merchant_Base, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp, IInteractable
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gemQuantity`** | `public Vector2 gemQuantity` |  |
| **`gemTypeCount`** | `public int gemTypeCount` |  |
| **`skillQuantity`** | `public Vector2 skillQuantity` |  |
| **`skillTypeCount`** | `public int skillTypeCount` |  |

## Methods

### `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [EntityAIContext](/api/Global.EntityAIContext) |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

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
