# Class: EntityAbility

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
public class EntityAbility : EntityComponent, ILogicUpdate, ICleanup
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilityPreset`** | `public AssetRef<AbilityTrigger>[] abilityPreset` |  |
| **`AttackAbilityIndex`** | `public const int AttackAbilityIndex = 63` |  |
| **`attackAbilityPreset`** | `public AssetRef<AttackTrigger> attackAbilityPreset` |  |
| **`ClientEvent_OnAbilityAdded`** | `public SafeAction<int, AbilityTrigger> ClientEvent_OnAbilityAdded` |  |
| **`ClientEvent_OnAbilityRemoved`** | `public SafeAction<int, AbilityTrigger> ClientEvent_OnAbilityRemoved` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abilities`** | `public IReadOnlyDictionary<int, AbilityTrigger> abilities { get; }` |  |
| **`attackAbility`** | `public AbilityTrigger attackAbility { get; }` |  |
| **`originalAttackAbility`** | `public AttackTrigger originalAttackAbility { get; }` |  |
| **`overridenAttackAbility`** | `public AbilityTrigger overridenAttackAbility { get; }` |  |

## Methods

### `AddAbility(AbilityTrigger)`

Add an ability to this entity. It will be equipped on empty index between 0 and 127.

```csharp
public void AddAbility(AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

### `AddAbility<T>()`

Add an ability to this entity. It will be equipped on empty index between 0 and 127.

```csharp
public T AddAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

### `Awake()`

```csharp
protected override void Awake()
```

### `GetAbility<T>()`

Get this entity's first ability of the given type. Can be null.

```csharp
public T GetAbility<T>() where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `` | `T` |  |

**Returns:** `T`

### `GetNewAbilityLockHandle(bool)`

```csharp
public AbilityLockHandle GetNewAbilityLockHandle(bool shouldShowLockIcon = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `shouldShowLockIcon` | `bool` |  |

**Returns:** `AbilityLockHandle`

### `IsAbilityCastLocked(int)`

Is an ability locked by AbilityLockHandle? Available everywhere.

```csharp
public bool IsAbilityCastLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

### `IsAbilityEditLocked(int)`

```csharp
public bool IsAbilityEditLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

### `IsAttackAbilityLocked(int)`

```csharp
public bool IsAttackAbilityLocked(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `RemoveAbility(int)`

```csharp
public AbilityTrigger RemoveAbility(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `AbilityTrigger`

### `RemoveAttackAbility()`

Remove previous attack ability from this entity.

```csharp
public AbilityTrigger RemoveAttackAbility()
```

**Returns:** `AbilityTrigger`

### `SetAbility(int, AbilityTrigger)`

Give this entity a new ability at the given index. Previously equipped ability will be unequipped.

```csharp
public void SetAbility(int index, AbilityTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `trigger` | [`AbilityTrigger`](/api/Global.AbilityTrigger) |  |

### `SetAttackAbility(AttackTrigger)`

Give a new attack ability to this entity. Previous one will be unequipped.

```csharp
public void SetAttackAbility(AttackTrigger trigger)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | [`AttackTrigger`](/api/Global.AttackTrigger) |  |

### `ShouldShowAbilityLockIcon(int)`

```csharp
public bool ShouldShowAbilityLockIcon(int index)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |

**Returns:** `bool`

### `TryGetAbility<T>(out T)`

```csharp
public bool TryGetAbility<T>(out T trigger) where T : AbilityTrigger
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `trigger` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`
