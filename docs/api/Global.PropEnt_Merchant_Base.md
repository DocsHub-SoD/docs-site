# Class: PropEnt_Merchant_Base

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEntity](/api/Global.PropEntity) → [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) → [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie)

```csharp
public abstract class PropEnt_Merchant_Base : PropEntity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp, IInteractable
```

## Fields (11)

::: details Click to expand Fields (11)

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
| **`merchandises`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public readonly SyncDictionary<string, MerchandiseData[]> merchandises` |  |
| **`onMerchandisePopulated`** | `public SafeAction<DewPlayer> onMerchandisePopulated` | Called on server after merchandise has been populated for certain player. |
| **`props`** | `public GameObject[] props` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public virtual bool canInteractWithMouse { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`interactPivot`** | `public virtual Transform interactPivot { get; }` |  |

:::

## Methods (16)

::: details `ActiveLogicUpdate(float)`

```csharp
protected override void ActiveLogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

:::

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CanInteract(Entity)`

```csharp
public virtual bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `CanRefresh(DewPlayer)`

Checked everywhere.

```csharp
public virtual bool CanRefresh(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `bool`

:::

::: details `CmdPurchase(int, NetworkConnectionToClient)`

```csharp
public void CmdPurchase(int index, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `index` | `int` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `CmdRefresh(NetworkConnectionToClient)`

```csharp
public void CmdRefresh(NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `CmdSell(NetworkBehaviour, NetworkConnectionToClient)`

```csharp
public void CmdSell(NetworkBehaviour target, NetworkConnectionToClient sender = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | `Mirror.NetworkBehaviour` |  |
| `sender` | `Mirror.NetworkConnectionToClient` |  |

:::

::: details `GetRefreshCost(DewPlayer)`

Available everywhere.

```csharp
public virtual Cost GetRefreshCost(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `Cost`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `OnInteract(Entity, bool)`

```csharp
public virtual void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

:::

::: details `OnPopulateMerchandises(DewPlayer)`

```csharp
protected abstract void OnPopulateMerchandises(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `OnRefresh(DewPlayer)`

```csharp
protected virtual void OnRefresh(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `OnSell(DewPlayer, NetworkBehaviour)`

```csharp
protected void OnSell(DewPlayer activator, NetworkBehaviour target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activator` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `target` | `Mirror.NetworkBehaviour` |  |

:::

::: details `PopulatePlayerMerchandises(DewPlayer)`

```csharp
public void PopulatePlayerMerchandises(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `SpawnMerchandise(MerchandiseData, DewPlayer, Cost)`

```csharp
protected void SpawnMerchandise(MerchandiseData data, DewPlayer player, Cost finalPrice)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `data` | [`MerchandiseData`](/api/Global.MerchandiseData) |  |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |
| `finalPrice` | [`Cost`](/api/Global.Cost) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `PropEnt_Merchant_Base`:*

[EditSkillManager](/api/Global.EditSkillManager) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · [Treasure](/api/Global.Treasure) · `UI_InGame_FloatingWindow_Shop`

### Dependencies (29)

*Types and components that `PropEnt_Merchant_Base` references or depends upon:*

[Actor](/api/Global.Actor) · [ClientEventManager](/api/Global.ClientEventManager) · [Cost](/api/Global.Cost) · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [DewResources](/api/Global.DewResources) · [EditSkillManager](/api/Global.EditSkillManager) · [Entity](/api/Global.Entity) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoLoadRoom](/api/Global.EventInfoLoadRoom) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [GameManager](/api/Global.GameManager) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · [HeroSkill](/api/Global.HeroSkill) · [IInteractable](/api/Global.IInteractable) · [IProp](/api/Global.IProp) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MerchandiseData](/api/Global.MerchandiseData) · `NetworkConnectionToClientExtension` · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [PropEntity](/api/Global.PropEntity) · [SafeAction`1](/api/Global.SafeAction`1) · `SetLayerRecursiveExtensions` · [SkillTrigger](/api/Global.SkillTrigger) · [Treasure](/api/Global.Treasure) · `Vector3FlattenExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`SaveVarFlags`](/enums#savevarflags)

:::
