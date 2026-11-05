# Class: FxEntityAnimation

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxEntityAnimation : MonoBehaviour, IEffectComponent, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animClip`** | `public DewAnimationClip animClip` |  |
| **`delay`** | `public float delay` |  |
| **`speed`** | `public float speed` |  |
| **`stopAnimationWhenStopped`** | `[ToggleLeft]
public bool stopAnimationWhenStopped` |  |

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
| `target` | [Entity](/api/Global.Entity) |  |

### `Play()`

```csharp
public void Play()
```

### `Stop()`

```csharp
public void Stop()
```
