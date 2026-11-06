# Class: DewAdvText

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewAdvText
```

## Methods (10)

::: details `Adv_ChatContent(DewPlayer, string)`

```csharp
public static string Adv_ChatContent(DewPlayer player, string content)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `content` | `string` |  |

**Returns:** `string`

:::

::: details `Adv_ColoredDescribedPlayerName(DewPlayer)`

```csharp
public static string Adv_ColoredDescribedPlayerName(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `string`

:::

::: details `Adv_Cost(Cost)`

```csharp
public static string Adv_Cost(Cost cost)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `cost` | [`Cost`](/api/Global.Cost) |  |

**Returns:** `string`

:::

::: details `Adv_DescribedPlayerName(DewPlayer)`

```csharp
public static string Adv_DescribedPlayerName(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `string`

:::

::: details `Adv_Format(string, params string[])`

```csharp
public static string Adv_Format(string template, params string[] args)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `template` | `string` |  |
| `args` | `string[]` |  |

**Returns:** `string`

:::

::: details `Adv_LocCurseName(string)`

```csharp
public static string Adv_LocCurseName(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `Adv_LocCurseShortDesc(string)`

```csharp
public static string Adv_LocCurseShortDesc(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `Adv_LocUI(string)`

```csharp
public static string Adv_LocUI(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `string`

:::

::: details `Adv_Number(float, string)`

```csharp
public static string Adv_Number(float value, string format = "#,##0")
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `value` | `float` |  |
| `format` | `string` |  |

**Returns:** `string`

:::

::: details `ConvertAdvToText(string)`

```csharp
public static string ConvertAdvToText(string adv)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `adv` | `string` |  |

**Returns:** `string`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (6)

*Classes and systems that invoke, reference, or depend on `DewAdvText`:*

[ChatManager](/api/Global.ChatManager) · `DewConsoleCommands` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_TheConsortOfNight` · `UI_Common_ChatBox_Item` · `UI_InGame_FloatingWindow_SeedOfTorment_Item`

### Dependencies (5)

*Types and components that `DewAdvText` references or depends upon:*

[ChatManager](/api/Global.ChatManager) · [Cost](/api/Global.Cost) · [DewLocalization](/api/Global.DewLocalization) · [DewPlayer](/api/Global.DewPlayer) · [DewSafety](/api/Global.DewSafety)

:::
