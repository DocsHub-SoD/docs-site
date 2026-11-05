# Class: FxAnimatorSetFloat

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class FxAnimatorSetFloat : MonoBehaviour, IEffectComponent, IAttachableToEntity
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animator`** | `public Animator animator` |  |
| **`delay`** | `public float delay` |  |
| **`parameter`** | `public string parameter` |  |
| **`value`** | `public AnimationCurve value` |  |

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
