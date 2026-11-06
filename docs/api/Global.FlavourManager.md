# Class: FlavourManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [FlavourManager](/api/Global.FlavourManager)

```csharp
public class FlavourManager : NetworkedManagerBase<FlavourManager>, ILogicUpdate, ISettingsChangedCallback
```

## Fields (20)

::: details Click to expand Fields (20)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chanceByRatio`** | `public AnimationCurve chanceByRatio` |  |
| **`damageRatioRange`** | `public Vector2 damageRatioRange` |  |
| **`deviateAngle`** | `public float deviateAngle` |  |
| **`disableOnLesser`** | `public bool disableOnLesser` |  |
| **`everyoneVicinityRadius`** | `public float everyoneVicinityRadius` | Everyone needs to be in this range to the monster for hit stop to occur. |
| **`hitStopDealDamage`** | `[Title("Damage Hit Time Stop", null, TitleAlignments.Left, true, true)] public GameObject hitStopDealDamage` |  |
| **`hitTimeStopCooldownTime`** | `public float hitTimeStopCooldownTime` |  |
| **`ignoreAssists`** | `[Title("Kill Feedback", null, TitleAlignments.Left, true, true)] public bool ignoreAssists` |  |
| **`killFeedback`** | `public GameObject killFeedback` |  |
| **`killFeedbackBoss`** | `public GameObject killFeedbackBoss` |  |
| **`killFeedbackLesser`** | `public GameObject killFeedbackLesser` |  |
| **`killFeedbackMiniBoss`** | `public GameObject killFeedbackMiniBoss` |  |
| **`killingBlowDamageMultiplier`** | `public float killingBlowDamageMultiplier` |  |
| **`minDamageAmount`** | `public float minDamageAmount` |  |
| **`onStunDurationMultiplier`** | `public float onStunDurationMultiplier` |  |
| **`screenKillEffects`** | `public FxVolume[] screenKillEffects` |  |
| **`shakeDamageRatioRange`** | `[Title("Damage Shake", null, TitleAlignments.Left, true, true)] public Vector2 shakeDamageRatioRange` |  |
| **`shakeDuration`** | `public AnimationCurve shakeDuration` |  |
| **`shakeIntensity`** | `public AnimationCurve shakeIntensity` |  |
| **`shakeInterval`** | `public float shakeInterval` |  |

:::

## Methods (4)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (15)

*Types and components that `FlavourManager` references or depends upon:*

[Actor](/api/Global.Actor) · [DewEffect](/api/Global.DewEffect) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoDamage](/api/Global.EventInfoDamage) · [GameManager](/api/Global.GameManager) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [Monster](/api/Global.Monster) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · `VectorPlaneTransformExtension`

:::
