# Class: EntitySound

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
public class EntitySound : EntityComponent, ILogicUpdate, ICleanup
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnFootstep`** | `public SafeAction ClientEvent_OnFootstep` |  |
| **`conversationClick`** | `public DewAudioClip conversationClick` |  |
| **`conversationStart`** | `public DewAudioClip conversationStart` |  |
| **`voiceDeath`** | `public DewAudioClip voiceDeath` |  |
| **`voiceIdle`** | `public DewAudioClip voiceIdle` |  |
| **`voiceIdleInterval`** | `public Vector2 voiceIdleInterval` |  |
| **`voiceStart`** | `public DewAudioClip voiceStart` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canDestroy`** | `public bool canDestroy { get; }` |  |

## Methods

### `DoFootstep()`

Play footstep effect.

```csharp
public void DoFootstep()
```

### `DoPeriodicSurfaceEffect()`

Do periodic effect on the surface the entity is currently on.

```csharp
public void DoPeriodicSurfaceEffect()
```

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnCleanup()`

```csharp
public void OnCleanup()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `Say(DewAudioClip, bool)`

```csharp
public void Say(DewAudioClip clip, bool interruptPrevious)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `clip` | [`DewAudioClip`](/api/Global.DewAudioClip) |  |
| `interruptPrevious` | `bool` |  |
