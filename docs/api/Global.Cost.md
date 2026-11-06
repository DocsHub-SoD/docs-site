# Struct: Cost

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct Cost
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dreamDust`** | `public int dreamDust` |  |
| **`gold`** | `public int gold` |  |
| **`healthPercentage`** | `public int healthPercentage` |  |
| **`platinumCoin`** | `public int platinumCoin` |  |
| **`stardust`** | `public int stardust` |  |

:::

## Methods (12)

::: details `CanAfford(DewPlayer, int)`

```csharp
public AffordType CanAfford(DewPlayer player, int playerStardust = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `playerStardust` | `int` |  |

**Returns:** `AffordType`

:::

::: details `CanAfford(Entity, int)`

```csharp
public AffordType CanAfford(Entity entity, int playerStardust = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `playerStardust` | `int` |  |

**Returns:** `AffordType`

:::

::: details `DreamDust(int)`

```csharp
public static Cost DreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `Equals(Cost)`

```csharp
public bool Equals(Cost other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`Cost`](/api/Global.Cost) |  |

**Returns:** `bool`

:::

::: details `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

:::

::: details `Gold(int)`

```csharp
public static Cost Gold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `HealthPercentage(int)`

```csharp
public static Cost HealthPercentage(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `MultiplyGold(float)`

```csharp
public Cost MultiplyGold(float scalar)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `scalar` | `float` |  |

**Returns:** `Cost`

:::

::: details `Platinum(int)`

```csharp
public static Cost Platinum(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `Stardust(int)`

```csharp
public static Cost Stardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (39)

*Classes and systems that invoke, reference, or depend on `Cost`:*

[Artifact](/api/Global.Artifact) · `CostDisplay` · `CostExtensions` · [DewAdvText](/api/Global.DewAdvText) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillShrine](/api/Global.EditSkillShrine) · [FloatCost](/api/Global.FloatCost) · [ICustomInteractable](/api/Global.ICustomInteractable) · [MerchandiseData](/api/Global.MerchandiseData) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · [Room_Shortcut](/api/Global.Room_Shortcut) · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Husk_I_ShopIntimidation` · [Shrine](/api/Global.Shrine) · `Shrine_AltarOfCleansing` · `Shrine_Ascension` · `Shrine_Disintegration` · `Shrine_Guidance` · `Shrine_Luck` · `Shrine_MawOfDoom` · `Shrine_MorasDomain_HerPresence` · `Shrine_UpgradeWell` · [Treasure](/api/Global.Treasure) · `UI_EmoteList_Item` · `UI_InGame_FloatingWindow_Shop` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_Interact_Custom` · `UI_InGame_Interact_Shrine` · `UI_InGame_SkillButton_EditSkill` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_ObliterationView` · `UI_Lobby_SkinList_Item` · `UI_NametagList_Item` · `UI_TravelerStory_Details_Story_ChapterItem` · `UI_TravelerStory_HeroNode` · `Mirror.GeneratedNetworkCode`

### Dependencies (4)

*Types and components that `Cost` references or depends upon:*

[DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [FloatCost](/api/Global.FloatCost)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#affordtype" class="enum-link" data-tooltip="Yes=0 · NoGold=1 · NoDreamDust=2 · NoStardust=3 · NoHealth=4 (+1 more)">AffordType</a>

:::
