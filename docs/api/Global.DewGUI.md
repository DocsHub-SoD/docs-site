# Class: DewGUI

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewGUI
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fieldBuilders`** | `public static List<(DewGUI.FieldBuilderCondition, DewGUI.FieldBuilder)> fieldBuilders` |  |
| **`SupportedBasicTypes`** | `public static readonly Type[] SupportedBasicTypes` |  |

:::

## Properties (13)

::: details Click to expand Properties (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canvasTransform`** | `public static RectTransform canvasTransform { get; }` |  |
| **`widgetBindItem`** | `public static UI_BindItem widgetBindItem { get; }` |  |
| **`widgetButton`** | `public static Button widgetButton { get; }` |  |
| **`widgetDropdown`** | `public static TMP_Dropdown widgetDropdown { get; }` |  |
| **`widgetInputField`** | `public static TMP_InputField widgetInputField { get; }` |  |
| **`widgetScrollRect`** | `public static ScrollRect widgetScrollRect { get; }` |  |
| **`widgetSlider`** | `public static Slider widgetSlider { get; }` |  |
| **`widgetTextBody`** | `public static TextMeshProUGUI widgetTextBody { get; }` |  |
| **`widgetTextHeader`** | `public static TextMeshProUGUI widgetTextHeader { get; }` |  |
| **`widgetTextLabel`** | `public static TextMeshProUGUI widgetTextLabel { get; }` |  |
| **`widgetToggleButton`** | `public static UI_Toggle widgetToggleButton { get; }` |  |
| **`widgetToggleCheck`** | `public static UI_Toggle widgetToggleCheck { get; }` |  |
| **`widgetWindow`** | `public static UI_Window widgetWindow { get; }` | The window comes with VerticalLayoutGroup and ContentSizeFitter, and is draggable by default. |

:::

## Methods (24)

::: details `ApplyLayoutGroupDefaultSettings(HorizontalLayoutGroup, TextAnchor)`

Helper for creating layout groups with nice default values.

```csharp
public static void ApplyLayoutGroupDefaultSettings(HorizontalLayoutGroup group, TextAnchor alignment = TextAnchor.MiddleLeft)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `group` | `UnityEngine.UI.HorizontalLayoutGroup` |  |
| `alignment` | `UnityEngine.TextAnchor` |  |

:::

::: details `ApplyLayoutGroupDefaultSettings(VerticalLayoutGroup, TextAnchor)`

Helper for creating layout groups with nice default values.

```csharp
public static void ApplyLayoutGroupDefaultSettings(VerticalLayoutGroup group, TextAnchor alignment = TextAnchor.UpperCenter)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `group` | `UnityEngine.UI.VerticalLayoutGroup` |  |
| `alignment` | `UnityEngine.TextAnchor` |  |

:::

::: details `CreateHorizontalFlexibleSpace(Transform)`

```csharp
public static LayoutElement CreateHorizontalFlexibleSpace(Transform parent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |

**Returns:** `UnityEngine.UI.LayoutElement`

:::

::: details `CreateHorizontalLayoutGroup(Transform, TextAnchor)`

Helper for creating layout groups with nice default values.

```csharp
public static HorizontalLayoutGroup CreateHorizontalLayoutGroup(Transform parent, TextAnchor alignment = TextAnchor.MiddleLeft)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |
| `alignment` | `UnityEngine.TextAnchor` |  |

**Returns:** `UnityEngine.UI.HorizontalLayoutGroup`

:::

::: details `CreateVerticalFlexibleSpace(Transform)`

```csharp
public static LayoutElement CreateVerticalFlexibleSpace(Transform parent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |

**Returns:** `UnityEngine.UI.LayoutElement`

:::

::: details `CreateVerticalLayoutGroup(Transform, TextAnchor)`

Helper for creating layout groups with nice default values.

```csharp
public static VerticalLayoutGroup CreateVerticalLayoutGroup(Transform parent, TextAnchor alignment = TextAnchor.UpperCenter)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |
| `alignment` | `UnityEngine.TextAnchor` |  |

**Returns:** `UnityEngine.UI.VerticalLayoutGroup`

:::

::: details `CreateWidgetsForObject(Type, object, Transform, out SafeAction, out SafeAction)`

Creates data-bound widgets for given object type.

```csharp
public static void CreateWidgetsForObject(Type type, object state, Transform parent, out SafeAction onChanged, out SafeAction requestUpdate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `state` | `object` |  |
| `parent` | `UnityEngine.Transform` |  |
| `onChanged` | [`SafeAction`](/api/Global.SafeAction) |  |
| `requestUpdate` | [`SafeAction`](/api/Global.SafeAction) |  |

:::

::: details `GenericInputFieldBuilder&lt;T&gt;(Transform, TryParseFunc&lt;T&gt;, CharacterValidation, out TMP_InputField)`

```csharp
public static FieldBuildResult GenericInputFieldBuilder<T>(Transform parent, DewGUI.TryParseFunc<T> tryParse, TMP_InputField.CharacterValidation validation, out TMP_InputField inputField)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `UnityEngine.Transform` |  |
| `tryParse` | [`DewGUI.TryParseFunc<T>`](/api/Global.DewGUI) |  |
| `validation` | `TMPro.TMP_InputField.TMPro.TMP_InputField.CharacterValidation` |  |
| `inputField` | `TMPro.TMP_InputField` |  |
| `` | `T` |  |

**Returns:** `FieldBuildResult`

:::

::: details `SetExpandHeight(GameObject, bool)`

```csharp
public static GameObject SetExpandHeight(this GameObject c, bool expand)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `expand` | `bool` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetExpandHeight(GameObject, float)`

```csharp
public static GameObject SetExpandHeight(this GameObject c, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `value` | `float` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetExpandHeight&lt;T&gt;(T, bool)`

```csharp
public static T SetExpandHeight<T>(this T c, bool expand) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `expand` | `bool` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetExpandHeight&lt;T&gt;(T, float)`

```csharp
public static T SetExpandHeight<T>(this T c, float value) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `value` | `float` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetExpandWidth(GameObject, bool)`

```csharp
public static GameObject SetExpandWidth(this GameObject c, bool expand)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `expand` | `bool` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetExpandWidth(GameObject, float)`

```csharp
public static GameObject SetExpandWidth(this GameObject c, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `value` | `float` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetExpandWidth&lt;T&gt;(T, bool)`

```csharp
public static T SetExpandWidth<T>(this T c, bool expand) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `expand` | `bool` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetExpandWidth&lt;T&gt;(T, float)`

```csharp
public static T SetExpandWidth<T>(this T c, float value) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `value` | `float` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetHeight(GameObject, float)`

```csharp
public static GameObject SetHeight(this GameObject c, float height)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `height` | `float` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetHeight&lt;T&gt;(T, float)`

```csharp
public static T SetHeight<T>(this T c, float height) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `height` | `float` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetText(GameObject, string)`

```csharp
public static GameObject SetText(this GameObject c, string text)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `text` | `string` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetText&lt;T&gt;(T, string)`

```csharp
public static T SetText<T>(this T c, string text) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `text` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetTextLocalized(GameObject, string)`

```csharp
public static GameObject SetTextLocalized(this GameObject c, string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `key` | `string` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetTextLocalized&lt;T&gt;(T, string)`

```csharp
public static T SetTextLocalized<T>(this T c, string key) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `key` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SetWidth(GameObject, float)`

```csharp
public static GameObject SetWidth(this GameObject c, float width)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `UnityEngine.GameObject` |  |
| `width` | `float` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `SetWidth&lt;T&gt;(T, float)`

```csharp
public static T SetWidth<T>(this T c, float width) where T : Component
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `c` | `T` |  |
| `width` | `float` |  |
| `` | `T` |  |

**Returns:** `T`

:::
