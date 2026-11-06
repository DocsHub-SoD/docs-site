# Struct: EntityAIContext

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EntityAIContext
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`targetEnemyLastKnownPosition`** | `public Vector3? targetEnemyLastKnownPosition` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`deltaTime`** | `public readonly float deltaTime { get; }` | Usually similar to aiInterval of this entity, but this can get longer if AI congestion control is active. |
| **`targetEnemy`** | `public readonly Entity targetEnemy { get; }` | Get this entity's primary target enemy. |
| **`targetEnemyElapsedTime`** | `public float targetEnemyElapsedTime { get; }` | Get elapsed time since this entity chose its primary target enemy. |
