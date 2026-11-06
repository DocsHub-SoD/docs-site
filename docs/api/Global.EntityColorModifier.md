# Class: EntityColorModifier

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class EntityColorModifier
```

## Properties (5)

::: details Click to expand Properties (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseColor`** | `public Color baseColor { get; set; }` |  |
| **`dissolveAmount`** | `public float dissolveAmount { get; set; }` |  |
| **`dissolveColor`** | `public Color? dissolveColor { get; set; }` |  |
| **`emission`** | `public Color emission { get; set; }` |  |
| **`opacity`** | `public float opacity { get; set; }` |  |

:::

## Methods (1)

::: details `Stop()`

Remove this color modifier from its parent.

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `EntityColorModifier`:*

[EntityVisual](/api/Global.EntityVisual) · [FxEntityColor](/api/Global.FxEntityColor) · `Mon_DarkCave_NightOlm` · `Se_DarkCondensationZone`

### Dependencies (2)

*Types and components that `EntityColorModifier` references or depends upon:*

[Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual)

:::
