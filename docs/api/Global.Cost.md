# Struct: Cost

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct Cost
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dreamDust`** | `public int dreamDust` |  |
| **`gold`** | `public int gold` |  |
| **`healthPercentage`** | `public int healthPercentage` |  |
| **`platinumCoin`** | `public int platinumCoin` |  |
| **`stardust`** | `public int stardust` |  |

## Methods

### `CanAfford(DewPlayer, int)`

```csharp
public AffordType CanAfford(DewPlayer player, int playerStardust = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |
| `playerStardust` | `int` |  |

**Returns:** `AffordType`

### `CanAfford(Entity, int)`

```csharp
public AffordType CanAfford(Entity entity, int playerStardust = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [Entity](/api/Global.Entity) |  |
| `playerStardust` | `int` |  |

**Returns:** `AffordType`

### `DreamDust(int)`

```csharp
public static Cost DreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

### `Equals(Cost)`

```csharp
public bool Equals(Cost other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [Cost](/api/Global.Cost) |  |

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

### `Gold(int)`

```csharp
public static Cost Gold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

### `HealthPercentage(int)`

```csharp
public static Cost HealthPercentage(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

### `MultiplyGold(float)`

```csharp
public Cost MultiplyGold(float scalar)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `scalar` | `float` |  |

**Returns:** `Cost`

### `Platinum(int)`

```csharp
public static Cost Platinum(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

### `Stardust(int)`

```csharp
public static Cost Stardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

### `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`
