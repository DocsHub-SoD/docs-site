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
