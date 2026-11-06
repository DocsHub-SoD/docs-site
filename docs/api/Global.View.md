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

## Fields (13)

::: details Click to expand Fields (13)

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

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShowing`** | `public bool isShowing { get; }` |  |

:::

## Methods (10)

::: details `Awake()`

```csharp
protected virtual void Awake()
```

:::

::: details `Hide()`

Hide this view. ShowBehaviour must be set to Manually.

```csharp
public void Hide()
```

:::

::: details `OnDestroy()`

```csharp
protected virtual void OnDestroy()
```

:::

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected virtual void OnEnable()
```

:::

::: details `OnHide()`

```csharp
protected virtual void OnHide()
```

:::

::: details `OnShow()`

```csharp
protected virtual void OnShow()
```

:::

::: details `Show()`

Show this view. ShowBehaviour must be set to Manually.

```csharp
public void Show()
```

:::

::: details `Start()`

```csharp
protected virtual void Start()
```

:::

::: details `Update()`

```csharp
protected virtual void Update()
```

:::
