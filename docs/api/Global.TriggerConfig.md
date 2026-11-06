# Class: TriggerConfig

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class TriggerConfig
```

## Fields (34)

::: details Click to expand Fields (34)

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
| **`startAnim`** | `[FormerlySerializedAs] [FormerlySerializedAs("animation")] [ShowIf("isActive", true)] public DewAnimationClip startAnim` |  |
| **`startCharges`** | `[SerializeField] [JsonProperty] [HorizontalGroup("HorizontalB", 0, 0, 0, 0)] [LabelText("Start")] [LabelWidth(55)] [SerializeField] [JsonProperty] public int startCharges` |  |
| **`targetValidator`** | `[ShowIf("isActive", true)] [HideLabel] public AbilityTargetValidator targetValidator` |  |
| **`triggerIcon`** | `[PreviewField(ObjectFieldAlignment.Left, Height = 40)] [HideLabel] [HorizontalGroup("HorizontalC", 40, 0, 0, 0)] public Sprite triggerIcon` |  |
| **`unstoppableWhileCasting`** | `[BoxGroup("A", false, false, 0)] [ToggleLeft] [HideIf("@!isActive", true)] public bool unstoppableWhileCasting` |  |
| **`victim`** | `[ShowIf("@(spawnedInstance is StatusEffect) && (castMethod.type == CastMethodType.Target)", true)] public TriggerConfig.StatusEffectVictimType victim` |  |

:::

## Properties (8)

::: details Click to expand Properties (8)

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

:::

## Methods (5)

::: details `CheckRange(CastInfo)`

Returns true if provided info can be casted immediately.Returns false if provided info needs further movement to get in range.You may call this regardless of cast method type,But note that CastMethodType.Point will always return true if isClamping is true.

```csharp
public bool CheckRange(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `bool`

:::

::: details `CheckRange(Entity, Entity)`

```csharp
public bool CheckRange(Entity caster, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `caster` | [`Entity`](/api/Global.Entity) |  |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `GetMoveToCastDestination(CastInfo)`

Get move-to-cast destination.

```csharp
public Vector3 GetMoveToCastDestination(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetMoveToCastRequiredDistance(CastInfo)`

Get move-to-cast required distance on XZ plane (agent position).

```csharp
public float GetMoveToCastRequiredDistance(CastInfo info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `float`

:::

::: details `IsStatusEffectNonTargeted()`

```csharp
public bool IsStatusEffectNonTargeted()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (55)

*Classes and systems that invoke, reference, or depend on `TriggerConfig`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [ActionAttackMove](/api/Global.ActionAttackMove) · [ActionCast](/api/Global.ActionCast) · `Ai_Mon_SnowMountain_VikingWarrior_Atk` · `At_Mon_Special_BossErebos_Ripple` · [AttackProjectile](/api/Global.AttackProjectile) · [AttackTrigger](/api/Global.AttackTrigger) · [ControlManager](/api/Global.ControlManager) · [EntityAI](/api/Global.EntityAI) · [EntityControl](/api/Global.EntityControl) · [GameResultManager](/api/Global.GameResultManager) · `Gem_E_Flexibility` · `Gem_E_Opportunity` · `Gem_L_ChaosApple` · `Gem_L_Paranoia` · [MeleeAttackInstance](/api/Global.MeleeAttackInstance) · `Mon_Despair_Displacer` · `Mon_Despair_ParalyticFly` · `Mon_Forest_Hound` · `Mon_Forest_SpiderSpitter` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_DivineAnimal` · `Mon_LavaLand_FireElemental` · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Rooter` · `Mon_Sky_BossNyx` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · `Mon_Special_BossErebos` · `Mon_Special_BossObliviax` · `Mon_Special_BossPolaris` · [PingManager](/api/Global.PingManager) · `Se_D_IceColdPresence` · `Se_HunterBuff` · `Se_R_UnbreakableDetermination` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Se_Star_Bismuth_F_IN_MoreProjByAtkSpd` · `Se_Star_Bismuth_F_VH_FullCharge` · `Se_Star_Lacerta_F_QT_AddedCharges` · [SkillTrigger](/api/Global.SkillTrigger) · `St_Q_Laceration` · `Star_Global_DodgeAbilityCooldown` · `Star_Lacerta_QuickTrigger` · `Star_Mist_AddDodgeCharge` · `Sum_R_SummonLittleBaam_Baam` · `UI_Dev_ConsoleSelectedEntityInfo` · `UI_InGame_HeroDetailWindow` · `UI_InGame_HeroDetailWindow_StatItem` · `UI_InGame_MovementSkillIndicator` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_SkillButton` · `UI_Lobby_SelectedHeroInfo_HeroStat` · `UI_Tooltip_SkillCooldown` · `UI_Tooltip_SkillMaxCharges`

### Dependencies (19)

*Types and components that `TriggerConfig` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [AbilitySelfValidator](/api/Global.AbilitySelfValidator) · [AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · [AssetRef`1](/api/Global.AssetRef`1) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [DewAnimationClip](/api/Global.DewAnimationClip) · [DewAudioClip](/api/Global.DewAudioClip) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [ICastMethodDataPoint](/api/Global.ICastMethodDataPoint) · [ICastMethodDataTarget](/api/Global.ICastMethodDataTarget) · [StatusEffect](/api/Global.StatusEffect) · [TriggerChannelData](/api/Global.TriggerChannelData) · [VariantDef](/api/Global.VariantDef) · `VectorPlaneTransformExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`CastMethodType`](/enums#castmethodtype)

:::
