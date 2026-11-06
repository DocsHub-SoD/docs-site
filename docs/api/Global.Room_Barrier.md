# Class: Room_Barrier

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour)

```csharp
public class Room_Barrier : DewNetworkBehaviour, ILogicUpdate
```

## Fields (4)

::: details Click to expand Fields (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canPassThroughOneWay`** | `public bool canPassThroughOneWay` |  |
| **`closedEffect`** | `public GameObject closedEffect` |  |
| **`openEffect`** | `public GameObject openEffect` |  |
| **`passThroughCollider`** | `[ShowIf("canPassThroughOneWay", true)] public DewCollider passThroughCollider` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isOpen`** | `public bool isOpen { get; }` |  |

:::

## Methods (8)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `Close()`

```csharp
public void Close()
```

:::

::: details `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

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

::: details `OnStopServer()`

```csharp
public override void OnStopServer()
```

:::

::: details `Open()`

```csharp
public void Open()
```

:::

::: details `Toggle()`

```csharp
public void Toggle()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `Room_Barrier`:*

`DarkCave_RandomOpenBarrier` · `PlayTutorial_Tutorial_Intro` · `PlayTutorial_Tutorial_SkillsAndEssences` · `SnowMountain_OpenSecretPlace` · `SpawnGemStarProp`

### Dependencies (12)

*Types and components that `Room_Barrier` references or depends upon:*

[Actor](/api/Global.Actor) · [DewCollider](/api/Global.DewCollider) · [DewGizmos](/api/Global.DewGizmos) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Room](/api/Global.Room) · [SafeAction](/api/Global.SafeAction) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [ZoneManager](/api/Global.ZoneManager)

:::
