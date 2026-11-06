# Class: UI_HoldToRapidClickButton

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_HoldToRapidClickButton : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onClick`** | `[InfoBox("Subscribe to this instead of Button's to prevent double clicks.", InfoMessageType.Info, null)] public UnityEvent onClick` |  |

## Methods

### `OnPointerDown(PointerEventData)`

```csharp
public void OnPointerDown(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

### `OnPointerUp(PointerEventData)`

```csharp
public void OnPointerUp(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |
