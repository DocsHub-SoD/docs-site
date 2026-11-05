# Class: PropEnt_Merchant_Base

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity) → [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) → [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie)

```csharp
public abstract class PropEnt_Merchant_Base : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp, IInteractable
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowRefresh`** | `public bool allowRefresh` |  |
| **`fxPurchase`** | `public GameObject fxPurchase` |  |
| **`fxPurchaseGem`** | `public GameObject fxPurchaseGem` |  |
| **`fxPurchaseSkill`** | `public GameObject fxPurchaseSkill` |  |
| **`fxPurchaseSouvenir`** | `public GameObject fxPurchaseSouvenir` |  |
| **`fxPurchaseTreasure`** | `public GameObject fxPurchaseTreasure` |  |
| **`fxSell`** | `public GameObject fxSell` |  |
| **`isSellEnabled`** | `public bool isSellEnabled` |  |
| **`merchandises`** | `[SaveVar(SaveVarFlags.Default)]
public readonly SyncDictionary&lt;string, MerchandiseData[]&gt; merchandises` |  |
| **`onMerchandisePopulated`** | `public SafeAction&lt;DewPlayer&gt; onMerchandisePopulated` | Called on server after merchandise has been populated for certain player. |
| **`props`** | `public GameObject[] props` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public virtual bool canInteractWithMouse { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`interactPivot`** | `public virtual Transform interactPivot { get; }` |  |

## Methods

### `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `CanInteract(Entity)`

```csharp
public virtual bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [Entity](/api/Global.Entity) |  |

**Returns:** `bool`

### `CanRefresh(DewPlayer)`

Checked everywhere.

```csharp
public virtual bool CanRefresh(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

**Returns:** `bool`

### `CmdPurchase(int, NetworkConnectionToClient)`

```csharp
public void CmdPurchase(int index, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `CmdRefresh(NetworkConnectionToClient)`

```csharp
public void CmdRefresh(NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `CmdSell(NetworkBehaviour, NetworkConnectionToClient)`

```csharp
public void CmdSell(NetworkBehaviour target, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkBehaviour` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

### `GetRefreshCost(DewPlayer)`

Available everywhere.

```csharp
public virtual Cost GetRefreshCost(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

**Returns:** `Cost`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnInteract(Entity, bool)`

```csharp
public virtual void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [Entity](/api/Global.Entity) |  |
| `alt` | `bool` |  |

### `OnPopulateMerchandises(DewPlayer)`

```csharp
protected abstract void OnPopulateMerchandises(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

### `OnRefresh(DewPlayer)`

```csharp
protected virtual void OnRefresh(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

### `OnSell(DewPlayer, NetworkBehaviour)`

```csharp
protected void OnSell(DewPlayer activator, NetworkBehaviour target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activator` | [DewPlayer](/api/Global.DewPlayer) |  |
| `target` | `Mirror.NetworkBehaviour` |  |

### `PopulatePlayerMerchandises(DewPlayer)`

```csharp
public void PopulatePlayerMerchandises(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |

### `SpawnMerchandise(MerchandiseData, DewPlayer, Cost)`

```csharp
protected void SpawnMerchandise(MerchandiseData data, DewPlayer player, Cost finalPrice)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [MerchandiseData](/api/Global.MerchandiseData) |  |
| `player` | [DewPlayer](/api/Global.DewPlayer) |  |
| `finalPrice` | [Cost](/api/Global.Cost) |  |
