# Class: CurseStatusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [AbilityInstance](/api/Global.AbilityInstance) → [StatusEffect](/api/Global.StatusEffect)

```csharp
[SaveActor(true)]
public class CurseStatusEffect : StatusEffect, ILogicUpdate, ICleanup, ICustomDestroyRoutine
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableStrengths`** | `[BoxGroup("Curse Settings", true, false, 0)] public HatredStrengthType availableStrengths` |  |
| **`chanceWeight`** | `[BoxGroup("Curse Settings", true, false, 0)] public float chanceWeight` |  |
| **`CurseEvent_OnProgressChanged`** | `public Action CurseEvent_OnProgressChanged` | Called on server. |
| **`dontRemoveOnKnockOut`** | `[NonSerialized] [SaveVar(SaveVarFlags.Default)] public bool dontRemoveOnKnockOut` |  |
| **`quest`** | `[NonSerialized] [SaveVar(SaveVarFlags.Default)] public Quest_KillToLiftCurse quest` |  |

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentProgress`** | `[SaveVar(SaveVarFlags.Default)] public int currentProgress { get; set; }` |  |
| **`currentStrength`** | `[SaveVar(SaveVarFlags.Default)] public HatredStrengthType currentStrength { get; set; }` |  |
| **`disableEndNotification`** | `public bool disableEndNotification { get; set; }` |  |
| **`disableStartNotification`** | `public bool disableStartNotification { get; set; }` |  |
| **`progressType`** | `[SaveVar(SaveVarFlags.Default)] public QuestProgressType progressType { get; set; }` |  |
| **`requiredAmount`** | `[SaveVar(SaveVarFlags.Default)] public int requiredAmount { get; set; }` |  |

:::

## Methods (6)

::: details `GetName()`

```csharp
public string GetName()
```

**Returns:** `string`

:::

::: details `GetValue&lt;T&gt;(T[])`

```csharp
public T GetValue<T>(T[] arr)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `arr` | `T[]` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `IsViable(Entity)`

Is this curse viable on this entity? Checked on server, on prefab CurseStatusEffect.If this returns false, this curse will not be chosen.

```csharp
public virtual bool IsViable(Entity target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

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

::: details `OnPrepare()`

```csharp
protected override void OnPrepare()
```

:::
