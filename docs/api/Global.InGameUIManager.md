# Class: InGameUIManager

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [UIManager](/api/Global.UIManager)

```csharp
public class InGameUIManager : UIManager, ILogicUpdate
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cmsgContainer`** | `public Transform cmsgContainer` |  |
| **`cmsgErrorPrefab`** | `public GameObject cmsgErrorPrefab` |  |
| **`cmsgGeneralPrefab`** | `public GameObject cmsgGeneralPrefab` |  |
| **`cmsgStartPivot`** | `public Transform cmsgStartPivot` |  |
| **`currentMockExit`** | `public Rift_MockExit currentMockExit` |  |
| **`disableOnEndingObjects`** | `public GameObject[] disableOnEndingObjects` |  |
| **`fullWorldMapNodeItems`** | `[NonSerialized] public List<RectTransform> fullWorldMapNodeItems` |  |
| **`miniWorldMapNodeItems`** | `[NonSerialized] public List<RectTransform> miniWorldMapNodeItems` |  |
| **`onHasWorldNodePingChanged`** | `public Action<bool> onHasWorldNodePingChanged` |  |
| **`onScoreboardDisplayedChanged`** | `public Action<bool> onScoreboardDisplayedChanged` |  |
| **`onShowWorldMessage`** | `public Action<WorldMessageSetting> onShowWorldMessage` |  |
| **`onWorldDisplayedChanged`** | `public Action<WorldDisplayStatus> onWorldDisplayedChanged` |  |
| **`whiteFadeCg`** | `public CanvasGroup whiteFadeCg` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disablePlayingInput`** | `public bool disablePlayingInput { get; }` |  |
| **`hasWorldNodePing`** | `public bool hasWorldNodePing { get; }` | Do we need mini world map instead of party display right now? |
| **`instance`** | `public static InGameUIManager instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`isDoingEnding`** | `public bool isDoingEnding { get; }` |  |
| **`isScoreboardDisplayed`** | `public bool isScoreboardDisplayed { get; set; }` |  |
| **`isWorldDisplayed`** | `public WorldDisplayStatus isWorldDisplayed { get; set; }` |  |
| **`lastWorldDisplayUnscaledTime`** | `public float lastWorldDisplayUnscaledTime { get; }` |  |
| **`softInstance`** | `public static InGameUIManager softInstance { get; }` |  |

:::

## Methods (15)

::: details `DecrementWorldNodePingCounter()`

This decrements internal counter. You must pair this with equivalent number EnableMiniWorldMap calls.

```csharp
public void DecrementWorldNodePingCounter()
```

:::

::: details `DisablePlayingInput()`

```csharp
public void DisablePlayingInput()
```

:::

::: details `EnablePlayingInput()`

```csharp
public void EnablePlayingInput()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetContinueRelatedDescription()`

```csharp
public string GetContinueRelatedDescription()
```

**Returns:** `string`

:::

::: details `GetWorldNodeUIPos(int)`

```csharp
public Vector2 GetWorldNodeUIPos(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `UnityEngine.Vector2`

:::

::: details `IncrementWorldNodePingCounter()`

```csharp
public void IncrementWorldNodePingCounter()
```

:::

::: details `OnStateChanged(string, string)`

```csharp
protected override void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

:::

::: details `SetIsDoingEnding(bool)`

```csharp
public void SetIsDoingEnding(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `SetWhiteFade(bool)`

```csharp
public void SetWhiteFade(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

:::

::: details `ShouldDoAutoFocus()`

```csharp
public override bool ShouldDoAutoFocus()
```

**Returns:** `bool`

:::

::: details `ShowCenterMessage(CenterMessageType, string, object[])`

```csharp
public void ShowCenterMessage(CenterMessageType type, string key, object[] formatArgs = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`CenterMessageType`](/api/Global.CenterMessageType) |  |
| `key` | `string` |  |
| `formatArgs` | `object[]` |  |

:::

::: details `ShowCenterMessageRaw(CenterMessageType, string)`

```csharp
public void ShowCenterMessageRaw(CenterMessageType type, string raw)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`CenterMessageType`](/api/Global.CenterMessageType) |  |
| `raw` | `string` |  |

:::

::: details `ShowWorldPopMessage(WorldMessageSetting)`

```csharp
public void ShowWorldPopMessage(WorldMessageSetting message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [`WorldMessageSetting`](/api/Global.WorldMessageSetting) |  |

:::

::: details `ValidateInGameActionMessage(bool)`

```csharp
public static bool ValidateInGameActionMessage(bool requireAliveHero = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `requireAliveHero` | `bool` |  |

**Returns:** `bool`

:::
