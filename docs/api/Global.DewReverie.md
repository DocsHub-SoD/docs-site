# Class: DewReverie

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewReverie
```

## Methods (9)

::: details `CheckSpecialReveries()`

```csharp
public static void CheckSpecialReveries()
```

:::

::: details `ClearDailyReverie(int)`

```csharp
public static void ClearDailyReverie(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

:::

::: details `ClearSpecialReverie()`

```csharp
public static void ClearSpecialReverie()
```

:::

::: details `ReceiveRewardOfReverie(ReverieDataBase)`

Receive the reward of a specific reverie. This does not remove the reverie.If succeeds, returns true.On error, this returns false and prints out error message to the user.

```csharp
public static UniTask<bool> ReceiveRewardOfReverie(DewProfile.ReverieDataBase data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewProfile.ReverieDataBase`](/api/Global.DewProfile) |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask<T><bool>`

:::

::: details `SetDailyReverie(int, Type)`

```csharp
public static void SetDailyReverie(int index, Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `type` | `System.Type` |  |

:::

::: details `SetDailyReverie&lt;T&gt;(int)`

```csharp
public static void SetDailyReverie<T>(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `` | `T` |  |

:::

::: details `SetRandomDailyReverie(int)`

```csharp
public static void SetRandomDailyReverie(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

:::

::: details `SetSpecialReverie(Type, DateTime)`

```csharp
public static void SetSpecialReverie(Type type, DateTime endDate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `endDate` | `System.DateTime` |  |

:::

::: details `StartNextSpecialReverieOrClear()`

```csharp
public static void StartNextSpecialReverieOrClear()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `DewReverie`:*

`UI_Reveries` · `UI_Reveries_DailySlot` · `UI_Reveries_SpecialSlot`

### Dependencies (5)

*Types and components that `DewReverie` references or depends upon:*

`DateTimeExtensions` · [Dew](/api/Global.Dew) · [DewReverieItem](/api/Global.DewReverieItem) · [DewSave](/api/Global.DewSave) · [DewSpecialReverieItem](/api/Global.DewSpecialReverieItem)

:::
