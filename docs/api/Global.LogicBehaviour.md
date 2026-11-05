# Class: LogicBehaviour

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [CharacterModelDisplay](/api/Global.CharacterModelDisplay) → [CinematicCameraHelper](/api/Global.CinematicCameraHelper) → [CustomLogicBehavior](/api/Global.CustomLogicBehavior) → [DewBeamRenderer](/api/Global.DewBeamRenderer) → [DewCanvas](/api/Global.DewCanvas) → [FxAttachToEntity](/api/Global.FxAttachToEntity) → [FxCastTelegraph](/api/Global.FxCastTelegraph) → [FxRepeatedEffect](/api/Global.FxRepeatedEffect) → [HighlightProvider](/api/Global.HighlightProvider) → `ManagerBase&lt;T&gt;` → [PlayLobby_Character](/api/Global.PlayLobby_Character) → [PlayLobby_Fireplace](/api/Global.PlayLobby_Fireplace) → [RoomSection](/api/Global.RoomSection) → [RoomSectionComponent](/api/Global.RoomSectionComponent) → [Title_LastGameCharacters](/api/Global.Title_LastGameCharacters) → [UI_BindItem](/api/Global.UI_BindItem) → [UI_GamepadBindButton](/api/Global.UI_GamepadBindButton)

```csharp
public class LogicBehaviour : MonoBehaviour, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public virtual bool shouldRegisterUpdates { get; }` |  |

## Methods

### `FrameUpdate()`

```csharp
public virtual void FrameUpdate()
```

### `GetComponent&lt;T&gt;(out T)`

```csharp
protected void GetComponent<T>(out T comp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `comp` | `T` |  |
| `` | `T` |  |

### `LogicUpdate(float)`

```csharp
public virtual void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDisable()`

```csharp
protected virtual void OnDisable()
```

### `OnEnable()`

```csharp
protected virtual void OnEnable()
```
