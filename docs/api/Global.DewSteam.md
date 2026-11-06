# Class: DewSteam

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewSteam
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onGameOverlayShownChanged`** | `public static SafeAction<bool> onGameOverlayShownChanged` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isAchievementReady`** | `public static bool isAchievementReady { get; }` |  |
| **`isInitialized`** | `public static bool isInitialized { get; }` |  |
| **`steamId`** | `public static CSteamID steamId { get; }` |  |

:::

## Methods (3)

::: details `GetTicketForWebApi(string)`

```csharp
public static UniTask<SteamTicketForWebApi> GetTicketForWebApi(string pchIdentity = "DewOwnership")
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pchIdentity` | `string` |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask<T><SteamTicketForWebApi>`

:::

::: details `TryStartGamepadInput(string, string, bool, bool, int, Action&lt;string&gt;, Action)`

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
| `onConfirm` | `System.Action<T><string>` |  |
| `onCancel` | `System.Action` |  |

**Returns:** `bool`

:::

::: details `UnsubscribeItem()`

```csharp
public static void UnsubscribeItem()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (17)

*Classes and systems that invoke, reference, or depend on `DewSteam`:*

[AchievementManager](/api/Global.AchievementManager) · `DecryptedItemData` · [DewAchievementItem](/api/Global.DewAchievementItem) · [DewMod](/api/Global.DewMod) · [DewNetworkAuthenticator](/api/Global.DewNetworkAuthenticator) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewSave](/api/Global.DewSave) · `LobbyServiceEOS` · `SteamCallbackRunner` · `SteamTicketForWebApi` · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_Lobby_InviteButtonController` · `UI_Title_CoopButtonManager` · `UI_Title_SplashView_SplashItem_GRAC` · `UI_Title_SplashView_SplashItem_Gift`

### Dependencies (6)

*Types and components that `DewSteam` references or depends upon:*

[DewBuildProfile](/api/Global.DewBuildProfile) · `JoinArrayExtensions` · [ManagerBase`1](/api/Global.ManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [TransitionManager](/api/Global.TransitionManager)

:::
