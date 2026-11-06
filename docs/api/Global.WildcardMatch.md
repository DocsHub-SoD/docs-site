# Class: WildcardMatch

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class WildcardMatch
```

## Methods

### `EqualsWildcard(string, string, bool)`

```csharp
public static bool EqualsWildcard(this string text, string wildcardString, bool ignoreCase)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` |  |
| `wildcardString` | `string` |  |
| `ignoreCase` | `bool` |  |

**Returns:** `bool`

### `EqualsWildcard(string, string)`

Compares a string to a wildcard pattern.
'?' matches any single character.
'*' matches any sequence of zero or more characters.
This implementation is case-sensitive.

```csharp
public static bool EqualsWildcard(this string text, string wildcardString)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` | The string to test. |
| `wildcardString` | `string` | The wildcard pattern to match against. |

**Returns:** `bool: True if the string matches the pattern, otherwise false.`
