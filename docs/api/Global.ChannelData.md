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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (9)

*Classes and systems that invoke, reference, or depend on `ChannelData`:*

`Ai_E_SliceThroat` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Primus_BossPrimusAeron_Rage_Atk` · `Ai_Mon_Sky_Baam_TeleportSequence` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Special_BossMaw_Atk` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_R_BladeFan` · [DamageInstance](/api/Global.DamageInstance)

### Dependencies (2)

*Types and components that `ChannelData` references or depends upon:*

[AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [Channel](/api/Global.Channel)

:::
