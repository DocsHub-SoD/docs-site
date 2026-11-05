# Class: DispByTarget

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [Displacement](/api/Global.Displacement)

```csharp
public class DispByTarget : Displacement
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cancelTime`** | `public float cancelTime` | Max duration of this displacement until it cancels itself.Default value is Infinity. |
| **`goalDistance`** | `public float goalDistance` | Goal distance. The displacement will finish when it reaches this distance to the target entity. |
| **`speed`** | `public float speed` | This displacement's speed in unit/s. |
| **`target`** | `public Entity target` | Target entity that this displacement will chase after. |
