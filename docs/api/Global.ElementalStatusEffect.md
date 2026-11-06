# Class: ElementalStatusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect) → [StackedStatusEffect](/api/Global.StackedStatusEffect)

```csharp
public class ElementalStatusEffect : StackedStatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IOtherPlayersTonedDownDisable
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ampAmount`** | `[NonSerialized] public float ampAmount` |  |
| **`stackScaledEmissions`** | `public ParticleSystem[] stackScaledEmissions` |  |

:::

## Methods (3)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `OnStackChange(int, int)`

```csharp
protected override void OnStackChange(int oldStack, int newStack)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldStack` | `int` |  |
| `newStack` | `int` |  |

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::
