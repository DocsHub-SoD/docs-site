# Class: ChargingChannelData

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class ChargingChannelData
```

## Fields (30)

::: details Click to expand Fields (30)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angleSpeedLimit`** | `[ShowIf("@castMethod.type == CastMethodType.Cone \|\| castMethod.type == CastMethodType.Arrow", true)] public float angleSpeedLimit` |  |
| **`canCancel`** | `[ToggleLeft] public bool canCancel` |  |
| **`cancelAnim`** | `public DewAnimationClip cancelAnim` |  |
| **`cancelEffect`** | `public GameObject cancelEffect` |  |
| **`canMove`** | `[ToggleLeft] public bool canMove` |  |
| **`castAnim`** | `public DewAnimationClip castAnim` |  |
| **`castDazeDuration`** | `public float castDazeDuration` |  |
| **`castEffect`** | `public GameObject castEffect` |  |
| **`castMethod`** | `[HideLabel] public CastMethodData castMethod` |  |
| **`castOnButtonRelease`** | `[ToggleLeft] public bool castOnButtonRelease` |  |
| **`chargeAnim`** | `public DewAnimationClip chargeAnim` |  |
| **`chargeEffect`** | `public GameObject chargeEffect` |  |
| **`chargeFullAnim`** | `public DewAnimationClip chargeFullAnim` |  |
| **`chargeFullDuration`** | `public float chargeFullDuration` |  |
| **`chargeFullEffect`** | `public GameObject chargeFullEffect` |  |
| **`completeAnim`** | `public DewAnimationClip completeAnim` |  |
| **`completeDazeDuration`** | `public float completeDazeDuration` |  |
| **`completeDuration`** | `public float completeDuration` |  |
| **`completeEffect`** | `public GameObject completeEffect` |  |
| **`completeWhenCast`** | `[ToggleLeft] public bool completeWhenCast` |  |
| **`rotateForwardOverrideRoationTime`** | `public float rotateForwardOverrideRoationTime` |  |
| **`rotateForwardWhenCast`** | `[ToggleLeft] public bool rotateForwardWhenCast` |  |
| **`rotateForwardWhenCharging`** | `[ToggleLeft] public bool rotateForwardWhenCharging` |  |
| **`rotateForwardWhenComplete`** | `[ToggleLeft] public bool rotateForwardWhenComplete` |  |
| **`selfSlowAmount`** | `[ShowIf("canMove", true)] public float selfSlowAmount` |  |
| **`selfValidator`** | `[HideLabel] public AbilitySelfValidator selfValidator` |  |
| **`setFillAmount`** | `[ToggleLeft] public bool setFillAmount` |  |
| **`showCastIndicator`** | `[ToggleLeft] public bool showCastIndicator` |  |
| **`showOnScreenTimer`** | `[ToggleLeft] public bool showOnScreenTimer` |  |
| **`targetValidator`** | `[HideLabel] public AbilityTargetValidator targetValidator` |  |

:::

## Methods (1)

::: details `Get(Actor)`

Create charging channel with clone of this data.You can modify the data in the created channel.

```csharp
public ChargingChannel Get(Actor effectParent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effectParent` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `ChargingChannel`

:::
