# Class: UI_GamepadFocusable

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DisallowMultipleComponent]`
- **Inheritance / Derived:** [UI_GamepadInputField](/api/Global.UI_GamepadInputField) → [UI_GamepadTextInput_Key](/api/Global.UI_GamepadTextInput_Key)

```csharp
[DisallowMultipleComponent]
public class UI_GamepadFocusable : MonoBehaviour, IGamepadFocusable, IGamepadFocusListener
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canHoldConfirmToRepeat`** | `public bool canHoldConfirmToRepeat` |  |
| **`display`** | `public SelectionDisplayType display` |  |
| **`focusOnEnable`** | `public bool focusOnEnable` |  |
| **`ignoreSelectableInteractivity`** | `public bool ignoreSelectableInteractivity` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isFocused`** | `public bool isFocused { get; }` |  |

:::

## Methods (6)

::: details `CanBeFocused()`

```csharp
public virtual bool CanBeFocused()
```

**Returns:** `bool`

:::

::: details `CanHoldConfirmToRepeat()`

```csharp
public bool CanHoldConfirmToRepeat()
```

**Returns:** `bool`

:::

::: details `GetSelectionDisplayType()`

```csharp
public SelectionDisplayType GetSelectionDisplayType()
```

**Returns:** `SelectionDisplayType`

:::

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected virtual void OnEnable()
```

:::

::: details `OnFocusStateChanged(bool)`

```csharp
public virtual void OnFocusStateChanged(bool state)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `state` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `UI_GamepadFocusable`:*

`UI_Collectables_ObjectItem` · `UI_Constellations_CategoryGroup` · `UI_Constellations_StarItem` · `UI_EmoteList_Item_GamepadFocusable` · [UI_GamepadInputField](/api/Global.UI_GamepadInputField) · [UI_GamepadTextInput_Key](/api/Global.UI_GamepadTextInput_Key) · `UI_InGame_CurrentArtifact` · `UI_Lobby_ChangeCharacterGamepadButton` · `UI_Lobby_Constellations_Skills_ContextMenu_Item` · `UI_Lobby_Loadout_AvailableSkills_Item` · `UI_PlayTutorial_AdvanceButton`

### Dependencies (5)

*Types and components that `UI_GamepadFocusable` references or depends upon:*

[Dew](/api/Global.Dew) · [GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusListener](/api/Global.IGamepadFocusListener) · [IGamepadFocusable](/api/Global.IGamepadFocusable) · [ManagerBase`1](/api/Global.ManagerBase`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`SelectionDisplayType`](/enums#selectiondisplaytype)

:::
