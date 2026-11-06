# Class: Actor

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[SelectionBase] [DewResourceLink]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [AbilityInstance](/api/Global.AbilityInstance) → [AbilityTrigger](/api/Global.AbilityTrigger) → [Artifact](/api/Global.Artifact) → [Entity](/api/Global.Entity) → [GameEffect](/api/Global.GameEffect) → [Gem](/api/Global.Gem) → [Rift](/api/Global.Rift) → [Room_Trap_Toggleable](/api/Global.Room_Trap_Toggleable) → [RoomModifierBase](/api/Global.RoomModifierBase) → [ServerActor](/api/Global.ServerActor) → [Shrine](/api/Global.Shrine) → [Treasure](/api/Global.Treasure)

```csharp
[SelectionBase]
[DewResourceLink(ResourceLinkBy.Type)]
public class Actor : DewNetworkBehaviour, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (28)

::: details Click to expand Fields (28)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ActorEvent_OnAbilityInstanceBeforePrepare`** | `public SafeAction<EventInfoAbilityInstance> ActorEvent_OnAbilityInstanceBeforePrepare` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnAbilityInstanceCreated`** | `public SafeAction<EventInfoAbilityInstance> ActorEvent_OnAbilityInstanceCreated` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnApplyElemental`** | `public SafeAction<EventInfoApplyElemental> ActorEvent_OnApplyElemental` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnAttackEffectTriggered`** | `public SafeAction<EventInfoAttackEffect> ActorEvent_OnAttackEffectTriggered` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnAttackHit`** | `public SafeAction<EventInfoAttackHit> ActorEvent_OnAttackHit` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnDealDamage`** | `public SafeAction<EventInfoDamage> ActorEvent_OnDealDamage` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnDoHeal`** | `public SafeAction<EventInfoHeal> ActorEvent_OnDoHeal` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnDoManaHeal`** | `public SafeAction<EventInfoHeal> ActorEvent_OnDoManaHeal` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnGiveShield`** | `public SafeAction<EventInfoShield> ActorEvent_OnGiveShield` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnKill`** | `public SafeAction<EventInfoKill> ActorEvent_OnKill` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnSpawnSummon`** | `public SafeAction<EventInfoSummon> ActorEvent_OnSpawnSummon` | Note that ActorEvents can also be from its descendants. |
| **`ActorEvent_OnSpendMana`** | `public SafeAction<EventInfoSpentMana> ActorEvent_OnSpendMana` | Note that ActorEvents can also be from its descendants. |
| **`children`** | `public readonly List<Actor> children` | Alive, non-destroyed children actors. |
| **`childrenInNetwork`** | `public readonly List<Actor> childrenInNetwork` | Children that are alive, or not yet despawned from the network. |
| **`ClientActorEvent_OnCreate`** | `public SafeAction<Actor> ClientActorEvent_OnCreate` | Called everywhere when an actor is created including child actors. |
| **`ClientActorEvent_OnDestroyed`** | `public SafeAction<Actor> ClientActorEvent_OnDestroyed` | Called everywhere when this actor is destroyed. |
| **`ClientEvent_OnPersistentSyncedDataChanged`** | `public SafeAction<string> ClientEvent_OnPersistentSyncedDataChanged` |  |
| **`dealtCooldownReductionByRatioProcessor`** | `public DataProcessorGroup<CooldownReductionByRatioSettings, Actor, AbilityTrigger> dealtCooldownReductionByRatioProcessor` | Processor for dealt cooldown reductions by ratio. This is only valid on server.All cooldown reductions done by this actor will be processed by this and every ancestor's preprocessors. |
| **`dealtCooldownReductionProcessor`** | `public DataProcessorGroup<CooldownReductionSettings, Actor, AbilityTrigger> dealtCooldownReductionProcessor` | Processor for dealt cooldown reductions of fixed amount. This is only valid on server.All cooldown reductions done by this actor will be processed by this and every ancestor's preprocessors. |
| **`dealtDamageProcessor`** | `public DataProcessorGroup<DamageData, Actor, Entity> dealtDamageProcessor` | Processor for all dealt damages (Except pure damage). This is only valid on server.All damages from this actor will be processed by this and every ancestors' preprocessors. |
| **`dealtHealProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> dealtHealProcessor` | Processor for dealt heals. This is only valid on server.All heals from this actor will be processed by this and every ancestors' preprocessors. |
| **`dealtManaHealProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> dealtManaHealProcessor` | Processor for dealt mana heals. This is only valid on server.All mana heals from this actor will be processed by this and every ancestors' preprocessors. |
| **`dealtShieldProcessor`** | `public DataProcessorGroup<HealData, Actor, Entity> dealtShieldProcessor` | Processor for received shields. This is only valid on server. |
| **`KilledByUnstoppableEffects`** | `public static Type[] KilledByUnstoppableEffects` |  |
| **`persistentData`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly Dictionary<string, string> persistentData` | Available on server. Generic persistent data storage that will be saved and loaded with this actor. |
| **`persistentSyncedData`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncDictionary<string, string> persistentSyncedData` | Available everywhere, and can only be set on server. Generic persistent synced data storage that will be saved and loaded with this actor, and be synced across the network.Use this to store states in the network context. (think: synced variables) |
| **`ScaleDurationByTenacityEffects`** | `public static Type[] ScaleDurationByTenacityEffects` |  |
| **`spawnedChildVarDefProcessor`** | `public DataProcessorGroup<VariantDef, Actor, Type> spawnedChildVarDefProcessor` |  |

:::

## Properties (15)

::: details Click to expand Properties (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ancestors`** | `public IEnumerable<Actor> ancestors { get; }` | Enumerable ancestors of this actor. Ordering is the same as the actor tree order, first element being the direct parent. |
| **`chainTempName`** | `public ReactionChain chainTempName { get; }` | Reaction chain of this actor. Available only on server. |
| **`creationTime`** | `public float creationTime { get; }` | Time of this actor's creation byTime.time. |
| **`firstEntity`** | `public Entity firstEntity { get; }` | The first entity in this actor's ancestor tree.This property can be used to e.g. find the caster of an ability instance. |
| **`firstTrigger`** | `public AbilityTrigger firstTrigger { get; }` | The first ability trigger in this actor's ancestor tree.This property can be used to e.g. find the ability instance's trigger. |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`isDestroyed`** | `public bool isDestroyed { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public virtual bool isDestroyedOnRoomChange { get; }` |  |
| **`isDestroyLocked`** | `public bool isDestroyLocked { get; }` | Is someone preventing this actor from being destroyed? Available only on server. |
| **`isNewInstance`** | `public bool isNewInstance { get; }` | Is it this actor created in this session of the game, or has been loaded from save?e.g. This will be false if this actor is part of a loaded game, or from previously visited node. |
| **`parentActor`** | `public Actor parentActor { get; set; }` |  |
| **`parentActorNetId`** | `public uint parentActorNetId { get; }` |  |
| **`persistentNetId`** | `public uint persistentNetId { get; }` | Mirror setsnetIdto 0 on despawn. This property will tell you its former netId even after being despawned. |
| **`position`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public Vector3 position { get; set; }` | Position of this actor. Same astransform.position. |
| **`rotation`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public Quaternion rotation { get; set; }` | Rotation of this actor. Same astransform.rotation. |

:::

## Methods (92)

::: details `ActiveFrameUpdate()`

Called everywhere every frame while this actor is active.

```csharp
protected virtual void ActiveFrameUpdate()
```

:::

::: details `ActiveLogicUpdate(float)`

Called everywhere every logic tick while this actor is active.

```csharp
protected virtual void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `AddData&lt;T&gt;(T)`

```csharp
public void AddData<T>(T data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `T` |  |
| `` | `T` |  |

:::

::: details `ApplyCooldownReduction(AbilityTrigger, CooldownReductionSettings)`

Apply cooldown reduction to all configs that can receive cooldown reduction.

```csharp
public void ApplyCooldownReduction(AbilityTrigger trigger, CooldownReductionSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `settings` | [`CooldownReductionSettings`](/api/Global.CooldownReductionSettings) |  |

:::

::: details `ApplyCooldownReduction(AbilityTrigger, float, bool, bool)`

Apply cooldown reduction to all configs that can receive cooldown reduction.

```csharp
public void ApplyCooldownReduction(AbilityTrigger trigger, float amount, bool scaled = true, bool ignoreCanReceiveCooldown = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `amount` | `float` |  |
| `scaled` | `bool` |  |
| `ignoreCanReceiveCooldown` | `bool` |  |

:::

::: details `ApplyCooldownReductionByRatio(AbilityTrigger, CooldownReductionByRatioSettings)`

Apply cooldown reduction to all configs that can receive cooldown reduction by ratio of max cooldown.

```csharp
public void ApplyCooldownReductionByRatio(AbilityTrigger trigger, CooldownReductionByRatioSettings settings)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `settings` | [`CooldownReductionByRatioSettings`](/api/Global.CooldownReductionByRatioSettings) |  |

:::

::: details `ApplyCooldownReductionByRatio(AbilityTrigger, float, bool)`

Apply cooldown reduction to all configs that can receive cooldown reduction by ratio of max cooldown.

```csharp
public void ApplyCooldownReductionByRatio(AbilityTrigger trigger, float ratio, bool ignoreCanReceiveCooldown = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `ratio` | `float` |  |
| `ignoreCanReceiveCooldown` | `bool` |  |

:::

::: details `ApplyElemental(ElementalType, Entity, int)`

```csharp
public ElementalStatusEffect ApplyElemental(ElementalType type, Entity to, int appliedStacks = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a> |  |
| `to` | [`Entity`](/api/Global.Entity) |  |
| `appliedStacks` | `int` |  |

**Returns:** `ElementalStatusEffect`

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `ClearExcludeFromRoomSave()`

Clear flag that excludes this actor from room save.Note this won't make non-saving by default actors to be saved.

```csharp
public void ClearExcludeFromRoomSave()
```

:::

::: details `CreateAbilityInstance(Type, Vector3, Quaternion?, CastInfo, Action&lt;AbilityInstance&gt;)`

```csharp
public AbilityInstance CreateAbilityInstance(Type type, Vector3 position, Quaternion? rotation, CastInfo info, Action<AbilityInstance> beforePrepare = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | [`System.Action<T><AbilityInstance>`](/api/Global.AbilityInstance) |  |

**Returns:** `AbilityInstance`

:::

::: details `CreateAbilityInstance&lt;T&gt;(T, Vector3, Quaternion?, CastInfo, Action&lt;T&gt;)`

```csharp
public T CreateAbilityInstance<T>(T prefab, Vector3 position, Quaternion? rotation, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateAbilityInstance&lt;T&gt;(Vector3, Quaternion?, CastInfo, Action&lt;T&gt;)`

```csharp
public T CreateAbilityInstance<T>(Vector3 position, Quaternion? rotation, CastInfo info, Action<T> beforePrepare = null) where T : AbilityInstance
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateActor&lt;T&gt;(T, Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public T CreateActor<T>(T prefab, Vector3 pos, Quaternion? rot, Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion?` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateActor&lt;T&gt;(Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public T CreateActor<T>(Vector3 pos, Quaternion? rot, Action<T> beforePrepare = null) where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion?` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateBasicEffect(Entity, BasicEffect, float, string, DuplicateEffectBehavior)`

Create a generic container status effect for applying basic effect to an entity.Give an id of null to prevent this behavior.The created status effect will be cleansable and killed by unstoppable if it contains a harmful effect.

```csharp
public Se_GenericEffectContainer CreateBasicEffect(Entity victim, BasicEffect eff, float duration, string id = null, DuplicateEffectBehavior onDuplicate = DuplicateEffectBehavior.ReplacePrevious)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `eff` | [`BasicEffect`](/api/Global.BasicEffect) |  |
| `duration` | `float` |  |
| `id` | `string` |  |
| `onDuplicate` | <a href="/enums#duplicateeffectbehavior" class="enum-link" data-tooltip="UsePrevious=0 · ReplacePrevious=1 · DoNothing=2">DuplicateEffectBehavior</a> |  |

**Returns:** `Se_GenericEffectContainer`

:::

::: details `CreateDamage(SourceType, float, float)`

```csharp
public DamageData CreateDamage(DamageData.SourceType type, float amount, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`DamageData.SourceType`](/api/Global.DamageData) |  |
| `amount` | `float` |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `CreateStatusEffect(Type, Entity, CastInfo, Action&lt;StatusEffect&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public StatusEffect CreateStatusEffect(Type type, Entity victim, CastInfo info, Action<StatusEffect> beforePrepare = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | [`System.Action<T><StatusEffect>`](/api/Global.StatusEffect) |  |

**Returns:** `StatusEffect`

:::

::: details `CreateStatusEffect&lt;T&gt;(T, Entity, CastInfo, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public T CreateStatusEffect<T>(T prefab, Entity victim, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CreateStatusEffect&lt;T&gt;(Entity, CastInfo, Action&lt;T&gt;)`

Create a new status effect and attach it to an entity.This can return null if the creation fails:e.g. Trying to apply a status effect with isKilledByUnstoppable flag to an unstoppable/invulnerable entity.

```csharp
public T CreateStatusEffect<T>(Entity victim, CastInfo info, Action<T> beforePrepare = null) where T : StatusEffect
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `CustomDestroyRoutine()`

```csharp
public void CustomDestroyRoutine()
```

:::

::: details `CustomRpc_ClearClientMessageHandlers()`

```csharp
public void CustomRpc_ClearClientMessageHandlers()
```

:::

::: details `CustomRpc_ClearServerMessageHandlers()`

```csharp
public void CustomRpc_ClearServerMessageHandlers()
```

:::

::: details `CustomRpc_RegisterClientMessageHandler&lt;T&gt;(Action&lt;T&gt;)`

Register a client RPC handler. (server to clients) Registering multiple handlers for same type will result in all handlers passed being called.

```csharp
public void CustomRpc_RegisterClientMessageHandler<T>(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |
| `` | `T` |  |

:::

::: details `CustomRpc_RegisterServerMessageHandler&lt;T&gt;(Action&lt;T&gt;)`

Register a server RPC handler. (client to server) Registering multiple handlers for same type will result in all handlers passed being called.

```csharp
public void CustomRpc_RegisterServerMessageHandler<T>(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |
| `` | `T` |  |

:::

::: details `CustomRpc_RegisterServerMessageHandler&lt;T&gt;(string, Action&lt;T, DewPlayer&gt;)`

Register a server RPC handler. (client to server) Registering multiple handlers for same type will result in all handlers passed being called.This variant allows you to receive the caller client as a parameter.

```csharp
public void CustomRpc_RegisterServerMessageHandler<T>(string type, Action<T, DewPlayer> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `string` |  |
| `handler` | [`System.Action<T1, T2><T,DewPlayer>`](/api/Global.DewPlayer) |  |
| `` | `T` |  |

:::

::: details `CustomRpc_SendMessageToAllClients&lt;T&gt;(T)`

Make a remote procedure call: Server =&gt; All Clients

```csharp
public void CustomRpc_SendMessageToAllClients<T>(T msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | `T` |  |
| `` | `T` |  |

:::

::: details `CustomRpc_SendMessageToClient&lt;T&gt;(DewPlayer, T)`

Make a remote procedure call: Server =&gt; Specific Client

```csharp
public void CustomRpc_SendMessageToClient<T>(DewPlayer target, T msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `msg` | `T` |  |
| `` | `T` |  |

:::

::: details `CustomRpc_SendMessageToServer&lt;T&gt;(T)`

Make a remote procedure call: Client =&gt; ServerHosts can also make use of this RPC.

```csharp
public void CustomRpc_SendMessageToServer<T>(T msg)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `msg` | `T` |  |
| `` | `T` |  |

:::

::: details `CustomRpc_UnregisterClientMessageHandler&lt;T&gt;()`

```csharp
public void CustomRpc_UnregisterClientMessageHandler<T>()
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

:::

::: details `CustomRpc_UnregisterClientMessageHandler&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public void CustomRpc_UnregisterClientMessageHandler<T>(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |
| `` | `T` |  |

:::

::: details `CustomRpc_UnregisterServerMessageHandler&lt;T&gt;()`

```csharp
public void CustomRpc_UnregisterServerMessageHandler<T>()
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

:::

::: details `CustomRpc_UnregisterServerMessageHandler&lt;T&gt;(Action&lt;T, DewPlayer&gt;)`

```csharp
public void CustomRpc_UnregisterServerMessageHandler<T>(Action<T, DewPlayer> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | [`System.Action<T1, T2><T,DewPlayer>`](/api/Global.DewPlayer) |  |
| `` | `T` |  |

:::

::: details `CustomRpc_UnregisterServerMessageHandler&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public void CustomRpc_UnregisterServerMessageHandler<T>(Action<T> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T>` |  |
| `` | `T` |  |

:::

::: details `DealDamage(DamageData, Entity, ReactionChain)`

Deal custom damage to the target entity.

```csharp
public void DealDamage(DamageData damage, Entity target, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `damage` | [`DamageData`](/api/Global.DamageData) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

:::

::: details `DefaultDamage(float, float)`

```csharp
public DamageData DefaultDamage(float amount, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `Destroy()`

Destroy this actor.It will do its own cleanups on server and then despawn.This is irreversible.

```csharp
public void Destroy()
```

:::

::: details `DestroyIfActive()`

```csharp
public void DestroyIfActive()
```

:::

::: details `DoBasicAttackHit(Entity, bool, bool, float, float)`

Make the parent entity do basic attack and deal damage to the target entity.By design this should be only used by basic attacks.This triggers Attack Effects if the hit was successful.

```csharp
public void DoBasicAttackHit(Entity target, bool isCriticalHit, bool isMain, float damage, float attackEffect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `isCriticalHit` | `bool` |  |
| `isMain` | `bool` |  |
| `damage` | `float` |  |
| `attackEffect` | `float` |  |

:::

::: details `DoHeal(HealData, Entity, ReactionChain)`

Heal an entity by some amount.

```csharp
public void DoHeal(HealData heal, Entity target, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heal` | [`HealData`](/api/Global.HealData) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

:::

::: details `DoManaHeal(HealData, Entity, ReactionChain)`

Grant an entity some mana.

```csharp
public void DoManaHeal(HealData heal, Entity target, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `heal` | [`HealData`](/api/Global.HealData) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

:::

::: details `ExcludeFromRoomSave()`

Mark this actor as excluded from room save.

```csharp
public void ExcludeFromRoomSave()
```

:::

::: details `FindData&lt;T&gt;(Predicate&lt;T&gt;)`

```csharp
public T FindData<T>(Predicate<T> predicate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `predicate` | `System.Predicate<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `FindFirstAncestorOfType&lt;T&gt;()`

Find first actor that matches the given type in this actor's ancestor tree.

```csharp
public T FindFirstAncestorOfType<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `FindFirstOfType&lt;T&gt;()`

Find first actor that matches the given type in this actor's ancestor tree including itself.

```csharp
public T FindFirstOfType<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetActorReadableName()`

```csharp
public virtual string GetActorReadableName()
```

**Returns:** `string`

:::

::: details `GetData&lt;T&gt;()`

```csharp
public T GetData<T>()
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetNetworkAuthorityConnection()`

```csharp
protected virtual NetworkConnectionToClient GetNetworkAuthorityConnection()
```

**Returns:** `Mirror.NetworkConnectionToClient`

:::

::: details `GetOriginalName()`

Get the original name of this actor, excluding (Clone) or variant suffixes.Useful when trying to figure out id of name-linked resources.

```csharp
public string GetOriginalName()
```

**Returns:** `string`

:::

::: details `GiveShield(Entity, float, float, bool, ReactionChain)`

```csharp
public Se_GenericShield_OneShot GiveShield(Entity victim, float amount, float duration, bool isDecay = false, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `victim` | [`Entity`](/api/Global.Entity) |  |
| `amount` | `float` |  |
| `duration` | `float` |  |
| `isDecay` | `bool` |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

**Returns:** `Se_GenericShield_OneShot`

:::

::: details `HasData&lt;T&gt;()`

```csharp
public bool HasData<T>()
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `Heal(float)`

```csharp
public HealData Heal(float amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |

**Returns:** `HealData`

:::

::: details `HideOnScreenTimerLocally(OnScreenTimerHandle)`

```csharp
public void HideOnScreenTimerLocally(OnScreenTimerHandle handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [`OnScreenTimerHandle`](/api/Global.OnScreenTimerHandle) |  |

:::

::: details `IsDescendantOf(Actor)`

Is this actor a descendant of the given actor?Is the given actor this actor's ancestor (parent/grand-parent/grand-grand-parent...)?

```csharp
public bool IsDescendantOf(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `bool`

:::

::: details `IsDescendantOf&lt;T&gt;()`

Is this actor a descendant of the given actor?Is the given actor this actor's ancestor (parent/grand-parent/grand-grand-parent...)?

```csharp
public bool IsDescendantOf<T>() where T : Actor
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `IsExcludedFromRoomSave()`

Is this actor marked as excluded from room saves?

```csharp
public bool IsExcludedFromRoomSave()
```

**Returns:** `bool`

:::

::: details `LockDestroy()`

Prevent this actor from being destroyed. You MUST call UnlockDestroy() after LockDestroy() call.

```csharp
public void LockDestroy()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `MagicDamage(float, float)`

```csharp
public DamageData MagicDamage(float amount, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `OnCreate()`

Called everywhere when this actor is created.

```csharp
protected virtual void OnCreate()
```

:::

::: details `OnCreate_ActorData()`

```csharp
public void OnCreate_ActorData()
```

:::

::: details `OnDestroyActor()`

Called everywhere when this actor is being destroyed.
This is different from similarly-named Unity event OnDestroy, as it is called before GameObject itself gets destroyed.

```csharp
protected virtual void OnDestroyActor()
```

:::

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected virtual void OnEnable()
```

:::

::: details `OnPrepare()`

Called on server right before actor is spawned.
Configure this actor's initial state here.

```csharp
protected virtual void OnPrepare()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopClient()`

```csharp
public override void OnStopClient()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `PhysicalDamage(float, float)`

```csharp
public DamageData PhysicalDamage(float amount, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `ProcessShieldAmount(float, Entity)`

```csharp
public float ProcessShieldAmount(float amount, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `float`

:::

::: details `ProcessSpawnedChildVarDefProcessor(ref VariantDef, Type)`

```csharp
public void ProcessSpawnedChildVarDefProcessor(ref VariantDef data, Type childType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`VariantDef`](/api/Global.VariantDef) |  |
| `childType` | `System.Type` |  |

:::

::: details `PureDamage(float, float)`

```csharp
public DamageData PureDamage(float amount, float procCoefficient = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `procCoefficient` | `float` |  |

**Returns:** `DamageData`

:::

::: details `RefundMana(float, Entity)`

Refund a certain amount of mana to an entity.This will not be processed, will not proc any callbacks nor display a mana heal number text.This shouldn't be used anywhere other than for canceled channels.

```csharp
public void RefundMana(float amount, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `RemoveData(object)`

```csharp
public bool RemoveData(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `RemoveData&lt;T&gt;()`

```csharp
public bool RemoveData<T>()
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `ResetCooldown(AbilityTrigger, bool)`

```csharp
public void ResetCooldown(AbilityTrigger trigger, bool ignoreCanReceiveCooldown = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `ignoreCanReceiveCooldown` | `bool` |  |

:::

::: details `ShouldBeSavedWithRoom()`

Should this actor be saved and loaded back in when revisiting nodes?This is checked on server on all active actors when changing rooms.

```csharp
public virtual bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::

::: details `ShowOnScreenTimerLocally(OnScreenTimerHandle)`

Show an on-screen timer with custom fill amount to local player.Null rawText will be automatically populated.

```csharp
public OnScreenTimerHandle ShowOnScreenTimerLocally(OnScreenTimerHandle handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | [`OnScreenTimerHandle`](/api/Global.OnScreenTimerHandle) |  |

**Returns:** `OnScreenTimerHandle`

:::

::: details `SpawnEntity&lt;T&gt;(T, Vector3, Quaternion?, DewPlayer, int, Action&lt;T&gt;)`

```csharp
public T SpawnEntity<T>(T entity, Vector3 pos, Quaternion? rot, DewPlayer owner, int level, Action<T> beforeSpawn = null) where T : Entity
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | `T` |  |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion?` |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SpawnEntity&lt;T&gt;(Vector3, Quaternion?, DewPlayer, int, Action&lt;T&gt;)`

```csharp
public T SpawnEntity<T>(Vector3 pos, Quaternion? rot, DewPlayer owner, int level, Action<T> beforeSpawn = null) where T : Entity
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |
| `rot` | `UnityEngine.Quaternion?` |  |
| `owner` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `level` | `int` |  |
| `beforeSpawn` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SpawnSummon&lt;T&gt;(Vector3, Quaternion?, Action&lt;T&gt;)`

```csharp
public T SpawnSummon<T>(Vector3 position, Quaternion? rotation, Action<T> beforePrepare = null) where T : Summon
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `SpendMana(float, Entity)`

Spend mana of the entity.

```csharp
public void SpendMana(float amount, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `float` |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `Teleport(Entity, Vector3)`

Teleport an entity to the targeted position.You should only feed in a valid position by usingDew.GetValidAgentPosition()beforehand.

```csharp
public void Teleport(Entity entity, Vector3 position)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::

::: details `TrackKills(float, Action&lt;EventInfoKill&gt;)`

Report any kills with contribution of this actor's damage with given grace period.You must Stop() the tracker to properly dispose it.

```csharp
public KillTracker TrackKills(float gracePeriod, Action<EventInfoKill> callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gracePeriod` | `float` |  |
| `callback` | [`System.Action<T><EventInfoKill>`](/api/Global.EventInfoKill) |  |

**Returns:** `KillTracker`

:::

::: details `TriggerAttackEffects(Entity, float, AttackEffectType, ReactionChain)`

```csharp
public void TriggerAttackEffects(Entity target, float strength, AttackEffectType type, ReactionChain chain = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |
| `strength` | `float` |  |
| `type` | <a href="/enums#attackeffecttype" class="enum-link" data-tooltip="BasicAttackMain=0 · BasicAttackSub=1 · Others=2">AttackEffectType</a> |  |
| `chain` | [`ReactionChain`](/api/Global.ReactionChain) |  |

:::

::: details `TryFindData&lt;T&gt;(Predicate&lt;T&gt;, out T)`

```csharp
public bool TryFindData<T>(Predicate<T> predicate, out T result)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `predicate` | `System.Predicate<T>` |  |
| `result` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `TryGetData&lt;T&gt;(out T)`

```csharp
public bool TryGetData<T>(out T data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `UnlockDestroy()`

```csharp
public void UnlockDestroy()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1189)

*Classes and systems that invoke, reference, or depend on `Actor`:*

`ACH_ANGER_MANAGEMENT_PROFESSIONAL` · `ACH_BARE_SKIN_SUPREMACY` · `ACH_BLACKCAT_DEJAVU` · `ACH_BURNING_LOVE` · `ACH_CHAOTIC_GOOD` · `ACH_EMBRACE_MORTALITY` · `ACH_EMPRESS_OF_PAIN` · `ACH_LEVIATHAN_ON_LAND` · `ACH_LOYAL_CUSTOMER` · `ACH_MASTER_OF_HAMMER` · `ACH_M_M_M_MONSTER_KILL` · `ACH_NOVICE_TREASURE_HUNTER` · `ACH_NO_NEED_FOR_YOUR_HELP` · `ACH_OVERFLOWING_HEALS` · `ACH_PEW_PEW_PEW` · `ACH_PRAISE_THE_SUN` · `ACH_REACTIVATED` · `ACH_REAP_WHAT_YOU_SOW` · `ACH_SHIELD_BATTERY` · `ACH_SIBLING_FIGHT` · `ACH_SNAKE_IN_THE_GRASS` · `ACH_TASTE_OF_THEIR_OWN_MEDICINE` · `ACH_WHY_YOU_BULLY_ME` · [AbilityInstance](/api/Global.AbilityInstance) · [AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionCast](/api/Global.ActionCast) · [ActionInteract](/api/Global.ActionInteract) · [ActorCheck](/api/Global.ActorCheck) · `ActorFlags` · [ActorManager](/api/Global.ActorManager) · `ActorRef`1` · `Actor_StarlessPath_GuidingCompassSpawner` · `Ai_ArcticTerritory` · `Ai_C_BackStep_Bomb` · `Ai_C_BeamOfLight` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_DarkBolt` · `Ai_C_DarkSpear` · `Ai_C_FlashFreeze` · `Ai_C_GlacialStomp` · `Ai_C_IceClaw` · `Ai_C_MassProtection` · `Ai_C_Pew` · `Ai_C_Pew_Projectile` · `Ai_C_PressurePoint` · `Ai_C_Sneeze` · `Ai_C_SparklingWaterGun` · `Ai_C_Starfall_Projectile` · `Ai_C_SwiftSlash` · `Ai_C_Whirlwind` · `Ai_Culinary_Pickup` · `Ai_Curse_AnchorOfMind_Anchor` · `Ai_Curse_DreamAfflictionInductive_Smite` · `Ai_Curse_IntermittentExplosion_Explosion` · `Ai_D_BeautifulThreat_Feather` · `Ai_D_BurningFist_Attack` · `Ai_D_ChargedAnguillian_Lightning` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_ExplosionArtist_DodgeExplosion` · `Ai_D_ExplosionArtist_LargeExplosion` · `Ai_D_IceColdPresence_AOE` · `Ai_D_IcyVeins_Damage` · `Ai_D_ParryMaster_Parry` · `Ai_D_PrismaticEyes_Attack` · `Ai_D_QuartetOfDeath_Explosion` · `Ai_D_Resolve_Push` · `Ai_D_SalamanderPowder_Projectile` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_D_SharedPain_Instance` · `Ai_E_Aftershock_Damage` · `Ai_E_Blink_Back` · `Ai_E_ClutchesOfMalice` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_E_CrimsonLance` · `Ai_E_DoomsdayMeteor` · `Ai_E_FinalExplosion_Explosion` · `Ai_E_FlameJet` · `Ai_E_FlameJet_Projectile` · `Ai_E_Harvest` · `Ai_E_MassCleanse` · `Ai_E_MysticDagger` · `Ai_E_SearingCharge` · `Ai_E_ShadowVolley` · `Ai_E_ShadowVolley_Projectile` · `Ai_E_SliceThroat` · `Ai_E_StygianRush` · `Ai_E_StygianRush_Rush` · `Ai_E_VileStrike_Damage` · `Ai_EmbraceNewIdentity` · `Ai_FirstBonusQualityUpgrader` · `Ai_Gem_C_Charcoal_Projectile` · `Ai_Gem_C_Sharp_Arrow` · `Ai_Gem_C_Vengence_Projectile` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_E_Fangs_Projectile` · `Ai_Gem_E_Predation_Pickup` · `Ai_Gem_E_Thunder` · `Ai_Gem_L_Embertail_Projectile` · `Ai_Gem_L_PureWhite_Projectile` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_R_Accuracy_Projectile` · `Ai_Gem_R_Blade` · `Ai_Gem_R_Celestial` · `Ai_Gem_R_Dusk_Projectile` · `Ai_Gem_R_Ricochet` · `Ai_Gem_R_Scorched_Meteor` · `Ai_Gem_R_Spiral_Fireball` · `Ai_Gem_U_GlacialCore_Projectile` · `Ai_Gem_U_LastStarlight` · `Ai_GenericDodge` · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `Ai_HunterArtillery_Big` · `Ai_HunterArtillery_Small` · `Ai_L_Blizzard_Instance` · `Ai_L_BloodStrike_Meat` · `Ai_L_ButchersStrike` · `Ai_L_CoinExplosion_Coin` · `Ai_L_CoinExplosion_Explosion` · `Ai_L_LightExplosion` · `Ai_L_LightExplosion_Instance` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_Multishot_Arrow` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_L_SpectreBullet` · `Ai_M_DreamyWaltz` · `Ai_M_DreamyWaltz_BuffExplosion` · `Ai_M_FeatheryDash` · `Ai_M_FrostyCharge` · `Ai_M_Sprint` · `Ai_MiniBoss_BloodThorn_MainThorn` · `Ai_MiniBoss_BloodThorn_Projectile` · `Ai_MiniBoss_BloodThorn_SubThorn` · `Ai_MiniBoss_IceAura_AoE` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_MiniBoss_SpinningArrow_Arrow` · `Ai_MirageSkin_Delusion_Missile` · `Ai_MirageSkin_Oblivion_Orb` · `Ai_MirageSkin_Oppression_Explode` · `Ai_MirageSkin_Pulverization_Stomp` · `Ai_Mon_DarkCave_BossSeeker_Atk_Projectile` · `Ai_Mon_DarkCave_BossSeeker_GreenChaserOrb` · `Ai_Mon_DarkCave_BossSeeker_RedFissure` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_MainInstance` · `Ai_Mon_DarkCave_BossSeeker_YellowDiagram_SubInstance` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Atk_Projectile` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Spawner` · `Ai_Mon_DarkCave_NightOlm_Atk_Projectile` · `Ai_Mon_DarkCave_Oppressor_Hypnotize` · `Ai_Mon_Despair_BossAzurak_Atk_InitDamage` · `Ai_Mon_Despair_BossAzurak_DoubleStomp` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_RoarAtk` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompBlock_Artillery` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_BossAzurak_StompProjectile_FirstAtk` · `Ai_Mon_Despair_BossAzurak_StompProjectile_Projectile` · `Ai_Mon_Despair_BossAzurak_StompTargetArea` · `Ai_Mon_Despair_Displacer_Blink` · `Ai_Mon_Despair_DreadBug_Jump` · `Ai_Mon_Despair_ParalyticFly_Atk` · `Ai_Mon_Despair_ParalyticFly_Paralyze` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_AltSkill_LineAtk` · `Ai_Mon_Forest_BossDemon_AltSkill_Stomp` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles` · `Ai_Mon_Forest_BossDemon_MainSkill_SpawnMissiles_Missile` · `Ai_Mon_Forest_BossDemon_SpecialAtk` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Forest_SpiderSpitter_Atk` · `Ai_Mon_Forest_SpiderSpitter_Backdash` · `Ai_Mon_Forest_SpiderWarrior_Jump` · `Ai_Mon_Forest_Treant_PowerBomb` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_FirstAtk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_HorizontalAtk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_JumpAtk` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_Spawner` · `Ai_Mon_Ink_BossDarkMoon_Blade` · `Ai_Mon_Ink_BossDarkMoon_Blade_Instance` · `Ai_Mon_Ink_BossDarkMoon_Blade_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_ShortDash` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Spawner` · `Ai_Mon_Ink_BossDarkMoon_Spear` · `Ai_Mon_Ink_BossDarkMoon_Spear_Instance` · `Ai_Mon_Ink_BossDarkMoon_TeleportDash` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_AoE` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Spawner` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNIght_BuddhasPalm_Spawner` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_BossWhiteNight_RageInstance` · `Ai_Mon_Ink_DivineAnimal_Missile` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_LavaLand_BossInfernus_AltAtk_Instance` · `Ai_Mon_LavaLand_BossInfernus_Atk` · `Ai_Mon_LavaLand_BossInfernus_BreathFire` · `Ai_Mon_LavaLand_BossInfernus_BreathFire_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Jump_Land` · `Ai_Mon_LavaLand_BossInfernus_PowerBomb` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_LavaLand_BossInfernus_Stomp` · `Ai_Mon_LavaLand_BossInfernus_Stomp_Eruption` · `Ai_Mon_LavaLand_BossInfernus_Swipe` · `Ai_Mon_LavaLand_BossInfernus_WallStunKnockback` · `Ai_Mon_LavaLand_FireElemental_BackDash` · `Ai_Mon_LavaLand_FireElemental_Destruct` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_FireElemental_Explosion` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_InfernoSpider_LavaAtk` · `Ai_Mon_LavaLand_Magmadon_AtkSpawner` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Polaris_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Arbalest` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_Meteor` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Doom_PyranasFireball` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_SmiteStorm_Smite` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Starfall_Instance` · `Ai_Mon_Primus_BossPrimusAeron_Adaptation_Orb` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Force_DropGiantSword` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Primus_BossPrimusAeron_Force_JumpAttack` · `Ai_Mon_Primus_BossPrimusAeron_Force_JumpAttack_ConeInstance` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_Mon_Primus_BossPrimusAeron_Rage_MassDelusion` · `Ai_Mon_Primus_SpawnAttack` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BossNyx_AltTeleport` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_LaserAtk_Instance` · `Ai_Mon_Sky_BossNyx_LineAtk` · `Ai_Mon_Sky_BossNyx_Starfall` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_Sky_BossNyx_Swipe` · `Ai_Mon_Sky_StarSeed_SelfDestruct` · `Ai_Mon_Sky_StarSeed_SelfDestruct_Projectile` · `Ai_Mon_SnowMountain_BossSkoll_Atk` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain` · `Ai_Mon_SnowMountain_BossSkoll_AuraBladeRain_Instance` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove_Land` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_SnowMountain_IceElemental_DoubleSwipe` · `Ai_Mon_SnowMountain_Scavenger_Jump` · `Ai_Mon_SnowMountain_Scavenger_Throw` · `Ai_Mon_SnowMountain_SnowWolf_Pounce` · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `Ai_Mon_Special_AmbushSpawner_Spawn` · `Ai_Mon_Special_BossErebos_AntiGravity_Instance` · `Ai_Mon_Special_BossErebos_AntiGravity_Spawner` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_Gaze_Spawner` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossErebos_StarRain_Spawner` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossMaw_AnnihilationStance_Instance` · `Ai_Mon_Special_BossMaw_Cataclysm_Meteor` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_DarkSpear` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_PillarOfFlame_Projectile` · `Ai_Mon_Special_BossMaw_PrecisionShot` · `Ai_Mon_Special_BossMaw_PrecisionShot_Projectile` · `Ai_Mon_Special_BossMaw_Purgatory_Heal` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossMaw_ScatterShot_ShortProjectile` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossMaw_SliceThroat` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Atk` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Ready` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_NeedleAtk_Ready` · `Ai_Mon_Special_BossObliviax_TurnAtk_Projectile` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Explosion` · `Ai_Mon_Special_BossPolaris_Holy_Atk_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_DisarmProjectile` · `Ai_Mon_Special_BossPolaris_Holy_GoldenSpear_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_BurningFloor` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_HealProjectile` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Instance` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_Mon_Special_BossPolaris_Holy_RainFire_Damage` · `Ai_Mon_Special_BossPolaris_Holy_SelfCleanse` · `Ai_Mon_Special_BossPolaris_Monster_Atk_FirstAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_SecondAtk` · `Ai_Mon_Special_BossPolaris_Monster_Atk_Spawner` · `Ai_Mon_Special_BossPolaris_Monster_Dash` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_Explosion` · `Ai_Mon_Special_BossPolaris_Monster_JumpStomp_LargerExplosion` · `Ai_Mon_Special_BossPolaris_Monster_Scream` · `Ai_Mon_Special_BossPolaris_Monster_SlashDash` · `Ai_Mon_Special_BossPolaris_Monster_Smite_Instance` · `Ai_Prop_Merchant_Flee` · `Ai_QR_DistortedMind_Damage` · `Ai_QR_DistortedMind_Spawner` · `Ai_QR_InfernalTales` · `Ai_QR_Innocence_Explosion` · `Ai_QR_Innocence_Projectile` · `Ai_QR_ValiantHeart` · `Ai_Q_BigBorealChunk_Explosion` · `Ai_Q_BigBorealChunk_Projectile` · `Ai_Q_BigBorealChunk_Spawner` · `Ai_Q_CruelSun` · `Ai_Q_CruelSun_Shockwave` · `Ai_Q_DeathMark_Projectile` · `Ai_Q_Discipline_Stomp` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_Q_EmbracingTheChill_Explosion` · `Ai_Q_EtherealInfluence` · `Ai_Q_EtherealInfluence_Projectile_Base` · `Ai_Q_EtherealInfluence_Projectile_Forward` · `Ai_Q_Fleche_Dash` · `Ai_Q_GoldenBurst` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Laceration_Dash` · `Ai_Q_Lunge` · `Ai_Q_MoonlightPact` · `Ai_Q_MoonlightPact_Fenrir_Atk` · `Ai_Q_MoonlightPact_Land` · `Ai_Q_Reduction_Spawner` · `Ai_Q_SuperNova` · `Ai_Q_SuperNova_Activate` · `Ai_Q_SylvanCall` · `Ai_Q_SylvanCall_LeafHound_Atk` · `Ai_R_AnnihilationStance_Projectile` · `Ai_R_BackOff_Damage` · `Ai_R_BackOff_Spawner` · `Ai_R_BaptismOfSun` · `Ai_R_BlackArbalest` · `Ai_R_BoneCrusher_Explosion` · `Ai_R_Cataclysm_Activate` · `Ai_R_Cataclysm_Meteor` · `Ai_R_ChainReaction` · `Ai_R_Chomp` · `Ai_R_DancingBlades` · `Ai_R_DarkGrenade_Shard` · `Ai_R_DarkGrenade_ShardSpawner` · `Ai_R_FlamingWhip` · `Ai_R_FrozenFists_PunchDash` · `Ai_R_Ignite` · `Ai_R_Immolation_Damage` · `Ai_R_Inspire_Roar` · `Ai_R_Lava_LavaField` · `Ai_R_NaturesWhisper` · `Ai_R_OrbOfLight_BackwardHealing` · `Ai_R_OrbOfLight_ForwardDamaging` · `Ai_R_Parry_Projectile` · `Ai_R_PrecisionShot` · `Ai_R_PrecisionShot_Projectile` · `Ai_R_QuickTrigger` · `Ai_R_QuickTrigger_Projectile` · `Ai_R_RepulsiveShield_Projectile` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_R_Scattershot_Projectile` · `Ai_R_Scattershot_Spawner` · `Ai_R_SerpentineBlessing` · `Ai_R_SerpentineBlessing_Projectile` · `Ai_R_ShadowOverdrive_Projectile` · `Ai_R_ShadowWalk` · `Ai_R_ShadowWalk_Projectile` · `Ai_R_Somersault` · `Ai_R_StaticDischarge` · `Ai_R_SummonLittleBaam` · `Ai_R_UnbreakableDetermination_SubExplosion` · `Ai_RandomGemUpgrade` · `Ai_RegenOrb_Projectile` · `Ai_ReviveHero` · `Ai_RoomMod_FireDevil_Tornado` · `Ai_Shrine_MawOfDoom_DestroyTarget` · `Ai_Shrine_SmallSoul_Attack` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Aurena_F_CR_ChargedCast_InstanceCharger` · `Ai_Star_Bismuth_D_BonusAttackEffect_Arrow` · `Ai_Star_Bismuth_F_IT_SmallerRingAddDisplacement_Dash` · `Ai_Star_Cetus_F_BA_LightningEcho_Lightning` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `Ai_Star_Yubar_F_EI_DashNoProjectile_Dash` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_BigChomp` · `Ai_U_Burrow_Emerge` · `Ai_U_HerWorld_Explosion` · `Ai_U_ShoutOfOblivion` · `Ai_U_WorldCracker` · `Ai_UnstableRatSwarm_Projectile` · `Ai_VeilOfDark` · [Artifact](/api/Global.Artifact) · `At_Atk_HuskSword` · `At_Atk_YubarStardust` · `At_Mon_Forest_BossDemon_MainSkill` · `At_Mon_Sky_StarSeed_SelfDestruct` · `At_Mon_Special_BossLightElemental_Summon` · `At_Mon_Special_BossPolaris_Monster_PizzaLightning` · [AttachToHero](/api/Global.AttachToHero) · [AttackProjectile](/api/Global.AttackProjectile) · [BossMonster](/api/Global.BossMonster) · [CameraManager](/api/Global.CameraManager) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CastInfo](/api/Global.CastInfo) · [ChargingChannel](/api/Global.ChargingChannel) · [ChargingChannelData](/api/Global.ChargingChannelData) · [ChoiceShrine](/api/Global.ChoiceShrine) · [ClientEventManager](/api/Global.ClientEventManager) · [ConsoleManager](/api/Global.ConsoleManager) · [ControlManager](/api/Global.ControlManager) · [ConversationManager](/api/Global.ConversationManager) · `ConversationShrineBase` · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [DamageData](/api/Global.DamageData) · [DamageInstance](/api/Global.DamageInstance) · [DashAttackInstance](/api/Global.DashAttackInstance) · `Despair_FogPositionController` · [Dew](/api/Global.Dew) · [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) · [DewCollider](/api/Global.DewCollider) · `DewConsoleCommands` · `DewDamageNumberRenderer` · [DewEffect](/api/Global.DewEffect) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [DewQuest](/api/Global.DewQuest) · [DewResources](/api/Global.DewResources) · [EditSkillManager](/api/Global.EditSkillManager) · [ElementalStatusEffect](/api/Global.ElementalStatusEffect) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntityGroundMarker](/api/Global.EntityGroundMarker) · [EntitySound](/api/Global.EntitySound) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoAbilityInstance](/api/Global.EventInfoAbilityInstance) · [EventInfoApplyElemental](/api/Global.EventInfoApplyElemental) · [EventInfoAttackEffect](/api/Global.EventInfoAttackEffect) · [EventInfoAttackFired](/api/Global.EventInfoAttackFired) · [EventInfoAttackHit](/api/Global.EventInfoAttackHit) · [EventInfoAttackMissed](/api/Global.EventInfoAttackMissed) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoDamageNegatedByImmunity](/api/Global.EventInfoDamageNegatedByImmunity) · [EventInfoDamageNegatedByShield](/api/Global.EventInfoDamageNegatedByShield) · `EventInfoDismantle` · [EventInfoHeal](/api/Global.EventInfoHeal) · [EventInfoKill](/api/Global.EventInfoKill) · [EventInfoSpentMana](/api/Global.EventInfoSpentMana) · [EventInfoSummon](/api/Global.EventInfoSummon) · [FinalDamageData](/api/Global.FinalDamageData) · [FlavourManager](/api/Global.FlavourManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · `Forest_Fireplace` · `Forest_LoopCat_Spawner` · [FxCastTelegraph](/api/Global.FxCastTelegraph) · [FxFindEntity](/api/Global.FxFindEntity) · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · [GameEffect](/api/Global.GameEffect) · `GameMod_DespairFixStuck` · `GameMod_GoldenLizard` · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · `GameMod_StarlessPath` · [GameResultManager](/api/Global.GameResultManager) · `Ge_CallOfTheRavenous` · `Ge_Obliviax_InterruptTravelAndKidnap` · `Ge_Shrine_Anitya` · `Ge_Shrine_PotOfGreed` · `Ge_TheConsortOfNight` · [Gem](/api/Global.Gem) · `Gem_C_Charcoal` · `Gem_C_Confidence` · `Gem_C_Guidance` · `Gem_C_Lethality` · `Gem_C_Love` · `Gem_C_Quicksilver` · `Gem_C_Regeneration` · `Gem_C_Shatter` · `Gem_C_Sulfur` · `Gem_C_Talc` · `Gem_C_Vengeance` · `Gem_C_Void` · `Gem_C_Wind` · `Gem_E_Aftershock` · `Gem_E_Apathy` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Direness` · `Gem_E_Domination` · `Gem_E_Fangs` · `Gem_E_Flexibility` · `Gem_E_Insensitivity` · `Gem_E_Insight` · `Gem_E_Inversion` · `Gem_E_Metal` · `Gem_E_Might` · `Gem_E_Obsidian` · `Gem_E_Omega` · `Gem_E_Opportunity` · `Gem_E_OurStory_Completed` · `Gem_E_OurStory_Unfinished` · `Gem_E_Overload` · `Gem_E_Pain` · `Gem_E_Predation` · `Gem_E_Protection` · `Gem_E_Reflex` · `Gem_E_Umbra` · `Gem_L_CamillasGift` · `Gem_L_ChaosApple` · `Gem_L_Culinary` · `Gem_L_DivineFaith` · `Gem_L_Embertail` · `Gem_L_Liberty` · `Gem_L_Paranoia` · `Gem_L_Supersymmetry` · `Gem_L_SuppressedArcanum` · `Gem_R_Abyss` · `Gem_R_Accuracy` · `Gem_R_Bleak` · `Gem_R_Blood` · `Gem_R_Composure` · `Gem_R_Contempt` · `Gem_R_Control` · `Gem_R_Epiphany` · `Gem_R_Flow` · `Gem_R_Frost` · `Gem_R_Glass` · `Gem_R_Hedgehog` · `Gem_R_Insatiable` · `Gem_R_Lightweight` · `Gem_R_Momentum` · `Gem_R_NightSky` · `Gem_R_Panic` · `Gem_R_Purity` · `Gem_R_Rejuvenation` · `Gem_R_Ricochet` · `Gem_R_Rigidity` · `Gem_R_Slippery` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_R_Wealth` · `Gem_U_EternalFlame` · `Gem_U_GlacialCore` · `Gem_U_GuidingCompass_NotCharged` · `Gem_U_LastStarlight` · `Gem_U_SoulPrison` · [HealData](/api/Global.HealData) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · `Hero_Aurena` · `Hero_Bismuth` · `Hero_Bismuth_BookController` · `Hero_Husk` · `IHoldableInHandExtension` · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · [InGameUIManager](/api/Global.InGameUIManager) · `Ink_BossRoomDamageGround` · `Ink_GhostBehavior` · `ItemWorldModel` · [KillTracker](/api/Global.KillTracker) · [Knockback](/api/Global.Knockback) · `LavaLand_IcePlace` · `LavaLand_Lava` · [LogicUpdateManager](/api/Global.LogicUpdateManager) · `LucidDream_BlandStarSoup` · `LucidDream_EmbraceMortality` · `LucidDream_FalseLifeline` · `LucidDream_FishScales` · `LucidDream_GrievousWounds` · `LucidDream_KindArmadillo` · `LucidDream_MarshOfDestiny` · `LucidDream_PrudentJellyfish` · `LucidDream_SparklingDreamFlask` · `LucidDream_TheDarkestUrge` · `LucidDream_WILD` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · [MockAbilityInstance](/api/Global.MockAbilityInstance) · [MockEntity](/api/Global.MockEntity) · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveBat` · `Mon_DarkCave_DarkElemental` · `Mon_DarkCave_NightOlm` · `Mon_DarkCave_Oppressor` · `Mon_DarkCave_SeekerHallucination` · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Despair_AzurakRollPillar` · `Mon_Despair_BossAzurak` · `Mon_Despair_DreadBug` · `Mon_Despair_UnstableRat` · `Mon_Despair_WretchedArtillery` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Forest_BossDemon` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_Forest_Treant` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossDarkMoonHallucination` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_BossWhiteNightHallucination` · `Mon_Ink_DivineAnimal` · `Mon_Ink_EgoSword` · `Mon_LavaLand_BossInfernus` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_InfernusPillar` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Polaris` · `Mon_Primus_BossPrimusAeron` · [Mon_RedGiant](/api/Global.Mon_RedGiant) · [Mon_RedMan](/api/Global.Mon_RedMan) · `Mon_Sky_Baam` · `Mon_Sky_BossNyx` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_BossSkoll` · `Mon_SnowMountain_LivingShards` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_SnowMountain_VikingWarrior` · `Mon_Special_AmbushSpawner` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossMaw` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · `Mon_Special_ObliviaxHallucination` · [Monster](/api/Global.Monster) · `NextZoneOverrideTreasure` · [ObjectiveArrowManager](/api/Global.ObjectiveArrowManager) · `Obliviax_Decoration_Generator` · [PickupInstance](/api/Global.PickupInstance) · [PickupManager](/api/Global.PickupManager) · [Pickup_BaseGoldOrb](/api/Global.Pickup_BaseGoldOrb) · [Pickup_DreamDust](/api/Global.Pickup_DreamDust) · [Pickup_HealthOrb](/api/Global.Pickup_HealthOrb) · [Pickup_ManaOrb](/api/Global.Pickup_ManaOrb) · [Pickup_RegenOrb](/api/Global.Pickup_RegenOrb) · [PingManager](/api/Global.PingManager) · `PlayTutorial_Tutorial` · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_SkillsAndEssences` · `Primus_Ending` · `Primus_Pizza0` · [Projectile](/api/Global.Projectile) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · [PropEnt_Merchant_Unmanned](/api/Global.PropEnt_Merchant_Unmanned) · `PropEnt_Sky_Orca` · `PropEnt_Stone_PitchBlackOre` · `PropEnt_Tutorial_Obstacle` · `PropEnt_VigilanteHaven_Obstacle` · [PropEntity](/api/Global.PropEntity) · `Quest_HuntedByObliviax` · `Quest_KillToLiftCurse` · `Quest_LostSoul` · [ReactionChain](/api/Global.ReactionChain) · [Rift](/api/Global.Rift) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [Room](/api/Global.Room) · [RoomMap](/api/Global.RoomMap) · `RoomMod_Ambush` · `RoomMod_Anitya` · `RoomMod_ArcticTerritory` · `RoomMod_Artifact` · `RoomMod_BlackRain` · `RoomMod_CallOfTheRavenous` · `RoomMod_CorruptedChaos_AuraOfPain` · `RoomMod_DarkCondensationZone` · `RoomMod_DistantMemories` · `RoomMod_EngulfedInFlame` · `RoomMod_FallenStar` · `RoomMod_FireDevil` · `RoomMod_FragmentOfRadiance_MysteriousPlace` · `RoomMod_FragmentOfRadiance_StartProp` · `RoomMod_GazeOfErebos` · `RoomMod_GoldEverywhere` · `RoomMod_GravityTraining` · `RoomMod_HarderFightBetterReward` · `RoomMod_HeroSoul` · `RoomMod_Hunted` · `RoomMod_InkStrikeWarning` · `RoomMod_InversionSigil` · `RoomMod_LeafPuppies` · `RoomMod_Limbo_Decorator` · `RoomMod_LingeringAuraOfGuidance` · `RoomMod_MeteoricLife` · `RoomMod_PureDream` · `RoomMod_RiskOfMeteors` · `RoomMod_SpawnAltarOfCleansing` · `RoomMod_SpawnAscension` · `RoomMod_SpawnBlessedGuidance` · `RoomMod_SpawnDestiny` · `RoomMod_SpawnDisintegration` · `RoomMod_SpawnEntanglement` · `RoomMod_SpawnHatred` · `RoomMod_SpawnJonasChamberRift` · `RoomMod_SpawnMawOfDoom` · `RoomMod_SpawnMiniBoss` · `RoomMod_SpawnMirrorOfRemorse` · `RoomMod_SpawnParadox` · `RoomMod_SpawnPileOfSnow` · `RoomMod_SpawnPotOfGreed` · `RoomMod_SpawnWell` · `RoomMod_StarCookie` · `RoomMod_StardustEverywhere` · `RoomMod_StrayMemory_StartProp` · `RoomMod_SymbioteHabitat` · `RoomMod_TheConsortOfNight_Raven` · `RoomMod_ToxicArea` · `RoomMod_UnstableRatSwarm` · `RoomMod_VeilOfDark` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomModifiers](/api/Global.RoomModifiers) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomProps](/api/Global.RoomProps) · [RoomRewards](/api/Global.RoomRewards) · [Room_Barrier](/api/Global.Room_Barrier) · [Room_Shortcut](/api/Global.Room_Shortcut) · [Room_Trap_Toggleable](/api/Global.Room_Trap_Toggleable) · `Se_AcceleratedTime` · `Se_ArcticTerritory` · `Se_AutoDetectPresence` · `Se_C_CorrosiveTrails_Spawner` · `Se_C_Hemorrhage_EmpowerAttack` · `Se_C_IceBlock` · `Se_Curse_AnchorOfMind` · `Se_Curse_DarkUrge` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_Curse_DreamAfflictionInductive` · `Se_Curse_Electrified` · `Se_Curse_EternalLoop` · `Se_Curse_FateOfGreed` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_Curse_IntermittentExplosion` · `Se_Curse_Lethargy` · `Se_Curse_LossOfIdentity` · `Se_Curse_SoftSkin` · `Se_Curse_UnstableEnergy` · `Se_Curse_VainDream` · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpieceEnGarde_Exposed` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_AstridsMasterpiecePriorite_Exposed` · `Se_D_BeautifulThreat` · `Se_D_BurningFist_EmpowerAttack` · `Se_D_ChargedAnguillian` · `Se_D_ConvergencePoint` · `Se_D_DoubleTap` · `Se_D_ExoticMatter` · `Se_D_IceColdPresence` · `Se_D_IceColdPresence_PersistentBuff` · `Se_D_IcyVeins` · `Se_D_MercyOfEl` · `Se_D_PrismaticEyes` · `Se_D_QuartetOfDeath_DeathMark` · `Se_D_ScarOfTheWind_NextAtkCrit` · `Se_D_TheKillingFlow` · `Se_D_TheKillingFlow_Crit` · `Se_D_TrueDuelist_Exposed` · `Se_DistantMemories` · `Se_E_CrimsonLance_BossDrop` · `Se_E_FinalExplosion` · `Se_E_Harvest_OnVictim` · `Se_E_LizardlyBlessing` · `Se_E_Permafrost_Stun` · `Se_E_Rewind` · `Se_E_UmbralEdge` · `Se_E_VileStrike` · `Se_Elm_Dark` · `Se_Elm_Fire` · `Se_Elm_Light` · `Se_EngulfedInFlame` · `Se_FallenStar_MonsterReinforcement` · `Se_FatalHitProtection_Invulnerable` · `Se_FishScales` · `Se_Gem_E_Fever_LivingBomb` · `Se_Gem_L_Culinary_Stack` · `Se_Gem_L_Liberty_Buff` · `Se_Gem_R_Frost_Stat` · `Se_Gem_R_Panic` · `Se_Gem_R_Wound_Wounded` · `Se_Gem_Regeneration` · `Se_GenericEffectContainer` · `Se_GenericHealOverTime` · `Se_GenericRevealed` · `Se_GenericShield_OneShot` · `Se_GenericShield_Stacking` · `Se_GenericStealth` · `Se_GoldEverywhere` · `Se_HarmlessWhispers` · `Se_HarmlessWhispers_GrantShield` · `Se_HeroBleedingOut` · `Se_HeroInCombatIcon` · `Se_HeroKnockedOut` · `Se_HeroOneShotProtection` · `Se_HunterBuff` · `Se_HunterBuff_ShadowWalk_Disappear` · `Se_L_ButchersStrike_KillTimer` · `Se_L_HerosReturn_Interrupt` · `Se_L_MentalCorruption` · `Se_L_Multishot_Buff` · `Se_L_PyranasFireball` · `Se_LingeringAuraOfGuidance` · `Se_M_Charge` · `Se_M_DreamyWaltz_Buff` · `Se_M_Sprint` · `Se_MiniBoss_BloodThorn` · `Se_MiniBoss_BloodThorn_Bleeding` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MiniBoss_SpinningArrow` · `Se_MiniBoss_UnstableExplosive` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Delusion_Delusional` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Oppression` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_Mon_DarkCave_BossSeeker_Hallucination_Disappear` · `Se_Mon_DarkCave_BossSeeker_Substitution` · `Se_Mon_DarkCave_BossSeeker_TunnelVision` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_Disappear` · `Se_Mon_DarkCave_BossSeeker_TunnelVision_PlayerLight` · `Se_Mon_DarkCave_DarkElemental_Teleport` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Ink_Boss_Rage` · `Se_Mon_LavaLand_BossInfernus_InvulShield` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Ongoing` · `Se_Mon_Primus_BossPrimusAeron_Adapt_IceBlock` · `Se_Mon_Primus_BossPrimusAeron_Adaptation` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_Mon_Sky_BossNyx_StarBuff` · `Se_Mon_SnowMountain_SnowWolf_SlowApproach` · `Se_Mon_SnowMountain_VikingWarrior_DmgReducer` · `Se_Mon_Special_BossErebos_SecondPhase` · `Se_Mon_Special_BossMaw_Cataclysm` · `Se_Mon_Special_BossMaw_ShieldConversion` · `Se_Mon_Special_BossPolaris_Adaptation` · `Se_Mon_Special_BossPolaris_CleansingFlame` · `Se_Mon_Special_BossPolaris_Holy_CounterSpell` · `Se_Mon_Special_BossPolaris_Holy_PhaseShifter` · `Se_Mon_Special_BossPolaris_Monster_Scream_SkillLocked` · `Se_MonsterSprint` · `Se_Nor_ReptilianThirdEye` · `Se_ObliviaxKidnap` · `Se_PlayTutorialHeroProtection` · `Se_PolarisHallucination` · `Se_PureDream` · `Se_Q_CruelSun_Armored` · `Se_Q_DeathMark_Marked` · `Se_Q_Discipline_Jump` · `Se_Q_Fleche_VictimTracker` · `Se_Q_GoldenBurst_Wither` · `Se_Q_IncendiaryRounds_EmpowerAttacks` · `Se_Q_SuperNova_Slow` · `Se_R_AnnihilationStance` · `Se_R_BaptismOfSun_Buff` · `Se_R_BoneCrusher` · `Se_R_BoneCrusher_Kidnapped` · `Se_R_Cataclysm` · `Se_R_Composure_Buff` · `Se_R_DangerousTheory` · `Se_R_Deception` · `Se_R_Frostbite_EmpowerAttacks` · `Se_R_FrozenFists` · `Se_R_Immolation` · `Se_R_Lava_Debuff` · `Se_R_NaturesWhisper_Buff` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_SanctuaryOfEl_Buff` · `Se_R_SerpentineBlessing_Buff` · `Se_R_Somersault_CritBonus` · `Se_R_Tranquility` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_BlackRain` · `Se_RoomMod_ToxicArea_Debuff` · `Se_RoomMod_WarpingField_Unstable` · `Se_Shrine_Chaos_StatBonus` · `Se_Shrine_Despair_Teleport` · `Se_Shrine_SmallSoul` · `Se_Star_Aurena_F_CR_EarnGold` · `Se_Star_Aurena_F_CR_NoHealCooldownReduction` · `Se_Star_Aurena_F_DT_UnstoppableAndRemoveDelusion` · `Se_Star_Aurena_F_GB_NoSacrificeAfterDodge` · `Se_Star_Aurena_I_BonusFromStones` · `Se_Star_Aurena_I_PotionGold` · `Se_Star_Aurena_L_HealAmpOnLowHp` · `Se_Star_Aurena_L_HealAmpWithPenalty` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Bismuth_D_BonusAttackEffect` · `Se_Star_Bismuth_D_Conquerer` · `Se_Star_Bismuth_D_Conquerer_Stacks` · `Se_Star_Bismuth_F_IT_SmallerRingAddDisplacement` · `Se_Star_Bismuth_F_VH_ResetOnDodge` · `Se_Star_Bismuth_F_VH_Shield` · `Se_Star_Bismuth_I_TreasureWithHealthPenalty` · `Se_Star_Cetus_F_BA_CdReductionOnKill` · `Se_Star_Cetus_F_BA_ChargeMsNoShield` · `Se_Star_Cetus_F_BI_MaxChargeTimePerLevel` · `Se_Star_Cetus_F_BI_SelfDamageAoeCold` · `Se_Star_Cetus_F_EM_InfiniteDuration` · `Se_Star_Cetus_F_FR_CdReductionOnTakeDamage` · `Se_Star_Cetus_F_FR_ChangeToUltHitReset` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_Cetus_I_FirstColdGemQualityBoost` · `Se_Star_Cetus_I_GetDreamDustOnBossKill` · `Se_Star_Cetus_L_ArmorBuffOnShield` · `Se_Star_Cetus_L_DodgeCdReductionOnHit` · `Se_Star_Cetus_L_FrostResistAndBuff` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Cetus_L_IncreaseDealtShield` · `Se_Star_Cetus_L_MaxHpDamagePenalty` · `Se_Star_D_BossDamageAmp` · `Se_Star_D_CritUpHitDecay` · `Se_Star_D_DamageBonusOnAllElemental` · `Se_Star_D_RiftFirstCastDamageUp` · `Se_Star_D_ShieldDamageAmp` · `Se_Star_D_TempAbilityPower` · `Se_Star_D_TempAttackDamage` · `Se_Star_Husk_D_DamageAmpOnLowHpTarget` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · `Se_Star_Husk_D_DarkAttackWithPenalty` · `Se_Star_Husk_F_AS_AddedDurationOnHit` · `Se_Star_Husk_F_DC_RecentDamageHoTWhileStealth` · `Se_Star_Husk_F_DE_MarkHitDodgeCDR` · `Se_Star_Husk_F_LA_DodgeResetOnRed` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Husk_L_DodgeCooldownOnKillOrAttack` · `Se_Star_Husk_L_DodgeCooldownOnKillWithEmptyCharges` · `Se_Star_I_DismantleDustToBonusGold` · `Se_Star_I_DismantleReroll` · `Se_Star_I_DreamDustOnKillChance` · `Se_Star_I_ExtraChaosOptionGoldOnUse` · `Se_Star_I_FirstBossGemDrop` · `Se_Star_I_FirstGemUpgrade` · `Se_Star_I_GoldRiskAndReturn` · `Se_Star_I_MawDiscountAndProtection` · `Se_Star_I_MoreShrineItems` · `Se_Star_I_StartGold` · `Se_Star_L_DamageReductionFromChilled` · `Se_Star_L_ElementalResistance` · `Se_Star_L_FatalHitProtection` · `Se_Star_L_HealOnAttack` · `Se_Star_L_HealOnKill` · `Se_Star_L_IgnoreDelusion` · `Se_Star_L_IncreaseMaxHealthByGuidance` · `Se_Star_L_MaxHealthUpHealDown` · `Se_Star_L_PostHitDamageImmune` · `Se_Star_L_PotionHealAmount` · `Se_Star_L_PotionOnBuyOrSell` · `Se_Star_L_ReceivedHealingAndShieldBonus` · `Se_Star_L_TempArmor` · `Se_Star_Lacerta_F_HC_NearDamage` · `Se_Star_Lacerta_F_HC_NoDelayDoubleCast` · `Se_Star_Lacerta_F_HC_ResetOnDodge` · `Se_Star_Lacerta_F_PS_CooldownReset` · `Se_Star_Lacerta_I_BonusFromStones` · `Se_Star_Lacerta_I_BossBounty` · `Se_Star_Lacerta_L_SpeedAfterDodge` · `Se_Star_Mist_D_BossDamageOnHighHp` · `Se_Star_Mist_D_HunterDamage` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Mist_F_PR_ShieldAndCrit` · `Se_Star_Mist_F_UD_HealLostHealth` · `Se_Star_Mist_I_BonusOnCatPet` · `Se_Star_Mist_L_AddedDodgeWithPenalty` · `Se_Star_Mist_L_PotionShield` · `Se_Star_Nachia_D_CanineLover` · `Se_Star_Nachia_D_SummonAtkSpd` · `Se_Star_Nachia_F_MP_StrongerFenrirNoCast` · `Se_Star_Nachia_F_SC_AtkSpd` · `Se_Star_Nachia_F_SC_SummonDmgReduction` · `Se_Star_Nachia_I_ForestKillDreamDust` · `Se_Star_Nachia_I_SummonKillGold` · `Se_Star_Nachia_L_AllyUnstoppable` · `Se_Star_Nachia_L_HealAndShieldAmp` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Vesper_D_BossHunterAmpWithPenalty` · `Se_Star_Vesper_I_StartGold` · `Se_Star_Vesper_L_FireResistance` · `Se_Star_Yubar_D_BonusDamageToLight` · `Se_Star_Yubar_F_EI_BiggerExplosion` · `Se_Star_Yubar_F_EI_DashNoProjectile` · `Se_Star_Yubar_F_SN_DodgeReset` · `Se_Star_Yubar_F_SN_PullEnemy` · `Se_Star_Yubar_F_TQ_LowerCooldownNoInvul` · `Se_Star_Yubar_I_DisintegrateDreamDust` · `Se_Star_Yubar_I_MoreDreamDustWithPenalty` · `Se_Star_Yubar_I_StarCookie` · `Se_StarlessPath_PowerOfGuidance` · `Se_Treasure_CrimsonElixir_AdBoost` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Se_U_BeamOfBalance` · `Se_U_Burrow` · `Se_U_EternalFlame_Curse` · `Se_U_HerWorld_Blackhole` · `Se_U_Hysteria` · `Se_WaypointTeleport` · [ServerActor](/api/Global.ServerActor) · [ShieldEffect](/api/Global.ShieldEffect) · [Shrine](/api/Global.Shrine) · `Shrine_AltarOfCleansing` · `Shrine_Anitya` · `Shrine_ArtifactGiver` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `Shrine_Destiny` · `Shrine_DreamdustBit` · `Shrine_DreamdustBox` · `Shrine_Entanglement` · `Shrine_FallenStar` · `Shrine_GoldBit` · `Shrine_GoldBox` · `Shrine_Guidance` · `Shrine_Hatred` · `Shrine_HeroSoul` · `Shrine_InvitationOfJonasMeeting` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_MawOfDoom` · `Shrine_Paradox` · `Shrine_Polaris_Teleporter` · `Shrine_PrimusEndingLightPillar` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · `Shrine_SmallSoul` · `Shrine_Stardust` · `Shrine_StarlessPath_EndingRift` · `Shrine_TheConsortOfNight` · `Shrine_TheConsortOfNight_Rift` · [SkillTrigger](/api/Global.SkillTrigger) · `Sky_BossIntruder` · `Sky_LightFogDamager` · [SpawnManager](/api/Global.SpawnManager) · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `Special_StrangePlace_HiddenSection` · `St_C_Whirlwind` · `St_D_BurningFist` · `St_D_CircleOfLife` · `St_D_DisintegratingClaw` · `St_D_HeartOfThePack` · `St_D_IceColdPresence` · `St_D_IcyVeins` · `St_D_MercyOfEl` · `St_D_ParryMaster` · `St_D_QuartetOfDeath` · `St_D_Resolve` · `St_D_SalamanderPowder` · `St_D_ScarOfTheWind` · `St_E_Harvest` · `St_L_HerosReturn` · `St_L_SmallMoltenCore` · `St_QR_InfernalTales` · `St_Q_DeathMark` · `St_Q_Discipline` · `St_Q_Fleche` · `St_Q_GoldenBurst` · `St_Q_MoonlightPact` · `St_Q_Reduction` · `St_R_AnnoyingBanner` · `St_R_DangerousTheory` · `St_R_FlamingWhip` · `St_R_LightningDance` · `St_R_Somersault` · `St_U_ShoutOfOblivion` · [StackedStatusEffect](/api/Global.StackedStatusEffect) · [StandardProjectile](/api/Global.StandardProjectile) · [StarEffect](/api/Global.StarEffect) · `Star_Global_Armor` · `Star_Global_DecreaseDamageFromChilled` · `Star_Global_ElementResistance` · `Star_Global_FatalHitProtection` · `Star_Global_KillDreamDustBonus` · `Star_Lacerta_HandCannon` · `Star_Mist_UnbreakableDeterminationHeal` · `Star_Vesper_Armor` · `Star_Yubar_EtherealInfluenceCooldownReduction` · `Star_Yubar_StrongerSuperNova` · `Star_Yubar_TranquilityDamage` · `StarlessPath_BossPolarisManager` · [StatusEffect](/api/Global.StatusEffect) · `StatusEffectRandomPickupInstance` · `Sum_L_SmallMoltenCore_Dragon` · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · [Summon](/api/Global.Summon) · `TempEffect` · [TickDamageInstance](/api/Global.TickDamageInstance) · `Trap_ArrowShooter` · `Trap_FlameJet` · `Trap_Lightning` · `Trap_UnstableMushroom` · [Treasure](/api/Global.Treasure) · `Treasure_BlueElixir` · `Treasure_Clairvoyance` · `Treasure_CloakOfGuidance` · `Treasure_CrimsonElixir` · `Treasure_DreamingStarfish` · `Treasure_FragmentOfDetermination` · `Treasure_InvitationToSecretMeetingOfJonas` · `Treasure_SparklingElixir` · `Treasure_StarSeekersJournal` · `Treasure_StrayMemory` · `Treasure_SuspiciousHat` · `Treasure_TokenOfGuidance` · `Treasure_TotallyGenuineTreasureMap` · `Treasure_TreasureMap` · [TriggerConfig](/api/Global.TriggerConfig) · `UI_DamageNumberGroup` · `UI_DamageNumberText` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_EntityFollow` · `UI_HealthBar_Simple` · `UI_InGame_CurseNotifications` · `UI_InGame_Difficulty` · `UI_InGame_FollowAndFaceHero_Base` · `UI_InGame_Interact_Base` · `UI_InGame_Interact_Rift` · `UI_InGame_LucidDreams` · `UI_InGame_Map` · `UI_InGame_Map_Item_Actor` · `UI_InGame_Map_Item_Entity` · `UI_InGame_Map_Item_Shrine` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_PickupNumbers_Number` · `UI_InGame_QuestDisplay_Item` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_Scoreboard_PlayerItem_Skill_Gem` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_StatusEffectIcons` · `UI_InGame_StatusEffectIcons_Item` · `UI_World_FollowAndFaceCamera` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (60)

*Types and components that `Actor` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilityTrigger](/api/Global.AbilityTrigger) · `ActionRef`1` · [ActorCheck](/api/Global.ActorCheck) · [ActorManager](/api/Global.ActorManager) · `ActorRef`1` · [BasicEffect](/api/Global.BasicEffect) · [CastInfo](/api/Global.CastInfo) · [CooldownReductionByRatioSettings](/api/Global.CooldownReductionByRatioSettings) · [CooldownReductionSettings](/api/Global.CooldownReductionSettings) · [DamageData](/api/Global.DamageData) · [DataProcessorGroup`3](/api/Global.DataProcessorGroup`3) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewElementals](/api/Global.DewElementals) · [DewLocalization](/api/Global.DewLocalization) · [DewMath](/api/Global.DewMath) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPersistence](/api/Global.DewPersistence) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [DewResources](/api/Global.DewResources) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · [ElementalStatusEffect](/api/Global.ElementalStatusEffect) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoAbilityInstance](/api/Global.EventInfoAbilityInstance) · [EventInfoApplyElemental](/api/Global.EventInfoApplyElemental) · [EventInfoAttackEffect](/api/Global.EventInfoAttackEffect) · [EventInfoAttackHit](/api/Global.EventInfoAttackHit) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoHeal](/api/Global.EventInfoHeal) · [EventInfoKill](/api/Global.EventInfoKill) · [EventInfoShield](/api/Global.EventInfoShield) · [EventInfoSpentMana](/api/Global.EventInfoSpentMana) · [EventInfoSummon](/api/Global.EventInfoSummon) · [FinalDamageData](/api/Global.FinalDamageData) · [FinalHealData](/api/Global.FinalHealData) · [HealData](/api/Global.HealData) · [ICleanup](/api/Global.ICleanup) · [ICustomDestroyRoutine](/api/Global.ICustomDestroyRoutine) · [KillTracker](/api/Global.KillTracker) · `ListExtensions` · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [OnScreenTimerHandle](/api/Global.OnScreenTimerHandle) · [ReactionChain](/api/Global.ReactionChain) · [SafeAction`1](/api/Global.SafeAction`1) · `Se_GenericEffectContainer` · `Se_GenericRevealed` · `Se_GenericShield_OneShot` · `Se_GenericStealth` · [ShieldEffect](/api/Global.ShieldEffect) · [SkillTrigger](/api/Global.SkillTrigger) · [StackedStatusEffect](/api/Global.StackedStatusEffect) · [StatusEffect](/api/Global.StatusEffect) · `TransformGetScenePathExtension`

### Related Enums (4)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#attackeffecttype" class="enum-link" data-tooltip="BasicAttackMain=0 · BasicAttackSub=1 · Others=2">AttackEffectType</a> · <a href="/enums#duplicateeffectbehavior" class="enum-link" data-tooltip="UsePrevious=0 · ReplacePrevious=1 · DoNothing=2">DuplicateEffectBehavior</a> · <a href="/enums#elementaltype" class="enum-link" data-tooltip="Fire=0 · Cold=1 · Light=2 · Dark=3">ElementalType</a> · <a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
