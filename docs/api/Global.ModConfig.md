# Class: ModConfig

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ExampleModConfig](/api/Global.ExampleModConfig)

```csharp
public abstract class ModConfig
```

## Methods (3)

::: details `BuildWidgets(Transform, out SafeAction, out SafeAction)`

```csharp
public virtual void BuildWidgets(Transform parent, out SafeAction onChanged, out SafeAction requestUpdate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |
| `onChanged` | [`SafeAction`](/api/Global.SafeAction) |  |
| `requestUpdate` | [`SafeAction`](/api/Global.SafeAction) |  |

:::

::: details `Clone()`

```csharp
public virtual ModConfig Clone()
```

**Returns:** `ModConfig`

:::

::: details `CopyTo(ModConfig)`

```csharp
public virtual void CopyTo(ModConfig other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`ModConfig`](/api/Global.ModConfig) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `ModConfig`:*

[DewMod](/api/Global.DewMod) · [ExampleModConfig](/api/Global.ExampleModConfig)

### Dependencies (1)

*Types and components that `ModConfig` references or depends upon:*

[DewGUI](/api/Global.DewGUI)

:::
