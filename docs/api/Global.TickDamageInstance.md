# Class: TickDamageInstance

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [DamageInstance](/api/Global.DamageInstance)

```csharp
public class TickDamageInstance : DamageInstance, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`delay`** | `[Title("Tick Damage Instance", null, TitleAlignments.Left, true, true)] public float delay` |  |
| **`fxLoop`** | `[LabelText("Fx Loop (After Delay)")] public GameObject fxLoop` |  |
| **`fxPerTick`** | `public GameObject fxPerTick` |  |
| **`fxTelegraph`** | `public GameObject fxTelegraph` |  |
| **`tickInterval`** | `public float tickInterval` |  |
| **`ticks`** | `public int ticks` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`duration`** | `[ShowInInspector] public float duration { get; }` |  |

:::

## Methods (3)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnCreateSequenced()`

```csharp
protected override IEnumerator OnCreateSequenced()
```

**Returns:** `System.Collections.IEnumerator`

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::
