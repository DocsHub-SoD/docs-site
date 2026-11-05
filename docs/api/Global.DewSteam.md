# Class: DewSteam

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewSteam
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onGameOverlayShownChanged`** | `public static SafeAction&lt;bool&gt; onGameOverlayShownChanged` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAchievementReady`** | `public static bool isAchievementReady { get; }` |  |
| **`isInitialized`** | `public static bool isInitialized { get; }` |  |
| **`steamId`** | `public static CSteamID steamId { get; }` |  |

## Methods

### `GetTicketForWebApi(string)`

```csharp
public static UniTask<SteamTicketForWebApi> GetTicketForWebApi(string pchIdentity = "DewOwnership")
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pchIdentity` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask&lt;T&gt;&lt;SteamTicketForWebApi&gt;`

### `TryStartGamepadInput(string, string, bool, bool, int, Action&lt;string&gt;, Action)`

If Steam gamepad input is not available, this returns false and no callbacks are called.

```csharp
public static bool TryStartGamepadInput(string previousText, string placeholderText, bool isMultiline, bool isPassword, int maxCharacters, Action<string> onConfirm, Action onCancel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `previousText` | `string` |  |
| `placeholderText` | `string` |  |
| `isMultiline` | `bool` |  |
| `isPassword` | `bool` |  |
| `maxCharacters` | `int` |  |
| `onConfirm` | `System.Action&lt;T&gt;&lt;string&gt;` |  |
| `onCancel` | `System.Action` |  |

**Returns:** `bool`

### `UnsubscribeItem()`

```csharp
public static void UnsubscribeItem()
```
