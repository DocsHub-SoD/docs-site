# Class: CharacterModelDisplay

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
public class CharacterModelDisplay : LogicBehaviour, ILogicUpdate
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessories`** | `public List<string> accessories` |  |
| **`appearDissolveAnimateTime`** | `public float appearDissolveAnimateTime` |  |
| **`fxCharacterChangeEffect`** | `public GameObject fxCharacterChangeEffect` |  |
| **`isFocused`** | `public bool isFocused` |  |
| **`opacity`** | `public float opacity` |  |
| **`skinType`** | `public string skinType` |  |

:::

## Methods (6)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetAbovePosition()`

```csharp
public Vector3 GetAbovePosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetCenterPosition()`

```csharp
public Vector3 GetCenterPosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `Setup(string)`

```csharp
public void Setup(string skinName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skinName` | `string` |  |

:::

::: details `UpdateAccessories()`

```csharp
public void UpdateAccessories()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `CharacterModelDisplay`:*

[PlayLobby_Character](/api/Global.PlayLobby_Character) · [PlayLobby_RotateCharacterTutorial](/api/Global.PlayLobby_RotateCharacterTutorial) · `UI_Lobby_PlayerNametag` · `UI_SkinList_PreviewWindow`

### Dependencies (8)

*Types and components that `CharacterModelDisplay` references or depends upon:*

[Accessory](/api/Global.Accessory) · [DewEffect](/api/Global.DewEffect) · [DewResources](/api/Global.DewResources) · [EntityModel](/api/Global.EntityModel) · [ILobbyCharacterModelOnFocus](/api/Global.ILobbyCharacterModelOnFocus) · [ILobbyCharacterModelSetup](/api/Global.ILobbyCharacterModelSetup) · [LogicBehaviour](/api/Global.LogicBehaviour) · `SetLayerRecursiveExtensions`

:::
