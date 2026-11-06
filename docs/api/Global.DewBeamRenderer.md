# Class: DewBeamRenderer

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(1100)]
public class DewBeamRenderer : LogicBehaviour, ILogicUpdate
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`acrossEffect`** | `public GameObject acrossEffect` |  |
| **`acrossEffectInterval`** | `[ShowIf("@acrossEffect != null", true)] public float acrossEffectInterval` |  |
| **`endEffect`** | `public GameObject endEffect` |  |
| **`lineRenderer`** | `public LineRenderer lineRenderer` |  |
| **`startEffect`** | `public GameObject startEffect` |  |

:::

## Methods (6)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnDisable()`

```csharp
protected override void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected override void OnEnable()
```

:::

::: details `SetEndPoint(Vector3)`

```csharp
public void SetEndPoint(Vector3 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector3` |  |

:::

::: details `SetPoints(Vector3, Vector3)`

```csharp
public void SetPoints(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

:::

::: details `SetStartPoint(Vector3)`

```csharp
public void SetStartPoint(Vector3 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector3` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (11)

*Classes and systems that invoke, reference, or depend on `DewBeamRenderer`:*

`Ai_Curse_AnchorOfMind_Anchor` · `Ai_D_SharedPain_Instance` · `Ai_E_ClutchesOfMalice_ReachAndPull` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Special_BossErebos_SpawnTormentor_Attacker_Instance` · `Ai_R_SummonLittleBaam_Baam_Atk` · `At_Atk_YubarStardust` · `Se_D_ConvergencePoint` · `Se_MirageSkin_Sanctification_Protected` · `Se_Mon_Sky_BigBaam_Main_Buff_Buffed` · `Se_Q_DeathMark_Marked`

### Dependencies (2)

*Types and components that `DewBeamRenderer` references or depends upon:*

[DewEffect](/api/Global.DewEffect) · [LogicBehaviour](/api/Global.LogicBehaviour)

:::
