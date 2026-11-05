# Class: UI_GamepadFocusableGroup

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_GamepadFocusableGroup : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`customTarget`** | `[ShowIf("@enterBehavior == EnterGroupBehavior.Custom", true)]
public GameObject customTarget` |  |
| **`enterBehavior`** | `[HideLabel]
[LabelText("When Entering")]
public EnterGroupBehavior enterBehavior` |  |

## Methods

### `GetEnterFocusable(GameObject, EnterGroupBehavior, Vector2)`

```csharp
public static IGamepadFocusable GetEnterFocusable(GameObject parent, EnterGroupBehavior enterBehavior, Vector2 direction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.GameObject` |  |
| `enterBehavior` | [EnterGroupBehavior](/api/Global.EnterGroupBehavior) |  |
| `direction` | `UnityEngine.Vector2` |  |

**Returns:** `IGamepadFocusable`

### `GetEnterFocusable(Vector2)`

```csharp
public virtual IGamepadFocusable GetEnterFocusable(Vector2 direction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector2` |  |

**Returns:** `IGamepadFocusable`

### `IsValid()`

```csharp
public bool IsValid()
```

**Returns:** `bool`
