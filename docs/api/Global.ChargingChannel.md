# Class: ChargingChannel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ChargingChannel
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castMethod`** | `public CastMethodData castMethod` | You must call UpdateCastMethod after making change to this. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castInfo`** | `public CastInfo castInfo { get; }` | Current cast info of this charging channel. |
| **`chargeAmount`** | `public float chargeAmount { get; }` |  |
| **`elapsedTime`** | `public float elapsedTime { get; }` |  |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`normalizedTime`** | `public float normalizedTime { get; }` |  |

## Methods

### `Cancel()`

```csharp
public void Cancel()
```

### `Dispatch(Entity, AbilityTrigger)`

```csharp
public ChargingChannel Dispatch(Entity entity, AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `ChargingChannel`

### `OnCancel(Action<ChargingChannel>)`

```csharp
public ChargingChannel OnCancel(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

### `OnCast(Action<ChargingChannel>)`

```csharp
public ChargingChannel OnCast(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

### `OnChargeFull(Action<ChargingChannel>)`

```csharp
public ChargingChannel OnChargeFull(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

### `OnComplete(Action<ChargingChannel>)`

```csharp
public ChargingChannel OnComplete(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

### `SetInitialInfo(CastInfo)`

```csharp
public ChargingChannel SetInitialInfo(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `ChargingChannel`

### `UpdateCastMethod()`

Send updated cast method to client to reflect the changes.

```csharp
public ChargingChannel UpdateCastMethod()
```

**Returns:** `ChargingChannel`
