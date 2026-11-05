# Class: ActorManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ActorManager](/api/Global.ActorManager)

```csharp
public class ActorManager : NetworkedManagerBase<ActorManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allActors`** | `public HashSet&lt;Actor&gt; allActors` | All actors present. This only includes active actors. |
| **`allActorsBeingDestroyed`** | `public HashSet&lt;Actor&gt; allActorsBeingDestroyed` |  |
| **`allEntities`** | `public HashSet&lt;Entity&gt; allEntities` | All entities present. This only includes alive entities. |
| **`allHeroes`** | `public List&lt;Hero&gt; allHeroes` | All heroes present. |
| **`ClientEvent_OnActorAdd`** | `public SafeAction&lt;Actor&gt; ClientEvent_OnActorAdd` |  |
| **`ClientEvent_OnActorRemove`** | `public SafeAction&lt;Actor&gt; ClientEvent_OnActorRemove` |  |
| **`ClientEvent_OnAwakeEntityAdd`** | `public SafeAction&lt;Entity&gt; ClientEvent_OnAwakeEntityAdd` |  |
| **`ClientEvent_OnAwakeEntityRemove`** | `public SafeAction&lt;Entity&gt; ClientEvent_OnAwakeEntityRemove` |  |
| **`ClientEvent_OnEntityAdd`** | `public SafeAction&lt;Entity&gt; ClientEvent_OnEntityAdd` |  |
| **`ClientEvent_OnEntityRemove`** | `public SafeAction&lt;Entity&gt; ClientEvent_OnEntityRemove` |  |
| **`ClientEvent_OnHeroAdd`** | `public SafeAction&lt;Hero&gt; ClientEvent_OnHeroAdd` |  |
| **`ClientEvent_OnHeroRemove`** | `public SafeAction&lt;Hero&gt; ClientEvent_OnHeroRemove` |  |
| **`ClientEvent_OnLocalHeroAdd`** | `public SafeAction&lt;Hero&gt; ClientEvent_OnLocalHeroAdd` |  |
| **`ClientEvent_OnLocalHeroRemove`** | `public SafeAction&lt;Hero&gt; ClientEvent_OnLocalHeroRemove` |  |
| **`enableUsefulActorName`** | `public static bool enableUsefulActorName` |  |
| **`onActorBeforePrepare`** | `public SafeAction&lt;Actor&gt; onActorBeforePrepare` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`numOfActors`** | `[ShowInInspector]
public int numOfActors { get; }` |  |
| **`numOfEntities`** | `[ShowInInspector]
public int numOfEntities { get; }` |  |
| **`numOfHeroes`** | `[ShowInInspector]
public int numOfHeroes { get; }` |  |
| **`serverActor`** | `public Actor serverActor { get; set; }` |  |

## Methods

### `CleanupActorsBeforeShutdown()`

```csharp
public static void CleanupActorsBeforeShutdown()
```

### `ClearSceneIdOfAllActors()`

```csharp
public void ClearSceneIdOfAllActors()
```

### `DoSleepLogicUpdate(float)`

```csharp
public void DoSleepLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnStart()`

```csharp
public override void OnStart()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```
