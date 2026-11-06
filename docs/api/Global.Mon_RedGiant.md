# Class: Mon_RedGiant

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [Monster](/api/Global.Monster)

```csharp
public class Mon_RedGiant : Monster, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`deathEffects`** | `public GameObject deathEffects` |  |
| **`dpsText`** | `public TextMeshPro dpsText` |  |

:::

## Methods (4)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

:::

::: details `OnDeath(EventInfoKill)`

```csharp
protected override void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (9)

*Types and components that `Mon_RedGiant` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [EntityAIContext](/api/Global.EntityAIContext) · [EntityControl](/api/Global.EntityControl) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoKill](/api/Global.EventInfoKill) · [Monster](/api/Global.Monster) · `QuaternionFlattenExtension` · [SafeAction`1](/api/Global.SafeAction`1)

:::
