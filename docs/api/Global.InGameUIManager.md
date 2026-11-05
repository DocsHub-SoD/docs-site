# Class: InGameUIManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [UIManager](/api/Global.UIManager) → [UIManager](/api/Global.UIManager)

```csharp
public class InGameUIManager : UIManager, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cmsgContainer`** | `public Transform cmsgContainer` |  |
| **`cmsgErrorPrefab`** | `public GameObject cmsgErrorPrefab` |  |
| **`cmsgGeneralPrefab`** | `public GameObject cmsgGeneralPrefab` |  |
| **`cmsgStartPivot`** | `public Transform cmsgStartPivot` |  |
| **`currentMockExit`** | `public Rift_MockExit currentMockExit` |  |
| **`disableOnEndingObjects`** | `public GameObject[] disableOnEndingObjects` |  |
| **`fullWorldMapNodeItems`** | `[NonSerialized]
public List&lt;RectTransform&gt; fullWorldMapNodeItems` |  |
| **`miniWorldMapNodeItems`** | `[NonSerialized]
public List&lt;RectTransform&gt; miniWorldMapNodeItems` |  |
| **`onHasWorldNodePingChanged`** | `public Action&lt;bool&gt; onHasWorldNodePingChanged` |  |
| **`onScoreboardDisplayedChanged`** | `public Action&lt;bool&gt; onScoreboardDisplayedChanged` |  |
| **`onShowWorldMessage`** | `public Action&lt;WorldMessageSetting&gt; onShowWorldMessage` |  |
| **`onWorldDisplayedChanged`** | `public Action&lt;WorldDisplayStatus&gt; onWorldDisplayedChanged` |  |
| **`whiteFadeCg`** | `public CanvasGroup whiteFadeCg` |  |

## Properties

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

## Methods

### `DecrementWorldNodePingCounter()`

This decrements internal counter. You must pair this with equivalent number EnableMiniWorldMap calls.

```csharp
public void DecrementWorldNodePingCounter()
```

### `DisablePlayingInput()`

```csharp
public void DisablePlayingInput()
```

### `EnablePlayingInput()`

```csharp
public void EnablePlayingInput()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetContinueRelatedDescription()`

```csharp
public string GetContinueRelatedDescription()
```

**Returns:** `string`

### `GetWorldNodeUIPos(int)`

```csharp
public Vector2 GetWorldNodeUIPos(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `UnityEngine.Vector2`

### `IncrementWorldNodePingCounter()`

```csharp
public void IncrementWorldNodePingCounter()
```

### `OnStateChanged(string, string)`

```csharp
protected override void OnStateChanged(string oldState, string newState)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldState` | `string` |  |
| `newState` | `string` |  |

### `SetIsDoingEnding(bool)`

```csharp
public void SetIsDoingEnding(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

### `SetWhiteFade(bool)`

```csharp
public void SetWhiteFade(bool value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `bool` |  |

### `ShouldDoAutoFocus()`

```csharp
public override bool ShouldDoAutoFocus()
```

**Returns:** `bool`

### `ShowCenterMessage(CenterMessageType, string, object[])`

```csharp
public void ShowCenterMessage(CenterMessageType type, string key, object[] formatArgs = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [CenterMessageType](/api/Global.CenterMessageType) |  |
| `key` | `string` |  |
| `formatArgs` | `object[]` |  |

### `ShowCenterMessageRaw(CenterMessageType, string)`

```csharp
public void ShowCenterMessageRaw(CenterMessageType type, string raw)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [CenterMessageType](/api/Global.CenterMessageType) |  |
| `raw` | `string` |  |

### `ShowWorldPopMessage(WorldMessageSetting)`

```csharp
public void ShowWorldPopMessage(WorldMessageSetting message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [WorldMessageSetting](/api/Global.WorldMessageSetting) |  |

### `ValidateInGameActionMessage(bool)`

```csharp
public static bool ValidateInGameActionMessage(bool requireAliveHero = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `requireAliveHero` | `bool` |  |

**Returns:** `bool`
