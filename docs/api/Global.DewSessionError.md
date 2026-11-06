# Class: DewSessionError

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewSessionError
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`args`** | `public object[] args` |  |

:::

## Methods (5)

::: details `Error()`

```csharp
public static DewSessionError Error()
```

**Returns:** `DewSessionError`

:::

::: details `Error(Exception)`

```csharp
public static DewSessionError Error(Exception e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | `System.Exception` |  |

**Returns:** `DewSessionError`

:::

::: details `Show(bool, bool)`

Output this error message on screen.

```csharp
public void Show(bool isFatal, bool isGame)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isFatal` | `bool` |  |
| `isGame` | `bool` |  |

:::

::: details `ShowError(bool, bool)`

Show a generic, unknown error

```csharp
public static void ShowError(bool isFatal = false, bool isGame = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isFatal` | `bool` |  |
| `isGame` | `bool` |  |

:::

::: details `ShowError(Exception, bool, bool)`

Fatal error will close the application after it's closed.

```csharp
public static void ShowError(Exception e, bool isFatal = false, bool isGame = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | `System.Exception` |  |
| `isFatal` | `bool` |  |
| `isGame` | `bool` |  |

:::
