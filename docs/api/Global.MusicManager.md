# Class: MusicManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [MusicManager](/api/Global.MusicManager)

```csharp
public class MusicManager : ManagerBase<MusicManager>, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fadeOutTime`** | `public float fadeOutTime` |  |
| **`volumeMultiplier`** | `public float volumeMultiplier` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

:::

## Methods (6)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `Pause()`

```csharp
public void Pause()
```

:::

::: details `Play(DewMusicItem)`

```csharp
public void Play(DewMusicItem music)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `music` | [`DewMusicItem`](/api/Global.DewMusicItem) |  |

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::

::: details `UnPause()`

```csharp
public void UnPause()
```

:::
