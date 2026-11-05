# Class: DewLocalization

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewLocalization
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`buildData`** | `public static DewLocalizationBuildData buildData { get; }` |  |
| **`data`** | `public static PerLanguageLocalizationData data { get; }` |  |

## Methods

### `CaptureDescriptionExpressions(IReadOnlyList&lt;LocaleNode&gt;, Dictionary&lt;string, string&gt;, DescriptionSettings)`

```csharp
public static void CaptureDescriptionExpressions(IReadOnlyList<LocaleNode> nodes, Dictionary<string, string> data, DewLocalization.DescriptionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodes` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;LocaleNode&gt;` |  |
| `data` | `System.Collections.Generic.Dictionary&lt;TKey, TValue&gt;&lt;string,string&gt;` |  |
| `settings` | [DewLocalization.DescriptionSettings](/api/Global.DewLocalization) |  |

### `ConvertDescriptionNodesToText(IReadOnlyList&lt;LocaleNode&gt;, DescriptionSettings)`

```csharp
public static string ConvertDescriptionNodesToText(IReadOnlyList<LocaleNode> nodes, DewLocalization.DescriptionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodes` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;LocaleNode&gt;` |  |
| `settings` | [DewLocalization.DescriptionSettings](/api/Global.DewLocalization) |  |

**Returns:** `string`

### `EvaluateAndRenderExpression(ExpressionData, DescriptionSettings, bool)`

```csharp
public static string EvaluateAndRenderExpression(ExpressionData exp, DewLocalization.DescriptionSettings settings, bool shouldShowDetail)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `exp` | `DewInternal.ExpressionData` |  |
| `settings` | [DewLocalization.DescriptionSettings](/api/Global.DewLocalization) |  |
| `shouldShowDetail` | `bool` |  |

**Returns:** `string`

### `GetAchievementDescription(string)`

```csharp
public static string GetAchievementDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetAchievementName(string)`

```csharp
public static string GetAchievementName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetArtifactKey(string)`

```csharp
public static string GetArtifactKey(string artifactType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactType` | `string` |  |

**Returns:** `string`

### `GetArtifactKey(Type)`

```csharp
public static string GetArtifactKey(Type artifactType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactType` | `System.Type` |  |

**Returns:** `string`

### `GetArtifactName(string)`

```csharp
public static string GetArtifactName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetArtifactShortStory(string)`

```csharp
public static string[] GetArtifactShortStory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string[]`

### `GetArtifactStory(string)`

```csharp
public static string GetArtifactStory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetConversationData(string)`

```csharp
public static ConversationData GetConversationData(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `DewInternal.ConversationData`

### `GetCurseDescription(string)`

```csharp
public static List<LocaleNode> GetCurseDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;LocaleNode&gt;`

### `GetCurseKey(string)`

```csharp
public static string GetCurseKey(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

### `GetCurseName(string)`

```csharp
public static string GetCurseName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetCurseShortDescription(string)`

```csharp
public static List<LocaleNode> GetCurseShortDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;LocaleNode&gt;`

### `GetFormat(string, string)`

```csharp
public static string GetFormat(string formatString, string lang = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formatString` | `string` |  |
| `lang` | `string` |  |

**Returns:** `string`

### `GetGemDescription(string)`

```csharp
public static IReadOnlyList<LocaleNode> GetGemDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;LocaleNode&gt;`

### `GetGemDescriptionKey(Gem)`

```csharp
public static string GetGemDescriptionKey(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [Gem](/api/Global.Gem) |  |

**Returns:** `string`

### `GetGemKey(string)`

```csharp
public static string GetGemKey(string gemType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemType` | `string` |  |

**Returns:** `string`

### `GetGemKey(Type)`

```csharp
public static string GetGemKey(Type gemType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemType` | `System.Type` |  |

**Returns:** `string`

### `GetGemMemory(string)`

```csharp
public static string GetGemMemory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetGemName(Gem)`

```csharp
public static string GetGemName(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [Gem](/api/Global.Gem) |  |

**Returns:** `string`

### `GetGemName(string)`

```csharp
public static string GetGemName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetGemNameKey(Gem)`

```csharp
public static string GetGemNameKey(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [Gem](/api/Global.Gem) |  |

**Returns:** `string`

### `GetGemShortDescription(string)`

```csharp
public static string GetGemShortDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetGemTemplate(string)`

```csharp
public static string GetGemTemplate(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetRecommendedSupportedLanguage()`

```csharp
public static string GetRecommendedSupportedLanguage()
```

**Returns:** `string`

### `GetSkillDescription(string, int)`

```csharp
public static List<LocaleNode> GetSkillDescription(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;LocaleNode&gt;`

### `GetSkillDescriptionKey(SkillTrigger, int)`

```csharp
public static string GetSkillDescriptionKey(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [SkillTrigger](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

### `GetSkillKey(string)`

```csharp
public static string GetSkillKey(string skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | `string` |  |

**Returns:** `string`

### `GetSkillKey(Type)`

```csharp
public static string GetSkillKey(Type skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | `System.Type` |  |

**Returns:** `string`

### `GetSkillLevelKey(int)`

```csharp
public static string GetSkillLevelKey(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `string`

### `GetSkillLevelSuffix(int)`

```csharp
public static string GetSkillLevelSuffix(int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |

**Returns:** `string`

### `GetSkillLevelTemplate(int, int?)`

```csharp
public static string GetSkillLevelTemplate(int level, int? toLevel = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `level` | `int` |  |
| `toLevel` | `int?` |  |

**Returns:** `string`

### `GetSkillMemory(string)`

```csharp
public static string GetSkillMemory(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetSkillName(SkillTrigger, int)`

```csharp
public static string GetSkillName(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [SkillTrigger](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

### `GetSkillName(string, int)`

```csharp
public static string GetSkillName(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `string`

### `GetSkillNameKey(SkillTrigger, int)`

```csharp
public static string GetSkillNameKey(SkillTrigger skill, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [SkillTrigger](/api/Global.SkillTrigger) |  |
| `configIndex` | `int` |  |

**Returns:** `string`

### `GetSkillShortDesc(string, int)`

```csharp
public static string GetSkillShortDesc(string key, int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `configIndex` | `int` |  |

**Returns:** `string`

### `GetStarDescription(string)`

```csharp
public static List<LocaleNode> GetStarDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;LocaleNode&gt;`

### `GetStarDescription(Type)`

```csharp
public static List<LocaleNode> GetStarDescription(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;LocaleNode&gt;`

### `GetStarLore(string)`

```csharp
public static string GetStarLore(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetStarName(string)`

```csharp
public static string GetStarName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetStarName(Type)`

```csharp
public static string GetStarName(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `string`

### `GetTreasureDescription(string)`

```csharp
public static IReadOnlyList<LocaleNode> GetTreasureDescription(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;LocaleNode&gt;`

### `GetTreasureKey(string)`

```csharp
public static string GetTreasureKey(string treasureType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `treasureType` | `string` |  |

**Returns:** `string`

### `GetTreasureLore(string)`

```csharp
public static string GetTreasureLore(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetTreasureName(string)`

```csharp
public static string GetTreasureName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `GetUIValue(string)`

```csharp
public static string GetUIValue(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

### `HighlightKeywords(string)`

```csharp
public static string HighlightKeywords(string input)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `input` | `string` |  |

**Returns:** `string`

### `Initialize()`

```csharp
public static void Initialize()
```

### `ProcessGenericBacktickedString(string, object, string)`

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

### `RenderChangedValue(string, string)`

```csharp
public static string RenderChangedValue(string prev, string after)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prev` | `string` |  |
| `after` | `string` |  |

**Returns:** `string`

### `RenderWeakenedValue(string, string)`

```csharp
public static string RenderWeakenedValue(string prev, string after)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prev` | `string` |  |
| `after` | `string` |  |

**Returns:** `string`

### `TryGetUIValue(string, out string)`

```csharp
public static bool TryGetUIValue(string key, out string value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `string` |  |

**Returns:** `bool`
