# Class: ModConfig

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ExampleModConfig](/api/Global.ExampleModConfig)

```csharp
public abstract class ModConfig
```

## Methods

### `BuildWidgets(Transform, out SafeAction, out SafeAction)`

```csharp
public virtual void BuildWidgets(Transform parent, out SafeAction onChanged, out SafeAction requestUpdate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |
| `onChanged` | [SafeAction](/api/Global.SafeAction) |  |
| `requestUpdate` | [SafeAction](/api/Global.SafeAction) |  |

### `Clone()`

```csharp
public virtual ModConfig Clone()
```

**Returns:** `ModConfig`

### `CopyTo(ModConfig)`

```csharp
public virtual void CopyTo(ModConfig other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [ModConfig](/api/Global.ModConfig) |  |
