# Class: SkillTrigger

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityTrigger](/api/Global.AbilityTrigger)

```csharp
public class SkillTrigger : AbilityTrigger, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IItem, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnHandOwnerChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnHandOwnerChanged` |  |
| **`ClientEvent_OnTempOwnerChanged`** | `public SafeAction<DewPlayer, DewPlayer> ClientEvent_OnTempOwnerChanged` |  |
| **`ClientSkillEvent_OnDismantleProgressChanged`** | `public SafeAction<float, float> ClientSkillEvent_OnDismantleProgressChanged` | Called everywhere when dismantle progress changes. |
| **`ClientSkillEvent_OnLevelChange`** | `public SafeAction<int, int> ClientSkillEvent_OnLevelChange` |  |
| **`customSkillHastePerLevel`** | `[BoxGroup("Skill Settings", true, false, 0)] [LabelText("Skill Haste Per Level")] [ShowIf("useCustomSkillHastePerLevel", true)] public float customSkillHastePerLevel` |  |
| **`DisableHeroTypeCheckOnIdentityMemories`** | `public static bool DisableHeroTypeCheckOnIdentityMemories` |  |
| **`DismantleDecayStartTime`** | `public const float DismantleDecayStartTime = 1` |  |
| **`DismantleTapMinInterval`** | `public const float DismantleTapMinInterval = 0.075` |  |
| **`DismantleTapStrength`** | `public const float DismantleTapStrength = 0.4` |  |
| **`endEffect`** | `[LabelText("End Effect (Attached)")] [BoxGroup("Skill Settings", true, false, 0)] public GameObject endEffect` |  |
| **`excludeFromPool`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`isLevelUpEnabled`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool isLevelUpEnabled` |  |
| **`rarity`** | `[BoxGroup("Skill Settings", true, false, 0)] public Rarity rarity` |  |
| **`showFillAmountOnScreen`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool showFillAmountOnScreen` |  |
| **`startEffect`** | `[LabelText("Start Effect (Attached)")] [BoxGroup("Skill Settings", true, false, 0)] public GameObject startEffect` |  |
| **`statBonus`** | `[NonSerialized] public StatBonus statBonus` |  |
| **`tags`** | `[BoxGroup("Skill Settings", true, false, 0)] public DescriptionTags tags` |  |
| **`type`** | `[BoxGroup("Skill Settings", true, false, 0)] public SkillType type` |  |
| **`Ult_GlobalChargeMultiplier`** | `public const float Ult_GlobalChargeMultiplier = 0.85` |  |
| **`Ult_OnKillBoss`** | `public const float Ult_OnKillBoss = 42.5` |  |
| **`Ult_OnKillLesser`** | `public const float Ult_OnKillLesser = 0.12750001` |  |
| **`Ult_OnKillMiniBoss`** | `public const float Ult_OnKillMiniBoss = 12.75` |  |
| **`Ult_OnKillNormal`** | `public const float Ult_OnKillNormal = 0.63750005` |  |
| **`Ult_PerDealtAttack`** | `public const float Ult_PerDealtAttack = 0.2125` |  |
| **`Ult_PerDealtDamageBossEnemyHealthRatio`** | `public const float Ult_PerDealtDamageBossEnemyHealthRatio = 25.5` |  |
| **`Ult_PerDealtDamageLesserEnemyHealthRatio`** | `public const float Ult_PerDealtDamageLesserEnemyHealthRatio = 0.12750001` |  |
| **`Ult_PerDealtDamageMiniBossEnemyHealthRatio`** | `public const float Ult_PerDealtDamageMiniBossEnemyHealthRatio = 12.75` |  |
| **`Ult_PerDealtDamageNormalEnemyHealthRatio`** | `public const float Ult_PerDealtDamageNormalEnemyHealthRatio = 0.25500003` |  |
| **`Ult_PerDealtElementalDamage`** | `public const float Ult_PerDealtElementalDamage = 0.0425` |  |
| **`Ult_PerDealtNonElementalDamage`** | `public const float Ult_PerDealtNonElementalDamage = 0.2125` |  |
| **`Ult_PerTakenDamageMyHealthRatio`** | `public const float Ult_PerTakenDamageMyHealthRatio = 25.5` |  |
| **`Ult_PerTakenElementalDamage`** | `public const float Ult_PerTakenElementalDamage = 0.0425` |  |
| **`Ult_PerTakenNonElementalDamage`** | `public const float Ult_PerTakenNonElementalDamage = 0.2125` |  |
| **`useCustomSkillHastePerLevel`** | `[BoxGroup("Skill Settings", true, false, 0)] public bool useCustomSkillHastePerLevel` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`characterSkillOwner`** | `[SaveVar(SaveVarFlags.Default)] public string characterSkillOwner { get; set; }` |  |
| **`dismantleProgress`** | `public float dismantleProgress { get; }` |  |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`handOwner`** | `public Hero handOwner { get; set; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`isAnimatingEmbraceNewIdentity`** | `public bool isAnimatingEmbraceNewIdentity { get; set; }` |  |
| **`isCharacterSkill`** | `public bool isCharacterSkill { get; }` |  |
| **`isLocked`** | `public bool isLocked { get; }` | Is this skill locked for local player? |
| **`level`** | `[SaveVar(SaveVarFlags.Default)] public int level { get; set; }` |  |
| **`mainConfigOriginalCharge`** | `public int mainConfigOriginalCharge { get; }` |  |
| **`maxSellGold`** | `public int maxSellGold { get; set; }` |  |
| **`owner`** | `public Hero owner { get; }` |  |
| **`sbCooldownMultiplier`** | `public float sbCooldownMultiplier { get; }` |  |
| **`sbCooldownMultiplierIgnoreReceiveCooldownReductionFlag`** | `public float sbCooldownMultiplierIgnoreReceiveCooldownReductionFlag { get; }` |  |
| **`sbCooldownOffset`** | `public float sbCooldownOffset { get; }` |  |
| **`sbCooldownOffsetIgnoreReceiveCooldownReductionFlag`** | `public float sbCooldownOffsetIgnoreReceiveCooldownReductionFlag { get; }` |  |
| **`skillHastePerLevel`** | `public float skillHastePerLevel { get; }` |  |
| **`skillType`** | `public HeroSkillLocation skillType { get; }` | Location of this skill trigger if equipped. |
| **`skipStartAnimation`** | `public bool skipStartAnimation { get; set; }` |  |
| **`specialOverlayColor`** | `public Color specialOverlayColor { get; set; }` |  |
| **`statEntity`** | `public Entity statEntity { get; }` |  |
| **`tempOwner`** | `public DewPlayer tempOwner { get; set; }` |  |
| **`worldModel`** | `public ItemWorldModel worldModel { get; }` |  |

## Methods

### `AddSkillBonus(SkillBonus)`

```csharp
public SkillBonus AddSkillBonus(SkillBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`SkillBonus`](/api/Global.SkillBonus) |  |

**Returns:** `SkillBonus`

### `Awake()`

```csharp
protected override void Awake()
```

### `CanInteract(Entity)`

```csharp
public bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `CreateDamage(SourceType, ScalingValue, float)`

```csharp
public DamageData CreateDamage(DamageData.SourceType type, ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DamageData.SourceType`](/api/Global.DamageData) |  |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `Damage(ScalingValue, float)`

```csharp
public DamageData Damage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `DefaultDamage(ScalingValue, float)`

```csharp
public DamageData DefaultDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `DismantleSkill()`

```csharp
public void DismantleSkill()
```

### `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

### `GetBuyGold()`

```csharp
public int GetBuyGold()
```

**Returns:** `int`

### `GetBuyGold(Rarity, int)`

```csharp
public static int GetBuyGold(Rarity rarity, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `level` | `int` |  |

**Returns:** `int`

### `GetCooldownTimeMultiplier(int)`

```csharp
public override float GetCooldownTimeMultiplier(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

### `GetCooldownTimeOffset(int)`

```csharp
public override float GetCooldownTimeOffset(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `float`

### `GetCooldownTimeOnLevel(int)`

```csharp
public float GetCooldownTimeOnLevel(int lvl)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `lvl` | `int` |  |

**Returns:** `float`

### `GetDismantleAmount(DewPlayer)`

```csharp
public int GetDismantleAmount(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `int`

### `GetFormattedSkillTitle()`

```csharp
public string GetFormattedSkillTitle()
```

**Returns:** `string`

### `GetGoldValue(Rarity, int)`

```csharp
public static int GetGoldValue(Rarity rarity, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `level` | `int` |  |

**Returns:** `int`

### `GetLoadoutHero()`

Get a hero that contains this skill in their loadout.Returns null if this is not from a hero.Note this can be an expensive operation to be calling every frame, since it will iterate through all hero types in the game.

```csharp
public Type GetLoadoutHero()
```

**Returns:** `System.Type`

### `GetSellGold()`

```csharp
public int GetSellGold()
```

**Returns:** `int`

### `GetSellGold(Rarity, int)`

```csharp
public static int GetSellGold(Rarity rarity, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `level` | `int` |  |

**Returns:** `int`

### `GetValue(ScalingValue)`

```csharp
public float GetValue(ScalingValue val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `float`

### `Heal(ScalingValue)`

```csharp
public HealData Heal(ScalingValue amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `HealData`

### `IsLockedFor(DewPlayer)`

```csharp
public bool IsLockedFor(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `MagicDamage(ScalingValue, float)`

```csharp
public DamageData MagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `OnCastComplete(int, CastInfo)`

```csharp
public override AbilityInstance OnCastComplete(int configIndex, CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `AbilityInstance`

### `OnEquip(Entity)`

```csharp
protected override void OnEquip(Entity newOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newOwner` | [`Entity`](/api/Global.Entity) |  |

### `OnLevelChange(int, int)`

Called everywhere when this skill's level is changed.

```csharp
protected virtual void OnLevelChange(int oldLevel, int newLevel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldLevel` | `int` |  |
| `newLevel` | `int` |  |

### `OnPrepare()`

```csharp
protected override void OnPrepare()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnUnequip(Entity)`

```csharp
protected override void OnUnequip(Entity formerOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `formerOwner` | [`Entity`](/api/Global.Entity) |  |

### `PhysicalDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `PhysicalMagicDamage(ScalingValue, float)`

```csharp
public DamageData PhysicalMagicDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `PureDamage(ScalingValue, float)`

```csharp
public DamageData PureDamage(ScalingValue value, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | [`ScalingValue`](/api/Global.ScalingValue) |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

### `RemoveSkillBonus(SkillBonus)`

```csharp
public void RemoveSkillBonus(SkillBonus bonus)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bonus` | [`SkillBonus`](/api/Global.SkillBonus) |  |

### `RpcSetPositionAndRotation(Vector3, Quaternion)`

```csharp
public void RpcSetPositionAndRotation(Vector3 pos, Quaternion rot)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion` |  |

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

### `ShouldTickCooldown(int)`

```csharp
protected override bool ShouldTickCooldown(int configIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `configIndex` | `int` |  |

**Returns:** `bool`

### `UpdateSkillBonus()`

```csharp
public void UpdateSkillBonus()
```
