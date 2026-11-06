# Class: AttackTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityTrigger](/api/Global.AbilityTrigger)

```csharp
public class AttackTrigger : AbilityTrigger, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowNonTargetedCast`** | `public bool allowNonTargetedCast` |  |
| **`factor`** | `public ScalingValue factor` |  |

:::

## Methods (18)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CallAttackCompleteBeforePrepareRoutines(EventInfoCast)`

```csharp
public void CallAttackCompleteBeforePrepareRoutines(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `CallAttackCompleteRoutines(AbilityInstance, int, CastInfo)`

```csharp
public void CallAttackCompleteRoutines(AbilityInstance newInstance, int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newInstance` | [`AbilityInstance`](/api/Global.AbilityInstance) |  |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `GetAnimationSpeed()`

```csharp
public override float GetAnimationSpeed()
```

**Returns:** `float`

:::

::: details `GetChannelDurationMultiplier()`

```csharp
public override float GetChannelDurationMultiplier()
```

**Returns:** `float`

:::

::: details `GetCooldownTimeMultiplier(int)`

```csharp
public override float GetCooldownTimeMultiplier(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

:::

::: details `GetPostDelayDurationMultiplier()`

```csharp
public override float GetPostDelayDurationMultiplier()
```

**Returns:** `float`

:::

::: details `OnCastCancelSetCooldownTime(int, CastInfo)`

```csharp
protected override void OnCastCancelSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastComplete(int, CastInfo)`

```csharp
public override AbilityInstance OnCastComplete(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `AbilityInstance`

:::

::: details `OnCastCompleteBeforePrepare(EventInfoCast)`

```csharp
public override void OnCastCompleteBeforePrepare(EventInfoCast cast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cast` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `OnCastCompleteSetCharge(int, CastInfo)`

```csharp
public override void OnCastCompleteSetCharge(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSetCooldownTime(int, CastInfo)`

```csharp
public override void OnCastCompleteSetCooldownTime(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastCompleteSetMinimumDelay(int, CastInfo)`

```csharp
public override void OnCastCompleteSetMinimumDelay(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnCastStart(int, CastInfo)`

```csharp
public override void OnCastStart(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnRotateForward(int, CastInfo)`

```csharp
protected override void OnRotateForward(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `OnStartChannel(int, CastInfo)`

```csharp
protected override void OnStartChannel(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

:::

::: details `ProcessRange(float)`

```csharp
public override float ProcessRange(float original)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `original` | `float` |  |

**Returns:** `float`

:::

::: details `UpdateConfigIndexForCrit()`

```csharp
public void UpdateConfigIndexForCrit()
```

:::
