# Class: PropEntity

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Entity](/api/Global.Entity) → [PropEnt_Merchant_Backpack](/api/Global.PropEnt_Merchant_Backpack) → [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) → [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) → [PropEnt_Stone_Gold](/api/Global.PropEnt_Stone_Gold) → [PropEnt_Stone_Nightmare](/api/Global.PropEnt_Stone_Nightmare)

```csharp
public class PropEntity : Entity, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IProp
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`hitInvulnerableTime`** | `[ShowIf("takeOneDamageOnHit", true)]
public float hitInvulnerableTime` |  |
| **`isUnstoppable`** | `public bool isUnstoppable` |  |
| **`takeOneDamageOnHit`** | `public bool takeOneDamageOnHit` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isRegularReward`** | `public virtual bool isRegularReward { get; }` |  |
| **`scaleSpawnRateWithPlayers`** | `public bool scaleSpawnRateWithPlayers { get; }` |  |

## Methods

### `GetStaggerSettings()`

```csharp
protected override Entity.StaggerSettings GetStaggerSettings()
```

**Returns:** `Entity.StaggerSettings`

### `OnCreate()`

```csharp
protected override void OnCreate()
```
