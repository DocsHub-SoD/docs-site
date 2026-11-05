# Class: ElementalStatusEffect

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect) → [StackedStatusEffect](/api/Global.StackedStatusEffect)

```csharp
public class ElementalStatusEffect : StackedStatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IOtherPlayersTonedDownDisable
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ampAmount`** | `[NonSerialized]
public float ampAmount` |  |
| **`stackScaledEmissions`** | `public ParticleSystem[] stackScaledEmissions` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `OnStackChange(int, int)`

```csharp
protected override void OnStackChange(int oldStack, int newStack)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldStack` | `int` |  |
| `newStack` | `int` |  |

### `OnStartClient()`

```csharp
public override void OnStartClient()
```
