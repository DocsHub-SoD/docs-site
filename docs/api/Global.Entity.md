# Class: Entity

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Hero](/api/Global.Hero) → [MockEntity](/api/Global.MockEntity) → [Monster](/api/Global.Monster) → [PropEntity](/api/Global.PropEntity) → [Summon](/api/Global.Summon)

```csharp
[LogicUpdatePriority(-400)]
[RequireComponent(typeof(EntityAI))]
[RequireComponent(typeof(EntityAnimation))]
[RequireComponent(typeof(EntityControl))]
[RequireComponent(typeof(EntityStatus))]
[RequireComponent(typeof(EntityVisual))]
[RequireComponent(typeof(EntityAbility))]
[RequireComponent(typeof(EntitySound))]
public class Entity : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEntityEvent_OnIsSleepingChanged`** | `public SafeAction<bool> ClientEntityEvent_OnIsSleepingChanged` |  |
| **`ClientEntityEvent_OnStatusEffectAdded`** | `public SafeAction<EventInfoStatusEffect> ClientEntityEvent_OnStatusEffectAdded` |  |
| **`ClientEntityEvent_OnStatusEffectRemoved`** | `public SafeAction<EventInfoStatusEffect> ClientEntityEvent_OnStatusEffectRemoved` |  |
| **`EntityEvent_OnAttackDodged`** | `public SafeAction<EventInfoAttackMissed> EntityEvent_OnAttackDodged` |  |
| **`EntityEvent_OnAttackEffectTriggered`** | `public SafeAction<EventInfoAttackEffect> EntityEvent_OnAttackEffectTriggered` |  |
| **`EntityEvent_OnAttackFired`** | `public SafeAction<EventInfoAttackFired> EntityEvent_OnAttackFired` |  |
| **`EntityEvent_OnAttackFiredBeforePrepare`** | `public SafeAction<EventInfoAttackFired> EntityEvent_OnAttackFiredBeforePrepare` |  |
| **`EntityEvent_OnAttackHit`** | `public SafeAction<EventInfoAttackHit> EntityEvent_OnAttackHit` |  |
| **`EntityEvent_OnAttackMissed`** | `public SafeAction<EventInfoAttackMissed> EntityEvent_OnAttackMissed` |  |
| **`EntityEvent_OnAttackTaken`** | `public SafeAction<EventInfoAttackHit> EntityEvent_OnAttackTaken` |  |
| **`EntityEvent_OnCastComplete`** | `public SafeAction<EventInfoCast> EntityEvent_OnCastComplete` |  |
| **`EntityEvent_OnCastCompleteBeforePrepare`** | `public SafeAction<EventInfoCast> EntityEvent_OnCastCompleteBeforePrepare` |  |
| **`EntityEvent_OnDamageNegatedByImmunity`** | `public SafeAction<EventInfoDamageNegatedByImmunity> EntityEvent_OnDamageNegatedByImmunity` |  |
| **`EntityEvent_OnDamageNegatedByShield`** | `public SafeAction<EventInfoDamageNegatedByShield> EntityEvent_OnDamageNegatedByShield` |  |
| **`EntityEvent_OnDeath`** | `public SafeAction<EventInfoKill> EntityEvent_OnDeath` |  |
| **`EntityEvent_OnGetManaSpent`** | `public SafeAction<EventInfoSpentMana> EntityEvent_OnGetManaSpent` |  |
| **`EntityEvent_OnTakeDamage`** | `public SafeAction<EventInfoDamage> EntityEvent_OnTakeDamage` |  |
| **`EntityEvent_OnTakeHeal`** | `public SafeAction<EventInfoHeal> EntityEvent_OnTakeHeal` |  |
| **`EntityEvent_OnTakeManaHeal`** | `public SafeAction<EventInfoHeal> EntityEvent_OnTakeManaHeal` |  |
| **`EntityEvent_OnTakeShield`** | `public SafeAction<EventInfoShield> EntityEvent_OnTakeShield` |  |
| **`takenDamageProcessor`** | `public DataProcessorGroup<DamageData, Actor, Entity> takenDamageProcessor` | Processor for all received damages (Except pure damage). This is only valid on server. |
| **`takenHealProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> takenHealProcessor` | Processor for received heals. This is only valid on server. |
| **`takenManaHealProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> takenManaHealProcessor` | Processor for received mana heals. This is only valid on server. |
| **`takenShieldProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> takenShieldProcessor` | Processor for received shields. This is only valid on server. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`Ability`** | `public EntityAbility Ability { get; }` |  |
| **`agentPosition`** | `public Vector3 agentPosition { get; }` |  |
| **`AI`** | `public EntityAI AI { get; }` |  |
| **`Animation`** | `public EntityAnimation Animation { get; }` |  |
| **`Control`** | `public EntityControl Control { get; }` |  |
| **`currentHealth`** | `public float currentHealth { get; }` |  |
| **`currentMana`** | `public float currentMana { get; }` |  |
| **`defaultOwner`** | `protected virtual DewPlayer defaultOwner { get; }` |  |
| **`isAlive`** | `public bool isAlive { get; }` |  |
| **`isDead`** | `public bool isDead { get; }` |  |
| **`isSleeping`** | `public bool isSleeping { get; }` |  |
| **`lastSection`** | `public RoomSection lastSection { get; }` | Section that this entity resided in. Even though an entity leaves a section, this variable will not be cleared.Available on server. Can be null. |
| **`level`** | `public int level { get; }` |  |
| **`maxHealth`** | `public float maxHealth { get; }` |  |
| **`maxMana`** | `public float maxMana { get; }` |  |
| **`normalizedHealth`** | `public float normalizedHealth { get; }` |  |
| **`normalizedMana`** | `public float normalizedMana { get; }` |  |
| **`owner`** | `[SaveVar(SaveVarFlags.Default)] public DewPlayer owner { get; set; }` |  |
| **`section`** | `public RoomSection section { get; }` | Section that this entity resides in. Available on server.Can be null. |
| **`Sound`** | `public EntitySound Sound { get; }` |  |
| **`Status`** | `public EntityStatus Status { get; }` |  |
| **`Visual`** | `public EntityVisual Visual { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `AIUpdate(ref EntityAIContext)`

AI update will not fire if entity is channeling an ability.

```csharp
protected virtual void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `CanAggroTo(Entity)`

```csharp
public virtual bool CanAggroTo(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `CheckEnemyOrNeutral(Entity)`

```csharp
public bool CheckEnemyOrNeutral(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `GetActorReadableName()`

```csharp
public override string GetActorReadableName()
```

**Returns:** `string`

### `GetNetworkAuthorityConnection()`

```csharp
protected override NetworkConnectionToClient GetNetworkAuthorityConnection()
```

**Returns:** `Mirror.NetworkConnectionToClient`

### `GetRelation(Entity)`

```csharp
public EntityRelation GetRelation(Entity other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `EntityRelation`

### `GetStaggerSettings()`

```csharp
protected virtual Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

### `GetTeamRelation(DewPlayer)`

```csharp
public TeamRelation GetTeamRelation(DewPlayer other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `TeamRelation`

### `Kill()`

Kill this entity. Note this can be prevented by death interrupts.

```csharp
public void Kill()
```

### `KillNoInterrupt()`

Kill this entity ignoring any death interrupts.

```csharp
public void KillNoInterrupt()
```

### `LoadEntityModelLocal()`

```csharp
public virtual void LoadEntityModelLocal()
```

### `OnDeath(EventInfoKill)`

Called everywhere when this entity dies.

```csharp
protected virtual void OnDeath(EventInfoKill info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoKill`](/api/Global.EventInfoKill) |  |

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnDrawGizmos()`

```csharp
protected virtual void OnDrawGizmos()
```

### `OnModelLoaded()`

```csharp
public virtual void OnModelLoaded()
```

### `OnPrepare()`

```csharp
protected override void OnPrepare()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `ProcessReceivedDamage(ref DamageData, Actor)`

Process the given damage with this entity's received damage preprocessors.

```csharp
public void ProcessReceivedDamage(ref DamageData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DamageData`](/api/Global.DamageData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

### `ProcessReceivedHeal(ref HealData, Actor)`

Process the given heal with this entity's received heal preprocessors.

```csharp
public void ProcessReceivedHeal(ref HealData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`HealData`](/api/Global.HealData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

### `ProcessReceivedManaHeal(ref HealData, Actor)`

Process the given mana heal with this entity's received mana heal preprocessors.

```csharp
public void ProcessReceivedManaHeal(ref HealData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`HealData`](/api/Global.HealData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

### `ProcessReceivedShield(ref HealData, Actor)`

```csharp
public void ProcessReceivedShield(ref HealData data, Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`HealData`](/api/Global.HealData) |  |
| `actor` | [`Actor`](/api/Global.Actor) |  |

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

### `Sleep()`

Make this entity sleep.

```csharp
public void Sleep()
```

### `Stagger(Vector3?)`

```csharp
public void Stagger(Vector3? dir)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dir` | `UnityEngine.Vector3?` |  |

### `WakeUp()`

Wake this entity up.

```csharp
public void WakeUp()
```
