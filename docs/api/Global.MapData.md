# Class: MapData

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class MapData
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`area`** | `public float area` | Total area of playable area. |
| **`cells`** | `public Cells2D<MapCellType> cells` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`innerPropNodeIndices`** | `public IReadOnlyList<(int, int)> innerPropNodeIndices { get; }` | Represents indices of prop placement nodes.These nodes are on inner playable area with some distance to a nearest wall. |
| **`outerPropNodeIndices`** | `public IReadOnlyList<(int, int)> outerPropNodeIndices { get; }` | Represents indices of prop placement nodes.These nodes are on playable area and close to a wall. |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `MapData`:*

`Obliviax_Decoration_Generator` · [RoomMap](/api/Global.RoomMap) · `RoomMod_GoldEverywhere` · `RoomMod_PureDream` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomMonsters](/api/Global.RoomMonsters)

### Dependencies (2)

*Types and components that `MapData` references or depends upon:*

[Cells2D`1](/api/Global.Cells2D`1) · [FlatTupleListWrapper`1](/api/Global.FlatTupleListWrapper`1)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`MapCellType`](/enums#mapcelltype)

:::
