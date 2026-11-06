# Class: TitleManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [TitleManager](/api/Global.TitleManager)

```csharp
public class TitleManager : ManagerBase<TitleManager>, ILogicUpdate, ISettingsChangedCallback
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`didConvertSave`** | `[NonSerialized] public bool didConvertSave` |  |
| **`didNotPlayTutorialObject`** | `public GameObject didNotPlayTutorialObject` |  |
| **`didPlayTutorialObject`** | `public GameObject didPlayTutorialObject` |  |
| **`langSelectionView`** | `public View langSelectionView` |  |
| **`onShowLangSelectionView`** | `public UnityEvent onShowLangSelectionView` |  |
| **`riftParticleSystem`** | `public ParticleSystem riftParticleSystem` |  |
| **`splashView`** | `public View splashView` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`needTutorial`** | `public bool needTutorial { get; }` |  |

:::

## Methods (11)

::: details `CheckTutorial(Action)`

Execute the callback if user has played tutorial.If not, ask if the user wants to skip the tutorial.

```csharp
public void CheckTutorial(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

:::

::: details `EnterCollectables()`

```csharp
public void EnterCollectables()
```

:::

::: details `EnterContinueDreaming()`

```csharp
public void EnterContinueDreaming()
```

:::

::: details `EnterSingleplayerLimbo()`

```csharp
public void EnterSingleplayerLimbo()
```

:::

::: details `EnterSingleplayerShapeOfDreams()`

```csharp
public void EnterSingleplayerShapeOfDreams()
```

:::

::: details `EnterTutorial()`

```csharp
public void EnterTutorial()
```

:::

::: details `ExitToDesktop()`

```csharp
public void ExitToDesktop()
```

:::

::: details `JoinLobby(string)`

```csharp
public void JoinLobby(string lobbyId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lobbyId` | `string` |  |

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

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::

::: details `ShowMods()`

```csharp
public void ShowMods()
```

:::
