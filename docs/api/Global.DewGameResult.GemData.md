# Struct: DewGameResult.GemData

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct DewGameResult.GemData
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`capturedTooltipFields`** | `public Dictionary<string, string> capturedTooltipFields` |  |
| **`location`** | `public GemLocation location` |  |
| **`name`** | `public string name` |  |
| **`netId`** | `public uint netId` |  |
| **`quality`** | `public int quality` |  |

:::

## Methods (2)

::: details `CaptureTooltipFields(Gem)`

```csharp
public void CaptureTooltipFields(Gem gem)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gem` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `GetGem()`

```csharp
public Gem GetGem()
```

**Returns:** `Gem`

:::
