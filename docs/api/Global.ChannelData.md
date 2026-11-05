# Class: ChannelData

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class ChannelData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockedActions`** | `[HorizontalGroup("A", 0, 0, 0, 0)]
[HideLabel]
[DisableIf("@duration &lt;= 0f")]
public Channel.BlockedAction blockedActions` |  |
| **`duration`** | `[HorizontalGroup("A", 0, 0, 0, 0)]
[LabelText("Channel Duration")]
public float duration` |  |
| **`selfValidator`** | `[HideLabel]
public AbilitySelfValidator selfValidator` |  |
| **`uncancellableTime`** | `[ShowIf("@duration &gt; 0f && ((byte)(blockedActions & Channel.BlockedAction.Cancelable)) != (byte)0", true)]
public float uncancellableTime` |  |

## Methods

### `Get()`

Create a channel using this data.

```csharp
public Channel Get()
```

**Returns:** `Channel`
