# Class: ConversationManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ConversationManager](/api/Global.ConversationManager)

```csharp
public class ConversationManager : NetworkedManagerBase<ConversationManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ClientEvent_OnConversationLineRequestedCompletion`** | `public SafeAction<uint> ClientEvent_OnConversationLineRequestedCompletion` |  |
| **`ClientEvent_OnConversationShowLineAndRequestUserInput`** | `public SafeAction<uint, ShownConversation> ClientEvent_OnConversationShowLineAndRequestUserInput` |  |
| **`ClientEvent_OnStartConversation`** | `public SafeAction<uint> ClientEvent_OnStartConversation` |  |
| **`ClientEvent_OnStopConversation`** | `public SafeAction<uint> ClientEvent_OnStopConversation` |  |
| **`convSettings`** | `public readonly Dictionary<uint, DewConversationSettings> convSettings` | Currently ongoing conversations. Available everywhere. |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hasOngoingLocalConversation`** | `public bool hasOngoingLocalConversation { get; }` | Does local has ongoing conversation with advance authority? |
| **`ongoingLocalConversation`** | `public DewConversationSettings ongoingLocalConversation { get; }` |  |

## Methods

### `CmdDoUserInputOnConversation(uint, int, int, NetworkConnectionToClient)`

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

### `CmdRequestLineCompletion(uint, int, NetworkConnectionToClient)`

```csharp
public void CmdRequestLineCompletion(uint id, int lineIndex, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |
| `lineIndex` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `StartConversation(DewConversationSettings)`

```csharp
public uint StartConversation(DewConversationSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`DewConversationSettings`](/api/Global.DewConversationSettings) |  |

**Returns:** `uint`

### `StartConversationRoutine(DewConversationSettings)`

A coroutine that ends when the conversation ends.

```csharp
public IEnumerator StartConversationRoutine(DewConversationSettings s)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [`DewConversationSettings`](/api/Global.DewConversationSettings) |  |

**Returns:** `System.Collections.IEnumerator`

### `StopConversation(uint)`

```csharp
public void StopConversation(uint id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |
