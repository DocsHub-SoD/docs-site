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
| **`currentZonePool`** | `[NonSerialized] [SaveVar(SaveVarFlags.Default)] public List<AssetRef<MirageSkinEffect>> currentZonePool` |  |
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
