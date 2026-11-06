# Class: ChargingChannel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class ChargingChannel
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castMethod`** | `public CastMethodData castMethod` | You must call UpdateCastMethod after making change to this. |

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`castInfo`** | `public CastInfo castInfo { get; }` | Current cast info of this charging channel. |
| **`chargeAmount`** | `public float chargeAmount { get; }` |  |
| **`elapsedTime`** | `public float elapsedTime { get; }` |  |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`normalizedTime`** | `public float normalizedTime { get; }` |  |

:::

## Methods (8)

::: details `Cancel()`

```csharp
public void Cancel()
```

:::

::: details `Dispatch(Entity, AbilityTrigger)`

```csharp
public ChargingChannel Dispatch(Entity entity, AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnCancel(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnCancel(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnCast(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnCast(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnChargeFull(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnChargeFull(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `OnComplete(Action&lt;ChargingChannel&gt;)`

```csharp
public ChargingChannel OnComplete(Action<ChargingChannel> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | [`System.Action<T><ChargingChannel>`](/api/Global.ChargingChannel) |  |

**Returns:** `ChargingChannel`

:::

::: details `SetInitialInfo(CastInfo)`

```csharp
public ChargingChannel SetInitialInfo(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `ChargingChannel`

:::

::: details `UpdateCastMethod()`

Send updated cast method to client to reflect the changes.

```csharp
public ChargingChannel UpdateCastMethod()
```

**Returns:** `ChargingChannel`

:::
