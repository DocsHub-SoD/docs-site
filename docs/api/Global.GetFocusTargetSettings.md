# Struct: GetFocusTargetSettings

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct GetFocusTargetSettings
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angleLimit`** | `public Vector2 angleLimit` |  |
| **`cacheData`** | `public GetFocusTargetCacheData cacheData` |  |
| **`condition`** | `public Func<IGamepadFocusable, bool> condition` | When condition is not null, focusable groups will be ignored. |
| **`customScoreFunc`** | `public Func<IGamepadFocusable, float> customScoreFunc` |  |
| **`direction`** | `public Vector3 direction` |  |
| **`normalizedDistLimit`** | `public Vector2 normalizedDistLimit` |  |
| **`normalizedPerpendicularDistLimit`** | `public Vector2 normalizedPerpendicularDistLimit` |  |
| **`useCenterOfRect`** | `public bool useCenterOfRect` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `GetFocusTargetSettings`:*

[GlobalUIManager](/api/Global.GlobalUIManager)

### Dependencies (1)

*Types and components that `GetFocusTargetSettings` references or depends upon:*

[GetFocusTargetCacheData](/api/Global.GetFocusTargetCacheData)

:::
