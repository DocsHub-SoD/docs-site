# Struct: GetFocusTargetSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct GetFocusTargetSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`angleLimit`** | `public Vector2 angleLimit` |  |
| **`cacheData`** | `public GetFocusTargetCacheData cacheData` |  |
| **`condition`** | `public Func&lt;IGamepadFocusable, bool&gt; condition` | When condition is not null, focusable groups will be ignored. |
| **`customScoreFunc`** | `public Func&lt;IGamepadFocusable, float&gt; customScoreFunc` |  |
| **`direction`** | `public Vector3 direction` |  |
| **`normalizedDistLimit`** | `public Vector2 normalizedDistLimit` |  |
| **`normalizedPerpendicularDistLimit`** | `public Vector2 normalizedPerpendicularDistLimit` |  |
| **`useCenterOfRect`** | `public bool useCenterOfRect` |  |
