# Struct: PerMonsterTypeData&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct PerMonsterTypeData<T>
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`boss`** | `public T boss` |  |
| **`lesser`** | `public T lesser` |  |
| **`miniBoss`** | `public T miniBoss` |  |
| **`normal`** | `public T normal` |  |

:::

## Methods (2)

::: details `Get(MonsterType)`

```csharp
public T Get(Monster.MonsterType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`Monster.MonsterType`](/api/Global.Monster) |  |

**Returns:** `T`

:::

::: details `Set(MonsterType, T)`

```csharp
public void Set(Monster.MonsterType type, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`Monster.MonsterType`](/api/Global.Monster) |  |
| `value` | `T` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `PerMonsterTypeData<T>`:*

[DewGameplayExperienceSettings](/api/Global.DewGameplayExperienceSettings) · [GameManager](/api/Global.GameManager) · [PickupManager](/api/Global.PickupManager)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
