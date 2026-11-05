# Class: SkillVisualOverrideItem

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class SkillVisualOverrideItem
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`changeHue`** | `public bool changeHue` |  |
| **`changeSaturation`** | `public bool changeSaturation` |  |
| **`changeValue`** | `public bool changeValue` |  |
| **`hue`** | `[Range(0, 360)]
[ShowIf("changeHue", true)]
public float hue` |  |
| **`saturationMultiplier`** | `[ShowIf("changeSaturation", true)]
public float saturationMultiplier` |  |
| **`targets`** | `public string[] targets` |  |
| **`valueMultiplier`** | `[ShowIf("changeValue", true)]
public float valueMultiplier` |  |

## Methods

### `Apply(GameObject)`

```csharp
public void Apply(GameObject gobj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gobj` | `UnityEngine.GameObject` |  |
