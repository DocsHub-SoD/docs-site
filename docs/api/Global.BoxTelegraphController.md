# Class: BoxTelegraphController

- **Category:** <span class="cat-dot" style="--cat-color: #a855f7" data-cat="Buffs & Statuses"></span> Buffs & Statuses
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class BoxTelegraphController : MonoBehaviour, IEffectComponent, IEffectWithSpeed
```

## Fields (11)

::: details Click to expand Fields (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`animateX`** | `public BoxTelegraphAnimType animateX` |  |
| **`animateXEase`** | `[HideLabel] [ShowIf("@animateX != BoxTelegraphAnimType.None", true)] public DewEase animateXEase` |  |
| **`animateY`** | `public BoxTelegraphAnimType animateY` |  |
| **`animateYEase`** | `[HideLabel] [ShowIf("@animateY != BoxTelegraphAnimType.None", true)] public DewEase animateYEase` |  |
| **`duration`** | `public float duration` |  |
| **`height`** | `public float height` |  |
| **`inners`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] inners` |  |
| **`outers`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] outers` |  |
| **`reds`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] reds` |  |
| **`whites`** | `[FoldoutGroup("References", 0)] public SpriteRenderer[] whites` |  |
| **`width`** | `public float width` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |
| **`value`** | `public float value { get; set; }` |  |

:::

## Methods (3)

::: details `ApplySpeedMultiplier(float)`

```csharp
public void ApplySpeedMultiplier(float speed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `speed` | `float` |  |

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

### Used By (2)

*Classes and systems that invoke, reference, or depend on `BoxTelegraphController`:*

`Ai_Mon_Special_BossObliviax_ChargeSequence_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk_ExtraAtk`

### Dependencies (4)

*Types and components that `BoxTelegraphController` references or depends upon:*

[EaseFunction](/api/Global.EaseFunction) · [EasingFunction](/api/Global.EasingFunction) · [IEffectComponent](/api/Global.IEffectComponent) · [IEffectWithSpeed](/api/Global.IEffectWithSpeed)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`BoxTelegraphAnimType`](/enums#boxtelegraphanimtype) · [`DewEase`](/enums#dewease)

:::
