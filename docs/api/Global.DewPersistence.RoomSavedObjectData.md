# Class: DewPersistence.RoomSavedObjectData

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewPersistence.RoomSavedObjectData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`guid`** | `public string guid` |  |
| **`persistenceData`** | `public Dictionary&lt;string, string&gt; persistenceData` |  |
| **`scenePath`** | `public string scenePath` |  |

## Methods

### `Capture(RoomSavedObject)`

This object is mutated, and self is returned.

```csharp
public DewPersistence.RoomSavedObjectData Capture(RoomSavedObject target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [RoomSavedObject](/api/Global.RoomSavedObject) |  |

**Returns:** `DewPersistence.RoomSavedObjectData`
