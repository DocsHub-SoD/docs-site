# Struct: AnalyticsEquipmentData

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct AnalyticsEquipmentData
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`gems`** | `public List<(GemLocation, string, int)> gems` |  |
| **`skills`** | `public List<(HeroSkillLocation, string, int)> skills` |  |

:::

## Methods (1)

::: details `ToBase64()`

```csharp
public string ToBase64()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `AnalyticsEquipmentData`:*

`InGameAnalyticsManager` · [InGameCrashReportManager](/api/Global.InGameCrashReportManager)

### Dependencies (5)

*Types and components that `AnalyticsEquipmentData` references or depends upon:*

[Gem](/api/Global.Gem) · [GemLocation](/api/Global.GemLocation) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · `ItemNumericIdDatabase`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`HeroSkillLocation`](/enums#heroskilllocation)

:::
