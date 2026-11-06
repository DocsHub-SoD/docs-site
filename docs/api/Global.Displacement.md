# Class: Displacement

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DispByDestination](/api/Global.DispByDestination) → [DispByTarget](/api/Global.DispByTarget)

```csharp
public abstract class Displacement
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`affectedByMovementSpeed`** | `public bool affectedByMovementSpeed` | Is this displacement affected by movement speed multiplier? |
| **`isCanceledByCC`** | `public bool isCanceledByCC` | Is this displacement canceled by crowd controls?Note the displacement will not be canceled by CCs applied previously, but by new CCs.Default value is true. |
| **`isDodging`** | `public bool isDodging` | Is this displacement dodging?Dodging displacement will not cancel channels even when they're not allowed to continue while dashing. |
| **`isFriendly`** | `public bool isFriendly` | Is this displacement considered a friendly displacement?This is used to determine if the displacement is Airborne or Dash, and it's fed to info structs of Displacement-related action callbacks.Default value is false. |
| **`MinimumDisplacementDuration`** | `public const float MinimumDisplacementDuration = 0.0001` |  |
| **`onCancel`** | `public Action onCancel` | Action that is called when this displacement is canceled.This can be due to CCs, auto-canceling behaviour of DispByTarget, manual cancelation, and etc. |
| **`onFinish`** | `public Action onFinish` | Action that is called when this displacement has successfully finished. |
| **`rotateForward`** | `public bool rotateForward` | Will the entity rotate towards its velocity during the displacement?Default value is true. |
| **`rotateSmoothly`** | `public bool rotateSmoothly` | Smoothly rotate if rotateForward is on.Default value is false. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`elapsedTime`** | `public float elapsedTime { get; }` | Time elapsed starting from the moment this displacement has started. |
| **`hasStarted`** | `public bool hasStarted { get; }` | Has this displacement started? |
| **`isAlive`** | `public bool isAlive { get; }` | Is this displacement on-going? |
