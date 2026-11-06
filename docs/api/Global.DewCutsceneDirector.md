# Class: DewCutsceneDirector

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[ExecuteAlways] [RequireComponent]`
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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (8)

*Classes and systems that invoke, reference, or depend on `DewCutsceneDirector`:*

[CameraManager](/api/Global.CameraManager) · [DewBossRoomEntry](/api/Global.DewBossRoomEntry) · `DewConsoleCommands` · `Ink_SecondCutscenePlay` · `Primus_Ending` · `Shrine_PrimusDoor` · `Sky_BossIntruder` · `StarlessPath_BossPolarisManager`

### Dependencies (8)

*Types and components that `DewCutsceneDirector` references or depends upon:*

[CameraManager](/api/Global.CameraManager) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityVisual](/api/Global.EntityVisual) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1)

:::
