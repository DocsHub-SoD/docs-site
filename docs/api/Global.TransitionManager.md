# Class: TransitionManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [TransitionManager](/api/Global.TransitionManager)

```csharp
public class TransitionManager : ManagerBase<TransitionManager>, ILogicUpdate
```

## Fields (11)

::: details Click to expand Fields (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`busyObject`** | `public GameObject busyObject` |  |
| **`fadeTime`** | `public float fadeTime` |  |
| **`fxTransition`** | `public GameObject fxTransition` |  |
| **`loadingTexts`** | `public TextMeshProUGUI[] loadingTexts` |  |
| **`newTipCooldownTime`** | `public float newTipCooldownTime` |  |
| **`onFadeIn`** | `public Action onFadeIn` |  |
| **`onFadeOut`** | `public Action onFadeOut` |  |
| **`onStateChanged`** | `public SafeAction onStateChanged` |  |
| **`screenFadeCg`** | `public CanvasGroup screenFadeCg` |  |
| **`tipText`** | `public TextMeshProUGUI tipText` |  |
| **`whiteFadeCg`** | `public CanvasGroup whiteFadeCg` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`state`** | `[ShowInInspector] public TransitionManager.StateType state { get; }` |  |

:::

## Methods (11)

::: details `FadeIn()`

```csharp
[Button]
public void FadeIn()
```

:::

::: details `FadeInRoutine()`

```csharp
public IEnumerator FadeInRoutine()
```

**Returns:** `System.Collections.IEnumerator`

:::

::: details `FadeOut()`

```csharp
[Button]
public void FadeOut()
```

:::

::: details `FadeOut(bool)`

```csharp
public void FadeOut(bool showTips)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `showTips` | `bool` |  |

:::

::: details `FadeOutRoutine(bool)`

```csharp
public IEnumerator FadeOutRoutine(bool showTips)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `showTips` | `bool` |  |

**Returns:** `System.Collections.IEnumerator`

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `LoadScene(string, bool)`

```csharp
public void LoadScene(string sceneName, bool dontFadeIn = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sceneName` | `string` |  |
| `dontFadeIn` | `bool` |  |

:::

::: details `PlayGame(DewNetworkStartSettings)`

```csharp
public void PlayGame(DewNetworkStartSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`DewNetworkStartSettings`](/api/Global.DewNetworkStartSettings) |  |

:::

::: details `SetBusy(bool)`

```csharp
public void SetBusy(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `UpdateLoadingStatus(LoadingStatus)`

```csharp
public void UpdateLoadingStatus(LoadingStatus status)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `status` | <a href="/enums#loadingstatus" class="enum-link" data-tooltip="Empty=0 · WaitingForService=1 · CheckingLobbyStatus=2 · CleaningUpPreviousLobby=3 · LeavingPreviousLobby=4 (+11 more)">LoadingStatus</a> |  |

:::

::: details `UpdateLoadingStatus(string)`

```csharp
public void UpdateLoadingStatus(string rawText)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rawText` | `string` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (27)

*Classes and systems that invoke, reference, or depend on `TransitionManager`:*

`Ai_Curse_AnchorOfMind_Anchor` · [CameraManager](/api/Global.CameraManager) · [CollectablesManager](/api/Global.CollectablesManager) · `DewConsoleCommands` · [DewMod](/api/Global.DewMod) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewSteam](/api/Global.DewSteam) · `DynamicResolution` · `EOSManager` · [EntityControl](/api/Global.EntityControl) · [GameManager](/api/Global.GameManager) · [GlobalUIManager](/api/Global.GlobalUIManager) · [LobbyServiceSteam](/api/Global.LobbyServiceSteam) · [LootManager](/api/Global.LootManager) · `RoomMod_StardustEverywhere` · [RoomMonsters](/api/Global.RoomMonsters) · `Se_Curse_AnchorOfMind` · `Se_D_PrismaticEyes` · `Se_D_TheKillingFlow` · `Se_Gem_E_Insensitivity_BombSpawner` · `Se_UsingShortcut` · `St_D_ScarOfTheWind` · `St_L_SmallMoltenCore` · `St_Q_MoonlightPact` · [TitleManager](/api/Global.TitleManager) · [UI_GamepadTextInput](/api/Global.UI_GamepadTextInput) · `UI_Title_ProfileSelection_ListWindow`

### Dependencies (7)

*Types and components that `TransitionManager` references or depends upon:*

[DewEffect](/api/Global.DewEffect) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkStartSettings](/api/Global.DewNetworkStartSettings) · [DewPlayer](/api/Global.DewPlayer) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [SafeAction](/api/Global.SafeAction)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#loadingstatus" class="enum-link" data-tooltip="Empty=0 · WaitingForService=1 · CheckingLobbyStatus=2 · CleaningUpPreviousLobby=3 · LeavingPreviousLobby=4 (+11 more)">LoadingStatus</a>

:::
