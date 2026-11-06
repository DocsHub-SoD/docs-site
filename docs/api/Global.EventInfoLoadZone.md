# Struct: EventInfoLoadZone

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoLoadZone
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`from`** | `public string from` |  |
| **`isLoadingFromSave`** | `public bool isLoadingFromSave` |  |
| **`isTraveling`** | `public bool isTraveling` | Is this load result of traveling through a rift? (including the start of the game)This is true if:We just started the gameWe moved to the next zone via exit riftWe are loading from save, and we were moving to the next zone.This is false if:We are loading from save and the player was already in this zone |
| **`to`** | `public string to` |  |

:::
