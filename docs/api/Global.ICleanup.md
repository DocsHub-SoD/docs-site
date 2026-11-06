# Interface: ICleanup

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ICleanup
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canDestroy`** | `bool canDestroy { get; }` | If anyICleanupreports false, destroy call will be delayed. |

## Methods

### `OnCleanup()`

Called on server to ready itself before getting destroyed.

```csharp
void OnCleanup()
```
