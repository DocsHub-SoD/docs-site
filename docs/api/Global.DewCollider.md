# Class: DewCollider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewCollider : MonoBehaviour
```

## Fields (10)

::: details Click to expand Fields (10)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`invokeEventsOnClients`** | `[ShowIf("receiveEntityCallbacks", true)] public bool invokeEventsOnClients` |  |
| **`maxDecimals`** | `[ShowIf("@shape == DewCollider.ColliderShape.Polygon", true)] public int maxDecimals` |  |
| **`offset`** | `[ShowIf("@shape == DewCollider.ColliderShape.Box \|\| shape == DewCollider.ColliderShape.Circle", true)] public Vector2 offset` |  |
| **`onEntityEnter`** | `[ShowIf("receiveEntityCallbacks", true)] public UnityEvent<Entity> onEntityEnter` |  |
| **`onEntityExit`** | `[ShowIf("receiveEntityCallbacks", true)] public UnityEvent<Entity> onEntityExit` |  |
| **`points`** | `[ShowIf("@shape == DewCollider.ColliderShape.Polygon", true)] public Vector2[] points` |  |
| **`radius`** | `[ShowIf("@shape == DewCollider.ColliderShape.Circle", true)] public float radius` |  |
| **`receiveEntityCallbacks`** | `public bool receiveEntityCallbacks` |  |
| **`shape`** | `[EnumToggleButtons] public DewCollider.ColliderShape shape` |  |
| **`size`** | `[ShowIf("@shape == DewCollider.ColliderShape.Box", true)] public Vector2 size` |  |

:::

## Methods (16)

::: details `GeneratePointsInCircle(int, float, float, Vector2[])`

```csharp
public static void GeneratePointsInCircle(int count, float radius, float angle, Vector2[] points)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `count` | `int` |  |
| `radius` | `float` |  |
| `angle` | `float` |  |
| `points` | `UnityEngine.Vector2[]` |  |

:::

::: details `GeneratePointsInCircle(int, float, float)`

```csharp
public static Vector2[] GeneratePointsInCircle(int count, float radius, float angle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `count` | `int` |  |
| `radius` | `float` |  |
| `angle` | `float` |  |

**Returns:** `UnityEngine.Vector2[]`

:::

::: details `GeneratePolygonPoints_Arc(float, float, int)`

```csharp
public void GeneratePolygonPoints_Arc(float arcRadius, float arcAngle, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `arcRadius` | `float` |  |
| `arcAngle` | `float` |  |
| `accuracy` | `int` |  |

:::

::: details `GeneratePolygonPoints_ArcDonut(float, float, float, int)`

```csharp
public void GeneratePolygonPoints_ArcDonut(float innerRadius, float outerRadius, float arcAngle = 360, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `innerRadius` | `float` |  |
| `outerRadius` | `float` |  |
| `arcAngle` | `float` |  |
| `accuracy` | `int` |  |

:::

::: details `GeneratePolygonPoints_Circle(float, int)`

```csharp
public void GeneratePolygonPoints_Circle(float circleRadius, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `circleRadius` | `float` |  |
| `accuracy` | `int` |  |

:::

::: details `GeneratePolygonPoints_Donut(float, float, int)`

```csharp
public void GeneratePolygonPoints_Donut(float innerRadius, float outerRadius, int accuracy = 20)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `innerRadius` | `float` |  |
| `outerRadius` | `float` |  |
| `accuracy` | `int` |  |

:::

::: details `GetEntities(out ListReturnHandle&lt;Entity&gt;, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `GetEntities(out ListReturnHandle&lt;Entity&gt;, IBinaryEntityValidator, Entity, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, IBinaryEntityValidator validator, Entity self, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `GetEntities(out ListReturnHandle&lt;Entity&gt;, IEntityValidator, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, IEntityValidator validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `GetEntities(out ListReturnHandle&lt;Entity&gt;, Func&lt;Entity, bool&gt;, CollisionCheckSettings)`

```csharp
public List<Entity> GetEntities(out ListReturnHandle<Entity> handle, Func<Entity, bool> validator, CollisionCheckSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<Entity>` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `settings` | [`CollisionCheckSettings`](/api/Global.CollisionCheckSettings) |  |

**Returns:** `System.Collections.Generic.List<T><Entity>`

:::

::: details `OverlapPoint(Vector2)`

```csharp
public bool OverlapPoint(Vector2 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector2` |  |

**Returns:** `bool`

:::

::: details `SweepEntitiesFromOrigin(int, IBinaryEntityValidator, Entity, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, IBinaryEntityValidator validator, Entity self, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

:::

::: details `SweepEntitiesFromOrigin(int, IEntityValidator, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, IEntityValidator validator, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

:::

::: details `SweepEntitiesFromOrigin(int, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

:::

::: details `SweepEntitiesFromOrigin(int, Func&lt;Entity, bool&gt;, bool)`

```csharp
public IEnumerable<List<Entity>> SweepEntitiesFromOrigin(int iterations, Func<Entity, bool> validator, bool includeUncollidable = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `iterations` | `int` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `includeUncollidable` | `bool` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><System.Collections.Generic.List<T><Entity>>`

:::

::: details `UpdateProxyCollider()`

```csharp
public void UpdateProxyCollider()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (191)

*Classes and systems that invoke, reference, or depend on `DewCollider`:*

`Ai_C_BackStep_Bomb` · `Ai_C_CorrosiveTrails_Gas` · `Ai_C_FlashFreeze` · `Ai_C_PressurePoint` · `Ai_C_Purgatory` · `Ai_C_Starfall` · `Ai_D_ExoticMatter_Projectile` · `Ai_D_Resolve_Push` · `Ai_E_AntiGravity` · `Ai_E_Blink` · `Ai_E_ChainLightning` · `Ai_E_ClutchesOfMalice` · `Ai_E_JusticeGuillotine` · `Ai_E_MassCleanse` · `Ai_E_SliceThroat` · `Ai_E_StygianRush_Rush` · `Ai_E_WinterDive` · `Ai_Gem_C_Void_Explosion` · `Ai_Gem_E_Thunder` · `Ai_Gem_L_SuppressedArcanum` · `Ai_Gem_R_Celestial` · `Ai_Gem_R_Glaciate` · `Ai_Gem_R_Shock_Lightning` · `Ai_Gem_R_Stillness` · `Ai_GlacialBarrier_Spawn` · `Ai_Hatred_Explosion` · `Ai_L_Blizzard_Instance` · `Ai_L_MentalCorruption_Projectile` · `Ai_L_SoulKiller` · `Ai_M_DreamyWaltz_BuffExplosion` · `Ai_MiniBoss_OrbSpitter_Orb` · `Ai_Mon_DarkCave_BossSeeker_PurpleOrb` · `Ai_Mon_DarkCave_BossSeeker_TunnelVision_SecondPoolAtk` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Arrow` · `Ai_Mon_DarkCave_DarkElemental_Barrage_Spawner` · `Ai_Mon_Despair_BossAzurak_AltAtk` · `Ai_Mon_Despair_BossAzurak_StompBlock` · `Ai_Mon_Despair_BossAzurak_StompGlobal` · `Ai_Mon_Despair_BossAzurak_StompProjectile` · `Ai_Mon_Despair_Displacer_SpawnEgg` · `Ai_Mon_Despair_WretchedArtillery_BarrageAtk_Missile` · `Ai_Mon_Forest_BossDemon_DelayedAtk` · `Ai_Mon_Forest_BossDemon_MainSkill_Stomp` · `Ai_Mon_Forest_Hound_Charge` · `Ai_Mon_Ink_Archer_Dodge` · `Ai_Mon_Ink_BossDarkMoon_AltAtk_FirstAtk` · `Ai_Mon_Ink_BossDarkMoon_Blade_Instance` · `Ai_Mon_Ink_BossDarkMoon_Blade_RageInstance` · `Ai_Mon_Ink_BossDarkMoon_Eclipse_Instance` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_Ink_BossDarkMoon_ShortDash_Atk` · `Ai_Mon_Ink_BossDarkMoon_SpawnEgoSword_Projectile` · `Ai_Mon_Ink_BossDarkMoon_Spear_Instance` · `Ai_Mon_Ink_BossDarkMoon_ThrowSpear_TeleportAtk_AfterAtk` · `Ai_Mon_Ink_BossWhiteNight_BuddhasPalm_Instance` · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_Eclipse` · `Ai_Mon_Ink_BossWhiteNight_DestructionWave_Wave` · `Ai_Mon_Ink_BossWhiteNight_EnergyWave_Instance` · `Ai_Mon_Ink_BossWhiteNight_OneInchPunch_Pull` · `Ai_Mon_Ink_BossWhiteNight_Oppression` · `Ai_Mon_Ink_BossWhiteNight_RageInstance` · `Ai_Mon_Ink_BossWhiteNight_RageInstance_Rock` · `Ai_Mon_Ink_DivineAnimal_Bite` · `Ai_Mon_Ink_DivineAnimal_Missile_Sub` · `Ai_Mon_Ink_DivineAnimal_Stomp` · `Ai_Mon_Ink_EgoSword_Atk` · `Ai_Mon_Ink_GhostBlade_DemolitionMan` · `Ai_Mon_Ink_GhostBlade_MeleeAtk` · `Ai_Mon_Ink_GhostBlade_SwiftStep_Atk` · `Ai_Mon_Ink_GhostSpear_Atk` · `Ai_Mon_Ink_Tiger_DashAtk` · `Ai_Mon_LavaLand_BossInfernus_Dash` · `Ai_Mon_LavaLand_FireElemental_DestructSub` · `Ai_Mon_LavaLand_FireElemental_ExplosionSub` · `Ai_Mon_LavaLand_FireElemental_LaserAtk` · `Ai_Mon_LavaLand_Magmadon_Charge` · `Ai_Mon_LavaLand_Magmadon_Charge_Projectile` · `Ai_Mon_LavaLand_SuperheatedWolf_SelfDestruct` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Force_Grab` · `Ai_Mon_Primus_SpawnAttack` · `Ai_Mon_Sky_Baam_Teleport` · `Ai_Mon_Sky_BigBaam_Main_Root` · `Ai_Mon_Sky_BigBaam_RangedAtk` · `Ai_Mon_Sky_BossNyx_PillarOfStars` · `Ai_Mon_Sky_BossNyx_Swipe` · `Ai_Mon_Sky_LittleBaam_Atk` · `Ai_Mon_Sky_StellaMatter_AtkSub` · `Ai_Mon_Sky_StellaMatter_Die` · `Ai_Mon_Sky_StellaMatter_Throw` · `Ai_Mon_Sky_StellaMatter_ThrowSub` · `Ai_Mon_SnowMountain_BossSkoll_AuraBlade` · `Ai_Mon_SnowMountain_BossSkoll_AuraSlice` · `Ai_Mon_SnowMountain_BossSkoll_SummonArrow_Instance` · `Ai_Mon_SnowMountain_LivingShards_Atk` · `Ai_Mon_SnowMountain_VikingWarrior_Shield` · `Ai_Mon_SnowMountain_VikingWarrior_ThrowShield` · `Ai_Mon_Special_BossErebos_AtkInstance` · `Ai_Mon_Special_BossErebos_Meteor` · `Ai_Mon_Special_BossErebos_StarRain_Instance` · `Ai_Mon_Special_BossErebos_Teleport_Instance` · `Ai_Mon_Special_BossLightElemental_Beam` · `Ai_Mon_Special_BossLightElemental_BeamAtk_Spawner` · `Ai_Mon_Special_BossLightElemental_Lightning_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction_Instance` · `Ai_Mon_Special_BossMaw_Chomp_DashAtk` · `Ai_Mon_Special_BossMaw_ShadowWalk` · `Ai_Mon_Special_BossMaw_SliceThroat_Atk` · `Ai_Mon_Special_BossObliviax_Artillery_Instance` · `Ai_Mon_Special_BossObliviax_BackStep_Instance` · `Ai_Mon_Special_BossObliviax_ChargeSequence_Spawner` · `Ai_Mon_Special_BossObliviax_DashAtk` · `Ai_Mon_Special_BossObliviax_TurnAtk` · `Ai_Mon_Special_BossObliviax_TurnAtk_DelayedAtk` · `Ai_Mon_Special_BossObliviax_TurretMode_Projectile` · `Ai_Mon_Special_BossPolaris_Holy_Beam_GravityPull` · `Ai_Nor_CosmicBlast` · `Ai_QR_InfernalTales` · `Ai_QR_Innocence_Spawner` · `Ai_QR_ValiantHeart` · `Ai_Q_EtherealInfluence` · `Ai_Q_Fleche_Dash` · `Ai_Q_GoldenBurst` · `Ai_Q_HandCannon` · `Ai_Q_IncendiaryRounds_Attack` · `Ai_Q_Laceration_Circle` · `Ai_Q_Lunge` · `Ai_Q_Riposte` · `Ai_Q_SuperNova` · `Ai_R_BackOff_Damage` · `Ai_R_BladeFan` · `Ai_R_ChainReaction` · `Ai_R_Fireball` · `Ai_R_Frostbite_Freeze` · `Ai_R_GlacialHammer` · `Ai_R_GreatFrostSword` · `Ai_R_Ignite` · `Ai_R_Inspire_Roar` · `Ai_R_PhantomBlade` · `Ai_R_PhaseShift` · `Ai_R_PillarOfFlame` · `Ai_R_ShadowWalk` · `Ai_R_Smite` · `Ai_R_StaticDischarge` · `Ai_R_WarBoomerang` · `Ai_Star_Yubar_F_SN_Pull` · `Ai_U_BeamOfBalance_Beam` · `Ai_U_Hysteria_Claw` · `Ai_UnstableRatSwarm_Projectile` · [DamageInstance](/api/Global.DamageInstance) · [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) · [EntityCallbackTrigger](/api/Global.EntityCallbackTrigger) · `Gem_E_Pain` · `Gem_L_Embertail` · `Gem_L_Paranoia` · `Gem_L_SolarEye` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · [Pickup_RegenOrb](/api/Global.Pickup_RegenOrb) · `Primus_Pizza0` · [RoomSection](/api/Global.RoomSection) · [Room_Barrier](/api/Global.Room_Barrier) · [Room_Trap_ProximityActivator](/api/Global.Room_Trap_ProximityActivator) · [Room_Waypoint](/api/Global.Room_Waypoint) · `Se_C_IceBlock` · `Se_D_ConvergencePoint` · `Se_FatalHitProtection_Invulnerable` · `Se_Gem_R_Wound_Wounded` · `Se_L_Multishot_Buff` · `Se_L_PyranasFireball` · `Se_M_Charge` · `Se_MiniBoss_UnstableExplosive_Explosion` · `Se_Mon_Despair_BossAzurak_RoarAtk_SafeZoneSpawner` · `Se_Mon_Ink_BossWhiteNight_Rush` · `Se_Mon_Ink_Boss_PhaseChange` · `Se_Mon_Primus_BossPrimusAeron_PhaseSwitcher` · `Se_Mon_Sky_BossNyx_PhaseChange` · `Se_Nor_MyOwnLittleNebula` · `Se_Nor_WindowToTheSoul_SpiritualDominance` · `Se_Nor_WindowToTheSoul_WeaknessRevealed` · `Se_R_BoneCrusher` · `Se_R_Parry_Start` · `Se_R_RepulsiveShield` · `Se_R_UnbreakableDetermination` · `Se_Treasure_FragmentOfDetermination_Invulnerable` · `Shrine_Guidance` · `Shrine_PrimusDoor` · `SpawnGemStarProp` · `St_D_SalamanderPowder` · `StarlessPath_BossPolarisManager` · `Trap_FlameJet`

### Dependencies (11)

*Types and components that `DewCollider` references or depends upon:*

[Actor](/api/Global.Actor) · [CollisionCheckSettings](/api/Global.CollisionCheckSettings) · [DewPhysics](/api/Global.DewPhysics) · [DewPool](/api/Global.DewPool) · [Entity](/api/Global.Entity) · [EntityCallbackTrigger](/api/Global.EntityCallbackTrigger) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) · [IEntityValidator](/api/Global.IEntityValidator) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1)

:::
