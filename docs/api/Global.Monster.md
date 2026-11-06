# Class: Monster

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [BossMonster](/api/Global.BossMonster) → [Mon_DreamTeller](/api/Global.Mon_DreamTeller) → [Mon_RedGiant](/api/Global.Mon_RedGiant) → [Mon_RedMan](/api/Global.Mon_RedMan)

```csharp
public class Monster : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chasePredictiveness`** | `[BoxGroup("Monster Settings", true, false, 0)] public float chasePredictiveness` |  |
| **`chaseRandomness`** | `[BoxGroup("Monster Settings", true, false, 0)] public float chaseRandomness` |  |
| **`disableLoot`** | `[NonSerialized] public bool disableLoot` |  |
| **`type`** | `[BoxGroup("Monster Settings", true, false, 0)] public Monster.MonsterType type` |  |

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`campPosition`** | `[SaveVar(SaveVarFlags.Default)] public Vector3? campPosition { get; }` | Available on server. |
| **`defaultOwner`** | `protected override DewPlayer defaultOwner { get; }` |  |
| **`isHunter`** | `public bool isHunter { get; set; }` |  |
| **`populationCost`** | `public float populationCost { get; set; }` |  |
| **`spawnPosOverride`** | `public virtual Vector3? spawnPosOverride { get; }` | Override spawn position for this monster. This has higher priority than all other spawn pos overrides. |
| **`spawnRotOverride`** | `public virtual Quaternion? spawnRotOverride { get; }` | Override spawn rotation for this monster. This has higher priority than all other spawn rot overrides. |

:::

## Methods (5)

::: details `AIUpdate(ref EntityAIContext)`

```csharp
protected override void AIUpdate(ref EntityAIContext context)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `context` | [`EntityAIContext`](/api/Global.EntityAIContext) |  |

:::

::: details `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::
