# Class: SafeAction

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Count`** | `public int Count { get; }` |  |

## Methods

### `Add(Action)`

```csharp
public SafeAction Add(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `SafeAction`

### `Contains(Action)`

```csharp
public bool Contains(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `bool`

### `Invoke()`

```csharp
public void Invoke()
```

### `Remove(Action)`

```csharp
public SafeAction Remove(Action handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action` |  |

**Returns:** `SafeAction`
