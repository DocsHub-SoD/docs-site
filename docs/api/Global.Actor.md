# Class: Actor

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
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
| **`persistentData`** | `[SaveVar(SaveVarFlags.Default)] public readonly Dictionary<string, string> persistentData` | Available on server. Generic persistent data storage that will be saved and loaded with this actor. |
| **`persistentSyncedData`** | `[SaveVar(SaveVarFlags.Default)] public readonly SyncDictionary<string, string> persistentSyncedData` | Available everywhere, and can only be set on server. Generic persistent synced data storage that will be saved and loaded with this actor, and be synced across the network.Use this to store states in the network context. (think: synced variables) |
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
| **`position`** | `[SaveVar(SaveVarFlags.Default)] public Vector3 position { get; set; }` | Position of this actor. Same astransform.position. |
| **`rotation`** | `[SaveVar(SaveVarFlags.Default)] public Quaternion rotation { get; set; }` | Rotation of this actor. Same astransform.rotation. |

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
| `type` | [`ElementalType`](/api/Global.ElementalType) |  |
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
| `onDuplicate` | [`DuplicateEffectBehavior`](/api/Global.DuplicateEffectBehavior) |  |

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
| `type` | [`AttackEffectType`](/api/Global.AttackEffectType) |  |
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
