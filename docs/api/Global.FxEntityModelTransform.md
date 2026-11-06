# Class: FxEntityModelTransform

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxEntityModelTransform : MonoBehaviour, IEffectComponent, IAttachableToEntity
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`duration`** | `public float duration` |  |
| **`from`** | `public Transform from` |  |
| **`normalizedLerpCurve`** | `public AnimationCurve normalizedLerpCurve` |  |
| **`to`** | `public Transform to` |  |

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

### Dependencies (3)

*Types and components that `FxEntityModelTransform` references or depends upon:*

[Entity](/api/Global.Entity) · [IAttachableToEntity](/api/Global.IAttachableToEntity) · [IEffectComponent](/api/Global.IEffectComponent)

:::
