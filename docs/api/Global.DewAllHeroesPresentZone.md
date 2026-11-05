# Class: DewAllHeroesPresentZone

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
| **`currentMembers`** | `public IReadOnlyList&lt;Hero&gt; currentMembers { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```
