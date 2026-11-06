# Class: UI_EmoteWheel

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [UI_EmoteWheel](/api/Global.UI_EmoteWheel)

```csharp
public class UI_EmoteWheel : SingletonBehaviour<UI_EmoteWheel>, ISettingsChangedCallback
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fxFocusChanged`** | `public GameObject fxFocusChanged` |  |
| **`fxHide`** | `public GameObject fxHide` |  |
| **`fxShow`** | `public GameObject fxShow` |  |
| **`it_emote`** | `public DewInputTrigger it_emote` |  |
| **`it_emoteCancel`** | `public DewInputTrigger it_emoteCancel` |  |
| **`it_emoteConfirm`** | `public DewInputTrigger it_emoteConfirm` |  |
| **`lineRenderer`** | `public UILineRenderer lineRenderer` |  |
| **`wheelItems`** | `public UI_EmoteWheel_Item[] wheelItems` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShown`** | `public bool isShown { get; }` |  |

## Methods

### `CheckValid()`

```csharp
public bool CheckValid()
```

**Returns:** `bool`

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

### `Show()`

```csharp
public void Show()
```
