# Class: Gem

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
public class Gem : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IItem, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnHandOwnerChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnHandOwnerChanged` |  |
| **`ClientEvent_OnOwnerChanged`** | `public SafeAction<Hero, Hero> ClientEvent_OnOwnerChanged` |  |
| **`ClientEvent_OnTempOwnerChanged`** | `public SafeAction<DewPlayer, DewPlayer> ClientEvent_OnTempOwnerChanged` |  |
| **`ClientGemEvent_OnCooldownReady`** | `public SafeAction ClientGemEvent_OnCooldownReady` |  |
| **`ClientGemEvent_OnCooldownReduced`** | `public SafeAction<float> ClientGemEvent_OnCooldownReduced` |  |
| **`ClientGemEvent_OnCooldownReducedByRatio`** | `public SafeAction<float> ClientGemEvent_OnCooldownReducedByRatio` |  |
| **`ClientGemEvent_OnCooldownStarted`** | `public SafeAction ClientGemEvent_OnCooldownStarted` |  |
| **`ClientGemEvent_OnFlash`** | `public SafeAction ClientGemEvent_OnFlash` |  |
| **`ClientGemEvent_OnQualityChanged`** | `public SafeAction<int, int> ClientGemEvent_OnQualityChanged` |  |
| **`cooldownTime`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isCooldownEnabled", true)] public ScalingValue cooldownTime` |  |
| **`enableStatBonus`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool enableStatBonus` |  |
| **`excludeFromPool`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`GemMergeExponent`** | `public const float GemMergeExponent = 1` |  |
| **`icon`** | `[BoxGroup("Gem Settings", true, false, 0)] public Sprite icon` |  |
| **`isCooldownEnabled`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool isCooldownEnabled` |  |
| **`isRateLimited`** | `[BoxGroup("Gem Settings", true, false, 0)] public bool isRateLimited` |  |
| **`rarity`** | `[BoxGroup("Gem Settings", true, false, 0)] public Rarity rarity` |  |
| **`rateLimitCount`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isRateLimited", true)] public ScalingValue rateLimitCount` |  |
| **`rateLimitTime`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isRateLimited", true)] public ScalingValue rateLimitTime` |  |
| **`readyEffect`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isCooldownEnabled", true)] public GameObject readyEffect` |  |
| **`setNumberDisplay`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("isRateLimited", true)] public bool setNumberDisplay` |  |
| **`statBonus`** | `[BoxGroup("Gem Settings", true, false, 0)] [ShowIf("enableStatBonus", true)] public StatBonus statBonus` |  |
| **`tags`** | `[BoxGroup("Gem Settings", true, false, 0)] public DescriptionTags tags` |  |
| **`tvDefaultAllExceptSelf`** | `protected AbilityTargetValidatorWrapper tvDefaultAllExceptSelf` |  |
| **`tvDefaultHarmfulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultHarmfulEffectTargets` |  |
| **`tvDefaultUsefulEffectTargets`** | `protected AbilityTargetValidatorWrapper tvDefaultUsefulEffectTargets` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`currentCooldown`** | `public float currentCooldown { get; }` |  |
| **`dismantleDreamDustOverride`** | `public int? dismantleDreamDustOverride { get; set; }` |  |
| **`dismantleProgress`** | `public float dismantleProgress { get; }` |  |
| **`effectiveLevel`** | `public int effectiveLevel { get; }` |  |
| **`fillAmount`** | `public float fillAmount { get; set; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`handOwner`** | `public Hero handOwner { get; set; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`isLocked`** | `public bool isLocked { get; }` | Is this gem locked for local player? |
| **`isNotReadyByRateLimit`** | `public bool isNotReadyByRateLimit { get; }` | Is this gem not ready because of rate limit? |
| **`isValid`** | `public bool isValid { get; }` | Returns true if gem is not destroyed, is active, and has owner. |
| **`location`** | `public GemLocation location { get; set; }` | Location of this gem if equipped to a hero. |
| **`maxCooldown`** | `public float maxCooldown { get; }` |  |
| **`maxSellGold`** | `public int maxSellGold { get; set; }` |  |
| **`numberDisplay`** | `public int? numberDisplay { get; set; }` |  |
| **`owner`** | `public Hero owner { get; set; }` |  |
| **`quality`** | `[SaveVar(SaveVarFlags.Default)] public int quality { get; set; }` |  |
| **`qualityType`** | `public Gem.QualityType qualityType { get; }` |  |
| **`sellGoldOverride`** | `public int? sellGoldOverride { get; set; }` |  |
| **`skill`** | `public SkillTrigger skill { get; set; }` |  |
| **`skipStartAnimation`** | `public bool skipStartAnimation { get; set; }` |  |
| **`tempOwner`** | `public DewPlayer tempOwner { get; set; }` |  |
| **`worldModel`** | `public ItemWorldModel worldModel { get; }` |  |

## Methods

### `ApplyCooldownReduction(float)`

```csharp
public void ApplyCooldownReduction(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

### `ApplyCooldownReductionByRatio(float)`

```csharp
public void ApplyCooldownReductionByRatio(float ratio)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ratio` | `float` |  |

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

### `CreateAbilityInstanceWithSource<T>(Actor, Vector3, Quaternion?, CastInfo, Action<T>)`

Create an ability instance on behalf of source actor, but make it inherit this gem's quality. You MUST ensure source will not be destroyed before calling this. Call this right after instance spawn or use Actor.LockDestroy().

```csharp
public T CreateAbilityInstanceWithSource<T>(Actor source, Vector3 position, Quaternion? rotation, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | [`Actor`](/api/Global.Actor) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

### `CreateBasicEffectWithSource(Actor, Entity, BasicEffect, float, string, DuplicateEffectBehavior)`

Create a basic effect container on behalf of source actor. You MUST ensure source will not be destroyed before calling this. Call this right after instance spawn or use Actor.LockDestroy().

```csharp
public Se_GenericEffectContainer CreateBasicEffectWithSource(Actor source, Entity victim, BasicEffect eff, float duration, string id, DuplicateEffectBehavior onDuplicate = DuplicateEffectBehavior.ReplacePrevious)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | [`Actor`](/api/Global.Actor) |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |
| `duration` | `float` |  |
| `id` | `string` |  |
| `onDuplicate` | [`DuplicateEffectBehavior`](/api/Global.DuplicateEffectBehavior) |  |

**Returns:** `Se_GenericEffectContainer`

### `CreateStatusEffectWithSource<T>(Actor, Entity, CastInfo, Action<T>)`

Create a status effect on behalf of source actor, but make it inherit this gem's quality. You MUST ensure source will not be destroyed before calling this. Call this right after instance spawn or use Actor.LockDestroy().

```csharp
public T CreateStatusEffectWithSource<T>(Actor source, Entity victim, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `source` | [`Actor`](/api/Global.Actor) |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

### `DismantleGem()`

```csharp
public void DismantleGem()
```

### `GetBuyGold()`

```csharp
public int GetBuyGold()
```

**Returns:** `int`

### `GetBuyGold(Rarity, int)`

```csharp
public static int GetBuyGold(Rarity rarity, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `quality` | `int` |  |

**Returns:** `int`

### `GetDismantleAmount(DewPlayer)`

```csharp
public int GetDismantleAmount(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `int`

### `GetGoldValue(Rarity, int)`

```csharp
public static int GetGoldValue(Rarity rarity, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `quality` | `int` |  |

**Returns:** `int`

### `GetMergedQuality(int, int)`

```csharp
public static int GetMergedQuality(int a, int b)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `int` |  |
| `b` | `int` |  |

**Returns:** `int`

### `GetQualityType(float)`

```csharp
public static Gem.QualityType GetQualityType(float quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `quality` | `float` |  |

**Returns:** `Gem.QualityType`

### `GetSellGold()`

```csharp
public int GetSellGold()
```

**Returns:** `int`

### `GetSellGold(Rarity, int)`

```csharp
public static int GetSellGold(Rarity rarity, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `rarity` | [`Rarity`](/api/Global.Rarity) |  |
| `quality` | `int` |  |

**Returns:** `int`

### `GetValue(ScalingValue)`

Gets value of the given scaling value using this gem's level and caster.

```csharp
public float GetValue(ScalingValue val)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `val` | [`ScalingValue`](/api/Global.ScalingValue) |  |

**Returns:** `float`

### `IsLockedFor(DewPlayer)`

```csharp
public bool IsLockedFor(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `bool`

### `IsReady()`

Is this gem ready? By default this checks if the gem is cooled down and has at least 1 use left (rate-limit).This must return the same value everywhere(server/clients) for consistent behavior.

```csharp
public virtual bool IsReady()
```

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `NotifyUse()`

Flash this gem in UI for highlighting or giving attention to player.If this gem is rate-limited, it will decrement remaining use.

```csharp
public void NotifyUse()
```

### `OnCastComplete(EventInfoCast)`

Called on server when equipped skill completes casting.

```csharp
protected virtual void OnCastComplete(EventInfoCast info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

### `OnCastCompleteBeforePrepare(EventInfoCast)`

Called on server when equipped skill creates ability instance before it is spawned and prepared.

```csharp
protected virtual void OnCastCompleteBeforePrepare(EventInfoCast info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

### `OnDealDamage(EventInfoDamage)`

Called on server when equipped skill deals damage.

```csharp
protected virtual void OnDealDamage(EventInfoDamage info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoDamage`](/api/Global.EventInfoDamage) |  |

### `OnDoHeal(EventInfoHeal)`

Called on server when equipped skill does heal.

```csharp
protected virtual void OnDoHeal(EventInfoHeal obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | [`EventInfoHeal`](/api/Global.EventInfoHeal) |  |

### `OnEquipGem(Hero)`

Called everywhere when this gem is picked up by hero.

```csharp
public virtual void OnEquipGem(Hero newOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newOwner` | [`Hero`](/api/Global.Hero) |  |

### `OnEquipSkill(SkillTrigger)`

Called everywhere when this gem starts taking effect on skill.

```csharp
public virtual void OnEquipSkill(SkillTrigger newSkill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `newSkill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

### `OnPrepare()`

```csharp
protected override void OnPrepare()
```

### `OnQualityChange(int, int)`

Called everywhere when this gem's quality is changed.

```csharp
protected virtual void OnQualityChange(int oldQuality, int newQuality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldQuality` | `int` |  |
| `newQuality` | `int` |  |

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnUnequipGem(Hero)`

Called everywhere when this gem is dropped by hero.

```csharp
public virtual void OnUnequipGem(Hero oldOwner)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldOwner` | [`Hero`](/api/Global.Hero) |  |

### `OnUnequipSkill(SkillTrigger)`

Called everywhere when this gem stops taking effect on skill.

```csharp
public virtual void OnUnequipSkill(SkillTrigger oldSkill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldSkill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

### `ResetCooldown()`

```csharp
public void ResetCooldown()
```

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

### `StartCooldown()`

```csharp
public void StartCooldown()
```
