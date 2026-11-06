# Class: ControlManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ControlManager](/api/Global.ControlManager)

```csharp
[LogicUpdatePriority(-500)]
public class ControlManager : ManagerBase<ControlManager>, ILogicUpdate
```

## Fields (76)

::: details Click to expand Fields (76)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`aimPointUi`** | `public GameObject aimPointUi` |  |
| **`attackMarker`** | `public CommandMarker attackMarker` |  |
| **`DirectionalControlStandStillActionGracePeriod`** | `public const float DirectionalControlStandStillActionGracePeriod = 0.3` |  |
| **`dismantleConstraint`** | `[NonSerialized] public Func<Object, bool> dismantleConstraint` |  |
| **`dropConstraint`** | `[NonSerialized] public Func<Object, bool> dropConstraint` |  |
| **`gemLocationConstraint`** | `[NonSerialized] public HeroSkillLocation? gemLocationConstraint` |  |
| **`HeroSkillTypes`** | `public static readonly HeroSkillLocation[] HeroSkillTypes` |  |
| **`interactMarker`** | `public CommandMarker interactMarker` |  |
| **`isDismantleDisabled`** | `[NonSerialized] public bool isDismantleDisabled` |  |
| **`isDodgeDisabled`** | `[NonSerialized] public bool isDodgeDisabled` |  |
| **`isEditSkillDisabled`** | `[NonSerialized] public bool isEditSkillDisabled` |  |
| **`isMainSkillDisabled`** | `[NonSerialized] public bool isMainSkillDisabled` |  |
| **`isWorldMapDisabled`** | `[NonSerialized] public bool isWorldMapDisabled` |  |
| **`it_attackInPlace`** | `public DewInputTrigger it_attackInPlace` |  |
| **`it_attackMoveImmediately`** | `public DewInputTrigger it_attackMoveImmediately` |  |
| **`it_attackMoveNormal`** | `public DewInputTrigger it_attackMoveNormal` |  |
| **`it_attackMoveOnRelease`** | `public DewInputTrigger it_attackMoveOnRelease` |  |
| **`it_cancelNormalCast`** | `public DewInputTrigger it_cancelNormalCast` |  |
| **`it_confirmCast`** | `public DewInputTrigger it_confirmCast` |  |
| **`it_editSkillHold`** | `public DewInputTrigger it_editSkillHold` |  |
| **`it_editSkillToggle`** | `public DewInputTrigger it_editSkillToggle` |  |
| **`it_interact`** | `public DewInputTrigger it_interact` |  |
| **`it_interactAlt`** | `public DewInputTrigger it_interactAlt` |  |
| **`it_move`** | `public DewInputTrigger it_move` |  |
| **`it_moveDown`** | `public DewInputTrigger it_moveDown` |  |
| **`it_moveLeft`** | `public DewInputTrigger it_moveLeft` |  |
| **`it_moveRight`** | `public DewInputTrigger it_moveRight` |  |
| **`it_moveUp`** | `public DewInputTrigger it_moveUp` |  |
| **`it_ping`** | `public DewInputTrigger it_ping` |  |
| **`it_scoreboard`** | `public DewInputTrigger it_scoreboard` |  |
| **`it_showDetails`** | `public DewInputTrigger it_showDetails` |  |
| **`it_skillE`** | `public DewInputTrigger it_skillE` |  |
| **`it_skillEEdit`** | `public DewInputTrigger it_skillEEdit` |  |
| **`it_skillEImmediately`** | `public DewInputTrigger it_skillEImmediately` |  |
| **`it_skillENormal`** | `public DewInputTrigger it_skillENormal` |  |
| **`it_skillEOnRelease`** | `public DewInputTrigger it_skillEOnRelease` |  |
| **`it_skillESelf`** | `public DewInputTrigger it_skillESelf` |  |
| **`it_skillIdentityEdit`** | `public DewInputTrigger it_skillIdentityEdit` |  |
| **`it_skillMovement`** | `public DewInputTrigger it_skillMovement` |  |
| **`it_skillMovementImmediately`** | `public DewInputTrigger it_skillMovementImmediately` |  |
| **`it_skillMovementNormal`** | `public DewInputTrigger it_skillMovementNormal` |  |
| **`it_skillMovementOnRelease`** | `public DewInputTrigger it_skillMovementOnRelease` |  |
| **`it_skillQ`** | `public DewInputTrigger it_skillQ` |  |
| **`it_skillQEdit`** | `public DewInputTrigger it_skillQEdit` |  |
| **`it_skillQImmediately`** | `public DewInputTrigger it_skillQImmediately` |  |
| **`it_skillQNormal`** | `public DewInputTrigger it_skillQNormal` |  |
| **`it_skillQOnRelease`** | `public DewInputTrigger it_skillQOnRelease` |  |
| **`it_skillQSelf`** | `public DewInputTrigger it_skillQSelf` |  |
| **`it_skillR`** | `public DewInputTrigger it_skillR` |  |
| **`it_skillREdit`** | `public DewInputTrigger it_skillREdit` |  |
| **`it_skillRImmediately`** | `public DewInputTrigger it_skillRImmediately` |  |
| **`it_skillRNormal`** | `public DewInputTrigger it_skillRNormal` |  |
| **`it_skillROnRelease`** | `public DewInputTrigger it_skillROnRelease` |  |
| **`it_skillRSelf`** | `public DewInputTrigger it_skillRSelf` |  |
| **`it_skillW`** | `public DewInputTrigger it_skillW` |  |
| **`it_skillWEdit`** | `public DewInputTrigger it_skillWEdit` |  |
| **`it_skillWImmediately`** | `public DewInputTrigger it_skillWImmediately` |  |
| **`it_skillWNormal`** | `public DewInputTrigger it_skillWNormal` |  |
| **`it_skillWOnRelease`** | `public DewInputTrigger it_skillWOnRelease` |  |
| **`it_skillWSelf`** | `public DewInputTrigger it_skillWSelf` |  |
| **`it_spectatorNextTarget`** | `public DewInputTrigger it_spectatorNextTarget` |  |
| **`it_stop`** | `public DewInputTrigger it_stop` |  |
| **`it_travelVote`** | `public DewInputTrigger it_travelVote` |  |
| **`it_travelVoteCancel`** | `public DewInputTrigger it_travelVoteCancel` |  |
| **`it_worldMap`** | `public DewInputTrigger it_worldMap` |  |
| **`it_zoomInCamera`** | `public DewInputTrigger it_zoomInCamera` |  |
| **`it_zoomOutCamera`** | `public DewInputTrigger it_zoomOutCamera` |  |
| **`moveMarker`** | `public CommandMarker moveMarker` |  |
| **`noTargetIndicator`** | `public GameObject noTargetIndicator` |  |
| **`noTargetIndicatorParent`** | `public Transform noTargetIndicatorParent` |  |
| **`onCastFailed`** | `public Action<AbilityTrigger> onCastFailed` |  |
| **`onFocusedInteractableChanged`** | `public Action<IInteractable> onFocusedInteractableChanged` |  |
| **`onSelectedEntityChanged`** | `public Action<Entity, Entity> onSelectedEntityChanged` |  |
| **`state`** | `public ControlManager.ControlState state` |  |
| **`targetEnemyIndicatorUi`** | `public GameObject targetEnemyIndicatorUi` |  |
| **`targetEnemyIndicatorWorld`** | `public GameObject targetEnemyIndicatorWorld` |  |

:::

## Properties (13)

::: details Click to expand Properties (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`aimDirection`** | `public Vector3? aimDirection { get; }` | This value is not normalized. Available when controlling with gamepad. |
| **`aimPoint`** | `public Vector3? aimPoint { get; }` | Position of the aim point. Available when controlling with gamepad. |
| **`controllingEntity`** | `public Entity controllingEntity { get; }` |  |
| **`focusedInteractable`** | `public IInteractable focusedInteractable { get; }` |  |
| **`isCharacterControlEnabled`** | `public bool isCharacterControlEnabled { get; }` |  |
| **`isFocusedInteractableAtCursor`** | `public bool isFocusedInteractableAtCursor { get; }` |  |
| **`isLastMovementDirectionFresh`** | `public bool isLastMovementDirectionFresh { get; }` |  |
| **`isMovementSchemeDirectional`** | `public bool isMovementSchemeDirectional { get; }` | Is current user's main movement scheme directional movement? |
| **`lastMovementDirection`** | `public Vector3 lastMovementDirection { get; }` |  |
| **`lastMovementStrength`** | `public float lastMovementStrength { get; }` |  |
| **`shouldProcessCharacterInput`** | `public bool shouldProcessCharacterInput { get; }` |  |
| **`shouldProcessCharacterInputAllowKnockedOut`** | `public bool shouldProcessCharacterInputAllowKnockedOut { get; }` |  |
| **`targetEnemy`** | `public Entity targetEnemy { get; }` | Available when controlling with gamepad. |

:::

## Methods (40)

::: details `AreControlsInverted()`

```csharp
public static bool AreControlsInverted()
```

**Returns:** `bool`

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CastAbility(AbilityTrigger, CastInfo, bool)`

```csharp
public void CastAbility(AbilityTrigger trigger, CastInfo info, bool shouldMoveToCast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `shouldMoveToCast` | `bool` |  |

:::

::: details `CastAbilityAtCursor(AbilityTrigger)`

Returns whether the cast attempt was successful or not.

```csharp
public bool CastAbilityAtCursor(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `CastAbilityAuto(AbilityTrigger)`

```csharp
public bool CastAbilityAuto(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `CastAbilityGamepad(AbilityTrigger)`

```csharp
public bool CastAbilityGamepad(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `CastAbilityInDirectionOfMovement(AbilityTrigger)`

```csharp
public bool CastAbilityInDirectionOfMovement(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `CastAbilityWithAim(AbilityTrigger)`

```csharp
public bool CastAbilityWithAim(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `DisableCharacterControls()`

```csharp
public void DisableCharacterControls()
```

:::

::: details `EnableCharacterControls()`

```csharp
public void EnableCharacterControls()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `GetAimAssistAttackTargetAngleGamepad()`

```csharp
public static float GetAimAssistAttackTargetAngleGamepad()
```

**Returns:** `float`

:::

::: details `GetAimAssistAttackTargetRange()`

```csharp
public static float GetAimAssistAttackTargetRange()
```

**Returns:** `float`

:::

::: details `GetAimAssistSphereCastRadius()`

```csharp
public static float GetAimAssistSphereCastRadius()
```

**Returns:** `float`

:::

::: details `GetCastInfo(CastMethodData, AbilityTargetValidator, CastInfo)`

```csharp
public CastInfo GetCastInfo(CastMethodData method, AbilityTargetValidator targetValidator, CastInfo prev = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `method` | [`CastMethodData`](/api/Global.CastMethodData) |  |
| `targetValidator` | [`AbilityTargetValidator`](/api/Global.AbilityTargetValidator) |  |
| `prev` | [`CastInfo`](/api/Global.CastInfo) |  |

**Returns:** `CastInfo`

:::

::: details `GetEntityFromScreenPoint(Vector2, Entity, IBinaryEntityValidator, float)`

```csharp
public static Entity GetEntityFromScreenPoint(Vector2 screenPoint, Entity self, IBinaryEntityValidator validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityFromScreenPoint(Vector2, IEntityValidator, float)`

```csharp
public static Entity GetEntityFromScreenPoint(Vector2 screenPoint, IEntityValidator validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityFromScreenPoint(Vector2, Func&lt;Entity, bool&gt;, float)`

```csharp
public static Entity GetEntityFromScreenPoint(Vector2 screenPoint, Func<Entity, bool> validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityFromScreenPoint(Vector2, float)`

```csharp
public static Entity GetEntityFromScreenPoint(Vector2 screenPoint, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityOnCursor(Entity, IBinaryEntityValidator, float)`

```csharp
public static Entity GetEntityOnCursor(Entity self, IBinaryEntityValidator validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `self` | [`Entity`](/api/Global.Entity) |  |
| `validator` | [`IBinaryEntityValidator`](/api/Global.IBinaryEntityValidator) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityOnCursor(IEntityValidator, float)`

```csharp
public static Entity GetEntityOnCursor(IEntityValidator validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityOnCursor(Func&lt;Entity, bool&gt;, float)`

```csharp
public static Entity GetEntityOnCursor(Func<Entity, bool> validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetEntityOnCursor(float)`

```csharp
public static Entity GetEntityOnCursor(float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

:::

::: details `GetFromScreenPoint&lt;T&gt;(Vector2, int, Func&lt;T, bool&gt;, float)`

```csharp
public static T GetFromScreenPoint<T>(Vector2 screenPoint, int layerMask, Func<T, bool> validator = null, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `layerMask` | `int` |  |
| `validator` | `System.Func<T, TResult><T,bool>` |  |
| `sphereCastRadius` | `float` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetHighlightableFromScreenPoint(Vector2)`

```csharp
public static HighlightProvider GetHighlightableFromScreenPoint(Vector2 screenPoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |

**Returns:** `HighlightProvider`

:::

::: details `GetHighlightableOnCursor()`

```csharp
public static HighlightProvider GetHighlightableOnCursor()
```

**Returns:** `HighlightProvider`

:::

::: details `GetInteractableFromScreenPoint(Vector2, float)`

```csharp
public static IInteractable GetInteractableFromScreenPoint(Vector2 screenPoint, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `IInteractable`

:::

::: details `GetInteractableOnCursor()`

```csharp
public static IInteractable GetInteractableOnCursor()
```

**Returns:** `IInteractable`

:::

::: details `GetMousePositionWithInversionInMind()`

```csharp
public static Vector2 GetMousePositionWithInversionInMind()
```

**Returns:** `UnityEngine.Vector2`

:::

::: details `GetSkillBinding(HeroSkillLocation)`

```csharp
public DewBinding GetSkillBinding(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

**Returns:** `DewBinding`

:::

::: details `GetSkillInputTrigger(HeroSkillLocation)`

```csharp
public DewInputTrigger GetSkillInputTrigger(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

**Returns:** `DewInputTrigger`

:::

::: details `GetWorldPositionOnGroundFromScreenPoint(Vector2, bool)`

```csharp
public static Vector3 GetWorldPositionOnGroundFromScreenPoint(Vector2 screenPoint, bool forDirectionalAttacks)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `forDirectionalAttacks` | `bool` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetWorldPositionOnGroundFromViewportPoint(Vector2, bool)`

```csharp
public static Vector3 GetWorldPositionOnGroundFromViewportPoint(Vector2 viewportPoint, bool forDirectionalAttacks)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `viewportPoint` | `UnityEngine.Vector2` |  |
| `forDirectionalAttacks` | `bool` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetWorldPositionOnGroundOnCursor(bool)`

```csharp
public static Vector3 GetWorldPositionOnGroundOnCursor(bool forDirectionalAttacks = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `forDirectionalAttacks` | `bool` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `IsInputFieldFocused()`

```csharp
public static bool IsInputFieldFocused()
```

**Returns:** `bool`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `SendPingGamepad()`

```csharp
public void SendPingGamepad()
```

:::

::: details `SetCastByKeyFlag(AbilityTrigger, bool, DewInputTrigger)`

```csharp
public void SetCastByKeyFlag(AbilityTrigger trigger, bool value, DewInputTrigger it)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `value` | `bool` |  |
| `it` | [`DewInputTrigger`](/api/Global.DewInputTrigger) |  |

:::

::: details `ShouldCastInDirectionOfMovement(AbilityTrigger)`

```csharp
public bool ShouldCastInDirectionOfMovement(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

:::

::: details `ShouldProcessPingInput()`

```csharp
public bool ShouldProcessPingInput()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (35)

*Classes and systems that invoke, reference, or depend on `ControlManager`:*

[CameraManager](/api/Global.CameraManager) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CinematicCameraHelper](/api/Global.CinematicCameraHelper) · [ConsoleManager](/api/Global.ConsoleManager) · [ConversationManager](/api/Global.ConversationManager) · `DewConsoleCommands` · [DewInput](/api/Global.DewInput) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillManager](/api/Global.EditSkillManager) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [InGameUIManager](/api/Global.InGameUIManager) · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · [ObjectHighlightManager](/api/Global.ObjectHighlightManager) · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_Intro` · `PlayTutorial_Tutorial_SkillsAndEssences` · `Se_ObliviaxKidnap` · `StarlessPath_BossPolarisManager` · `UI_Common_ChatBox` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `UI_EntityHealthBar` · `UI_EntityHealthBarMain` · `UI_EntityTalk` · `UI_InGame_CooldownTimeNotification` · `UI_InGame_InteractGroup` · `UI_InGame_InvertedControlsCursor` · `UI_InGame_MouseInputReceiver` · `UI_InGame_Result_HeroSkillItem` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButtons` · `UI_InGame_WorldMap`

### Dependencies (64)

*Types and components that `ControlManager` references or depends upon:*

[AbilityTargetValidator](/api/Global.AbilityTargetValidator) · [AbilityTrigger](/api/Global.AbilityTrigger) · [ActionAttackMove](/api/Global.ActionAttackMove) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [CameraManager](/api/Global.CameraManager) · [CastIndicatorManager](/api/Global.CastIndicatorManager) · [CastInfo](/api/Global.CastInfo) · [CastMethodData](/api/Global.CastMethodData) · [CommandMarker](/api/Global.CommandMarker) · [ComponentCache`2](/api/Global.ComponentCache`2) · [ConversationManager](/api/Global.ConversationManager) · [Dew](/api/Global.Dew) · [DewBinding](/api/Global.DewBinding) · [DewControlSettings_User](/api/Global.DewControlSettings_User) · [DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [DewPhysics](/api/Global.DewPhysics) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillManager](/api/Global.EditSkillManager) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [EntityCheck](/api/Global.EntityCheck) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [FeedbackManager](/api/Global.FeedbackManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [GlobalUIManager](/api/Global.GlobalUIManager) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · `HeroSkillTypeExtensions` · [HighlightProvider](/api/Global.HighlightProvider) · [IBinaryEntityValidator](/api/Global.IBinaryEntityValidator) · [ICastMethodDataPoint](/api/Global.ICastMethodDataPoint) · [IEntityValidator](/api/Global.IEntityValidator) · [IGamepadPingProxyParent](/api/Global.IGamepadPingProxyParent) · [IInteractable](/api/Global.IInteractable) · `IInteractableUnityNullCheckExtension` · [IPingableChoiceItem](/api/Global.IPingableChoiceItem) · [IPingableCustom](/api/Global.IPingableCustom) · [IPingableShopItem](/api/Global.IPingableShopItem) · [IPingableUIElement](/api/Global.IPingableUIElement) · [IPingableWorldNode](/api/Global.IPingableWorldNode) · [IWorldPositionReceiver](/api/Global.IWorldPositionReceiver) · [InGameUIManager](/api/Global.InGameUIManager) · [InputManager](/api/Global.InputManager) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MessageManager](/api/Global.MessageManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PingManager](/api/Global.PingManager) · [Rift](/api/Global.Rift) · [Rift_RoomExit](/api/Global.Rift_RoomExit) · [SingletonBehaviour`1](/api/Global.SingletonBehaviour`1) · [SkillTrigger](/api/Global.SkillTrigger) · [SpawnManager](/api/Global.SpawnManager) · [TriggerConfig](/api/Global.TriggerConfig) · [UIManager](/api/Global.UIManager) · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `Vector3FlattenExtension` · `VectorPlaneTransformExtension` · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#castconfirmtype" class="enum-link" data-tooltip="Normal=0 · Immediately=1 · OnRelease=2">CastConfirmType</a> · <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> · <a href="/enums#skilltype" class="enum-link" data-tooltip="Normal=0 · Ultimate=1">SkillType</a>

:::
