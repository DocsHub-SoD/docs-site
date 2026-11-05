# Class: ObjectHighlightManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ObjectHighlightManager](/api/Global.ObjectHighlightManager)

```csharp
public class ObjectHighlightManager : ManagerBase<ObjectHighlightManager>, ILogicUpdate, ICinematicCameraHelperStateReceiver
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ally`** | `public ObjectHighlightManager.OutlineStyle ally` |  |
| **`enemy`** | `public ObjectHighlightManager.OutlineStyle enemy` |  |
| **`interactable`** | `public ObjectHighlightManager.OutlineStyle interactable` |  |
| **`isObjectHighlightDisabled`** | `[NonSerialized]
public bool isObjectHighlightDisabled` |  |
| **`MouseDownStrength`** | `public const float MouseDownStrength = 0.6` |  |
| **`MouseOverStrength`** | `public const float MouseOverStrength = 0.4` |  |
| **`neutral`** | `public ObjectHighlightManager.OutlineStyle neutral` |  |
| **`own`** | `public ObjectHighlightManager.OutlineStyle own` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetProfile()`

```csharp
public static HighlightProfile GetProfile()
```

**Returns:** `HighlightPlus.HighlightProfile`

### `OnCinematicCameraHelperChanged(bool)`

```csharp
public void OnCinematicCameraHelperChanged(bool on)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `on` | `bool` |  |
