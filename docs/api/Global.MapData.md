# Class: MapData

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class MapData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`area`** | `public float area` | Total area of playable area. |
| **`cells`** | `public Cells2D<MapCellType> cells` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`innerPropNodeIndices`** | `public IReadOnlyList<(int, int)> innerPropNodeIndices { get; }` | Represents indices of prop placement nodes.These nodes are on inner playable area with some distance to a nearest wall. |
| **`outerPropNodeIndices`** | `public IReadOnlyList<(int, int)> outerPropNodeIndices { get; }` | Represents indices of prop placement nodes.These nodes are on playable area and close to a wall. |
