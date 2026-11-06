# Class: DataProcessorGroup&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DataProcessorGroup<T> where T : struct
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`count`** | `public int count { get; }` |  |

:::

## Methods (4)

::: details `Add(DataProcessor&lt;T&gt;, int)`

Processors with lower priority value will be executed first.

```csharp
public void Add(DataProcessor<T> processor, int priority = 0)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<T>` |  |
| `priority` | `int` |  |

:::

::: details `Clear()`

```csharp
public void Clear()
```

:::

::: details `Process(ref T)`

```csharp
public void Process(ref T data)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | `T` |  |

:::

::: details `Remove(DataProcessor&lt;T&gt;)`

```csharp
public void Remove(DataProcessor<T> processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `processor` | `DataProcessor<T>` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (7)

*Classes and systems that invoke, reference, or depend on `DataProcessorGroup<T>`:*

[EntityStatus](/api/Global.EntityStatus) · `Gem_L_Supersymmetry` · `Se_D_TheKillingFlow` · `Se_R_AnnihilationStance` · `Se_Star_Cetus_D_AdApUpByBonusHp` · `Se_Star_Vesper_D_ConvertAPToAD` · `Se_Star_Yubar_D_ConvertADToAP`

### Dependencies (2)

*Types and components that `DataProcessorGroup<T>` references or depends upon:*

[DataProcessor`1](/api/Global.DataProcessor`1) · `IPoolClearable`

:::
