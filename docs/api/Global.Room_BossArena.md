# Class: Room_BossArena

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [Room_BossArena](/api/Global.Room_BossArena)

```csharp
public class Room_BossArena : SingletonBehaviour<Room_BossArena>
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`radius`** | `public float radius` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`center`** | `public Vector3 center { get; }` |  |

:::

## Methods (2)

::: details `GetRandomPathablePosition()`

```csharp
public Vector3 GetRandomPathablePosition()
```

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetRandomPosition()`

```csharp
public Vector3 GetRandomPosition()
```

**Returns:** `UnityEngine.Vector3`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `Room_BossArena`:*

`Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Special_BossMaw_Purgatory_Trap` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `At_Mon_Special_BossMaw_Purgatory` · `Mon_Special_BossPolaris` · `Primus_Pizza0` · `Se_Mon_Primus_BossPrimusAeron_Adapt_Doom_Initial` · `Se_Mon_Primus_BossPrimusAeron_Force_GoldRain`

### Dependencies (3)

*Types and components that `Room_BossArena` references or depends upon:*

[Dew](/api/Global.Dew) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1) · `VectorPlaneTransformExtension`

:::
