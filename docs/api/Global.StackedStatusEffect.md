# Class: StackedStatusEffect

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect) → [ElementalStatusEffect](/api/Global.ElementalStatusEffect)

```csharp
public abstract class StackedStatusEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`autoDecay`** | `[BoxGroup("Stack Settings", true, false, 0)]
[ToggleGroup("Stack Settings/autoDecay", "Auto Decay")]
public bool autoDecay` |  |
| **`decayAllAtOnce`** | `[BoxGroup("Stack Settings", true, false, 0)]
[ToggleGroup("Stack Settings/autoDecay", "Auto Decay")]
[ToggleLeft]
public bool decayAllAtOnce` |  |
| **`decayCount`** | `[BoxGroup("Stack Settings", true, false, 0)]
[HideIf("decayAllAtOnce", true)]
[ToggleGroup("Stack Settings/autoDecay", "Auto Decay")]
public int decayCount` |  |
| **`decayTime`** | `[BoxGroup("Stack Settings", true, false, 0)]
[ToggleGroup("Stack Settings/autoDecay", "Auto Decay")]
public float decayTime` |  |
| **`killOnZeroStack`** | `[BoxGroup("Stack Settings", true, false, 0)]
public bool killOnZeroStack` |  |
| **`maxStack`** | `[BoxGroup("Stack Settings", true, false, 0)]
public int maxStack` |  |
| **`resetTimerOnStackChange`** | `[BoxGroup("Stack Settings", true, false, 0)]
[ToggleGroup("Stack Settings/autoDecay", "Auto Decay")]
[ToggleLeft]
public bool resetTimerOnStackChange` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`remainingDecayTime`** | `public float remainingDecayTime { get; }` |  |
| **`stack`** | `public int stack { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `AddStack(int)`

```csharp
public void AddStack(int value = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `int` |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnStackChange(int, int)`

Called everywhere when stack count changes.

```csharp
protected virtual void OnStackChange(int oldStack, int newStack)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `oldStack` | `int` |  |
| `newStack` | `int` |  |

### `RemoveStack(int)`

```csharp
public void RemoveStack(int value = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `int` |  |

### `ResetDecayTimer()`

```csharp
public void ResetDecayTimer()
```

### `SetStack(int)`

```csharp
public void SetStack(int stack)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `stack` | `int` |  |
