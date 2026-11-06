# Class: EntityAbility

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityAbility : EntityComponent, ILogicUpdate, ICleanup
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityPreset`** | `public AssetRef<AbilityTrigger>[] abilityPreset` |  |
| **`AttackAbilityIndex`** | `public const int AttackAbilityIndex = 63` |  |
| **`attackAbilityPreset`** | `public AssetRef<AttackTrigger> attackAbilityPreset` |  |
| **`ClientEvent_OnAbilityAdded`** | `public SafeAction<int, AbilityTrigger> ClientEvent_OnAbilityAdded` |  |
| **`ClientEvent_OnAbilityRemoved`** | `public SafeAction<int, AbilityTrigger> ClientEvent_OnAbilityRemoved` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilities`** | `public IReadOnlyDictionary<int, AbilityTrigger> abilities { get; }` |  |
| **`attackAbility`** | `public AbilityTrigger attackAbility { get; }` |  |
| **`originalAttackAbility`** | `public AttackTrigger originalAttackAbility { get; }` |  |
| **`overridenAttackAbility`** | `public AbilityTrigger overridenAttackAbility { get; }` |  |

:::

## Methods (17)

::: details `AddAbility(AbilityTrigger)`

Add an ability to this entity. It will be equipped on empty index between 0 and 127.

```csharp
public void AddAbility(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

:::

::: details `AddAbility&lt;T&gt;()`

Add an ability to this entity. It will be equipped on empty index between 0 and 127.

```csharp
public T AddAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `GetAbility&lt;T&gt;()`

Get this entity's first ability of the given type. Can be null.

```csharp
public T GetAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetNewAbilityLockHandle(bool)`

```csharp
public AbilityLockHandle GetNewAbilityLockHandle(bool shouldShowLockIcon = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `shouldShowLockIcon` | `bool` |  |

**Returns:** `AbilityLockHandle`

:::

::: details `IsAbilityCastLocked(int)`

Is an ability locked by AbilityLockHandle? Available everywhere.

```csharp
public bool IsAbilityCastLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `IsAbilityEditLocked(int)`

```csharp
public bool IsAbilityEditLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `IsAttackAbilityLocked(int)`

```csharp
public bool IsAttackAbilityLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `OnStartClient()`

```csharp
public override void OnStartClient()
```

:::

::: details `OnStartServer()`

```csharp
public override void OnStartServer()
```

:::

::: details `RemoveAbility(int)`

```csharp
public AbilityTrigger RemoveAbility(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityTrigger`

:::

::: details `RemoveAttackAbility()`

Remove previous attack ability from this entity.

```csharp
public AbilityTrigger RemoveAttackAbility()
```

**Returns:** `AbilityTrigger`

:::

::: details `SetAbility(int, AbilityTrigger)`

Give this entity a new ability at the given index. Previously equipped ability will be unequipped.

```csharp
public void SetAbility(int index, AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

:::

::: details `SetAttackAbility(AttackTrigger)`

Give a new attack ability to this entity. Previous one will be unequipped.

```csharp
public void SetAttackAbility(AttackTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AttackTrigger`](/api/Global.AttackTrigger) |  |

:::

::: details `ShouldShowAbilityLockIcon(int)`

```csharp
public bool ShouldShowAbilityLockIcon(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

:::

::: details `TryGetAbility&lt;T&gt;(out T)`

```csharp
public bool TryGetAbility<T>(out T trigger) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::
