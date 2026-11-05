# Class: DashAttackInstance

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class DashAttackInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`damageGracePeriod`** | `[Title("Dash Attack Instance", null, TitleAlignments.Left, true, true)]
public float damageGracePeriod` |  |
| **`dash`** | `[InlineProperty]
[HideLabel]
public Dash dash` |  |
| **`isDirectionMode`** | `public bool isDirectionMode` |  |

## Methods

### `ActiveFrameUpdate()`

```csharp
protected override void ActiveFrameUpdate()
```

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnBeforeDispatchDamage(ref DamageData, Entity)`

```csharp
protected override void OnBeforeDispatchDamage(ref DamageData dmg, Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dmg` | [DamageData](/api/Global.DamageData) |  |
| `target` | [Entity](/api/Global.Entity) |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnSetupDash(DispByDestination)`

```csharp
protected virtual void OnSetupDash(DispByDestination disp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `disp` | [DispByDestination](/api/Global.DispByDestination) |  |
