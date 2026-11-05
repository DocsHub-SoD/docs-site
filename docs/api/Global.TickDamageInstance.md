# Class: TickDamageInstance

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class TickDamageInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`delay`** | `[Title("Tick Damage Instance", null, TitleAlignments.Left, true, true)]
public float delay` |  |
| **`fxLoop`** | `[LabelText("Fx Loop (After Delay)")]
public GameObject fxLoop` |  |
| **`fxPerTick`** | `public GameObject fxPerTick` |  |
| **`fxTelegraph`** | `public GameObject fxTelegraph` |  |
| **`tickInterval`** | `public float tickInterval` |  |
| **`ticks`** | `public int ticks` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`duration`** | `[ShowInInspector]
public float duration { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnCreateSequenced()`

```csharp
protected override IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```
