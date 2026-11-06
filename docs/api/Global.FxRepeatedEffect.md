# Class: FxRepeatedEffect

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(500)]
public class FxRepeatedEffect : LogicBehaviour, ILogicUpdate, IEffectComponent, IAttachableToEntity
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`interval`** | `public float interval` |  |
| **`playNew`** | `public bool playNew` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (4)

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `Play()`

```csharp
public void Play()
```

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (6)

*Types and components that `FxRepeatedEffect` references or depends upon:*

[ActorCheck](/api/Global.ActorCheck) · [DewEffect](/api/Global.DewEffect) · [Entity](/api/Global.Entity) · [IAttachableToEntity](/api/Global.IAttachableToEntity) · [IEffectComponent](/api/Global.IEffectComponent) · [LogicBehaviour](/api/Global.LogicBehaviour)

:::
