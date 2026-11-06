# Class: Hero

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity)

```csharp
[RequireComponent(typeof(HeroSkill))]
public class Hero : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (26)

::: details Click to expand Fields (26)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessories`** | `[SaveVar(SaveVarFlags.Default)] public readonly SyncList<string> accessories` |  |
| **`cDestruction`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cDestruction` |  |
| **`cDisplayBaseAngle`** | `[BoxGroup("Constellation Settings", true, false, 0)] public float cDisplayBaseAngle` |  |
| **`cFlexible`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cFlexible` |  |
| **`cImagination`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cImagination` |  |
| **`classType`** | `[BoxGroup("Hero Settings", true, false, 0)] public Hero.HeroClassType classType` |  |
| **`ClientHeroEvent_OnIsInCombatChanged`** | `public SafeAction<bool> ClientHeroEvent_OnIsInCombatChanged` |  |
| **`ClientHeroEvent_OnKillOrAssist`** | `public SafeAction<EventInfoKill> ClientHeroEvent_OnKillOrAssist` |  |
| **`ClientHeroEvent_OnKnockedOut`** | `public SafeAction<EventInfoKill> ClientHeroEvent_OnKnockedOut` |  |
| **`ClientHeroEvent_OnLevelChanged`** | `public SafeAction<EventInfoHeroLevelUp> ClientHeroEvent_OnLevelChanged` |  |
| **`ClientHeroEvent_OnRevive`** | `public SafeAction<Hero> ClientHeroEvent_OnRevive` |  |
| **`ClientHeroEvent_OnSkillUse`** | `public SafeAction<EventInfoSkillUse> ClientHeroEvent_OnSkillUse` |  |
| **`cLife`** | `[BoxGroup("Constellation Settings", true, false, 0)] public HeroConstellationSettings cLife` |  |
| **`decoConstellationPrefab`** | `[BoxGroup("Hero Settings", true, false, 0)] public GameObject decoConstellationPrefab` |  |
| **`difficulty`** | `[BoxGroup("Hero Settings", true, false, 0)] public Hero.HeroDifficulty difficulty` |  |
| **`dismantleProcessor`** | `public DataProcessorGroup<int, Hero, Actor> dismantleProcessor` |  |
| **`excludeFromPool`** | `[BoxGroup("Hero Settings", true, false, 0)] public bool excludeFromPool` |  |
| **`HeroEvent_OnAbilityInstanceBeforePrepareFromSkill`** | `public SafeAction<EventInfoSkillAbilityInstance> HeroEvent_OnAbilityInstanceBeforePrepareFromSkill` |  |
| **`HeroEvent_OnAbilityInstanceCreatedFromSkill`** | `public SafeAction<EventInfoSkillAbilityInstance> HeroEvent_OnAbilityInstanceCreatedFromSkill` |  |
| **`icon`** | `[BoxGroup("Hero Settings", true, false, 0)] public Sprite icon` |  |
| **`InCombatCheckInterval`** | `public const float InCombatCheckInterval = 0.5` |  |
| **`isWeaponHolstered`** | `[NonSerialized] public bool isWeaponHolstered` | Checked locally. |
| **`mainColor`** | `[BoxGroup("Hero Settings", true, false, 0)] public Color mainColor` |  |
| **`MarkAsInCombatDuration`** | `public const float MarkAsInCombatDuration = 2` |  |
| **`maxLevelOverride`** | `public int? maxLevelOverride` |  |
| **`summons`** | `[NonSerialized] public List<Summon> summons` | Available everywhere. |

:::

## Properties (9)

::: details Click to expand Properties (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`exp`** | `[SaveVar(SaveVarFlags.ApplyAfterCreation)] public int exp { get; }` |  |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`isInCombat`** | `public bool isInCombat { get; }` | Did this hero dealt damage to an enemy or took damage from an enemy?Available everywhere. |
| **`isKnockedOut`** | `public bool isKnockedOut { get; }` |  |
| **`loadout`** | `public HeroLoadoutData loadout { get; set; }` |  |
| **`maxExp`** | `public int maxExp { get; }` |  |
| **`maxLevel`** | `public int maxLevel { get; }` |  |
| **`Skill`** | `public HeroSkill Skill { get; }` |  |
| **`skin`** | `public string skin { get; set; }` |  |

:::

## Methods (19)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CmdTeleportToWaypoint(Room_Waypoint)`

```csharp
public void CmdTeleportToWaypoint(Room_Waypoint waypoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `waypoint` | [`Room_Waypoint`](/api/Global.Room_Waypoint) |  |

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetConstellationSettings(StarType)`

```csharp
public HeroConstellationSettings GetConstellationSettings(StarType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`StarType`](/api/Global.StarType) |  |

**Returns:** `HeroConstellationSettings`

:::

::: details `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

:::

::: details `IsMeleeHero()`

```csharp
public bool IsMeleeHero()
```

**Returns:** `bool`

:::

::: details `IsRangedHero()`

```csharp
public bool IsRangedHero()
```

**Returns:** `bool`

:::

::: details `LoadEntityModelLocal()`

```csharp
public override void LoadEntityModelLocal()
```

:::

::: details `MarkAsInCombat()`

```csharp
public void MarkAsInCombat()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnModelLoaded()`

```csharp
public override void OnModelLoaded()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartAuthority()`

```csharp
public override void OnStartAuthority()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopAuthority()`

```csharp
public override void OnStopAuthority()
```

:::

::: details `ReceiveExperience(int)`

Add to experience of this hero.

```csharp
public void ReceiveExperience(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

:::
