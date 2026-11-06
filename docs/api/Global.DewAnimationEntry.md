# Class: DewAnimationEntry

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class DewAnimationEntry
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`duration`** | `[MinValue(1.401298464324817E-45)] public float duration` |  |
| **`rawClip`** | `public AnimationClip rawClip` |  |
| **`timeCurve`** | `[LabelText("Ease")] public DewEase timeCurve` |  |
| **`trimRange`** | `[MinMaxSlider(0, "_rawClipLength", false)] public Vector2 trimRange` |  |

:::

## Methods (1)

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `DewAnimationEntry`:*

[DewAnimationClip](/api/Global.DewAnimationClip)

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#dewease" class="enum-link" data-tooltip="Linear=0 · EaseInQuad=1 · EaseOutQuad=2 · EaseInOutQuad=3 · EaseInCubic=4 (+27 more)">DewEase</a>

:::
