# Class: UI_Dropdown

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class UI_Dropdown : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onValueChanged`** | `public SafeAction&lt;object&gt; onValueChanged` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`index`** | `public int index { get; set; }` |  |
| **`value`** | `public object value { get; set; }` |  |

## Methods

### `AddOption(string, object)`

```csharp
public void AddOption(string text, object val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` |  |
| `val` | `object` |  |

### `ClearOptions()`

```csharp
public void ClearOptions()
```

### `SetValueWithoutNotify(object)`

```csharp
public void SetValueWithoutNotify(object val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | `object` |  |
