# Class: DewLocalization

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewLocalization
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buildData`** | `public static DewLocalizationBuildData buildData { get; }` |  |
| **`data`** | `public static PerLanguageLocalizationData data { get; }` |  |

:::

## Methods (55)

::: details `CaptureDescriptionExpressions(IReadOnlyList&lt;LocaleNode&gt;, Dictionary&lt;string, string&gt;, DescriptionSettings)`

```csharp
public static void CaptureDescriptionExpressions(IReadOnlyList<LocaleNode> nodes, Dictionary<string, string> data, DewLocalization.DescriptionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodes` | `System.Collections.Generic.IReadOnlyList<T><LocaleNode>` |  |
| `data` | `System.Collections.Generic.Dictionary<TKey, TValue><string,string>` |  |
| `settings` | [`DewLocalization.DescriptionSettings`](/api/Global.DewLocalization) |  |

:::

::: details `ConvertDescriptionNodesToText(IReadOnlyList&lt;LocaleNode&gt;, DescriptionSettings)`

```csharp
public static string ConvertDescriptionNodesToText(IReadOnlyList<LocaleNode> nodes, DewLocalization.DescriptionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodes` | `System.Collections.Generic.IReadOnlyList<T><LocaleNode>` |  |
| `settings` | [`DewLocalization.DescriptionSettings`](/api/Global.DewLocalization) |  |

**Returns:** `string`

:::

::: details `EvaluateAndRenderExpression(ExpressionData, DescriptionSettings, bool)`

```csharp
public static string EvaluateAndRenderExpression(ExpressionData exp, DewLocalization.DescriptionSettings settings, bool shouldShowDetail)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `exp` | `DewInternal.ExpressionData` |  |
| `settings` | [`DewLocalization.DescriptionSettings`](/api/Global.DewLocalization) |  |
| `shouldShowDetail` | `bool` |  |

**Returns:** `string`

:::

::: details `GetAchievementDescription(string)`

```csharp
public static string GetAchievementDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetAchievementName(string)`

```csharp
public static string GetAchievementName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetArtifactKey(string)`

```csharp
public static string GetArtifactKey(string artifactType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactType` | `string` |  |

**Returns:** `string`

:::

::: details `GetArtifactKey(Type)`

```csharp
public static string GetArtifactKey(Type artifactType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetArtifactName(string)`

```csharp
public static string GetArtifactName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetArtifactShortStory(string)`

```csharp
public static string[] GetArtifactShortStory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string[]`

:::

::: details `GetArtifactStory(string)`

```csharp
public static string GetArtifactStory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetConversationData(string)`

```csharp
public static ConversationData GetConversationData(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `DewInternal.ConversationData`

:::

::: details `GetCurseDescription(string)`

```csharp
public static List<LocaleNode> GetCurseDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetCurseKey(string)`

```csharp
public static string GetCurseKey(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

:::

::: details `GetCurseName(string)`

```csharp
public static string GetCurseName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetCurseShortDescription(string)`

```csharp
public static List<LocaleNode> GetCurseShortDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetFormat(string, string)`

```csharp
public static string GetFormat(string formatString, string lang = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formatString` | `string` |  |
| `lang` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemDescription(string)`

```csharp
public static IReadOnlyList<LocaleNode> GetGemDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList<T><LocaleNode>`

:::

::: details `GetGemDescriptionKey(Gem)`

```csharp
public static string GetGemDescriptionKey(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `string`

:::

::: details `GetGemKey(string)`

```csharp
public static string GetGemKey(string gemType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemType` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemKey(Type)`

```csharp
public static string GetGemKey(Type gemType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetGemMemory(string)`

```csharp
public static string GetGemMemory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemName(Gem)`

```csharp
public static string GetGemName(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `string`

:::

::: details `GetGemName(string)`

```csharp
public static string GetGemName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemNameKey(Gem)`

```csharp
public static string GetGemNameKey(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `string`

:::

::: details `GetGemShortDescription(string)`

```csharp
public static string GetGemShortDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetGemTemplate(string)`

```csharp
public static string GetGemTemplate(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetRecommendedSupportedLanguage()`

```csharp
public static string GetRecommendedSupportedLanguage()
```

**Returns:** `string`

:::

::: details `GetSkillDescription(string, int)`

```csharp
public static List<LocaleNode> GetSkillDescription(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetSkillDescriptionKey(SkillTrigger, int)`

```csharp
public static string GetSkillDescriptionKey(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillKey(string)`

```csharp
public static string GetSkillKey(string skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | `string` |  |

**Returns:** `string`

:::

::: details `GetSkillKey(Type)`

```csharp
public static string GetSkillKey(Type skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetSkillLevelKey(int)`

```csharp
public static string GetSkillLevelKey(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillLevelSuffix(int)`

```csharp
public static string GetSkillLevelSuffix(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillLevelTemplate(int, int?)`

```csharp
public static string GetSkillLevelTemplate(int level, int? toLevel = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `toLevel` | `int?` |  |

**Returns:** `string`

:::

::: details `GetSkillMemory(string)`

```csharp
public static string GetSkillMemory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetSkillName(SkillTrigger, int)`

```csharp
public static string GetSkillName(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillName(string, int)`

```csharp
public static string GetSkillName(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillNameKey(SkillTrigger, int)`

```csharp
public static string GetSkillNameKey(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetSkillShortDesc(string, int)`

```csharp
public static string GetSkillShortDesc(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `string`

:::

::: details `GetStarDescription(string)`

```csharp
public static List<LocaleNode> GetStarDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetStarDescription(Type)`

```csharp
public static List<LocaleNode> GetStarDescription(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `System.Collections.Generic.List<T><LocaleNode>`

:::

::: details `GetStarLore(string)`

```csharp
public static string GetStarLore(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetStarName(string)`

```csharp
public static string GetStarName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetStarName(Type)`

```csharp
public static string GetStarName(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `string`

:::

::: details `GetTreasureDescription(string)`

```csharp
public static IReadOnlyList<LocaleNode> GetTreasureDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList<T><LocaleNode>`

:::

::: details `GetTreasureKey(string)`

```csharp
public static string GetTreasureKey(string treasureType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `treasureType` | `string` |  |

**Returns:** `string`

:::

::: details `GetTreasureLore(string)`

```csharp
public static string GetTreasureLore(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetTreasureName(string)`

```csharp
public static string GetTreasureName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `GetUIValue(string)`

```csharp
public static string GetUIValue(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `HighlightKeywords(string)`

```csharp
public static string HighlightKeywords(string input)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `input` | `string` |  |

**Returns:** `string`

:::

::: details `Initialize()`

```csharp
public static void Initialize()
```

:::

::: details `ProcessGenericBacktickedString(string, object, string)`

refObject can be any object including System.Type.Supported Field Types: Field/const value in refObject, Field/const value in refType instance of DewResources Database.

```csharp
public static string ProcessGenericBacktickedString(string text, object refObject, string lang = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `text` | `string` |  |
| `refObject` | `object` |  |
| `lang` | `string` |  |

**Returns:** `string`

:::

::: details `RenderChangedValue(string, string)`

```csharp
public static string RenderChangedValue(string prev, string after)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prev` | `string` |  |
| `after` | `string` |  |

**Returns:** `string`

:::

::: details `RenderWeakenedValue(string, string)`

```csharp
public static string RenderWeakenedValue(string prev, string after)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prev` | `string` |  |
| `after` | `string` |  |

**Returns:** `string`

:::

::: details `TryGetUIValue(string, out string)`

```csharp
public static bool TryGetUIValue(string key, out string value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `string` |  |

**Returns:** `bool`

:::
