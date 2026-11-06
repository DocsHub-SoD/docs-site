# Class: TitleManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [TitleManager](/api/Global.TitleManager)

```csharp
public class TitleManager : ManagerBase<TitleManager>, ILogicUpdate, ISettingsChangedCallback
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didConvertSave`** | `[NonSerialized] public bool didConvertSave` |  |
| **`didNotPlayTutorialObject`** | `public GameObject didNotPlayTutorialObject` |  |
| **`didPlayTutorialObject`** | `public GameObject didPlayTutorialObject` |  |
| **`langSelectionView`** | `public View langSelectionView` |  |
| **`onShowLangSelectionView`** | `public UnityEvent onShowLangSelectionView` |  |
| **`riftParticleSystem`** | `public ParticleSystem riftParticleSystem` |  |
| **`splashView`** | `public View splashView` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`needTutorial`** | `public bool needTutorial { get; }` |  |

## Methods

### `CheckTutorial(Action)`

Execute the callback if user has played tutorial.If not, ask if the user wants to skip the tutorial.

```csharp
public void CheckTutorial(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

### `EnterCollectables()`

```csharp
public void EnterCollectables()
```

### `EnterContinueDreaming()`

```csharp
public void EnterContinueDreaming()
```

### `EnterSingleplayerLimbo()`

```csharp
public void EnterSingleplayerLimbo()
```

### `EnterSingleplayerShapeOfDreams()`

```csharp
public void EnterSingleplayerShapeOfDreams()
```

### `EnterTutorial()`

```csharp
public void EnterTutorial()
```

### `ExitToDesktop()`

```csharp
public void ExitToDesktop()
```

### `JoinLobby(string)`

```csharp
public void JoinLobby(string lobbyId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobbyId` | `string` |  |

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

### `ShowMods()`

```csharp
public void ShowMods()
```
