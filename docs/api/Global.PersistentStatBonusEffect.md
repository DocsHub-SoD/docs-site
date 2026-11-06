# Class: PersistentStatBonusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[SaveActor(true)]
public class PersistentStatBonusEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bonus`** | `[SaveVar(SaveVarFlags.Default)] public StatBonus bonus` |  |

## Methods

### `OnCreate()`

```csharp
protected override void OnCreate()
```
