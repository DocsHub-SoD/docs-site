# Class: AbilityTrigger.ChangedConfigHandle

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class AbilityTrigger.ChangedConfigHandle
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`configIndex`** | `public int configIndex { get; }` |  |
| **`duration`** | `public float duration { get; }` |  |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`previousConfigIndex`** | `public int previousConfigIndex { get; }` |  |
| **`remainingTime`** | `public float remainingTime { get; }` |  |
| **`setFillAmount`** | `public bool setFillAmount { get; }` |  |

## Methods

### `Stop()`

Stop this config change. This will not call onExpire!

```csharp
public void Stop()
```
