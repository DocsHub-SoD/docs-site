# Class: DewPersistence.GeneralData

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewPersistence.GemData](/api/Global.DewPersistence.GemData) → [DewPersistence.RoomActorData](/api/Global.DewPersistence.RoomActorData) → [DewPersistence.SkillData](/api/Global.DewPersistence.SkillData) → [DewPersistence.StatusEffectData](/api/Global.DewPersistence.StatusEffectData)

```csharp
public class DewPersistence.GeneralData
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`persistenceData`** | `public Dictionary<string, string> persistenceData` |  |
| **`prevNetId`** | `public uint prevNetId` |  |
| **`resId`** | `public string resId` |  |
| **`resType`** | `public ResourceLinkBy resType` |  |

:::

## Methods (2)

::: details `Capture(Actor)`

This object is mutated, and self is returned.

```csharp
public virtual DewPersistence.GeneralData Capture(Actor target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `DewPersistence.GeneralData`

:::

::: details `GetPrefab&lt;T&gt;()`

```csharp
public virtual T GetPrefab<T>() where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (0)

*No outgoing class dependencies recorded.*

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#resourcelinkby" class="enum-link" data-tooltip="None=0 · Type=1 · Guid=2 · Name=3">ResourceLinkBy</a>

:::
