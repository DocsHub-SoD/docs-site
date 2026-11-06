# Class: GlobalUIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [GlobalUIManager](/api/Global.GlobalUIManager)

```csharp
public class GlobalUIManager : ManagerBase<GlobalUIManager>, ILogicUpdate
```

## Fields (26)

::: details Click to expand Fields (26)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentMenuView`** | `[NonSerialized] public IMenuView currentMenuView` |  |
| **`devFloatingTextParent`** | `public RectTransform devFloatingTextParent` |  |
| **`devFloatingTextPrefab`** | `public TextMeshProUGUI devFloatingTextPrefab` |  |
| **`focusDisplayAnimationTarget`** | `public Transform focusDisplayAnimationTarget` |  |
| **`focusDisplayBoxObject`** | `public GameObject focusDisplayBoxObject` |  |
| **`focusDisplayCircleObject`** | `public GameObject focusDisplayCircleObject` |  |
| **`focusDisplayObject`** | `public GameObject focusDisplayObject` |  |
| **`focusDisplayTransform`** | `public RectTransform focusDisplayTransform` |  |
| **`fontBody`** | `public TMP_FontAsset fontBody` |  |
| **`fontHeading`** | `public TMP_FontAsset fontHeading` |  |
| **`fontHeadingBold`** | `public TMP_FontAsset fontHeadingBold` |  |
| **`fontHeadingLight`** | `public TMP_FontAsset fontHeadingLight` |  |
| **`fxHighlightHide`** | `public GameObject fxHighlightHide` |  |
| **`fxHighlightShow`** | `public GameObject fxHighlightShow` |  |
| **`fxTick`** | `public GameObject fxTick` |  |
| **`isBackDisabled`** | `[NonSerialized] public bool isBackDisabled` |  |
| **`onFocusedChanged`** | `public Action<IGamepadFocusable, IGamepadFocusable> onFocusedChanged` |  |
| **`tooltipBoxCanvasGroup`** | `public CanvasGroup tooltipBoxCanvasGroup` |  |
| **`tooltipBoxTransform`** | `public RectTransform tooltipBoxTransform` |  |
| **`tutHighlightBackdropBottom`** | `public RectTransform tutHighlightBackdropBottom` |  |
| **`tutHighlightBackdropLeft`** | `public RectTransform tutHighlightBackdropLeft` |  |
| **`tutHighlightBackdropRight`** | `public RectTransform tutHighlightBackdropRight` |  |
| **`tutHighlightBackdropTop`** | `public RectTransform tutHighlightBackdropTop` |  |
| **`tutHighlightBox`** | `public RectTransform tutHighlightBox` |  |
| **`tutHighlightObject`** | `public GameObject tutHighlightObject` |  |
| **`tutHighlightText`** | `public TextMeshProUGUI tutHighlightText` |  |

:::

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`focused`** | `public IGamepadFocusable focused { get; }` |  |
| **`isTooltipShown`** | `public bool isTooltipShown { get; }` |  |
| **`isTutorialHighlighting`** | `public bool isTutorialHighlighting { get; }` |  |
| **`lastFocusChangeUnscaledTime`** | `public float lastFocusChangeUnscaledTime { get; }` |  |
| **`tooltipScreenSpaceRect`** | `public Rect tooltipScreenSpaceRect { get; }` |  |

:::

## Methods (26)

::: details `AddBackHandler(MonoBehaviour, int, Func&lt;bool&gt;)`

Add handler for back buttons.Handler must return boolean value as indication of whether the back button event is consumed or not.Callback with highest priority will fire first when back button is pressed.If priority is the same, last added item will be fired first.If owner is destroyed, back handler will automatically be unregistered.

```csharp
public BackHandler AddBackHandler(MonoBehaviour owner, int priority, Func<bool> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `owner` | `UnityEngine.MonoBehaviour` |  |
| `priority` | `int` |  |
| `callback` | `System.Func<TResult><bool>` |  |

**Returns:** `BackHandler`

:::

::: details `AddGamepadFocusable(IGamepadFocusable)`

```csharp
public void AddGamepadFocusable(IGamepadFocusable focusable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `focusable` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

:::

::: details `ClickHighlightForTutorial()`

```csharp
public void ClickHighlightForTutorial()
```

:::

::: details `EnforceFontFallbackOrder()`

```csharp
public void EnforceFontFallbackOrder()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetFocusedComponent&lt;T&gt;()`

```csharp
public T GetFocusedComponent<T>() where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetIntersectingRects(List&lt;Rect&gt;, Vector2, Vector2, float, float)`

```csharp
public static List<GlobalUIManager.RectResult> GetIntersectingRects(List<Rect> rects, Vector2 origin, Vector2 direction, float angle, float radius)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rects` | `System.Collections.Generic.List<T><UnityEngine.Rect>` |  |
| `origin` | `UnityEngine.Vector2` |  |
| `direction` | `UnityEngine.Vector2` |  |
| `angle` | `float` |  |
| `radius` | `float` |  |

**Returns:** `System.Collections.Generic.List<T><GlobalUIManager.RectResult>`

:::

::: details `GoBack()`

Handle go back event with registered handlers.

```csharp
public void GoBack()
```

:::

::: details `HighlightForTutorial(TutorialHighlightSettings)`

```csharp
public IEnumerator HighlightForTutorial(TutorialHighlightSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | `TutorialHighlightSettings` |  |

**Returns:** `System.Collections.IEnumerator`

:::

::: details `IsUIElementClickable(RectTransform)`

This checks for occlusions.

```csharp
public bool IsUIElementClickable(RectTransform rectTransform)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rectTransform` | `UnityEngine.RectTransform` |  |

**Returns:** `bool`

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

::: details `MoveFocus(Vector3, float, float, float, Func&lt;IGamepadFocusable, bool&gt;, Func&lt;IGamepadFocusable, float&gt;)`

```csharp
public bool MoveFocus(Vector3 direction, float angleLimit, float normalizedPerpendicularDistLimit, float normalizedDistLimit, Func<IGamepadFocusable, bool> condition = null, Func<IGamepadFocusable, float> customScoreFunc = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector3` |  |
| `angleLimit` | `float` |  |
| `normalizedPerpendicularDistLimit` | `float` |  |
| `normalizedDistLimit` | `float` |  |
| `condition` | [`System.Func<T, TResult><IGamepadFocusable,bool>`](/api/Global.IGamepadFocusable) |  |
| `customScoreFunc` | [`System.Func<T, TResult><IGamepadFocusable,float>`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `MoveFocus(Vector3, Vector2, Vector2, Vector2, Func&lt;IGamepadFocusable, bool&gt;, Func&lt;IGamepadFocusable, float&gt;)`

```csharp
public bool MoveFocus(Vector3 direction, Vector2 angleLimit, Vector2 normalizedPerpendicularDistLimit, Vector2 normalizedDistLimit, Func<IGamepadFocusable, bool> condition = null, Func<IGamepadFocusable, float> customScoreFunc = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector3` |  |
| `angleLimit` | `UnityEngine.Vector2` |  |
| `normalizedPerpendicularDistLimit` | `UnityEngine.Vector2` |  |
| `normalizedDistLimit` | `UnityEngine.Vector2` |  |
| `condition` | [`System.Func<T, TResult><IGamepadFocusable,bool>`](/api/Global.IGamepadFocusable) |  |
| `customScoreFunc` | [`System.Func<T, TResult><IGamepadFocusable,float>`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `MoveFocus(Vector3)`

```csharp
public bool MoveFocus(Vector3 direction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector3` |  |

**Returns:** `bool`

:::

::: details `PopulateCacheData(ref GetFocusTargetSettings, out Action)`

Populate cache data for the given settings to make consecutive GetTarget calls faster.

```csharp
public void PopulateCacheData(ref GetFocusTargetSettings settings, out Action handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`GetFocusTargetSettings`](/api/Global.GetFocusTargetSettings) |  |
| `handle` | `System.Action` |  |

:::

::: details `RemoveBackHandler(BackHandler)`

Remove the provided back handler if it exists in current handler list.If owner is destroyed, back handler will automatically be unregistered.

```csharp
public void RemoveBackHandler(BackHandler handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [`BackHandler`](/api/Global.BackHandler) |  |

:::

::: details `RemoveGamepadFocusable(IGamepadFocusable)`

```csharp
public void RemoveGamepadFocusable(IGamepadFocusable focusable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `focusable` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

:::

::: details `SetFocus(IGamepadFocusable)`

```csharp
public void SetFocus(IGamepadFocusable focusable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `focusable` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

:::

::: details `SetFocusOnComponent(Component)`

```csharp
public void SetFocusOnComponent(Component focusable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `focusable` | `UnityEngine.Component` |  |

:::

::: details `SetFocusOnFirstFocusable(GameObject)`

```csharp
public void SetFocusOnFirstFocusable(GameObject parent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.GameObject` |  |

:::

::: details `ShowDevText(string, bool)`

Show developer-only floating text in top-left corner of the screen for some time.This is not shown to non-developers.

```csharp
public void ShowDevText(string rawText, bool log = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rawText` | `string` |  |
| `log` | `bool` |  |

:::

::: details `SimulateClickOnUIElement(Component)`

```csharp
public void SimulateClickOnUIElement(Component comp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `comp` | `UnityEngine.Component` |  |

:::

::: details `TryGetFocusTarget(GetFocusTargetSettings, out IGamepadFocusable)`

```csharp
public bool TryGetFocusTarget(GetFocusTargetSettings s, out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`GetFocusTargetSettings`](/api/Global.GetFocusTargetSettings) |  |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryGetFocusTargetGeneric(Vector3, Func&lt;IGamepadFocusable, bool&gt;, out IGamepadFocusable)`

```csharp
public bool TryGetFocusTargetGeneric(Vector3 direction, Func<IGamepadFocusable, bool> condition, out IGamepadFocusable next)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `direction` | `UnityEngine.Vector3` |  |
| `condition` | [`System.Func<T, TResult><IGamepadFocusable,bool>`](/api/Global.IGamepadFocusable) |  |
| `next` | [`IGamepadFocusable`](/api/Global.IGamepadFocusable) |  |

**Returns:** `bool`

:::

::: details `TryMoveFocusBack()`

```csharp
public bool TryMoveFocusBack()
```

**Returns:** `bool`

:::

::: details `UnhighlightForTutorial()`

```csharp
public void UnhighlightForTutorial()
```

:::
