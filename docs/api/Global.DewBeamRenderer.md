# Class: DewBeamRenderer

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(1100)]
public class DewBeamRenderer : LogicBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`acrossEffect`** | `public GameObject acrossEffect` |  |
| **`acrossEffectInterval`** | `[ShowIf("@acrossEffect != null", true)]
public float acrossEffectInterval` |  |
| **`endEffect`** | `public GameObject endEffect` |  |
| **`lineRenderer`** | `public LineRenderer lineRenderer` |  |
| **`startEffect`** | `public GameObject startEffect` |  |

## Methods

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```

### `SetEndPoint(Vector3)`

```csharp
public void SetEndPoint(Vector3 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector3` |  |

### `SetPoints(Vector3, Vector3)`

```csharp
public void SetPoints(Vector3 start, Vector3 end)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `start` | `UnityEngine.Vector3` |  |
| `end` | `UnityEngine.Vector3` |  |

### `SetStartPoint(Vector3)`

```csharp
public void SetStartPoint(Vector3 point)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `point` | `UnityEngine.Vector3` |  |
