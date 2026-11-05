# Class: DewPersistence.GeneralData

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistence.GemData](/api/Global.DewPersistence.GemData) → [DewPersistence.RoomActorData](/api/Global.DewPersistence.RoomActorData) → [DewPersistence.SkillData](/api/Global.DewPersistence.SkillData) → [DewPersistence.StatusEffectData](/api/Global.DewPersistence.StatusEffectData)

```csharp
public class DewPersistence.GeneralData
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`persistenceData`** | `public Dictionary&lt;string, string&gt; persistenceData` |  |
| **`prevNetId`** | `public uint prevNetId` |  |
| **`resId`** | `public string resId` |  |
| **`resType`** | `public ResourceLinkBy resType` |  |

## Methods

### `Capture(Actor)`

This object is mutated, and self is returned.

```csharp
public virtual DewPersistence.GeneralData Capture(Actor target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [Actor](/api/Global.Actor) |  |

**Returns:** `DewPersistence.GeneralData`

### `GetPrefab&lt;T&gt;()`

```csharp
public virtual T GetPrefab<T>() where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`
