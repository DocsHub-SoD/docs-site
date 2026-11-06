# Struct: PerRarityData&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct PerRarityData<T>
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`character`** | `public T character` |  |
| **`common`** | `public T common` |  |
| **`epic`** | `public T epic` |  |
| **`identity`** | `public T identity` |  |
| **`legendary`** | `public T legendary` |  |
| **`rare`** | `public T rare` |  |
| **`unique`** | `public T unique` |  |

:::

## Methods (2)

::: details `Get(Rarity)`

```csharp
public T Get(Rarity rarity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |

**Returns:** `T`

:::

::: details `Set(Rarity, T)`

```csharp
public void Set(Rarity rarity, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `value` | `T` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (9)

*Classes and systems that invoke, reference, or depend on `PerRarityData<T>`:*

[DewGameplayExperienceSettings](/api/Global.DewGameplayExperienceSettings) · [GameManager](/api/Global.GameManager) · [Gem](/api/Global.Gem) · [LootManager](/api/Global.LootManager) · `Se_Star_Bismuth_I_KnowledgeBook` · `Shrine_Ascension` · `Shrine_Chaos` · [SkillTrigger](/api/Global.SkillTrigger) · `UI_InGame_FloatingWindow_Chaos_Item`

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`Rarity`](/enums#rarity)

:::
