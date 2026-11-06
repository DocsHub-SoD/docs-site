# Class: Channel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class Channel
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockedActions`** | `public Channel.BlockedAction blockedActions` | Blocked actions for the owner of this channel.This channel will fail if any of the cancelable blocks is disobeyed. |
| **`duration`** | `public float duration` | Total duration of this channel. |
| **`isAttack`** | `public bool isAttack` | Only a single attack channel can exist in an entity. |
| **`onCancel`** | `public Action onCancel` | Callback function to be called when this channel has been canceled.This can be because of either an invalidation flag from any of the validators, or cancelable block being canceled by an entity. |
| **`onComplete`** | `public Action onComplete` | Callback function to be called when this channel has been successfully completed. |
| **`onTick`** | `public Action<float> onTick` | Called every logic update tick while channel is alive. |
| **`uncancellableTime`** | `public float uncancellableTime` | If this channel is cancellable, it won't be cancellable during this period to prevent accidental cancel. |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`elapsedTime`** | `public float elapsedTime { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |

:::

## Methods (8)

::: details `AddOnCancel(Action)`

```csharp
public Channel AddOnCancel(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

**Returns:** `Channel`

:::

::: details `AddOnComplete(Action)`

```csharp
public Channel AddOnComplete(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

**Returns:** `Channel`

:::

::: details `AddOnTick(Action&lt;float&gt;)`

```csharp
public Channel AddOnTick(Action<float> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action<T><float>` |  |

**Returns:** `Channel`

:::

::: details `AddValidation(IBinaryEntityValidator, Entity)`

Adds an binary entity validation for this channel. This channel will fail if any of the added validators evaluates to false.

```csharp
public Channel AddValidation(IBinaryEntityValidator validator, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Channel`

:::

::: details `AddValidation(IEntityValidator)`

Adds an entity validation for this channel. This channel will fail if any of the added validators evaluates to false.

```csharp
public Channel AddValidation(IEntityValidator validator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |

**Returns:** `Channel`

:::

::: details `Cancel()`

Cancel this channel next channel update.

```csharp
public Channel Cancel()
```

**Returns:** `Channel`

:::

::: details `Complete()`

Complete this channel next channel update.

```csharp
public Channel Complete()
```

**Returns:** `Channel`

:::

::: details `Dispatch(Entity)`

Dispatch this channel.

```csharp
public Channel Dispatch(Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Channel`

:::
