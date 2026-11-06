# Class: SafeAction

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |

:::

## Methods (4)

::: details `Add(Action)`

```csharp
public SafeAction Add(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `SafeAction`

:::

::: details `Contains(Action)`

```csharp
public bool Contains(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `bool`

:::

::: details `Invoke()`

```csharp
public void Invoke()
```

:::

::: details `Remove(Action)`

```csharp
public SafeAction Remove(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `SafeAction`

:::
