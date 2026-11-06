# Class: EditSkillShrine

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Shrine](/api/Global.Shrine)

```csharp
public abstract class EditSkillShrine : Shrine, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IProp, IBanRoomNodesNearby
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canRepeatConfirmHold`** | `[BoxGroup("EditSkillShrine Settings", true, false, 0)] [ToggleLeft] public bool canRepeatConfirmHold` |  |
| **`canTargetGem`** | `[BoxGroup("EditSkillShrine Settings", true, false, 0)] [ToggleLeft] public bool canTargetGem` |  |
| **`canTargetSkill`** | `[BoxGroup("EditSkillShrine Settings", true, false, 0)] [ToggleLeft] public bool canTargetSkill` |  |
| **`fxEnterEditMode`** | `[BoxGroup("EditSkillShrine Settings", true, false, 0)] public GameObject fxEnterEditMode` |  |
| **`fxEnterEditModeLocal`** | `[BoxGroup("EditSkillShrine Settings", true, false, 0)] public GameObject fxEnterEditModeLocal` |  |
| **`GenericGemIndicatorColor`** | `public static readonly Color GenericGemIndicatorColor` |  |
| **`GenericSkillIndicatorColor`** | `public static readonly Color GenericSkillIndicatorColor` |  |
| **`shouldExitEditModeAfterAction`** | `[BoxGroup("EditSkillShrine Settings", true, false, 0)] [ToggleLeft] public bool shouldExitEditModeAfterAction` |  |

## Methods

### `CmdActivateEditSkillAction(HeroSkillLocation?, GemLocation?, NetworkConnectionToClient)`

```csharp
public void CmdActivateEditSkillAction(HeroSkillLocation? skillLoc, GemLocation? gemLoc, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skillLoc` | [`HeroSkillLocation?`](/api/Global.HeroSkillLocation) |  |
| `gemLoc` | [`GemLocation?`](/api/Global.GemLocation) |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `EnterEditSkill(DewPlayer, string)`

Make the player enter edit skill mode of this shrine.

```csharp
public void EnterEditSkill(DewPlayer player, string customData = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `customData` | `string` |  |

### `EnterEditSkill(Entity, string)`

Make the player enter edit skill mode of this shrine.

```csharp
public void EnterEditSkill(Entity entity, string customData = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `customData` | `string` |  |

### `GetCost(Entity)`

```csharp
public override Cost? GetCost(Entity activator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activator` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Cost?`

### `GetCustomData(DewPlayer)`

Get the custom data for the player, provided with the EnterEditSkill call.Available everywhere.

```csharp
public string GetCustomData(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `string`

### `GetEditSkillBackdropColor()`

The color of the backdrop behind skill buttons in this edit skill mode. Disabled by default.

```csharp
public virtual Color GetEditSkillBackdropColor()
```

**Returns:** `UnityEngine.Color`

### `GetEditSkillIndicatorColor()`

The color of the editskill indicator text.

```csharp
public virtual Color GetEditSkillIndicatorColor()
```

**Returns:** `UnityEngine.Color`

### `GetEditSkillIndicatorRawText()`

Text to show on editskill indicator of this shrine's action.

```csharp
public virtual string GetEditSkillIndicatorRawText()
```

**Returns:** `string`

### `GetTargetInfo(DewPlayer, GemLocation, Gem)`

Checked everywhere.

```csharp
public virtual EditSkillTargetInfo GetTargetInfo(DewPlayer player, GemLocation loc, Gem target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `target` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `EditSkillTargetInfo`

### `GetTargetInfo(DewPlayer, HeroSkillLocation, SkillTrigger)`

Checked everywhere.

```csharp
public virtual EditSkillTargetInfo GetTargetInfo(DewPlayer player, HeroSkillLocation loc, SkillTrigger target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `loc` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `target` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `EditSkillTargetInfo`

### `GetTargetTypes(DewPlayer)`

```csharp
public virtual EditSkillTargetType GetTargetTypes(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `EditSkillTargetType`

### `OnActivateEditSkill(DewPlayer, GemLocation, Gem)`

Called on server. Return true to denote success, which will show the activation effect, spend the cost, and deduct use count.Note this will be called only if all validations has been passed.

```csharp
protected virtual bool OnActivateEditSkill(DewPlayer player, GemLocation loc, Gem target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `loc` | [`GemLocation`](/api/Global.GemLocation) |  |
| `target` | [`Gem`](/api/Global.Gem) |  |

**Returns:** `bool`

### `OnActivateEditSkill(DewPlayer, HeroSkillLocation, SkillTrigger)`

Called on server. Return true to denote success, which will show the activation effect, spend the cost, and deduct use count.Note this will be called only if all validations has been passed.

```csharp
protected virtual bool OnActivateEditSkill(DewPlayer player, HeroSkillLocation loc, SkillTrigger target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `loc` | [`HeroSkillLocation`](/api/Global.HeroSkillLocation) |  |
| `target` | [`SkillTrigger`](/api/Global.SkillTrigger) |  |

**Returns:** `bool`

### `OnUse(Entity)`

```csharp
protected override bool OnUse(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

### `ShouldExitEditModeAfterAction()`

Checked on local client. You can override this to dynamically adjust behavior for each player.

```csharp
public virtual bool ShouldExitEditModeAfterAction()
```

**Returns:** `bool`
