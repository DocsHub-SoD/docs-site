# Class: InGameReverieManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [InGameReverieManager](/api/Global.InGameReverieManager)

```csharp
public class InGameReverieManager : ManagerBase<InGameReverieManager>, ILogicUpdate
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableTrackingReveries`** | `public bool disableTrackingReveries` |  |
| **`RerollMaxCount`** | `public const int RerollMaxCount = 3` |  |
| **`SpecialReverieIndex`** | `public const int SpecialReverieIndex = -99` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isTrackingReveries`** | `public bool isTrackingReveries { get; }` |  |

:::

## Methods (1)

::: details `CompleteReverie(DewReverieItem)`

```csharp
public void CompleteReverie(DewReverieItem item)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `item` | [`DewReverieItem`](/api/Global.DewReverieItem) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `InGameReverieManager`:*

[DewReverieItem](/api/Global.DewReverieItem)

### Dependencies (12)

*Types and components that `InGameReverieManager` references or depends upon:*

[Dew](/api/Global.Dew) · [DewGameObserverWithProgress](/api/Global.DewGameObserverWithProgress) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistentGameObserver](/api/Global.DewPersistentGameObserver) · [DewPlayer](/api/Global.DewPlayer) · [DewReverieItem](/api/Global.DewReverieItem) · [DewSave](/api/Global.DewSave) · [GameManager](/api/Global.GameManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1)

:::
