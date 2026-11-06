# Class: DevCanvas

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [DevCanvas](/api/Global.DevCanvas)

```csharp
public class DevCanvas : SingletonBehaviour<DevCanvas>, ISettingsChangedCallback
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`consoleObject`** | `public GameObject consoleObject` |  |
| **`state`** | `[NonSerialized] public DevCanvas.DevCanvasState state` |  |

:::

## Methods (1)

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (5)

*Types and components that `DevCanvas` references or depends upon:*

[DewLocalization](/api/Global.DewLocalization) · [GlobalUIManager](/api/Global.GlobalUIManager) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [ManagerBase`1](/api/Global.ManagerBase`1) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1)

:::
