# Struct: DewGameResult.SkillData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct DewGameResult.SkillData
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`capturedTooltipFields`** | `public Dictionary<string, string> capturedTooltipFields` |  |
| **`cooldownTime`** | `public float cooldownTime` |  |
| **`level`** | `public int level` |  |
| **`loc`** | `public HeroSkillLocation loc` |  |
| **`maxCharges`** | `public int maxCharges` |  |
| **`name`** | `public string name` |  |
| **`netId`** | `public uint netId` |  |
| **`type`** | `public SkillType type` |  |

:::

## Methods (2)

::: details `CaptureTooltipFields(SkillTrigger)`

```csharp
public void CaptureTooltipFields(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

:::

::: details `GetSkillTrigger()`

```csharp
public SkillTrigger GetSkillTrigger()
```

**Returns:** `SkillTrigger`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`HeroSkillLocation`](/enums#heroskilllocation) · [`SkillType`](/enums#skilltype)

:::
