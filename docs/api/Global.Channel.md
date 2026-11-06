# Class: Channel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class Channel
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockedActions`** | `public Channel.BlockedAction blockedActions` | Blocked actions for the owner of this channel.This channel will fail if any of the cancelable blocks is disobeyed. |
| **`duration`** | `public float duration` | Total duration of this channel. |
| **`isAttack`** | `public bool isAttack` | Only a single attack channel can exist in an entity. |
| **`onCancel`** | `public Action onCancel` | Callback function to be called when this channel has been canceled.This can be because of either an invalidation flag from any of the validators, or cancelable block being canceled by an entity. |
| **`onComplete`** | `public Action onComplete` | Callback function to be called when this channel has been successfully completed. |
| **`onTick`** | `public Action<float> onTick` | Called every logic update tick while channel is alive. |
| **`uncancellableTime`** | `public float uncancellableTime` | If this channel is cancellable, it won't be cancellable during this period to prevent accidental cancel. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`elapsedTime`** | `public float elapsedTime { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |

## Methods

### `AddOnCancel(Action)`

```csharp
public Channel AddOnCancel(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

**Returns:** `Channel`

### `AddOnComplete(Action)`

```csharp
public Channel AddOnComplete(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

**Returns:** `Channel`

### `AddOnTick(Action<float>)`

```csharp
public Channel AddOnTick(Action<float> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action<T><float>` |  |

**Returns:** `Channel`

### `AddValidation(IBinaryEntityValidator, Entity)`

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

### `AddValidation(IEntityValidator)`

Adds an entity validation for this channel. This channel will fail if any of the added validators evaluates to false.

```csharp
public Channel AddValidation(IEntityValidator validator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |

**Returns:** `Channel`

### `Cancel()`

Cancel this channel next channel update.

```csharp
public Channel Cancel()
```

**Returns:** `Channel`

### `Complete()`

Complete this channel next channel update.

```csharp
public Channel Complete()
```

**Returns:** `Channel`

### `Dispatch(Entity)`

Dispatch this channel.

```csharp
public Channel Dispatch(Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Channel`
