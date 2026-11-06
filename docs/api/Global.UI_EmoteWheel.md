# Class: UI_EmoteWheel

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [UI_EmoteWheel](/api/Global.UI_EmoteWheel)

```csharp
public class UI_EmoteWheel : SingletonBehaviour<UI_EmoteWheel>, ISettingsChangedCallback
```

## Fields (8)

::: details Click to expand Fields (8)

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

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShown`** | `public bool isShown { get; }` |  |

:::

## Methods (3)

::: details `CheckValid()`

```csharp
public bool CheckValid()
```

**Returns:** `bool`

:::

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::

::: details `Show()`

```csharp
public void Show()
```

:::
