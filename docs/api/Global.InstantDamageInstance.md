# Class: InstantDamageInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class InstantDamageInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`damageDelay`** | `[Title("Instant Damage Instance", null, TitleAlignments.Left, true, true)] [LabelText("Delay")] public float damageDelay` |  |
| **`mainEffectAfterDelay`** | `[LabelText("Main Effect (After Delay)")] public GameObject mainEffectAfterDelay` |  |

## Methods

### `OnAfterDelay()`

Called after instant damage instance's delay on server.

```csharp
protected virtual void OnAfterDelay()
```

### `OnCreateSequenced()`

```csharp
protected override IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`
