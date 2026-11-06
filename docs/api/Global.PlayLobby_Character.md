# Class: PlayLobby_Character

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(2000)]
public class PlayLobby_Character : LogicBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`characterRotation`** | `public float? characterRotation` |  |
| **`forceSetup`** | `public string forceSetup` |  |
| **`fxClick`** | `public GameObject fxClick` |  |
| **`model`** | `public CharacterModelDisplay model` |  |
| **`playerIndex`** | `public int playerIndex` |  |

## Methods

### `Click()`

```csharp
public void Click()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `IsLocalPlayer()`

```csharp
public bool IsLocalPlayer()
```

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |
