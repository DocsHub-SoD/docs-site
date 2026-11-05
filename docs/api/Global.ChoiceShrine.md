# Class: ChoiceShrine

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Shrine](/api/Global.Shrine)

```csharp
public abstract class ChoiceShrine : Shrine, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IProp, IBanRoomNodesNearby
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`choices`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncDictionary&lt;string, ChoiceShrineItem[]&gt; choices` |  |
| **`ClientEvent_OnChoicesUpdated`** | `public SafeAction ClientEvent_OnChoicesUpdated` |  |
| **`itemCount`** | `public int itemCount` |  |
| **`onItemsPopulated`** | `public SafeAction&lt;DewPlayer&gt; onItemsPopulated` | Called on server. |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `CmdChoose(int, NetworkConnectionToClient)`

```csharp
public void CmdChoose(int index, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnPopulateChoices(DewPlayer)`

```csharp
protected abstract void OnPopulateChoices(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

### `OnUse(Entity)`

```csharp
protected override bool OnUse(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`

### `PopulatePlayerChoices(DewPlayer)`

```csharp
public void PopulatePlayerChoices(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |
