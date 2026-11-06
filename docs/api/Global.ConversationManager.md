# Class: ConversationManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ConversationManager](/api/Global.ConversationManager)

```csharp
public class ConversationManager : NetworkedManagerBase<ConversationManager>, ILogicUpdate
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnConversationLineRequestedCompletion`** | `public SafeAction<uint> ClientEvent_OnConversationLineRequestedCompletion` |  |
| **`ClientEvent_OnConversationShowLineAndRequestUserInput`** | `public SafeAction<uint, ShownConversation> ClientEvent_OnConversationShowLineAndRequestUserInput` |  |
| **`ClientEvent_OnStartConversation`** | `public SafeAction<uint> ClientEvent_OnStartConversation` |  |
| **`ClientEvent_OnStopConversation`** | `public SafeAction<uint> ClientEvent_OnStopConversation` |  |
| **`convSettings`** | `public readonly Dictionary<uint, DewConversationSettings> convSettings` | Currently ongoing conversations. Available everywhere. |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hasOngoingLocalConversation`** | `public bool hasOngoingLocalConversation { get; }` | Does local has ongoing conversation with advance authority? |
| **`ongoingLocalConversation`** | `public DewConversationSettings ongoingLocalConversation { get; }` |  |

:::

## Methods (7)

::: details `CmdDoUserInputOnConversation(uint, int, int, NetworkConnectionToClient)`

```csharp
public void CmdDoUserInputOnConversation(uint id, int lineIndexFrom, int userInput, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |
| `lineIndexFrom` | `int` |  |
| `userInput` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `CmdRequestLineCompletion(uint, int, NetworkConnectionToClient)`

```csharp
public void CmdRequestLineCompletion(uint id, int lineIndex, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |
| `lineIndex` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `StartConversation(DewConversationSettings)`

```csharp
public uint StartConversation(DewConversationSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`DewConversationSettings`](/api/Global.DewConversationSettings) |  |

**Returns:** `uint`

:::

::: details `StartConversationRoutine(DewConversationSettings)`

A coroutine that ends when the conversation ends.

```csharp
public IEnumerator StartConversationRoutine(DewConversationSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`DewConversationSettings`](/api/Global.DewConversationSettings) |  |

**Returns:** `System.Collections.IEnumerator`

:::

::: details `StopConversation(uint)`

```csharp
public void StopConversation(uint id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (10)

*Classes and systems that invoke, reference, or depend on `ConversationManager`:*

[CameraManager](/api/Global.CameraManager) · [ControlManager](/api/Global.ControlManager) · `ConversationShrineBase` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_Intro` · `PlayTutorial_Tutorial_SkillsAndEssences` · `Shrine_ArtifactGiver` · `UI_InGame_Conversations_Instance` · `UI_InGame_CurrentArtifact`

### Dependencies (18)

*Types and components that `ConversationManager` references or depends upon:*

[Actor](/api/Global.Actor) · [ControlManager](/api/Global.ControlManager) · [DewConversationExecutionContext](/api/Global.DewConversationExecutionContext) · [DewConversationSettings](/api/Global.DewConversationSettings) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [ManagerBase`1](/api/Global.ManagerBase`1) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [WildcardMatch](/api/Global.WildcardMatch) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

:::
