# Class: EntityAnimation

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityAnimation : EntityComponent, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityAnimStatus`** | `public EntityAnimation.AbilityAnimationStatus abilityAnimStatus` |  |
| **`animator`** | `[NonSerialized] public Animator animator` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`model`** | `public EntityModel model { get; }` |  |

:::

## Methods (11)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `PlayAbilityAnimation(DewAnimationClip, float, float)`

```csharp
public void PlayAbilityAnimation(DewAnimationClip clip, float speed, float clipSelectValue)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
| `speed` | `float` |  |
| `clipSelectValue` | `float` |  |

:::

::: details `PlayAbilityAnimation(DewAnimationClip, float)`

```csharp
public void PlayAbilityAnimation(DewAnimationClip clip, float speed = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |
| `speed` | `float` |  |

:::

::: details `PlayStaggerAnimation()`

```csharp
public void PlayStaggerAnimation()
```

:::

::: details `ReplaceAnimation(ReplaceableAnimationType, AnimationClip)`

```csharp
public void ReplaceAnimation(EntityAnimation.ReplaceableAnimationType type, AnimationClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `clip` | `UnityEngine.AnimationClip` |  |

:::

::: details `ReplaceAnimationLocal(ReplaceableAnimationType, AnimationClipWithSpeed)`

```csharp
public void ReplaceAnimationLocal(EntityAnimation.ReplaceableAnimationType type, AnimationClipWithSpeed newData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `newData` | [`AnimationClipWithSpeed`](/api/Global.AnimationClipWithSpeed) |  |

:::

::: details `ReplaceAnimationLocal(ReplaceableAnimationType, AnimationClip)`

```csharp
public void ReplaceAnimationLocal(EntityAnimation.ReplaceableAnimationType type, AnimationClip newClip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`EntityAnimation.ReplaceableAnimationType`](/api/Global.EntityAnimation) |  |
| `newClip` | `UnityEngine.AnimationClip` |  |

:::

::: details `SetupModel()`

```csharp
public void SetupModel()
```

:::

::: details `StopAbilityAnimation()`

```csharp
public void StopAbilityAnimation()
```

:::

::: details `StopAbilityAnimation(DewAnimationClip)`

Stop ability animation if currently playing animation is given clip.

```csharp
public void StopAbilityAnimation(DewAnimationClip clip)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAnimationClip`](/api/Global.DewAnimationClip) |  |

:::
