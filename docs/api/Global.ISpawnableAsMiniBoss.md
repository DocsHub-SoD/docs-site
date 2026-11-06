# Interface: ISpawnableAsMiniBoss

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ISpawnableAsMiniBoss
```

## Methods

### `GiveGenericMiniBossBonus(Entity, float)`

```csharp
public static void GiveGenericMiniBossBonus(Entity entity, float postDelayMultiplier = 0.5)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `postDelayMultiplier` | `float` |  |

### `OnBeforeSpawnAsMiniBoss()`

Called on server before being spawned as an elite.

```csharp
void OnBeforeSpawnAsMiniBoss()
```

### `OnCreateAsMiniBoss()`

Called everywhere after being spawned as an elite.

```csharp
void OnCreateAsMiniBoss()
```
