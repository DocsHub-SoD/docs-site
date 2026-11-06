# Class: ChannelData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class ChannelData
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockedActions`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [HideLabel] [DisableIf("@duration <= 0f")] public Channel.BlockedAction blockedActions` |  |
| **`duration`** | `[HorizontalGroup("A", 0, 0, 0, 0)] [LabelText("Channel Duration")] public float duration` |  |
| **`selfValidator`** | `[HideLabel] public AbilitySelfValidator selfValidator` |  |
| **`uncancellableTime`** | `[ShowIf("@duration > 0f && ((byte)(blockedActions & Channel.BlockedAction.Cancelable)) != (byte)0", true)] public float uncancellableTime` |  |

:::

## Methods (1)

::: details `Get()`

Create a channel using this data.

```csharp
public Channel Get()
```

**Returns:** `Channel`

:::
