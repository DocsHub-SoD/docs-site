# Class: DewAllHeroesPresentZone

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
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
