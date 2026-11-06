# Interface: IGamepadFocusListener

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IGamepadFocusListener
```

## Methods (2)

::: details `IsValid()`

```csharp
bool IsValid()
```

**Returns:** `bool`

:::

::: details `OnFocusStateChanged(bool)`

```csharp
void OnFocusStateChanged(bool state)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `state` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `IGamepadFocusListener`:*

[GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusable](/api/Global.IGamepadFocusable) · [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable) · [UI_GamepadInputField](/api/Global.UI_GamepadInputField) · `UI_InGame_Conversations_Instance` · `UI_InGame_FloatingWindow_Chaos` · `UI_InGame_FloatingWindow_CorruptedChaos` · `UI_InGame_SkillButtons` · `UI_InGame_WorldMap` · `UI_Settings_Item` · `UI_Settings_Item_SelectControlPresets`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
