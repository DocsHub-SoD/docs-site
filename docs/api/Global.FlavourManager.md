# Class: FlavourManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [FlavourManager](/api/Global.FlavourManager)

```csharp
public class FlavourManager : NetworkedManagerBase<FlavourManager>, ILogicUpdate, ISettingsChangedCallback
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`chanceByRatio`** | `public AnimationCurve chanceByRatio` |  |
| **`damageRatioRange`** | `public Vector2 damageRatioRange` |  |
| **`deviateAngle`** | `public float deviateAngle` |  |
| **`disableOnLesser`** | `public bool disableOnLesser` |  |
| **`everyoneVicinityRadius`** | `public float everyoneVicinityRadius` | Everyone needs to be in this range to the monster for hit stop to occur. |
| **`hitStopDealDamage`** | `[Title("Damage Hit Time Stop", null, TitleAlignments.Left, true, true)]
public GameObject hitStopDealDamage` |  |
| **`hitTimeStopCooldownTime`** | `public float hitTimeStopCooldownTime` |  |
| **`ignoreAssists`** | `[Title("Kill Feedback", null, TitleAlignments.Left, true, true)]
public bool ignoreAssists` |  |
| **`killFeedback`** | `public GameObject killFeedback` |  |
| **`killFeedbackBoss`** | `public GameObject killFeedbackBoss` |  |
| **`killFeedbackLesser`** | `public GameObject killFeedbackLesser` |  |
| **`killFeedbackMiniBoss`** | `public GameObject killFeedbackMiniBoss` |  |
| **`killingBlowDamageMultiplier`** | `public float killingBlowDamageMultiplier` |  |
| **`minDamageAmount`** | `public float minDamageAmount` |  |
| **`onStunDurationMultiplier`** | `public float onStunDurationMultiplier` |  |
| **`screenKillEffects`** | `public FxVolume[] screenKillEffects` |  |
| **`shakeDamageRatioRange`** | `[Title("Damage Shake", null, TitleAlignments.Left, true, true)]
public Vector2 shakeDamageRatioRange` |  |
| **`shakeDuration`** | `public AnimationCurve shakeDuration` |  |
| **`shakeIntensity`** | `public AnimationCurve shakeIntensity` |  |
| **`shakeInterval`** | `public float shakeInterval` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```
