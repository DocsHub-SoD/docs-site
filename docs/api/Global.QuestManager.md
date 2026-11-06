# Class: QuestManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [QuestManager](/api/Global.QuestManager)

```csharp
public class QuestManager : NetworkedManagerBase<QuestManager>, ILogicUpdate
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`activeQuests`** | `[NonSerialized] public List<DewQuest> activeQuests` |  |
| **`ClientEvent_OnArtifactAppraised`** | `public SafeAction<string, bool> ClientEvent_OnArtifactAppraised` | Called everywhere when an artifact is appraised.Second boolean parameter denotes whether the artifact is new and now unlocked. |
| **`ClientEvent_OnArtifactPickedUp`** | `public SafeAction<string, DewPlayer, Vector3> ClientEvent_OnArtifactPickedUp` | Called everywhere when an artifact is picked up. Parameters denote: artifact type, player, artifact world position |
| **`ClientEvent_OnArtifactRemoved`** | `public SafeAction<string> ClientEvent_OnArtifactRemoved` |  |
| **`ClientEvent_OnQuestAdded`** | `public SafeAction<DewQuest> ClientEvent_OnQuestAdded` |  |
| **`ClientEvent_OnQuestRemoved`** | `public SafeAction<DewQuest> ClientEvent_OnQuestRemoved` |  |
| **`didCollectArtifactThisLoop`** | `[SaveVar] [NonSerialized] [SaveVar(SaveVarFlags.Default)] public bool didCollectArtifactThisLoop` | Available on server. |
| **`undiscoveredArtifacts`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] [NonSerialized] public List<string> undiscoveredArtifacts` | Available on server. List of artifacts that are not discovered by any clients. |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`artifactPool`** | `public Type[] artifactPool { get; }` |  |
| **`currentArtifact`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public string currentArtifact { get; }` |  |

:::

## Methods (11)

::: details `DiscoverArtifactAndShowStory(string)`

Discover an artifact and show the story to everyone.

```csharp
public void DiscoverArtifactAndShowStory(string artifact)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifact` | `string` |  |

:::

::: details `HasQuest(Type)`

```csharp
public bool HasQuest(Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |

**Returns:** `bool`

:::

::: details `HasQuest&lt;T&gt;()`

```csharp
public bool HasQuest<T>() where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `PickUpArtifact(string, DewPlayer, Vector3)`

```csharp
public void PickUpArtifact(string artifactName, DewPlayer player, Vector3 worldPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `artifactName` | `string` |  |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `worldPos` | `UnityEngine.Vector3` |  |

:::

::: details `RemoveArtifact()`

```csharp
public void RemoveArtifact()
```

:::

::: details `StartQuest&lt;T&gt;(T, Action&lt;T&gt;)`

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

:::

::: details `StartQuest&lt;T&gt;(Action&lt;T&gt;)`

```csharp
public T StartQuest<T>(Action<T> beforePrepare = null) where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `beforePrepare` | `System.Action<T>` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `TryGetQuest(Type, out DewQuest)`

```csharp
public bool TryGetQuest(Type type, out DewQuest quest)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `quest` | [`DewQuest`](/api/Global.DewQuest) |  |

**Returns:** `bool`

:::

::: details `TryGetQuest&lt;T&gt;(out T)`

```csharp
public bool TryGetQuest<T>(out T quest) where T : DewQuest
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `quest` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (19)

*Classes and systems that invoke, reference, or depend on `QuestManager`:*

[Artifact](/api/Global.Artifact) · [CurseStatusEffect](/api/Global.CurseStatusEffect) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Primus_Ending` · `RoomMod_Artifact` · `RoomMod_DreamTeller` · `Se_HeroKnockedOut` · `Shrine_ArtifactGiver` · `Shrine_FragmentOfRadiance` · `Shrine_InvitationOfJonasMeeting` · `Shrine_StrayMemory_StartProp` · `Shrine_TheConsortOfNight` · `Treasure_InvitationToSecretMeetingOfJonas` · `Treasure_StarSeekersJournal` · `Treasure_StrayMemory` · `Treasure_TotallyGenuineTreasureMap` · `Treasure_TreasureMap` · `UI_InGame_CurrentArtifact`

### Dependencies (15)

*Types and components that `QuestManager` references or depends upon:*

[Dew](/api/Global.Dew) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · [DewResources](/api/Global.DewResources) · [DewSave](/api/Global.DewSave) · [Entity](/api/Global.Entity) · [InGameUIManager](/api/Global.InGameUIManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags)

:::
