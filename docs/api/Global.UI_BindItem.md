# Class: UI_BindItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
public class UI_BindItem : LogicBehaviour, ILogicUpdate, ILangaugeChangedCallback
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowedTypes`** | `public BindingType allowedTypes` |  |
| **`allowModifiers`** | `public bool allowModifiers` |  |
| **`hoverObject`** | `public GameObject hoverObject` |  |
| **`keyDisplayText`** | `public TextMeshProUGUI keyDisplayText` |  |
| **`notHoverObject`** | `public GameObject notHoverObject` |  |
| **`onValueChanged`** | `public Action<DewBinding> onValueChanged` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`value`** | `public DewBinding value { get; set; }` |  |

:::

## Methods (5)

::: details `OnLanguageChanged()`

```csharp
public void OnLanguageChanged()
```

:::

::: details `OnPointerEnter(PointerEventData)`

```csharp
public void OnPointerEnter(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

:::

::: details `OnPointerExit(PointerEventData)`

```csharp
public void OnPointerExit(PointerEventData eventData)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventData` | `UnityEngine.EventSystems.PointerEventData` |  |

:::

::: details `StartListening()`

```csharp
public void StartListening()
```

:::

::: details `UpdateValueDontNotify(DewBinding)`

```csharp
public void UpdateValueDontNotify(DewBinding newReference)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newReference` | [`DewBinding`](/api/Global.DewBinding) |  |

:::
