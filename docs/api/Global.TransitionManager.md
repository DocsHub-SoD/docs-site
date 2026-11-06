# Class: TransitionManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [TransitionManager](/api/Global.TransitionManager)

```csharp
public class TransitionManager : ManagerBase<TransitionManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`busyObject`** | `public GameObject busyObject` |  |
| **`fadeTime`** | `public float fadeTime` |  |
| **`fxTransition`** | `public GameObject fxTransition` |  |
| **`loadingTexts`** | `public TextMeshProUGUI[] loadingTexts` |  |
| **`newTipCooldownTime`** | `public float newTipCooldownTime` |  |
| **`onFadeIn`** | `public Action onFadeIn` |  |
| **`onFadeOut`** | `public Action onFadeOut` |  |
| **`onStateChanged`** | `public SafeAction onStateChanged` |  |
| **`screenFadeCg`** | `public CanvasGroup screenFadeCg` |  |
| **`tipText`** | `public TextMeshProUGUI tipText` |  |
| **`whiteFadeCg`** | `public CanvasGroup whiteFadeCg` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`state`** | `[ShowInInspector] public TransitionManager.StateType state { get; }` |  |

## Methods

### `FadeIn()`

```csharp
[Button]
public void FadeIn()
```

### `FadeInRoutine()`

```csharp
public IEnumerator FadeInRoutine()
```

**Returns:** `System.Collections.IEnumerator`

### `FadeOut()`

```csharp
[Button]
public void FadeOut()
```

### `FadeOut(bool)`

```csharp
public void FadeOut(bool showTips)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `showTips` | `bool` |  |

### `FadeOutRoutine(bool)`

```csharp
public IEnumerator FadeOutRoutine(bool showTips)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `showTips` | `bool` |  |

**Returns:** `System.Collections.IEnumerator`

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `LoadScene(string, bool)`

```csharp
public void LoadScene(string sceneName, bool dontFadeIn = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sceneName` | `string` |  |
| `dontFadeIn` | `bool` |  |

### `PlayGame(DewNetworkStartSettings)`

```csharp
public void PlayGame(DewNetworkStartSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`DewNetworkStartSettings`](/api/Global.DewNetworkStartSettings) |  |

### `SetBusy(bool)`

```csharp
public void SetBusy(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

### `UpdateLoadingStatus(LoadingStatus)`

```csharp
public void UpdateLoadingStatus(LoadingStatus status)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `status` | [`LoadingStatus`](/api/Global.LoadingStatus) |  |

### `UpdateLoadingStatus(string)`

```csharp
public void UpdateLoadingStatus(string rawText)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rawText` | `string` |  |
