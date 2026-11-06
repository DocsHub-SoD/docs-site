# Class: ChatManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ChatManager](/api/Global.ChatManager)

```csharp
public class ChatManager : NetworkedManagerBase<ChatManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ChatContentColorHex`** | `public const string ChatContentColorHex = "#e4edf0"` |  |
| **`ChatMessage_MaxLength`** | `public const int ChatMessage_MaxLength = 100` |  |
| **`ChatMessage_RateLimitCount`** | `public const int ChatMessage_RateLimitCount = 8` |  |
| **`ChatMessage_RateLimitLockTime`** | `public const float ChatMessage_RateLimitLockTime = 8` |  |
| **`ChatMessage_RateLimitTimeframe`** | `public const float ChatMessage_RateLimitTimeframe = 12` |  |
| **`ClientEvent_OnEmoteReceived`** | `public SafeAction<DewPlayer, string> ClientEvent_OnEmoteReceived` |  |
| **`ClientEvent_OnMessageReceived`** | `public SafeAction<ChatManager.Message> ClientEvent_OnMessageReceived` |  |
| **`Emote_CooldownTime`** | `public const float Emote_CooldownTime = 1.4` |  |

## Methods

### `BroadcastAdvText(string)`

```csharp
public void BroadcastAdvText(string advText)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `advText` | `string` |  |

### `BroadcastMessage(Message)`

```csharp
public void BroadcastMessage(ChatManager.Message message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [`ChatManager.Message`](/api/Global.ChatManager) |  |

### `CmdSendAchievementMessage(string, NetworkConnectionToClient)`

```csharp
public void CmdSendAchievementMessage(string achKey, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `achKey` | `string` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `CmdSendChatMessage(string, NetworkConnectionToClient)`

```csharp
public void CmdSendChatMessage(string content, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `content` | `string` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `CmdSendEmote(string, NetworkConnectionToClient)`

```csharp
public void CmdSendEmote(string emoteName, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `CmdSendPingMessage(string, NetworkConnectionToClient)`

```csharp
public void CmdSendPingMessage(string advMessage, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `advMessage` | `string` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `GetColoredDescribedPlayerName(DewPlayer)`

```csharp
public static string GetColoredDescribedPlayerName(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `string`

### `GetColoredGemName(string, int)`

```csharp
public static string GetColoredGemName(string typeName, int quality)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |
| `quality` | `int` |  |

**Returns:** `string`

### `GetColoredSkillName(string, int)`

```csharp
public static string GetColoredSkillName(string typeName, int level)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `typeName` | `string` |  |
| `level` | `int` |  |

**Returns:** `string`

### `GetDescribedPlayerName(DewPlayer)`

```csharp
public static string GetDescribedPlayerName(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `string`

### `GetFormattedChatContent(string, string)`

```csharp
public static string GetFormattedChatContent(string playerName, string content)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `playerName` | `string` |  |
| `content` | `string` |  |

**Returns:** `string`

### `GetPlayerColorHex(DewPlayer)`

```csharp
public static string GetPlayerColorHex(DewPlayer player = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `string`

### `IncrementRateAndCheck(NetworkConnectionToClient)`

Increment chat rate of given player. Returns true if succeeds.Returns false if the player have exceeded the rate limit.

```csharp
public bool IncrementRateAndCheck(NetworkConnectionToClient connection)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `connection` | `Mirror.NetworkConnectionToClient` |  |

**Returns:** `bool`

### `IsChatLocked(NetworkConnectionToClient)`

Is chat disabled for given player? Chat will be disabled temporarily if a player sends chat messages too fast.

```csharp
public bool IsChatLocked(NetworkConnectionToClient connection)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `connection` | `Mirror.NetworkConnectionToClient` |  |

**Returns:** `bool`

### `IsPlayerMuted(DewPlayer)`

```csharp
public bool IsPlayerMuted(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `bool`

### `IsPlayerMutedByNetId(uint)`

```csharp
public bool IsPlayerMutedByNetId(uint playerNetId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `playerNetId` | `uint` |  |

**Returns:** `bool`

### `IsPlayerMutedBySteamId(ulong)`

```csharp
public bool IsPlayerMutedBySteamId(ulong playerSteamId)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `playerSteamId` | `ulong` |  |

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `MutePlayer(DewPlayer)`

```csharp
public void MutePlayer(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `RpcShowEmote(string, DewPlayer)`

```csharp
public void RpcShowEmote(string emoteName, DewPlayer sender)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `emoteName` | `string` |  |
| `sender` | [`DewPlayer`](/api/Global.DewPlayer) |  |

### `SendChatLockedNotice(NetworkConnectionToClient)`

```csharp
public void SendChatLockedNotice(NetworkConnectionToClient target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkConnectionToClient` |  |

### `SendChatMessage(NetworkConnection, Message)`

```csharp
public void SendChatMessage(NetworkConnection target, ChatManager.Message message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkConnection` |  |
| `message` | [`ChatManager.Message`](/api/Global.ChatManager) |  |

### `ShowMessageLocally(Message)`

```csharp
public void ShowMessageLocally(ChatManager.Message message)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `message` | [`ChatManager.Message`](/api/Global.ChatManager) |  |

### `UnmutePlayer(DewPlayer)`

```csharp
public void UnmutePlayer(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
