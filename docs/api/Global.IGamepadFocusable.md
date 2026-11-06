# Interface: IGamepadFocusable

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IGamepadFocusable : IGamepadFocusListener
```

## Methods (5)

::: details `CanBeFocused()`

```csharp
bool CanBeFocused()
```

**Returns:** `bool`

:::

::: details `CanHoldConfirmToRepeat()`

```csharp
bool CanHoldConfirmToRepeat()
```

**Returns:** `bool`

:::

::: details `GetBehavior()`

```csharp
FocusableBehavior GetBehavior()
```

**Returns:** `FocusableBehavior`

:::

::: details `GetSelectionDisplayType()`

```csharp
SelectionDisplayType GetSelectionDisplayType()
```

**Returns:** `SelectionDisplayType`

:::

::: details `GetTransform()`

```csharp
RectTransform GetTransform()
```

**Returns:** `UnityEngine.RectTransform`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (27)

*Classes and systems that invoke, reference, or depend on `IGamepadFocusable`:*

`ContextMenu` · [GlobalUIManager](/api/Global.GlobalUIManager) · `UI_DropdownControls` · `UI_EmoteList_EditEmote` · `UI_EmoteList_EditEmoteWheel_FloatingEmote` · [UI_GamepadFocusable](/api/Global.UI_GamepadFocusable) · [UI_GamepadFocusableGroup](/api/Global.UI_GamepadFocusableGroup) · [UI_GamepadInputField](/api/Global.UI_GamepadInputField) · [UI_GamepadNavigationHint](/api/Global.UI_GamepadNavigationHint) · `UI_GamepadScrollRect` · `UI_GamepadShoulderControls` · `UI_InGame_Conversations_Instance` · `UI_InGame_HeroDetailWindow` · `UI_InGame_SkillButtons` · `UI_InGame_WorldMap` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_FloatingStar` · `UI_Lobby_Constellations_HeroConstellation` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_DejavuWindow` · `UI_Lobby_DifficultyGroup_GamepadFocusableGroup` · `UI_Lobby_HeroList` · `UI_Settings_Item` · `UI_Settings_Item_SelectControlPresets` · `UI_TooltipManager` · `UI_Tooltip_ObjEditSkillActions` · `UI_TravelerStory_HeroConstellation`

### Dependencies (3)

*Types and components that `IGamepadFocusable` references or depends upon:*

[GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusListener](/api/Global.IGamepadFocusListener) · [ManagerBase`1](/api/Global.ManagerBase`1)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`FocusableBehavior`](/enums#focusablebehavior) · [`SelectionDisplayType`](/enums#selectiondisplaytype)

:::
