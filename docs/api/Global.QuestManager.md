# Class: QuestManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [QuestManager](/api/Global.QuestManager)

```csharp
public class QuestManager : NetworkedManagerBase<QuestManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeQuests`** | `[NonSerialized] public List<DewQuest> activeQuests` |  |
| **`ClientEvent_OnArtifactAppraised`** | `public SafeAction<string, bool> ClientEvent_OnArtifactAppraised` | Called everywhere when an artifact is appraised.Second boolean parameter denotes whether the artifact is new and now unlocked. |
| **`ClientEvent_OnArtifactPickedUp`** | `public SafeAction<string, DewPlayer, Vector3> ClientEvent_OnArtifactPickedUp` | Called everywhere when an artifact is picked up. Parameters denote: artifact type, player, artifact world position |
| **`ClientEvent_OnArtifactRemoved`** | `public SafeAction<string> ClientEvent_OnArtifactRemoved` |  |
| **`ClientEvent_OnQuestAdded`** | `public SafeAction<DewQuest> ClientEvent_OnQuestAdded` |  |
| **`ClientEvent_OnQuestRemoved`** | `public SafeAction<DewQuest> ClientEvent_OnQuestRemoved` |  |
| **`didCollectArtifactThisLoop`** | `[NonSerialized] [SaveVar(SaveVarFlags.Default)] public bool didCollectArtifactThisLoop` | Available on server. |
| **`undiscoveredArtifacts`** | `[SaveVar(SaveVarFlags.Default)] [NonSerialized] public List<string> undiscoveredArtifacts` | Available on server. List of artifacts that are not discovered by any clients. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`artifactPool`** | `public Type[] artifactPool { get; }` |  |
| **`currentArtifact`** | `[SaveVar(SaveVarFlags.Default)] public string currentArtifact { get; }` |  |

## Methods

### `DiscoverArtifactAndShowStory(string)`

Discover an artifact and show the story to everyone.

```csharp
public void DiscoverArtifactAndShowStory(string artifact)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifact` | `string` |  |

### `HasQuest(Type)`

```csharp
public bool HasQuest(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `bool`

### `HasQuest<T>()`

```csharp
public bool HasQuest<T>() where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `PickUpArtifact(string, DewPlayer, Vector3)`

```csharp
public void PickUpArtifact(string artifactName, DewPlayer player, Vector3 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactName` | `string` |  |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `worldPos` | `UnityEngine.Vector3` |  |

### `RemoveArtifact()`

```csharp
public void RemoveArtifact()
```

### `StartQuest<T>(T, Action<T>)`

```csharp
public T StartQuest<T>(T prefab, Action<T> beforePrepare = null) where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `prefab` | `T` |  |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

### `StartQuest<T>(Action<T>)`

```csharp
public T StartQuest<T>(Action<T> beforePrepare = null) where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

### `TryGetQuest(Type, out DewQuest)`

```csharp
public bool TryGetQuest(Type type, out DewQuest quest)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `quest` | [`DewQuest`](/api/Global.DewQuest) |  |

**Returns:** `bool`

### `TryGetQuest<T>(out T)`

```csharp
public bool TryGetQuest<T>(out T quest) where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `quest` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`
