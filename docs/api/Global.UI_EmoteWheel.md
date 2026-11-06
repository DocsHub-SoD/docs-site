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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `UI_EmoteWheel`:*

[ControlManager](/api/Global.ControlManager)

### Dependencies (17)

*Types and components that `UI_EmoteWheel` references or depends upon:*

[ChatManager](/api/Global.ChatManager) · [ControlManager](/api/Global.ControlManager) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [GlobalUIManager](/api/Global.GlobalUIManager) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [LobbyUIManager](/api/Global.LobbyUIManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · `RectTransformGetWorldRectExtension` · [SafeAction`2](/api/Global.SafeAction`2) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1) · [UIManager](/api/Global.UIManager) · [UI_EmoteWheel_Item](/api/Global.UI_EmoteWheel_Item) · [UI_StationaryEmote](/api/Global.UI_StationaryEmote)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`InputMode`](/enums#inputmode)

:::
