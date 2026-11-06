# Class: TriggerConfig

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class TriggerConfig
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`alwaysCastImmediately`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool alwaysCastImmediately` |  |
| **`appliedStatusEffectRef`** | `[HideIf("isActive", true)] public StatusEffect appliedStatusEffectRef` |  |
| **`canConsumeCastBonus`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool canConsumeCastBonus` |  |
| **`canReceiveCooldownReduction`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [LabelText("Can Receive Cooldown Reduction")] public bool canReceiveCooldownReduction` |  |
| **`castByMoveDirectionByDefault`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool castByMoveDirectionByDefault` |  |
| **`castByMoveDirectionGamepad`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool castByMoveDirectionGamepad` |  |
| **`castMethod`** | `[ShowIf("isActive", true)] [HideLabel] [BoxGroup("B", false, false, 0)] public CastMethodData castMethod` | You must callAbilityTrigger.SyncCastMethodChangesafter modifying this on server. |
| **`castVoice`** | `[ShowIf("isActive", true)] public DewAudioClip castVoice` |  |
| **`channel`** | `[HideLabel] [ShowIf("isActive", true)] public TriggerChannelData channel` |  |
| **`destroyExistingEffect`** | `[ShowIf("@(spawnedInstance is StatusEffect)", true)] public bool destroyExistingEffect` |  |
| **`effectOnCast`** | `[ShowIf("isActive", true)] [LabelText("Channel Effect")] public GameObject effectOnCast` |  |
| **`endAnim`** | `[ShowIf("isActive", true)] public DewAnimationClip endAnim` |  |
| **`faceForward`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [LabelText("Face Forward When Cast")] [HideIf("@castMethod.type == CastMethodType.None \|\| !isActive", true)] public bool faceForward` |  |
| **`ignoreAbilityLock`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool ignoreAbilityLock` |  |
| **`ignoreAimDirectionGamepad`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool ignoreAimDirectionGamepad` |  |
| **`ignoreBlock`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [LabelText("Ignore Channel Block")] [HideIf("@!isActive", true)] public bool ignoreBlock` |  |
| **`isActive`** | `[VerticalGroup("HorizontalC/VerticalA", 0)] public bool isActive` |  |
| **`lockCastUntilKilled`** | `[ToggleLeft] public bool lockCastUntilKilled` |  |
| **`lockCooldownUntilKilled`** | `[ToggleLeft] public bool lockCooldownUntilKilled` |  |
| **`moveTowardsCastDirection`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [ShowIf("isActive", true)] public bool moveTowardsCastDirection` |  |
| **`overrideRotation`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [ShowIf("@isActive && faceForward", true)] public bool overrideRotation` |  |
| **`overrideRotationDuration`** | `[BoxGroup("A", false, false, 0)] [LabelText("Duration")] [ShowIf("@overrideRotation && isActive", true)] public float overrideRotationDuration` |  |
| **`postDelay`** | `[ShowIf("isActive", true)] public float postDelay` |  |
| **`postponeBasicCommand`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [LabelText("Continue Basic Command Afterwards")] [ShowIf("isActive", true)] public bool postponeBasicCommand` |  |
| **`predictionSettings`** | `[ShowIf("isActive", true)] public AbilityTrigger.PredictionSettings predictionSettings` |  |
| **`selfValidator`** | `[HideLabel] [BoxGroup("A", false, false, 0)] [ShowIf("isActive", true)] public AbilitySelfValidator selfValidator` |  |
| **`setFillAmount`** | `[ShowIf("IsStatusEffectNonTargeted", true)] public bool setFillAmount` |  |
| **`spawnedInstanceRef`** | `[InfoBox("StatusEffect will be applied to the caster.", "IsStatusEffectNonTargeted")] [ShowIf("isActive", true)] public AssetRef<AbilityInstance> spawnedInstanceRef` |  |
| **`startAnim`** | `[FormerlySerializedAs("animation")] [ShowIf("isActive", true)] public DewAnimationClip startAnim` |  |
| **`startCharges`** | `[HorizontalGroup("HorizontalB", 0, 0, 0, 0)] [LabelText("Start")] [LabelWidth(55)] [SerializeField] [JsonProperty] public int startCharges` |  |
| **`targetValidator`** | `[ShowIf("isActive", true)] [HideLabel] public AbilityTargetValidator targetValidator` |  |
| **`triggerIcon`** | `[PreviewField(ObjectFieldAlignment.Left, Height = 40)] [HideLabel] [HorizontalGroup("HorizontalC", 40, 0, 0, 0)] public Sprite triggerIcon` |  |
| **`unstoppableWhileCasting`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool unstoppableWhileCasting` |  |
| **`victim`** | `[ShowIf("@(spawnedInstance is StatusEffect) && (castMethod.type == CastMethodType.Target)", true)] public TriggerConfig.StatusEffectVictimType victim` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedCharges`** | `public int addedCharges { get; set; }` |  |
| **`appliedStatusEffect`** | `public StatusEffect appliedStatusEffect { get; set; }` |  |
| **`cooldownTime`** | `public float cooldownTime { get; set; }` |  |
| **`effectiveRange`** | `public float effectiveRange { get; }` |  |
| **`manaCost`** | `public float manaCost { get; set; }` |  |
| **`maxCharges`** | `public int maxCharges { get; set; }` |  |
| **`minimumDelay`** | `public float minimumDelay { get; set; }` |  |
| **`spawnedInstance`** | `public AbilityInstance spawnedInstance { get; set; }` |  |

## Methods

### `CheckRange(CastInfo)`

Returns true if provided info can be casted immediately.Returns false if provided info needs further movement to get in range.You may call this regardless of cast method type,But note that CastMethodType.Point will always return true if isClamping is true.

```csharp
public bool CheckRange(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `bool`

### `CheckRange(Entity, Entity)`

```csharp
public bool CheckRange(Entity caster, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `caster` | [`Entity`](/api/Global.Entity) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `GetMoveToCastDestination(CastInfo)`

Get move-to-cast destination.

```csharp
public Vector3 GetMoveToCastDestination(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `UnityEngine.Vector3`

### `GetMoveToCastRequiredDistance(CastInfo)`

Get move-to-cast required distance on XZ plane (agent position).

```csharp
public float GetMoveToCastRequiredDistance(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `float`

### `IsStatusEffectNonTargeted()`

```csharp
public bool IsStatusEffectNonTargeted()
```

**Returns:** `bool`
