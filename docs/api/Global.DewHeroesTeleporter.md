# Class: DewHeroesTeleporter

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewHeroesTeleporter : MonoBehaviour, IPlayerPathablePoint
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`destination`** | `[InfoBox("Heroes will be teleported to the destination spread in local x-axis", InfoMessageType.Info, null)] public Transform destination` |  |
| **`spacing`** | `public float spacing` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`pathablePosition`** | `public Vector3 pathablePosition { get; }` |  |

:::

## Methods (1)

::: details `TeleportAllHeroes()`

```csharp
public void TeleportAllHeroes()
```

:::
