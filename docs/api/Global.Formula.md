# Struct: Formula

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public struct Formula
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`formula`** | `[FormerlySerializedAs] [HideLabel] [SuffixLabel("f(x)", true)] [ValidateInput("IsValid", "Expression Error", InfoMessageType.Error)] [FormerlySerializedAs("forumla")] public string formula` |  |

:::

## Methods (2)

::: details `Bake()`

```csharp
public void Bake()
```

:::

::: details `Evaluate(float)`

```csharp
public float Evaluate(float x)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `x` | `float` |  |

**Returns:** `float`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (14)

*Classes and systems that invoke, reference, or depend on `Formula`:*

[DewGameplayExperienceSettings](/api/Global.DewGameplayExperienceSettings) · [GameManager](/api/Global.GameManager) · [Gem](/api/Global.Gem) · [LootManager](/api/Global.LootManager) · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) · `RoomMod_Hunted` · [RoomRewards](/api/Global.RoomRewards) · `Se_MirageSkin_Delusion_Delusional` · [Section_Monsters](/api/Global.Section_Monsters) · `Shrine_Destiny` · `Shrine_MawOfDoom` · `Shrine_MirrorOfRemorse` · [SkillTrigger](/api/Global.SkillTrigger)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
