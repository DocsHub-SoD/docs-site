# Class: DewSurfaceData

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewSurfaceData : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`banDecorations`** | `public bool banDecorations` |  |
| **`excludeLesserMonster`** | `[ShowIf("fxPeriodicEffect", true)] public bool excludeLesserMonster` |  |
| **`fxHeroFootstep`** | `public GameObject fxHeroFootstep` |  |
| **`fxPeriodicEffect`** | `public GameObject fxPeriodicEffect` |  |
| **`onlyWhenWalking`** | `[ShowIf("fxPeriodicEffect", true)] public bool onlyWhenWalking` |  |
| **`periodicEffectInterval`** | `[ShowIf("fxPeriodicEffect", true)] public Vector2 periodicEffectInterval` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`defaultSurface`** | `public static DewSurfaceData defaultSurface { get; }` |  |
