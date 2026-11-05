# Class: RoomSectionComponent

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [Section_Monsters](/api/Global.Section_Monsters) → [Section_Props](/api/Global.Section_Props)

```csharp
[LogicUpdatePriority(200)]
[RequireComponent(typeof(RoomSection))]
public class RoomSectionComponent : LogicBehaviour, ILogicUpdate
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`section`** | `public RoomSection section { get; }` |  |

## Methods

### `Awake()`

```csharp
protected virtual void Awake()
```
