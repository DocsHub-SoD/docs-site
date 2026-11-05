# Struct: Formula

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public struct Formula
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`formula`** | `[HideLabel]
[SuffixLabel("f(x)", true)]
[ValidateInput("IsValid", "Expression Error", InfoMessageType.Error)]
[FormerlySerializedAs("forumla")]
public string formula` |  |

## Methods

### `Bake()`

```csharp
public void Bake()
```

### `Evaluate(float)`

```csharp
public float Evaluate(float x)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `x` | `float` |  |

**Returns:** `float`
