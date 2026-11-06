# Class: View

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[ExecuteAlways]
[RequireComponent(typeof(CanvasGroup))]
[RequireComponent(typeof(Canvas))]
public class View : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockRaycastWhenShown`** | `[ToggleLeft] public bool blockRaycastWhenShown` |  |
| **`disableGameObjectWhenHidden`** | `[ToggleLeft] public bool disableGameObjectWhenHidden` |  |
| **`disablesInGamePlayingInput`** | `[ToggleLeft] public bool disablesInGamePlayingInput` |  |
| **`fadeTime`** | `public float fadeTime` |  |
| **`hideEffect`** | `public GameObject hideEffect` |  |
| **`ignoreOn`** | `[ShowIf("@showBehavior == View.ShowBehavior.UseState", true)] public List<string> ignoreOn` |  |
| **`instances`** | `public static List<View> instances` |  |
| **`interactableWhenShown`** | `[ToggleLeft] public bool interactableWhenShown` |  |
| **`onHide`** | `public UnityEvent onHide` |  |
| **`onShow`** | `public UnityEvent onShow` |  |
| **`showBehavior`** | `public View.ShowBehavior showBehavior` |  |
| **`showEffect`** | `public GameObject showEffect` |  |
| **`showOn`** | `[ShowIf("@showBehavior == View.ShowBehavior.UseState", true)] public List<string> showOn` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShowing`** | `public bool isShowing { get; }` |  |

## Methods

### `Awake()`

```csharp
protected virtual void Awake()
```

### `Hide()`

Hide this view. ShowBehaviour must be set to Manually.

```csharp
public void Hide()
```

### `OnDestroy()`

```csharp
protected virtual void OnDestroy()
```

### `OnDisable()`

```csharp
protected virtual void OnDisable()
```

### `OnEnable()`

```csharp
protected virtual void OnEnable()
```

### `OnHide()`

```csharp
protected virtual void OnHide()
```

### `OnShow()`

```csharp
protected virtual void OnShow()
```

### `Show()`

Show this view. ShowBehaviour must be set to Manually.

```csharp
public void Show()
```

### `Start()`

```csharp
protected virtual void Start()
```

### `Update()`

```csharp
protected virtual void Update()
```
