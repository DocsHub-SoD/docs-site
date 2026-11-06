# Class: FxEntityAnimation

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxEntityAnimation : MonoBehaviour, IEffectComponent, IAttachableToEntity
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animClip`** | `public DewAnimationClip animClip` |  |
| **`delay`** | `public float delay` |  |
| **`speed`** | `public float speed` |  |
| **`stopAnimationWhenStopped`** | `[ToggleLeft] public bool stopAnimationWhenStopped` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (3)

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

*Types and components that `FxEntityAnimation` references or depends upon:*

[ActorCheck](/api/Global.ActorCheck) · [DewAnimationClip](/api/Global.DewAnimationClip) · [Entity](/api/Global.Entity) · [EntityAnimation](/api/Global.EntityAnimation) · [IAttachableToEntity](/api/Global.IAttachableToEntity) · [IEffectComponent](/api/Global.IEffectComponent)

:::
