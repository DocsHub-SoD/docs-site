# Class: DewCutsceneDirector

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
[ExecuteAlways]
[RequireComponent(typeof(PlayableDirector))]
public class DewCutsceneDirector : DewNetworkBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`cutsceneStartDelay`** | `public float cutsceneStartDelay` |  |
| **`disableAi`** | `public bool disableAi` |  |
| **`disableEndTransition`** | `public bool disableEndTransition` |  |
| **`disableStartTransition`** | `public bool disableStartTransition` |  |
| **`enableSkip`** | `public bool enableSkip` |  |
| **`endBeforeTimelineStops`** | `public bool endBeforeTimelineStops` |  |
| **`onFinish`** | `public Action onFinish` |  |
| **`onFinishAfterFadeIn`** | `public Action onFinishAfterFadeIn` | Called everywhere when this cutscene stops playing. |
| **`onPlay`** | `public Action onPlay` |  |
| **`reenableAiDelay`** | `[ShowIf("disableAi", true)]
public float reenableAiDelay` |  |
| **`stopAllPlayers`** | `public bool stopAllPlayers` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isPlaying`** | `public bool isPlaying { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `CmdSkip()`

```csharp
public void CmdSkip()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `Play()`

```csharp
[Button]
public void Play()
```

### `PlayNetworked()`

```csharp
public void PlayNetworked()
```
