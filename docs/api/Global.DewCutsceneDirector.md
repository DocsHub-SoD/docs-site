# Class: DewCutsceneDirector

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
[ExecuteAlways]
[RequireComponent(typeof(PlayableDirector))]
public class DewCutsceneDirector : DewNetworkBehaviour, ILogicUpdate
```

## Fields (11)

::: details Click to expand Fields (11)

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
| **`reenableAiDelay`** | `[ShowIf("disableAi", true)] public float reenableAiDelay` |  |
| **`stopAllPlayers`** | `public bool stopAllPlayers` |  |

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

::: details `CmdSkip()`

```csharp
public void CmdSkip()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `Play()`

```csharp
[Button]
public void Play()
```

:::

::: details `PlayNetworked()`

```csharp
public void PlayNetworked()
```

:::
