# Struct: PerMonsterTypeData&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct PerMonsterTypeData<T>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`boss`** | `public T boss` |  |
| **`lesser`** | `public T lesser` |  |
| **`miniBoss`** | `public T miniBoss` |  |
| **`normal`** | `public T normal` |  |

## Methods

### `Get(MonsterType)`

```csharp
public T Get(Monster.MonsterType type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`Monster.MonsterType`](/api/Global.Monster) |  |

**Returns:** `T`

### `Set(MonsterType, T)`

```csharp
public void Set(Monster.MonsterType type, T value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`Monster.MonsterType`](/api/Global.Monster) |  |
| `value` | `T` |  |
