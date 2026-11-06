# Class: DewInGameTutorialItem

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewInGameTutorialItem
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`mgr`** | `public InGameTutorialManager mgr { get; set; }` |  |

:::

## Methods (9)

::: details `OnStart()`

```csharp
public virtual void OnStart()
```

:::

::: details `OnStop()`

```csharp
public virtual void OnStop()
```

:::

::: details `TutComplete()`

```csharp
protected void TutComplete()
```

:::

::: details `TutCreateArrow()`

```csharp
protected TutorialArrow TutCreateArrow()
```

**Returns:** `TutorialArrow`

:::

::: details `TutDelayedExecution(Action, float)`

```csharp
protected void TutDelayedExecution(Action func, float seconds)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |
| `seconds` | `float` |  |

:::

::: details `TutGetCoroutiner()`

```csharp
protected Coroutiner TutGetCoroutiner()
```

**Returns:** `Coroutiner`

:::

::: details `TutOnFrameUpdate(Action)`

```csharp
protected void TutOnFrameUpdate(Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |

:::

::: details `TutOnLogicUpdate(Action)`

```csharp
protected void TutOnLogicUpdate(Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |

:::

::: details `TutOnOutOfCombat(Action)`

```csharp
protected void TutOnOutOfCombat(Action func)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `func` | `System.Action` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `DewInGameTutorialItem`:*

[InGameTutorialManager](/api/Global.InGameTutorialManager) · `Tut_Cleanse` · `Tut_ShopSell` · `Tut_World` · `Tut_WorldHunt`

### Dependencies (3)

*Types and components that `DewInGameTutorialItem` references or depends upon:*

[Coroutiner](/api/Global.Coroutiner) · [InGameTutorialManager](/api/Global.InGameTutorialManager) · `TutorialArrow`

:::
