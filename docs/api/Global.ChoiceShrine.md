# Class: ChoiceShrine

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Shrine](/api/Global.Shrine)

```csharp
public abstract class ChoiceShrine : Shrine, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IProp, IBanRoomNodesNearby
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`choices`** | `[SaveVar(SaveVarFlags.Default)] public readonly SyncDictionary<string, ChoiceShrineItem[]> choices` |  |
| **`ClientEvent_OnChoicesUpdated`** | `public SafeAction ClientEvent_OnChoicesUpdated` |  |
| **`itemCount`** | `public int itemCount` |  |
| **`onItemsPopulated`** | `public SafeAction<DewPlayer> onItemsPopulated` | Called on server. |

:::

## Methods (7)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CmdChoose(int, NetworkConnectionToClient)`

```csharp
public void CmdChoose(int index, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnPopulateChoices(DewPlayer)`

```csharp
protected abstract void OnPopulateChoices(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `OnUse(Entity)`

```csharp
protected override bool OnUse(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `PopulatePlayerChoices(DewPlayer)`

```csharp
public void PopulatePlayerChoices(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::
