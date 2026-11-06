# Class: UI_GamepadFocusableGroup

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_GamepadFocusableGroup : MonoBehaviour
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`customTarget`** | `[ShowIf("@enterBehavior == EnterGroupBehavior.Custom", true)] public GameObject customTarget` |  |
| **`enterBehavior`** | `[HideLabel] [LabelText("When Entering")] public EnterGroupBehavior enterBehavior` |  |

:::

## Methods (3)

::: details `GetEnterFocusable(GameObject, EnterGroupBehavior, Vector2)`

```csharp
public static IGamepadFocusable GetEnterFocusable(GameObject parent, EnterGroupBehavior enterBehavior, Vector2 direction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.GameObject` |  |
| `enterBehavior` | [`EnterGroupBehavior`](/api/Global.EnterGroupBehavior) |  |
| `direction` | `UnityEngine.Vector2` |  |

**Returns:** `IGamepadFocusable`

:::

::: details `GetEnterFocusable(Vector2)`

```csharp
public virtual IGamepadFocusable GetEnterFocusable(Vector2 direction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector2` |  |

**Returns:** `IGamepadFocusable`

:::

::: details `IsValid()`

```csharp
public bool IsValid()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `UI_GamepadFocusableGroup`:*

[GlobalUIManager](/api/Global.GlobalUIManager) · `UI_Collectables_MainView` · [UI_GamepadNavigationHint](/api/Global.UI_GamepadNavigationHint) · `UI_GamepadShoulderControls` · `UI_Lobby_DifficultyGroup_GamepadFocusableGroup`

### Dependencies (6)

*Types and components that `UI_GamepadFocusableGroup` references or depends upon:*

`GetComponentsNonAllocExtension` · [GlobalUIManager](/api/Global.GlobalUIManager) · [IGamepadFocusable](/api/Global.IGamepadFocusable) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · `RectTransformGetWorldRectExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`EnterGroupBehavior`](/enums#entergroupbehavior)

:::
