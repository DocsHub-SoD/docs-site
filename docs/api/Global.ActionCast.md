# Class: ActionCast

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ActionBase](/api/Global.ActionBase)

```csharp
public class ActionCast : ActionBase
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`configIndex`** | `public int configIndex` |  |
| **`info`** | `public CastInfo info` |  |
| **`isPredictedOnCast`** | `public bool isPredictedOnCast` |  |
| **`predictTarget`** | `public Entity predictTarget` |  |
| **`skipRangeCheck`** | `public bool skipRangeCheck` |  |
| **`trigger`** | `public AbilityTrigger trigger` |  |

## Methods

### `GetMoveDestination()`

```csharp
public override Vector3? GetMoveDestination()
```

**Returns:** `UnityEngine.Vector3?`

### `GetMoveDestinationRequiredDistance()`

```csharp
public override float GetMoveDestinationRequiredDistance()
```

**Returns:** `float`

### `Tick()`

```csharp
public override bool Tick()
```

**Returns:** `bool`

### `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`
