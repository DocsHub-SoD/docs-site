# Class: Dash

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class Dash
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`affectedByMovementSpeed`** | `public bool affectedByMovementSpeed` |  |
| **`canGoOverTerrain`** | `public bool canGoOverTerrain` |  |
| **`distance`** | `public float distance` |  |
| **`duration`** | `public float duration` |  |
| **`ease`** | `public DewEase ease` |  |
| **`rotateForward`** | `public bool rotateForward` |  |
| **`useLinearSweep`** | `public bool useLinearSweep` |  |

:::

## Methods (2)

::: details `ApplyByDestination(Entity, Vector3, Action&lt;DispByDestination&gt;)`

```csharp
public void ApplyByDestination(Entity ent, Vector3 dest, Action<DispByDestination> beforeApply = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `dest` | `UnityEngine.Vector3` |  |
| `beforeApply` | [`System.Action<T><DispByDestination>`](/api/Global.DispByDestination) |  |

:::

::: details `ApplyByDirection(Entity, Vector3, Action&lt;DispByDestination&gt;)`

```csharp
public void ApplyByDirection(Entity ent, Vector3 dir, Action<DispByDestination> beforeApply = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |
| `dir` | `UnityEngine.Vector3` |  |
| `beforeApply` | [`System.Action<T><DispByDestination>`](/api/Global.DispByDestination) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `Dash`:*

`Ai_C_IceClaw` · `Ai_C_MagicSword` · `Ai_D_ScarOfTheWind_DashAtk` · `Ai_Mon_DarkCave_CaveBat_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Adapt_IceClaw` · `Ai_Mon_Primus_BossPrimusAeron_Dash` · `Ai_Mon_Primus_BossPrimusAeron_Rage_DashAttack` · `Ai_R_BlackArbalest` · `Ai_R_ShadowWalk` · `Ai_U_Hysteria_Claw` · [DashAttackInstance](/api/Global.DashAttackInstance)

### Dependencies (4)

*Types and components that `Dash` references or depends upon:*

[Dew](/api/Global.Dew) · [DispByDestination](/api/Global.DispByDestination) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#dewease" class="enum-link" data-tooltip="Linear=0 · EaseInQuad=1 · EaseOutQuad=2 · EaseInOutQuad=3 · EaseInCubic=4 (+27 more)">DewEase</a>

:::
