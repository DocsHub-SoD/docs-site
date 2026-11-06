# Class: DamageInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DashAttackInstance](/api/Global.DashAttackInstance) → [InstantDamageInstance](/api/Global.InstantDamageInstance) → [TickDamageInstance](/api/Global.TickDamageInstance)

```csharp
public abstract class DamageInstance : AbilityInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`applyElemental`** | `public bool applyElemental` |  |
| **`attackEffect`** | `public float attackEffect` |  |
| **`attackEffectType`** | `[ShowIf("@attackEffect > 0.001f", true)] public AttackEffectType attackEffectType` |  |
| **`cancelIfCasterDead`** | `public bool cancelIfCasterDead` |  |
| **`closeEnemyDistanceThreshold`** | `public float closeEnemyDistanceThreshold` |  |
| **`closeEnemyMultiplier`** | `public float closeEnemyMultiplier` |  |
| **`cooldownTime`** | `[ShowIf("_isCooldownCheck", true)] public float cooldownTime` |  |
| **`destroyWhenDone`** | `public bool destroyWhenDone` |  |
| **`dmgFactor`** | `public ScalingValue dmgFactor` |  |
| **`doKnockback`** | `public bool doKnockback` |  |
| **`duplicateCheck`** | `public DamageInstance.DuplicateCheckType duplicateCheck` |  |
| **`elemental`** | `[ShowIf("applyElemental", true)] public ElementalType elemental` |  |
| **`elementalChance`** | `[ShowIf("applyElemental", true)] public float elementalChance` |  |
| **`forceMergeNumbers`** | `public bool forceMergeNumbers` |  |
| **`heroDamageMultiplier`** | `public float heroDamageMultiplier` |  |
| **`hitEffect`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] public GameObject hitEffect` |  |
| **`hittable`** | `public AbilityTargetValidator hittable` |  |
| **`isDamageOverTime`** | `public bool isDamageOverTime` |  |
| **`knockbackSettings`** | `[ShowIf("doKnockback", true)] [InlineProperty] [HideLabel] public Knockback knockbackSettings` |  |
| **`knockupAmount`** | `[Title("Extras", null, TitleAlignments.Left, true, true)] public float knockupAmount` |  |
| **`mainEffect`** | `[LabelText("Main Effect (Obsolete, Use Start Effect)")] [HideIf("@mainEffect == null", true)] public GameObject mainEffect` |  |
| **`monsterDamageMultiplier`** | `public float monsterDamageMultiplier` |  |
| **`multiplyDamageByMaxHp`** | `public bool multiplyDamageByMaxHp` |  |
| **`onHit`** | `public SafeAction<Entity> onHit` |  |
| **`origin`** | `public DamageInstance.OriginType origin` |  |
| **`procCoefficient`** | `public float procCoefficient` |  |
| **`range`** | `[Title("General", null, TitleAlignments.Left, true, true)] public DewCollider range` |  |
| **`strengthMultiplier`** | `public float strengthMultiplier` | Affects damage amount, knockup amount and proc coefficient. |
| **`type`** | `[Title("Damage", null, TitleAlignments.Left, true, true)] public DamageData.SourceType type` |  |
| **`useDirectionOfCast`** | `[ShowIf("doKnockback", true)] public bool useDirectionOfCast` |  |

## Methods

### `AddToDuplicateTracker(Entity)`

```csharp
protected void AddToDuplicateTracker(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

### `CheckShouldBeDestroyed()`

```csharp
protected bool CheckShouldBeDestroyed()
```

**Returns:** `bool`

### `DoCollisionChecks()`

Can be called multiple times. Duplicates will be excluded.

```csharp
protected void DoCollisionChecks()
```

### `IsDuplicate(Entity)`

```csharp
protected bool IsDuplicate(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `OnBeforeDispatchDamage(ref DamageData, Entity)`

Called on server to process damage before applying it.

```csharp
protected virtual void OnBeforeDispatchDamage(ref DamageData dmg, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dmg` | [`DamageData`](/api/Global.DamageData) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

### `OnCollisionCheck()`

```csharp
protected virtual void OnCollisionCheck()
```

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnHit(Entity)`

Called on server when this instance hits an entity.

```csharp
protected virtual void OnHit(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

### `OnValidateTarget(Entity)`

Called on server to validate hits on entity. Return false here to ignore certain hit on an entity.

```csharp
protected virtual bool OnValidateTarget(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `ShouldUseDefaultAbilityTargetValidator()`

```csharp
protected virtual bool ShouldUseDefaultAbilityTargetValidator()
```

**Returns:** `bool`
