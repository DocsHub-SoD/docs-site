# Struct: Formula

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public struct Formula
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`formula`** | `[HideLabel] [SuffixLabel("f(x)", true)] [ValidateInput("IsValid", "Expression Error", InfoMessageType.Error)] [FormerlySerializedAs("forumla")] public string formula` |  |

:::

## Methods (2)

::: details `Bake()`

```csharp
public void Bake()
```

:::

::: details `Evaluate(float)`

```csharp
public float Evaluate(float x)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `x` | `float` |  |

**Returns:** `float`

:::
