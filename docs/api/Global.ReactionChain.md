# Struct: ReactionChain

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct ReactionChain
```

## Methods (5)

::: details `DidReact(Actor, bool)`

Check if the actor has already contributed to this reaction chain.

```csharp
public bool DidReact(Actor actor, bool checkOnlyType = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |
| `checkOnlyType` | `bool` |  |

**Returns:** `bool`

:::

::: details `Equals(ReactionChain)`

```csharp
public bool Equals(ReactionChain other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`ReactionChain`](/api/Global.ReactionChain) |  |

**Returns:** `bool`

:::

::: details `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

:::

::: details `New(Actor)`

Returns new reaction chain with given actor in contribution.

```csharp
public ReactionChain New(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `ReactionChain`

:::
