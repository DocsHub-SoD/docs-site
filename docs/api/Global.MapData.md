# Class: MapData

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
| **`cells`** | `public Cells2D&lt;MapCellType&gt; cells` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`innerPropNodeIndices`** | `public IReadOnlyList&lt;(int, int)&gt; innerPropNodeIndices { get; }` | Represents indices of prop placement nodes.These nodes are on inner playable area with some distance to a nearest wall. |
| **`outerPropNodeIndices`** | `public IReadOnlyList&lt;(int, int)&gt; outerPropNodeIndices { get; }` | Represents indices of prop placement nodes.These nodes are on playable area and close to a wall. |
