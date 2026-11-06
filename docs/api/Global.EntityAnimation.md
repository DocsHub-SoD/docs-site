# Class: EntityAnimation

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityAnimation : EntityComponent, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityAnimStatus`** | `public EntityAnimation.AbilityAnimationStatus abilityAnimStatus` |  |
| **`animator`** | `[NonSerialized] public Animator animator` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`model`** | `public EntityModel model { get; }` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `PlayAbilityAnimation(DewAnimationClip, float, float)`

```csharp
public void PlayAbilityAnimation(DewAnimationClip clip, float speed, float clipSelectValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
| `speed` | `float` |  |
| `clipSelectValue` | `float` |  |

### `PlayAbilityAnimation(DewAnimationClip, float)`

```csharp
public void PlayAbilityAnimation(DewAnimationClip clip, float speed = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
| `speed` | `float` |  |

### `PlayStaggerAnimation()`

```csharp
public void PlayStaggerAnimation()
```

### `ReplaceAnimation(ReplaceableAnimationType, AnimationClip)`

```csharp
public void ReplaceAnimation(EntityAnimation.ReplaceableAnimationType type, AnimationClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `clip` | `UnityEngine.AnimationClip` |  |

### `ReplaceAnimationLocal(ReplaceableAnimationType, AnimationClipWithSpeed)`

```csharp
public void ReplaceAnimationLocal(EntityAnimation.ReplaceableAnimationType type, AnimationClipWithSpeed newData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `newData` | [`AnimationClipWithSpeed`](/api/Global.AnimationClipWithSpeed) |  |

### `ReplaceAnimationLocal(ReplaceableAnimationType, AnimationClip)`

```csharp
public void ReplaceAnimationLocal(EntityAnimation.ReplaceableAnimationType type, AnimationClip newClip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `newClip` | `UnityEngine.AnimationClip` |  |

### `SetupModel()`

```csharp
public void SetupModel()
```

### `StopAbilityAnimation()`

```csharp
public void StopAbilityAnimation()
```

### `StopAbilityAnimation(DewAnimationClip)`

Stop ability animation if currently playing animation is given clip.

```csharp
public void StopAbilityAnimation(DewAnimationClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
