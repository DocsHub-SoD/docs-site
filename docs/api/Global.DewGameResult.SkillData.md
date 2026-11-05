# Struct: DewGameResult.SkillData

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct DewGameResult.SkillData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`capturedTooltipFields`** | `public Dictionary&lt;string, string&gt; capturedTooltipFields` |  |
| **`cooldownTime`** | `public float cooldownTime` |  |
| **`level`** | `public int level` |  |
| **`loc`** | `public HeroSkillLocation loc` |  |
| **`maxCharges`** | `public int maxCharges` |  |
| **`name`** | `public string name` |  |
| **`netId`** | `public uint netId` |  |
| **`type`** | `public SkillType type` |  |

## Methods

### `CaptureTooltipFields(SkillTrigger)`

```csharp
public void CaptureTooltipFields(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [SkillTrigger](/api/Global.SkillTrigger) |  |

### `GetSkillTrigger()`

```csharp
public SkillTrigger GetSkillTrigger()
```

**Returns:** `SkillTrigger`
