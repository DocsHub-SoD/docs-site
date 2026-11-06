# Class: ControlManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ControlManager](/api/Global.ControlManager)

```csharp
[LogicUpdatePriority(-500)]
public class ControlManager : ManagerBase<ControlManager>, ILogicUpdate
```

## Fields

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

## Properties

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

## Methods

### `AreControlsInverted()`

```csharp
public static bool AreControlsInverted()
```

**Returns:** `bool`

### `Awake()`

```csharp
protected override void Awake()
```

### `CastAbility(AbilityTrigger, CastInfo, bool)`

```csharp
public void CastAbility(AbilityTrigger trigger, CastInfo info, bool shouldMoveToCast)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `shouldMoveToCast` | `bool` |  |

### `CastAbilityAtCursor(AbilityTrigger)`

Returns whether the cast attempt was successful or not.

```csharp
public bool CastAbilityAtCursor(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `CastAbilityAuto(AbilityTrigger)`

```csharp
public bool CastAbilityAuto(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `CastAbilityGamepad(AbilityTrigger)`

```csharp
public bool CastAbilityGamepad(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `CastAbilityInDirectionOfMovement(AbilityTrigger)`

```csharp
public bool CastAbilityInDirectionOfMovement(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `CastAbilityWithAim(AbilityTrigger)`

```csharp
public bool CastAbilityWithAim(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `DisableCharacterControls()`

```csharp
public void DisableCharacterControls()
```

### `EnableCharacterControls()`

```csharp
public void EnableCharacterControls()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetAimAssistAttackTargetAngleGamepad()`

```csharp
public static float GetAimAssistAttackTargetAngleGamepad()
```

**Returns:** `float`

### `GetAimAssistAttackTargetRange()`

```csharp
public static float GetAimAssistAttackTargetRange()
```

**Returns:** `float`

### `GetAimAssistSphereCastRadius()`

```csharp
public static float GetAimAssistSphereCastRadius()
```

**Returns:** `float`

### `GetCastInfo(CastMethodData, AbilityTargetValidator, CastInfo)`

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

### `GetEntityFromScreenPoint(Vector2, Entity, IBinaryEntityValidator, float)`

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

### `GetEntityFromScreenPoint(Vector2, IEntityValidator, float)`

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

### `GetEntityFromScreenPoint(Vector2, Func<Entity, bool>, float)`

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

### `GetEntityFromScreenPoint(Vector2, float)`

```csharp
public static Entity GetEntityFromScreenPoint(Vector2 screenPoint, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

### `GetEntityOnCursor(Entity, IBinaryEntityValidator, float)`

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

### `GetEntityOnCursor(IEntityValidator, float)`

```csharp
public static Entity GetEntityOnCursor(IEntityValidator validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`IEntityValidator`](/api/Global.IEntityValidator) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

### `GetEntityOnCursor(Func<Entity, bool>, float)`

```csharp
public static Entity GetEntityOnCursor(Func<Entity, bool> validator, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `validator` | [`System.Func<T, TResult><Entity,bool>`](/api/Global.Entity) |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

### `GetEntityOnCursor(float)`

```csharp
public static Entity GetEntityOnCursor(float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sphereCastRadius` | `float` |  |

**Returns:** `Entity`

### `GetFromScreenPoint<T>(Vector2, int, Func<T, bool>, float)`

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

### `GetHighlightableFromScreenPoint(Vector2)`

```csharp
public static HighlightProvider GetHighlightableFromScreenPoint(Vector2 screenPoint)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |

**Returns:** `HighlightProvider`

### `GetHighlightableOnCursor()`

```csharp
public static HighlightProvider GetHighlightableOnCursor()
```

**Returns:** `HighlightProvider`

### `GetInteractableFromScreenPoint(Vector2, float)`

```csharp
public static IInteractable GetInteractableFromScreenPoint(Vector2 screenPoint, float sphereCastRadius = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `sphereCastRadius` | `float` |  |

**Returns:** `IInteractable`

### `GetInteractableOnCursor()`

```csharp
public static IInteractable GetInteractableOnCursor()
```

**Returns:** `IInteractable`

### `GetMousePositionWithInversionInMind()`

```csharp
public static Vector2 GetMousePositionWithInversionInMind()
```

**Returns:** `UnityEngine.Vector2`

### `GetSkillBinding(HeroSkillLocation)`

```csharp
public DewBinding GetSkillBinding(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `DewBinding`

### `GetSkillInputTrigger(HeroSkillLocation)`

```csharp
public DewInputTrigger GetSkillInputTrigger(HeroSkillLocation type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |

**Returns:** `DewInputTrigger`

### `GetWorldPositionOnGroundFromScreenPoint(Vector2, bool)`

```csharp
public static Vector3 GetWorldPositionOnGroundFromScreenPoint(Vector2 screenPoint, bool forDirectionalAttacks)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `screenPoint` | `UnityEngine.Vector2` |  |
| `forDirectionalAttacks` | `bool` |  |

**Returns:** `UnityEngine.Vector3`

### `GetWorldPositionOnGroundFromViewportPoint(Vector2, bool)`

```csharp
public static Vector3 GetWorldPositionOnGroundFromViewportPoint(Vector2 viewportPoint, bool forDirectionalAttacks)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `viewportPoint` | `UnityEngine.Vector2` |  |
| `forDirectionalAttacks` | `bool` |  |

**Returns:** `UnityEngine.Vector3`

### `GetWorldPositionOnGroundOnCursor(bool)`

```csharp
public static Vector3 GetWorldPositionOnGroundOnCursor(bool forDirectionalAttacks = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `forDirectionalAttacks` | `bool` |  |

**Returns:** `UnityEngine.Vector3`

### `IsInputFieldFocused()`

```csharp
public static bool IsInputFieldFocused()
```

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `SendPingGamepad()`

```csharp
public void SendPingGamepad()
```

### `SetCastByKeyFlag(AbilityTrigger, bool, DewInputTrigger)`

```csharp
public void SetCastByKeyFlag(AbilityTrigger trigger, bool value, DewInputTrigger it)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |
| `value` | `bool` |  |
| `it` | [`DewInputTrigger`](/api/Global.DewInputTrigger) |  |

### `ShouldCastInDirectionOfMovement(AbilityTrigger)`

```csharp
public bool ShouldCastInDirectionOfMovement(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

**Returns:** `bool`

### `ShouldProcessPingInput()`

```csharp
public bool ShouldProcessPingInput()
```

**Returns:** `bool`
