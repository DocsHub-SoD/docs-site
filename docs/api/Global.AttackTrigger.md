# Class: AttackTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityTrigger](/api/Global.AbilityTrigger)

```csharp
public class AttackTrigger : AbilityTrigger, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowNonTargetedCast`** | `public bool allowNonTargetedCast` |  |
| **`factor`** | `public ScalingValue factor` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `CallAttackCompleteBeforePrepareRoutines(EventInfoCast)`

```csharp
public void CallAttackCompleteBeforePrepareRoutines(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

### `CallAttackCompleteRoutines(AbilityInstance, int, CastInfo)`

```csharp
public void CallAttackCompleteRoutines(AbilityInstance newInstance, int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newInstance` | [`AbilityInstance`](/api/Global.AbilityInstance) |  |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `GetAnimationSpeed()`

```csharp
public override float GetAnimationSpeed()
```

**Returns:** `float`

### `GetChannelDurationMultiplier()`

```csharp
public override float GetChannelDurationMultiplier()
```

**Returns:** `float`

### `GetCooldownTimeMultiplier(int)`

```csharp
public override float GetCooldownTimeMultiplier(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

### `GetPostDelayDurationMultiplier()`

```csharp
public override float GetPostDelayDurationMultiplier()
```

**Returns:** `float`

### `OnCastCancelSetCooldownTime(int, CastInfo)`

```csharp
protected override void OnCastCancelSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastComplete(int, CastInfo)`

```csharp
public override AbilityInstance OnCastComplete(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `AbilityInstance`

### `OnCastCompleteBeforePrepare(EventInfoCast)`

```csharp
public override void OnCastCompleteBeforePrepare(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

### `OnCastCompleteSetCharge(int, CastInfo)`

```csharp
public override void OnCastCompleteSetCharge(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastCompleteSetCooldownTime(int, CastInfo)`

```csharp
public override void OnCastCompleteSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastCompleteSetMinimumDelay(int, CastInfo)`

```csharp
public override void OnCastCompleteSetMinimumDelay(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnCastStart(int, CastInfo)`

```csharp
public override void OnCastStart(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnRotateForward(int, CastInfo)`

```csharp
protected override void OnRotateForward(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `OnStartChannel(int, CastInfo)`

```csharp
protected override void OnStartChannel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

### `ProcessRange(float)`

```csharp
public override float ProcessRange(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

### `UpdateConfigIndexForCrit()`

```csharp
public void UpdateConfigIndexForCrit()
```
