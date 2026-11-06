# Class: DewAllHeroesPresentZone

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[RequireComponent]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
[RequireComponent(typeof(DewCollider))]
public class DewAllHeroesPresentZone : DewNetworkBehaviour, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onActivate`** | `public UnityEvent onActivate` |  |
| **`once`** | `public bool once` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentMembers`** | `public IReadOnlyList<Hero> currentMembers { get; }` |  |

:::

## Methods (1)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `DewAllHeroesPresentZone`:*

[DewBossRoomEntry](/api/Global.DewBossRoomEntry)

### Dependencies (7)

*Types and components that `DewAllHeroesPresentZone` references or depends upon:*

[Actor](/api/Global.Actor) · [DewCollider](/api/Global.DewCollider) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Hero](/api/Global.Hero) · [InGameUIManager](/api/Global.InGameUIManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · `VectorPlaneTransformExtension`

:::
