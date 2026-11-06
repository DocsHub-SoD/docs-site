# Class: CharacterModelDisplay

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
public class CharacterModelDisplay : LogicBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessories`** | `public List<string> accessories` |  |
| **`appearDissolveAnimateTime`** | `public float appearDissolveAnimateTime` |  |
| **`fxCharacterChangeEffect`** | `public GameObject fxCharacterChangeEffect` |  |
| **`isFocused`** | `public bool isFocused` |  |
| **`opacity`** | `public float opacity` |  |
| **`skinType`** | `public string skinType` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetAbovePosition()`

```csharp
public Vector3 GetAbovePosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetCenterPosition()`

```csharp
public Vector3 GetCenterPosition()
```

**Returns:** `UnityEngine.Vector3`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `Setup(string)`

```csharp
public void Setup(string skinName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skinName` | `string` |  |

### `UpdateAccessories()`

```csharp
public void UpdateAccessories()
```
