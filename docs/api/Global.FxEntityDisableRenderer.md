# Class: FxEntityDisableRenderer

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxEntityDisableRenderer : MonoBehaviour, IEffectComponent, IAttachableToEntity
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`delay`** | `public float delay` |  |

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

### Dependencies (5)

*Types and components that `FxEntityDisableRenderer` references or depends upon:*

[ActorCheck](/api/Global.ActorCheck) · [Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual) · [IAttachableToEntity](/api/Global.IAttachableToEntity) · [IEffectComponent](/api/Global.IEffectComponent)

:::
