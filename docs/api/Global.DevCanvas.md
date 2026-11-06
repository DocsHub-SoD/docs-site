# Class: DevCanvas

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [DevCanvas](/api/Global.DevCanvas)

```csharp
public class DevCanvas : SingletonBehaviour<DevCanvas>, ISettingsChangedCallback
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`consoleObject`** | `public GameObject consoleObject` |  |
| **`state`** | `[NonSerialized] public DevCanvas.DevCanvasState state` |  |

## Methods

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```
