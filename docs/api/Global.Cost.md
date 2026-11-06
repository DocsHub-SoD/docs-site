# Struct: Cost

- **Category:** <span class="cat-dot" style="--cat-color: #eab308" data-cat="Items & Economy"></span> Items & Economy
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct Cost
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`dreamDust`** | `public int dreamDust` |  |
| **`gold`** | `public int gold` |  |
| **`healthPercentage`** | `public int healthPercentage` |  |
| **`platinumCoin`** | `public int platinumCoin` |  |
| **`stardust`** | `public int stardust` |  |

:::

## Methods (12)

::: details `CanAfford(DewPlayer, int)`

```csharp
public AffordType CanAfford(DewPlayer player, int playerStardust = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `playerStardust` | `int` |  |

**Returns:** `AffordType`

:::

::: details `CanAfford(Entity, int)`

```csharp
public AffordType CanAfford(Entity entity, int playerStardust = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `playerStardust` | `int` |  |

**Returns:** `AffordType`

:::

::: details `DreamDust(int)`

```csharp
public static Cost DreamDust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `Equals(Cost)`

```csharp
public bool Equals(Cost other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`Cost`](/api/Global.Cost) |  |

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

::: details `Gold(int)`

```csharp
public static Cost Gold(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `HealthPercentage(int)`

```csharp
public static Cost HealthPercentage(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `MultiplyGold(float)`

```csharp
public Cost MultiplyGold(float scalar)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `scalar` | `float` |  |

**Returns:** `Cost`

:::

::: details `Platinum(int)`

```csharp
public static Cost Platinum(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `Stardust(int)`

```csharp
public static Cost Stardust(int amount)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `amount` | `int` |  |

**Returns:** `Cost`

:::

::: details `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

:::
