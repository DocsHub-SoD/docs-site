# Class: EntitySound

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
public class EntitySound : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (7)

::: details Click to expand Fields (7)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnFootstep`** | `public SafeAction ClientEvent_OnFootstep` |  |
| **`conversationClick`** | `public DewAudioClip conversationClick` |  |
| **`conversationStart`** | `public DewAudioClip conversationStart` |  |
| **`voiceDeath`** | `public DewAudioClip voiceDeath` |  |
| **`voiceIdle`** | `public DewAudioClip voiceIdle` |  |
| **`voiceIdleInterval`** | `public Vector2 voiceIdleInterval` |  |
| **`voiceStart`** | `public DewAudioClip voiceStart` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canDestroy`** | `public bool canDestroy { get; }` |  |

:::

## Methods (8)

::: details `DoFootstep()`

Play footstep effect.

```csharp
public void DoFootstep()
```

:::

::: details `DoPeriodicSurfaceEffect()`

Do periodic effect on the surface the entity is currently on.

```csharp
public void DoPeriodicSurfaceEffect()
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

::: details `OnCleanup()`

```csharp
public void OnCleanup()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `Say(DewAudioClip, bool)`

```csharp
public void Say(DewAudioClip clip, bool interruptPrevious)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAudioClip`](/api/Global.DewAudioClip) |  |
| `interruptPrevious` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `EntitySound`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Entity](/api/Global.Entity) · [EntityFootsteps](/api/Global.EntityFootsteps)

### Dependencies (21)

*Types and components that `EntitySound` references or depends upon:*

[Actor](/api/Global.Actor) · [Dew](/api/Global.Dew) · [DewAudioClip](/api/Global.DewAudioClip) · [DewAudioSource](/api/Global.DewAudioSource) · [DewEffect](/api/Global.DewEffect) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewSurfaceData](/api/Global.DewSurfaceData) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityComponent](/api/Global.EntityComponent) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [EventInfoKill](/api/Global.EventInfoKill) · [ICleanup](/api/Global.ICleanup) · `NetworkReaderWriterExtensions` · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · `VectorPlaneTransformExtension`

:::
