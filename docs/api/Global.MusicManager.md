# Class: MusicManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [MusicManager](/api/Global.MusicManager)

```csharp
public class MusicManager : ManagerBase<MusicManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fadeOutTime`** | `public float fadeOutTime` |  |
| **`volumeMultiplier`** | `public float volumeMultiplier` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `Pause()`

```csharp
public void Pause()
```

### `Play(DewMusicItem)`

```csharp
public void Play(DewMusicItem music)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `music` | [DewMusicItem](/api/Global.DewMusicItem) |  |

### `Stop()`

```csharp
public void Stop()
```

### `UnPause()`

```csharp
public void UnPause()
```
