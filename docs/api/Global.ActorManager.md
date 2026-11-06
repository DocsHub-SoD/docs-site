# Class: ActorManager

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ActorManager](/api/Global.ActorManager)

```csharp
public class ActorManager : NetworkedManagerBase<ActorManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allActors`** | `public HashSet<Actor> allActors` | All actors present. This only includes active actors. |
| **`allActorsBeingDestroyed`** | `public HashSet<Actor> allActorsBeingDestroyed` |  |
| **`allEntities`** | `public HashSet<Entity> allEntities` | All entities present. This only includes alive entities. |
| **`allHeroes`** | `public List<Hero> allHeroes` | All heroes present. |
| **`ClientEvent_OnActorAdd`** | `public SafeAction<Actor> ClientEvent_OnActorAdd` |  |
| **`ClientEvent_OnActorRemove`** | `public SafeAction<Actor> ClientEvent_OnActorRemove` |  |
| **`ClientEvent_OnAwakeEntityAdd`** | `public SafeAction<Entity> ClientEvent_OnAwakeEntityAdd` |  |
| **`ClientEvent_OnAwakeEntityRemove`** | `public SafeAction<Entity> ClientEvent_OnAwakeEntityRemove` |  |
| **`ClientEvent_OnEntityAdd`** | `public SafeAction<Entity> ClientEvent_OnEntityAdd` |  |
| **`ClientEvent_OnEntityRemove`** | `public SafeAction<Entity> ClientEvent_OnEntityRemove` |  |
| **`ClientEvent_OnHeroAdd`** | `public SafeAction<Hero> ClientEvent_OnHeroAdd` |  |
| **`ClientEvent_OnHeroRemove`** | `public SafeAction<Hero> ClientEvent_OnHeroRemove` |  |
| **`ClientEvent_OnLocalHeroAdd`** | `public SafeAction<Hero> ClientEvent_OnLocalHeroAdd` |  |
| **`ClientEvent_OnLocalHeroRemove`** | `public SafeAction<Hero> ClientEvent_OnLocalHeroRemove` |  |
| **`enableUsefulActorName`** | `public static bool enableUsefulActorName` |  |
| **`onActorBeforePrepare`** | `public SafeAction<Actor> onActorBeforePrepare` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`numOfActors`** | `[ShowInInspector] public int numOfActors { get; }` |  |
| **`numOfEntities`** | `[ShowInInspector] public int numOfEntities { get; }` |  |
| **`numOfHeroes`** | `[ShowInInspector] public int numOfHeroes { get; }` |  |
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
