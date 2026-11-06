# Class: SafeAction&lt;T1, T2, T3&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class SafeAction<T1, T2, T3>
```

## Methods (4)

::: details `Add(Action&lt;T1, T2, T3&gt;)`

```csharp
public SafeAction<T1, T2, T3> Add(Action<T1, T2, T3> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2, T3>` |  |

**Returns:** `SafeAction<T1, T2, T3>`

:::

::: details `Contains(Action&lt;T1, T2, T3&gt;)`

```csharp
public bool Contains(Action<T1, T2, T3> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2, T3>` |  |

**Returns:** `bool`

:::

::: details `Invoke(T1, T2, T3)`

```csharp
public void Invoke(T1 a, T2 b, T3 c)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `a` | `T1` |  |
| `b` | `T2` |  |
| `c` | `T3` |  |

:::

::: details `Remove(Action&lt;T1, T2, T3&gt;)`

```csharp
public SafeAction<T1, T2, T3> Remove(Action<T1, T2, T3> handler)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handler` | `System.Action<T1, T2, T3>` |  |

**Returns:** `SafeAction<T1, T2, T3>`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (7)

*Classes and systems that invoke, reference, or depend on `SafeAction<T1, T2, T3>`:*

[ClientEventManager](/api/Global.ClientEventManager) · [DewPlayer](/api/Global.DewPlayer) · [Gem](/api/Global.Gem) · [HeroSkill](/api/Global.HeroSkill) · [QuestManager](/api/Global.QuestManager) · [SkillTrigger](/api/Global.SkillTrigger) · `UI_InGame_CurrentArtifact`

### Dependencies (3)

*Types and components that `SafeAction<T1, T2, T3>` references or depends upon:*

[DewPool](/api/Global.DewPool) · `IPoolClearable` · [ListReturnHandle`1](/api/Global.ListReturnHandle`1)

:::
