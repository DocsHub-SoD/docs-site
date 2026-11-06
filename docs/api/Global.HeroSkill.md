# Class: HeroSkill

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent) → [HeroComponent](/api/Global.HeroComponent)

```csharp
public class HeroSkill : HeroComponent, ILogicUpdate, ICleanup
```

## Fields (17)

::: details Click to expand Fields (17)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientHeroEvent_OnGemDrop`** | `public SafeAction<Gem> ClientHeroEvent_OnGemDrop` |  |
| **`ClientHeroEvent_OnGemEquip`** | `public SafeAction<Gem> ClientHeroEvent_OnGemEquip` |  |
| **`ClientHeroEvent_OnGemPickup`** | `public SafeAction<Gem> ClientHeroEvent_OnGemPickup` |  |
| **`ClientHeroEvent_OnGemQualityChanged`** | `public SafeAction<Gem, int, int> ClientHeroEvent_OnGemQualityChanged` |  |
| **`ClientHeroEvent_OnGemSwap`** | `public SafeAction<GemLocation, GemLocation> ClientHeroEvent_OnGemSwap` |  |
| **`ClientHeroEvent_OnGemUnequip`** | `public SafeAction<Gem> ClientHeroEvent_OnGemUnequip` |  |
| **`ClientHeroEvent_OnSkillDrop`** | `public SafeAction<SkillTrigger> ClientHeroEvent_OnSkillDrop` |  |
| **`ClientHeroEvent_OnSkillEquip`** | `public SafeAction<SkillTrigger> ClientHeroEvent_OnSkillEquip` |  |
| **`ClientHeroEvent_OnSkillLevelChanged`** | `public SafeAction<SkillTrigger, int, int> ClientHeroEvent_OnSkillLevelChanged` |  |
| **`ClientHeroEvent_OnSkillPickup`** | `public SafeAction<SkillTrigger> ClientHeroEvent_OnSkillPickup` |  |
| **`ClientHeroEvent_OnSkillSwap`** | `public SafeAction<HeroSkillLocation, HeroSkillLocation> ClientHeroEvent_OnSkillSwap` |  |
| **`ClientHeroEvent_OnSkillUnequip`** | `public SafeAction<SkillTrigger> ClientHeroEvent_OnSkillUnequip` |  |
| **`loadoutMovement`** | `public AssetRef<SkillTrigger>[] loadoutMovement` |  |
| **`loadoutQ`** | `public AssetRef<SkillTrigger>[] loadoutQ` |  |
| **`loadoutR`** | `public AssetRef<SkillTrigger>[] loadoutR` |  |
| **`loadoutTrait`** | `public AssetRef<SkillTrigger>[] loadoutTrait` |  |
| **`starNormalizedStrength`** | `[NonSerialized] [SaveVar(SaveVarFlags.Default)] public float starNormalizedStrength` |  |

:::

## Properties (14)

::: details Click to expand Properties (14)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`E`** | `public SkillTrigger E { get; set; }` |  |
| **`gems`** | `public IReadOnlyDictionary<GemLocation, Gem> gems { get; }` |  |
| **`holdingObject`** | `public IItem holdingObject { get; }` |  |
| **`Identity`** | `public SkillTrigger Identity { get; set; }` |  |
| **`maxGemCountE`** | `public int maxGemCountE { get; set; }` |  |
| **`maxGemCountIdentity`** | `public int maxGemCountIdentity { get; set; }` |  |
| **`maxGemCountMovement`** | `public int maxGemCountMovement { get; set; }` |  |
| **`maxGemCountQ`** | `public int maxGemCountQ { get; set; }` |  |
| **`maxGemCountR`** | `public int maxGemCountR { get; set; }` |  |
| **`maxGemCountW`** | `public int maxGemCountW { get; set; }` |  |
| **`Movement`** | `public SkillTrigger Movement { get; set; }` |  |
| **`Q`** | `public SkillTrigger Q { get; set; }` |  |
| **`R`** | `public SkillTrigger R { get; set; }` |  |
| **`W`** | `public SkillTrigger W { get; set; }` |  |

:::

## Methods (36)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CanReplaceSkill(HeroSkillLocation)`

```csharp
public bool CanReplaceSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `bool`

:::

::: details `CmdEquipGem(GemLocation, Gem)`

```csharp
public void CmdEquipGem(GemLocation loc, Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `CmdEquipSkill(HeroSkillLocation, SkillTrigger)`

```csharp
public void CmdEquipSkill(HeroSkillLocation type, SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

:::

::: details `CmdMoveGem(Gem, Vector3)`

```csharp
public void CmdMoveGem(Gem gem, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `CmdMoveSkill(SkillTrigger, Vector3)`

```csharp
public void CmdMoveSkill(SkillTrigger skill, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `CmdStopHoldInHand()`

```csharp
public void CmdStopHoldInHand()
```

:::

::: details `CmdSwapSlotGem(GemLocation, GemLocation)`

```csharp
public void CmdSwapSlotGem(GemLocation a, GemLocation b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | [`GemLocation`](/api/Global.GemLocation) |  |
| `b` | [`GemLocation`](/api/Global.GemLocation) |  |

:::

::: details `CmdSwapSlotSkill(HeroSkillLocation, HeroSkillLocation)`

```csharp
public void CmdSwapSlotSkill(HeroSkillLocation a, HeroSkillLocation b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `b` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

:::

::: details `CmdUnequipGem(GemLocation, Vector3)`

```csharp
public void CmdUnequipGem(GemLocation loc, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `CmdUnequipSkill(HeroSkillLocation, Vector3)`

```csharp
public void CmdUnequipSkill(HeroSkillLocation type, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `EquipGem(GemLocation, Gem)`

```csharp
public void EquipGem(GemLocation loc, Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `EquipSkill(HeroSkillLocation, SkillTrigger, bool)`

```csharp
public void EquipSkill(HeroSkillLocation type, SkillTrigger skill, bool ignoreCanReplace = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `ignoreCanReplace` | `bool` |  |

:::

::: details `GetCurrentGemCount(HeroSkillLocation)`

```csharp
public int GetCurrentGemCount(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `int`

:::

::: details `GetEmptyGemSlot(HeroSkillLocation)`

```csharp
public int GetEmptyGemSlot(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `int`

:::

::: details `GetFirstGem(HeroSkillLocation)`

```csharp
public Gem GetFirstGem(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `Gem`

:::

::: details `GetGem(GemLocation)`

```csharp
public Gem GetGem(GemLocation loc)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |

**Returns:** `Gem`

:::

::: details `GetGemsInSkill(HeroSkillLocation)`

```csharp
public IEnumerable<Gem> GetGemsInSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><Gem>`

:::

::: details `GetGemsPairInSkill(HeroSkillLocation)`

```csharp
public IEnumerable<KeyValuePair<GemLocation, Gem>> GetGemsPairInSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.KeyValuePair<TKey, TValue><GemLocation,Gem>>`

:::

::: details `GetLoadoutSkills(HeroSkillLocation)`

```csharp
public SkillTrigger[] GetLoadoutSkills(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `SkillTrigger[]`

:::

::: details `GetMaxGemCount(HeroSkillLocation)`

```csharp
public int GetMaxGemCount(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `int`

:::

::: details `GetSkill(HeroSkillLocation)`

```csharp
public SkillTrigger GetSkill(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `SkillTrigger`

:::

::: details `HasGemOfType(string)`

```csharp
public bool HasGemOfType(string type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |

**Returns:** `bool`

:::

::: details `HoldInHand(IItem)`

```csharp
public void HoldInHand(IItem holdable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `holdable` | [`IItem`](/api/Global.IItem) |  |

:::

::: details `MergeGem(Gem, Gem)`

```csharp
public void MergeGem(Gem victim, Gem receivingGem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Gem`](/api/Global.Gem) |  |
| `receivingGem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `SetMaxGemCount(HeroSkillLocation, int)`

```csharp
public void SetMaxGemCount(HeroSkillLocation type, int count)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `count` | `int` |  |

:::

::: details `StopHoldInHand()`

```csharp
public void StopHoldInHand()
```

:::

::: details `TryGetEquippedGemOfSameType(Type, out GemLocation, out Gem)`

```csharp
public bool TryGetEquippedGemOfSameType(Type type, out GemLocation loc, out Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `bool`

:::

::: details `TryGetGem(GemLocation, out Gem)`

```csharp
public bool TryGetGem(GemLocation loc, out Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `bool`

:::

::: details `TryGetGemLocation(Gem, out GemLocation)`

```csharp
public bool TryGetGemLocation(Gem gem, out GemLocation location)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |
| `location` | [`GemLocation`](/api/Global.GemLocation) |  |

**Returns:** `bool`

:::

::: details `TryGetSkill(HeroSkillLocation, out SkillTrigger)`

```csharp
public bool TryGetSkill(HeroSkillLocation type, out SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `bool`

:::

::: details `TryGetSkillLocation(SkillTrigger, out HeroSkillLocation)`

```csharp
public bool TryGetSkillLocation(SkillTrigger skill, out HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `bool`

:::

::: details `UnequipGem(GemLocation, Vector3)`

```csharp
public Gem UnequipGem(GemLocation loc, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `position` | `UnityEngine.Vector3` |  |

**Returns:** `Gem`

:::

::: details `UnequipSkill(HeroSkillLocation, Vector3, bool)`

```csharp
public SkillTrigger UnequipSkill(HeroSkillLocation type, Vector3 position, bool ignoreCanReplace = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `position` | `UnityEngine.Vector3` |  |
| `ignoreCanReplace` | `bool` |  |

**Returns:** `SkillTrigger`

:::
