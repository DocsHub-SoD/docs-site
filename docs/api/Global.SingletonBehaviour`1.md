# Class: SingletonBehaviour&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DevCanvas](/api/Global.DevCanvas) → [Room_BossArena](/api/Global.Room_BossArena) → [Special_RoomAnnouncer](/api/Global.Special_RoomAnnouncer) → [UI_BindingWindow](/api/Global.UI_BindingWindow) → [UI_EmoteWheel](/api/Global.UI_EmoteWheel) → [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput)

```csharp
public class SingletonBehaviour<T> : MonoBehaviour where T : MonoBehaviour
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static T instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static T softInstance { get; }` |  |

## Methods

### `Awake()`

```csharp
protected virtual void Awake()
```
