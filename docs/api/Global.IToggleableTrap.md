# Interface: IToggleableTrap

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IToggleableTrap : IBanRoomNodesNearby, IBanCampsNearby
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isOn`** | `bool isOn { get; }` |  |

:::

## Methods (2)

::: details `StartTrap()`

```csharp
void StartTrap()
```

:::

::: details `StopTrap()`

```csharp
void StopTrap()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `IToggleableTrap`:*

[Room_Trap_Toggleable](/api/Global.Room_Trap_Toggleable)

### Dependencies (2)

*Types and components that `IToggleableTrap` references or depends upon:*

[IBanCampsNearby](/api/Global.IBanCampsNearby) · [IBanRoomNodesNearby](/api/Global.IBanRoomNodesNearby)

:::
