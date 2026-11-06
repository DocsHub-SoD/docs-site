# Class: DewPhysics

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewPhysics
```

## Methods (12)

::: details `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, IBinaryEntityValidator, Entity, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, IBinaryEntityValidator validator, Entity self, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, IEntityValidator, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, IEntityValidator validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `OverlapCircleAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Func&lt;Entity, bool&gt;, CollisionCheckSettings)`

```csharp
public static List<Entity> OverlapCircleAllEntities(out ListReturnHandle<Entity> handle, Vector3 center, float radius, Func<Entity, bool> validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `center` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, IBinaryEntityValidator, Entity, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, IBinaryEntityValidator validator, Entity self, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, IEntityValidator, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, IEntityValidator validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `SphereCastAllEntities(out ListReturnHandle&lt;Entity&gt;, Vector3, float, Vector3, float, Func&lt;Entity, bool&gt;, CollisionCheckSettings)`

```csharp
public static List<Entity> SphereCastAllEntities(out ListReturnHandle<Entity> handle, Vector3 origin, float radius, Vector3 direction, float maxDistance, Func<Entity, bool> validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `origin` | `UnityEngine.Vector3` |  |
| `radius` | `float` |  |
| `direction` | `UnityEngine.Vector3` |  |
| `maxDistance` | `float` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `TryGetCollidableWithProjectile(Collider2D, out ICollidableWithProjectile)`

```csharp
public static bool TryGetCollidableWithProjectile(Collider2D collider, out ICollidableWithProjectile collidable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `collidable` | [`ICollidableWithProjectile`](/api/Global.ICollidableWithProjectile) |  |

**Returns:** `bool`

:::

::: details `TryGetEntity(Collider2D, out Entity)`

```csharp
public static bool TryGetEntity(Collider2D collider, out Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `TryGetInteractable(Collider2D, out IInteractable)`

```csharp
public static bool TryGetInteractable(Collider2D collider, out IInteractable interactable)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `interactable` | [`IInteractable`](/api/Global.IInteractable) |  |

**Returns:** `bool`

:::

::: details `TryGetProxy(Collider2D, out ProxyCollider)`

```csharp
public static bool TryGetProxy(Collider2D collider, out ProxyCollider proxy)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `collider` | `UnityEngine.Collider2D` |  |
| `proxy` | [`ProxyCollider`](/api/Global.ProxyCollider) |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (92)

*Classes and systems that invoke, reference, or depend on `DewPhysics`:*

[ActionAttackMove](/api/Global.ActionAttackMove) · `Ai_ArcticTerritory` · `Ai_C_BeamOfLight` · `Ai_C_MassProtection` · `Ai_D_SharedPain_Instance` · `Ai_E_SearingCharge` · `Ai_E_StygianRush_Rush` · `Ai_Gem_U_LastStarlight` · `Ai_L_SmallMoltenCore_Dragon_Atk` · `Ai_M_FrostyCharge` · `Ai_MiniBoss_IceAura_AoE` · `Ai_Mon_Despair_BossAzurak_DoubleStomp_Instance` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Ink_Archer_Atk` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_Projectile` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_LavaLand_BossInfernus_Roar_Projectile` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_Atk` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Sky_BossNyx_Blackhole` · `Ai_Mon_Sky_BossNyx_StellarDash` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_Special_BossErebos_Gaze_Instance` · `Ai_Mon_Special_BossErebos_SpawnBlackhole_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Slow` · `Ai_Mon_Special_BossErebos_Teleport` · `Ai_Mon_Special_BossMaw_Chomp_Charge` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossMaw_ShadowOverdrive_Projectile` · `Ai_Mon_Special_BossObliviax_ChargeSequence_MissileAtk` · `Ai_Q_EmbracingTheChill_AreaDoT` · `Ai_R_BackOff_Spawner` · `Ai_R_DancingBlades` · `Ai_R_NaturesWhisper` · `Ai_R_SanctuaryOfEl_Ground` · `Ai_Sky_BossIntruder_Instance` · `Ai_Star_Mist_F_LG_ChainAttack_Phantom` · `Ai_U_WorldCracker` · `Ai_VeilOfDark` · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · [DewCollider](/api/Global.DewCollider) · [Entity](/api/Global.Entity) · [EntityAI](/api/Global.EntityAI) · [EntityCallbackTrigger](/api/Global.EntityCallbackTrigger) · [EntityControl](/api/Global.EntityControl) · `Forest_Fireplace` · `Gem_C_Vengeance` · `Gem_E_Blossom` · `Gem_E_Insight` · `Gem_E_Reflex` · `Gem_L_Paranoia` · `Gem_R_Ricochet` · `Gem_R_Snow` · `Gem_R_Spiral` · `Gem_U_GlacialCore` · `Gem_U_LastStarlight` · `Hero_Bismuth` · `Ink_BossRoomDamageGround` · `LavaLand_IcePlace` · `Mon_GoldenLizard_ElusiveLizard` · `Mon_Special_BossPolaris` · [PickupInstance](/api/Global.PickupInstance) · [Projectile](/api/Global.Projectile) · `Se_D_AstridsMasterpieceEnGarde` · `Se_D_AstridsMasterpiecePriorite` · `Se_D_ChargedAnguillian` · `Se_D_ExoticMatter` · `Se_EngulfedInFlame` · `Se_Gem_R_Hedgehog_Aura` · `Se_GenericStealth` · `Se_M_Charge` · `Se_MiniBoss_IceAura` · `Se_MiniBoss_OrbSpitter` · `Se_MirageSkin_Delusion` · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Pulverization` · `Se_MirageSkin_Sanctification` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Husk_I_ShopIntimidation` · `Se_Star_Mist_F_LG_ChainAttack` · `Se_Star_Nachia_L_SummonBonus` · `Se_Star_Vesper_D_ADWithNearbyBurning` · `Se_U_HerWorld_Blackhole` · `St_C_Starfall` · `Sum_R_AnnoyingBanner` · `Sum_R_SummonLittleBaam_Baam` · [Summon](/api/Global.Summon)

### Dependencies (14)

*Types and components that `DewPhysics` references or depends upon:*

[Actor](/api/Global.Actor) · [CollisionCheckSettings](/api/Global.CollisionCheckSettings) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) · [ICollidableWithProjectile](/api/Global.ICollidableWithProjectile) · [IEntityValidator](/api/Global.IEntityValidator) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [ProxyCollider](/api/Global.ProxyCollider) · `Vector3FlattenExtension` · `VectorPlaneTransformExtension`

:::
