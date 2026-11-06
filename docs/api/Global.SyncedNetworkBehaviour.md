# Struct: SyncedNetworkBehaviour

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct SyncedNetworkBehaviour
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`componentIndex`** | `public byte componentIndex` |  |
| **`netId`** | `public uint netId` |  |

:::

## Methods (3)

::: details `Equals(SyncedNetworkBehaviour)`

```csharp
public bool Equals(SyncedNetworkBehaviour other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`SyncedNetworkBehaviour`](/api/Global.SyncedNetworkBehaviour) |  |

**Returns:** `bool`

:::

::: details `Equals(uint, int)`

```csharp
public bool Equals(uint netId, int componentIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `netId` | `uint` |  |
| `componentIndex` | `int` |  |

**Returns:** `bool`

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `SyncedNetworkBehaviour`:*

[EntityAbility](/api/Global.EntityAbility) · [HeroSkill](/api/Global.HeroSkill) · `NetworkBehaviourDictionaryWrapper`2` · `NetworkBehaviourListWrapper`1` · `Mirror.GeneratedNetworkCode`

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
