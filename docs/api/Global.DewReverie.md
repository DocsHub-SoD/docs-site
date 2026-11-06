# Class: DewReverie

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewReverie
```

## Methods

### `CheckSpecialReveries()`

```csharp
public static void CheckSpecialReveries()
```

### `ClearDailyReverie(int)`

```csharp
public static void ClearDailyReverie(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

### `ClearSpecialReverie()`

```csharp
public static void ClearSpecialReverie()
```

### `ReceiveRewardOfReverie(ReverieDataBase)`

Receive the reward of a specific reverie. This does not remove the reverie.If succeeds, returns true.On error, this returns false and prints out error message to the user.

```csharp
public static UniTask<bool> ReceiveRewardOfReverie(DewProfile.ReverieDataBase data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`DewProfile.ReverieDataBase`](/api/Global.DewProfile) |  |

**Returns:** `Cysharp.Threading.Tasks.UniTask<T><bool>`

### `SetDailyReverie(int, Type)`

```csharp
public static void SetDailyReverie(int index, Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `type` | `System.Type` |  |

### `SetDailyReverie<T>(int)`

```csharp
public static void SetDailyReverie<T>(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `` | `T` |  |

### `SetRandomDailyReverie(int)`

```csharp
public static void SetRandomDailyReverie(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

### `SetSpecialReverie(Type, DateTime)`

```csharp
public static void SetSpecialReverie(Type type, DateTime endDate)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `endDate` | `System.DateTime` |  |

### `StartNextSpecialReverieOrClear()`

```csharp
public static void StartNextSpecialReverieOrClear()
```
