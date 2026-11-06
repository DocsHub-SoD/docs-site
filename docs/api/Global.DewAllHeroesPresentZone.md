# Class: DewAllHeroesPresentZone

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
[RequireComponent(typeof(DewCollider))]
public class DewAllHeroesPresentZone : DewNetworkBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`onActivate`** | `public UnityEvent onActivate` |  |
| **`once`** | `public bool once` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentMembers`** | `public IReadOnlyList<Hero> currentMembers { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```
