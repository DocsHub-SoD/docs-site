# Class: GameMod_MirageSkin

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect) → [GameModifierBase](/api/Global.GameModifierBase)

```csharp
public class GameMod_MirageSkin : GameModifierBase, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseChancesByPlayerCount`** | `public GameMod_MirageSkin.MirageSkinChancePerPlayer[] baseChancesByPlayerCount` |  |
| **`currentZonePool`** | `[SaveVar] [NonSerialized] [SaveVar(SaveVarFlags.Default)] public List<AssetRef<MirageSkinEffect>> currentZonePool` |  |
| **`softInstance`** | `public static GameMod_MirageSkin softInstance` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static GameMod_MirageSkin instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |

:::

## Methods (4)

::: details `GetCurrentBaseMirageChance()`

```csharp
public float GetCurrentBaseMirageChance()
```

**Returns:** `float`

:::

::: details `OnCreate()`

```csharp
protected override void OnCreate()
```

:::

::: details `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

:::

::: details `RefreshPool()`

```csharp
public void RefreshPool()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (4)

*Classes and systems that invoke, reference, or depend on `GameMod_MirageSkin`:*

`RoomMod_FallenStar` · `RoomMod_HarderFightBetterReward` · `RoomMod_Hunted` · [RoomMonsters](/api/Global.RoomMonsters)

### Dependencies (18)

*Types and components that `GameMod_MirageSkin` references or depends upon:*

[Actor](/api/Global.Actor) · `ArrayGetClampedExtensions` · [AssetRef`1](/api/Global.AssetRef`1) · [Dew](/api/Global.Dew) · [DewRandom](/api/Global.DewRandom) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EntityStatus](/api/Global.EntityStatus) · [EventInfoLoadRoom](/api/Global.EventInfoLoadRoom) · [EventInfoLoadZone](/api/Global.EventInfoLoadZone) · [GameEffect](/api/Global.GameEffect) · [GameModifierBase](/api/Global.GameModifierBase) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [Room](/api/Global.Room) · [SafeAction`1](/api/Global.SafeAction`1) · [SingletonDewNetworkBehaviour`1](/api/Global.SingletonDewNetworkBehaviour`1) · [ZoneManager](/api/Global.ZoneManager)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#savevarflags" class="enum-link" data-tooltip="Default=0 · ApplyAfterCreation=1 · ApplyAfterFrameDelay=2">SaveVarFlags</a>

:::
