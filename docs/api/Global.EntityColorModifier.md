# Class: EntityColorModifier

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class EntityColorModifier
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseColor`** | `public Color baseColor { get; set; }` |  |
| **`dissolveAmount`** | `public float dissolveAmount { get; set; }` |  |
| **`dissolveColor`** | `public Color? dissolveColor { get; set; }` |  |
| **`emission`** | `public Color emission { get; set; }` |  |
| **`opacity`** | `public float opacity { get; set; }` |  |

## Methods

### `Stop()`

Remove this color modifier from its parent.

```csharp
public void Stop()
```
