# Class: DispByDestination

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [Displacement](/api/Global.Displacement)

```csharp
public class DispByDestination : Displacement
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canGoOverTerrain`** | `public bool canGoOverTerrain` | Can this displacement go over terrain/go through walls?If this is false, the displacement might end up not reaching the desired destination.Default value is true. |
| **`curve`** | `public Vector4 curve` | Cubic bezier parameter. Use this to curve the movement trajectory.https://cubic-bezier.com/ |
| **`curveHorizontalDistance`** | `public float? curveHorizontalDistance` | Set the horizontal sway magnitude of the curve.If not set, the curve will be scaled to the length of the linear line. |
| **`destination`** | `public Vector3 destination` | Destination of this displacement. You should feed in a valid agent position using Dew.GetValidAgentPosition() |
| **`duration`** | `public float duration` | Duration of this displacement. |
| **`ease`** | `public DewEase ease` | Type of ease function that this displacement will follow over its course. |
