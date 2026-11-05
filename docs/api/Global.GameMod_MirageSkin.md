# Class: GameMod_MirageSkin

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [GameEffect](/api/Global.GameEffect) → [GameModifierBase](/api/Global.GameModifierBase)

```csharp
public class GameMod_MirageSkin : GameModifierBase, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`baseChancesByPlayerCount`** | `public GameMod_MirageSkin.MirageSkinChancePerPlayer[] baseChancesByPlayerCount` |  |
| **`currentZonePool`** | `[NonSerialized]
[SaveVar(SaveVarFlags.Default)]
public List&lt;AssetRef&lt;MirageSkinEffect&gt;&gt; currentZonePool` |  |
| **`softInstance`** | `public static GameMod_MirageSkin softInstance` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static GameMod_MirageSkin instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |

## Methods

### `GetCurrentBaseMirageChance()`

```csharp
public float GetCurrentBaseMirageChance()
```

**Returns:** `float`

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `RefreshPool()`

```csharp
public void RefreshPool()
```
