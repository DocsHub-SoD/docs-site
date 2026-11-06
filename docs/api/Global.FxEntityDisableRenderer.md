# Class: FxEntityDisableRenderer

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxEntityDisableRenderer : MonoBehaviour, IEffectComponent, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`delay`** | `public float delay` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

## Methods

### `OnAttachToEntity(Entity)`

```csharp
public void OnAttachToEntity(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

### `Play()`

```csharp
public void Play()
```

### `Stop()`

```csharp
public void Stop()
```
