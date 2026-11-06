# Class: EditSkillManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [EditSkillManager](/api/Global.EditSkillManager)

```csharp
public class EditSkillManager : ManagerBase<EditSkillManager>, ILogicUpdate
```

## Fields (18)

::: details Click to expand Fields (18)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`backButtonPriority`** | `public int backButtonPriority` |  |
| **`canRepeatConfirmHold`** | `[NonSerialized] public bool canRepeatConfirmHold` |  |
| **`confirmHoldAudio`** | `public DewAudioSource confirmHoldAudio` |  |
| **`confirmHoldGem`** | `[NonSerialized] public GemLocation confirmHoldGem` |  |
| **`confirmHoldNormalizedAmount`** | `[NonSerialized] public float confirmHoldNormalizedAmount` |  |
| **`confirmHoldSkill`** | `[NonSerialized] public HeroSkillLocation confirmHoldSkill` |  |
| **`didClickWhileConfirmHolding`** | `[NonSerialized] public bool didClickWhileConfirmHolding` |  |
| **`dropToGroundBlocker`** | `public RectTransform dropToGroundBlocker` |  |
| **`isConfirmHoldingGem`** | `[NonSerialized] public bool isConfirmHoldingGem` |  |
| **`isConfirmHoldingSkill`** | `[NonSerialized] public bool isConfirmHoldingSkill` |  |
| **`onDraggingObjectChanged`** | `public Action<Object> onDraggingObjectChanged` |  |
| **`OnGemSlotClientState`** | `public Action<GemLocation, Gem> OnGemSlotClientState` |  |
| **`OnGemVisibleClientState`** | `public Action<Gem, bool> OnGemVisibleClientState` |  |
| **`onModeChanged`** | `public Action<EditSkillManager.ModeType> onModeChanged` |  |
| **`onSelectedSlotChanged`** | `public Action onSelectedSlotChanged` |  |
| **`OnSkillSlotClientState`** | `public Action<HeroSkillLocation, SkillTrigger> OnSkillSlotClientState` |  |
| **`OnSkillVisibleClientState`** | `public Action<SkillTrigger, bool> OnSkillVisibleClientState` |  |
| **`skillButtons`** | `public GameObject skillButtons` |  |

:::

## Properties (12)

::: details Click to expand Properties (12)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentModeSetFrameCount`** | `public int currentModeSetFrameCount { get; }` |  |
| **`currentProvider`** | `public Actor currentProvider { get; }` |  |
| **`draggingObject`** | `public Object draggingObject { get; }` |  |
| **`isConfirmHolding`** | `public bool isConfirmHolding { get; }` |  |
| **`isDragging`** | `public bool isDragging { get; }` |  |
| **`isSelectingGround`** | `public bool isSelectingGround { get; }` |  |
| **`lastCurrentProviderSetUnscaledTime`** | `public float lastCurrentProviderSetUnscaledTime { get; }` |  |
| **`lastModeSetUnscaledTime`** | `public float lastModeSetUnscaledTime { get; }` |  |
| **`mode`** | `public EditSkillManager.ModeType mode { get; }` |  |
| **`selectedGemSlot`** | `public GemLocation? selectedGemSlot { get; set; }` |  |
| **`selectedSkillSlot`** | `public HeroSkillLocation? selectedSkillSlot { get; set; }` |  |
| **`shouldEndAfterAction`** | `public bool shouldEndAfterAction { get; }` |  |

:::

## Methods (35)

::: details `ClearGamepadSelection()`

```csharp
public void ClearGamepadSelection()
```

:::

::: details `DoBack()`

```csharp
public bool DoBack()
```

**Returns:** `bool`

:::

::: details `DoClickOnGemSlot(GemLocation)`

```csharp
public void DoClickOnGemSlot(GemLocation location)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `location` | [`GemLocation`](/api/Global.GemLocation) |  |

:::

::: details `DoClickOnSkillButton(HeroSkillLocation)`

```csharp
public void DoClickOnSkillButton(HeroSkillLocation skillType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillType` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

:::

::: details `DoConfirm()`

```csharp
public bool DoConfirm()
```

**Returns:** `bool`

:::

::: details `DoDpadDown()`

```csharp
public bool DoDpadDown()
```

**Returns:** `bool`

:::

::: details `DoDpadLeft()`

```csharp
public bool DoDpadLeft()
```

**Returns:** `bool`

:::

::: details `DoDpadRight()`

```csharp
public bool DoDpadRight()
```

**Returns:** `bool`

:::

::: details `DoDpadUp()`

```csharp
public bool DoDpadUp()
```

**Returns:** `bool`

:::

::: details `EndDrag(bool)`

```csharp
public void EndDrag(bool isCancel)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `isCancel` | `bool` |  |

:::

::: details `EndEdit()`

```csharp
public void EndEdit()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `IsSlotHighlighted(GemLocation)`

```csharp
public bool IsSlotHighlighted(GemLocation gemLoc)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemLoc` | [`GemLocation`](/api/Global.GemLocation) |  |

**Returns:** `bool`

:::

::: details `IsSlotHighlighted(HeroSkillLocation)`

```csharp
public bool IsSlotHighlighted(HeroSkillLocation skillLoc)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillLoc` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

**Returns:** `bool`

:::

::: details `IsSlotSelectable(GemLocation)`

```csharp
public bool IsSlotSelectable(GemLocation gemLoc)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gemLoc` | [`GemLocation`](/api/Global.GemLocation) |  |

**Returns:** `bool`

:::

::: details `IsSlotSelectable(HeroSkillLocation)`

```csharp
public bool IsSlotSelectable(HeroSkillLocation skillLoc)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillLoc` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

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

::: details `NotifyEndOfAction()`

This will end edit if it is marked to end after action.

```csharp
public void NotifyEndOfAction()
```

:::

::: details `SelectAnyRelevantSlot()`

```csharp
public void SelectAnyRelevantSlot()
```

:::

::: details `SelectGround()`

```csharp
public void SelectGround()
```

:::

::: details `SetClientState_MergeGemVictim(Gem)`

```csharp
public void SetClientState_MergeGemVictim(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `SetClientState_SetGemSlot(GemLocation, Gem)`

```csharp
public void SetClientState_SetGemSlot(GemLocation loc, Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `gem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `SetClientState_SetSkillSlot(HeroSkillLocation, SkillTrigger)`

```csharp
public void SetClientState_SetSkillSlot(HeroSkillLocation type, SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

:::

::: details `ShouldUseHoldToConfirm(GemLocation)`

```csharp
public bool ShouldUseHoldToConfirm(GemLocation gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`GemLocation`](/api/Global.GemLocation) |  |

**Returns:** `bool`

:::

::: details `ShouldUseHoldToConfirm(HeroSkillLocation)`

```csharp
public bool ShouldUseHoldToConfirm(HeroSkillLocation skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

**Returns:** `bool`

:::

::: details `StartConfirmHold(GemLocation)`

```csharp
public void StartConfirmHold(GemLocation gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`GemLocation`](/api/Global.GemLocation) |  |

:::

::: details `StartConfirmHold(HeroSkillLocation)`

```csharp
public void StartConfirmHold(HeroSkillLocation skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | <a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a> |  |

:::

::: details `StartDrag(Object)`

```csharp
public void StartDrag(Object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |

:::

::: details `StartEditSkillShrine(EditSkillShrine)`

```csharp
public void StartEditSkillShrine(EditSkillShrine provider)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `provider` | [`EditSkillShrine`](/api/Global.EditSkillShrine) |  |

:::

::: details `StartEquipGem(Gem)`

```csharp
public void StartEquipGem(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `StartEquipSkill(SkillTrigger)`

```csharp
public void StartEquipSkill(SkillTrigger skill)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skill` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

:::

::: details `StartRegularEdit(bool)`

```csharp
public void StartRegularEdit(bool endAfterAction)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `endAfterAction` | `bool` |  |

:::

::: details `StartSell(PropEnt_Merchant_Base)`

```csharp
public void StartSell(PropEnt_Merchant_Base merchant)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `merchant` | [`PropEnt_Merchant_Base`](/api/Global.PropEnt_Merchant_Base) |  |

:::

::: details `StopConfirmHold(bool)`

```csharp
public void StopConfirmHold(bool showHelpIfNeeded = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `showHelpIfNeeded` | `bool` |  |

:::

::: details `UnselectGround()`

```csharp
public void UnselectGround()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (29)

*Classes and systems that invoke, reference, or depend on `EditSkillManager`:*

[ControlManager](/api/Global.ControlManager) · [EditSkillShrine](/api/Global.EditSkillShrine) · [HeroSkill](/api/Global.HeroSkill) · `Primus_Ending` · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `Shrine_Entanglement` · `Shrine_MawOfDoom` · `StarlessPath_BossPolarisManager` · `UI_InGame_EditSkillBackdrop` · `UI_InGame_EditSkillShrineText` · `UI_InGame_FloatingGem` · `UI_InGame_FloatingSkill` · `UI_InGame_GemSlot` · `UI_InGame_GemSlot_EditSkill` · `UI_InGame_HeroDetailWindow` · `UI_InGame_MouseInputReceiver_EditSkill` · `UI_InGame_SkillButton` · `UI_InGame_SkillButton_EditSkill` · `UI_InGame_SkillButtons` · `UI_InGame_SkillButtonsBottomBar` · `UI_InGame_SkillNotifications` · `UI_InGame_TimerDisplay` · `UI_TooltipSection_Gem` · `UI_TooltipSection_Skill` · `UI_Tooltip_EditSkillShrineTooltip` · `UI_Tooltip_EquipSwapActionIndicator` · `UI_Tooltip_EquippedGemDescriber` · `UI_Tooltip_ObjEditSkillActions` · `UI_Tooltip_SkillTitle`

### Dependencies (38)

*Types and components that `EditSkillManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · [CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · `CostExtensions` · [Dew](/api/Global.Dew) · [DewAudioSource](/api/Global.DewAudioSource) · [DewInput](/api/Global.DewInput) · [DewInputTrigger](/api/Global.DewInputTrigger) · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [EditSkillShrine](/api/Global.EditSkillShrine) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [EntityCheck](/api/Global.EntityCheck) · [FeedbackManager](/api/Global.FeedbackManager) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [Gem](/api/Global.Gem) · [GemLocation](/api/Global.GemLocation) · [GlobalUIManager](/api/Global.GlobalUIManager) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · [IEditSkillDropTargetGemSlot](/api/Global.IEditSkillDropTargetGemSlot) · [IEditSkillDropTargetSkillButton](/api/Global.IEditSkillDropTargetSkillButton) · `IHoldableInHandExtension` · [IInteractable](/api/Global.IInteractable) · [IItem](/api/Global.IItem) · [InGameUIManager](/api/Global.InGameUIManager) · [InputManager](/api/Global.InputManager) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `RectTransformGetWorldRectExtension` · [SafeAction`1](/api/Global.SafeAction`1) · [SkillTrigger](/api/Global.SkillTrigger) · [UIManager](/api/Global.UIManager) · `Vector3FlattenExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a>

:::
