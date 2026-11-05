# Struct: ReactionChain

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct ReactionChain
```

## Methods

### `DidReact(Actor, bool)`

Check if the actor has already contributed to this reaction chain.

```csharp
public bool DidReact(Actor actor, bool checkOnlyType = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |
| `checkOnlyType` | `bool` |  |

**Returns:** `bool`

### `Equals(ReactionChain)`

```csharp
public bool Equals(ReactionChain other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [ReactionChain](/api/Global.ReactionChain) |  |

**Returns:** `bool`

### `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

### `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

### `New(Actor)`

Returns new reaction chain with given actor in contribution.

```csharp
public ReactionChain New(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |

**Returns:** `ReactionChain`
