# Class: FxSelectiveVisibility

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DisallowMultipleComponent]
public class FxSelectiveVisibility : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forceFail`** | `public static bool forceFail` |  |
| **`hideOnSummons`** | `[ShowIf("@visibleTo != EffectVisibility.Everyone", true)]
public bool hideOnSummons` |  |
| **`invertVisibility`** | `public bool invertVisibility` |  |
| **`parent`** | `[HideInInspector]
public Actor parent` |  |
| **`visibleTo`** | `[InfoBox("@_helpText", InfoMessageType.Info, null)]
public EffectVisibility visibleTo` |  |
| **`wasDisabled`** | `[HideInInspector]
public bool wasDisabled` |  |

## Methods

### `IsVisibleLocally()`

```csharp
public bool IsVisibleLocally()
```

**Returns:** `bool`

### `OnAfterDeserialize()`

```csharp
public void OnAfterDeserialize()
```

### `OnBeforeSerialize()`

```csharp
public void OnBeforeSerialize()
```
