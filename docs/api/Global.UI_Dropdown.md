# Class: UI_Dropdown

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_Dropdown : MonoBehaviour
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onValueChanged`** | `public SafeAction<object> onValueChanged` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`index`** | `public int index { get; set; }` |  |
| **`value`** | `public object value { get; set; }` |  |

:::

## Methods (3)

::: details `AddOption(string, object)`

```csharp
public void AddOption(string text, object val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` |  |
| `val` | `object` |  |

:::

::: details `ClearOptions()`

```csharp
public void ClearOptions()
```

:::

::: details `SetValueWithoutNotify(object)`

```csharp
public void SetValueWithoutNotify(object val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | `object` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `UI_Dropdown`:*

`UI_Lobby_AllowMidJoins` · `UI_Title_CreateLobbyView`

### Dependencies (2)

*Types and components that `UI_Dropdown` references or depends upon:*

`ArrayGetOrDefaultExtensions` · [SafeAction`1](/api/Global.SafeAction`1)

:::
