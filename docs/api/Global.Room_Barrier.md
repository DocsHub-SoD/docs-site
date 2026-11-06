# Class: Room_Barrier

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
public class Room_Barrier : DewNetworkBehaviour, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canPassThroughOneWay`** | `public bool canPassThroughOneWay` |  |
| **`closedEffect`** | `public GameObject closedEffect` |  |
| **`openEffect`** | `public GameObject openEffect` |  |
| **`passThroughCollider`** | `[ShowIf("canPassThroughOneWay", true)] public DewCollider passThroughCollider` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isOpen`** | `public bool isOpen { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `Close()`

```csharp
public void Close()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `Open()`

```csharp
public void Open()
```

### `Toggle()`

```csharp
public void Toggle()
```
