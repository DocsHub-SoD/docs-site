# Class: AbilityTrigger.ChangedConfigHandle

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class AbilityTrigger.ChangedConfigHandle
```

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`configIndex`** | `public int configIndex { get; }` |  |
| **`duration`** | `public float duration { get; }` |  |
| **`isActive`** | `public bool isActive { get; }` |  |
| **`previousConfigIndex`** | `public int previousConfigIndex { get; }` |  |
| **`remainingTime`** | `public float remainingTime { get; }` |  |
| **`setFillAmount`** | `public bool setFillAmount { get; }` |  |

:::

## Methods (1)

::: details `Stop()`

Stop this config change. This will not call onExpire!

```csharp
public void Stop()
```

:::
