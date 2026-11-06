# Class: CurseStatusEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[SaveActor]`
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
| **`dontRemoveOnKnockOut`** | `[SyncVar] [SaveVar] [NonSerialized] [SaveVar(SaveVarFlags.Default)] public bool dontRemoveOnKnockOut` |  |
| **`quest`** | `[SyncVar] [SaveVar] [NonSerialized] [SaveVar(SaveVarFlags.Default)] public Quest_KillToLiftCurse quest` |  |

:::

## Properties (6)

::: details Click to expand Properties (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentProgress`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int currentProgress { get; set; }` |  |
| **`currentStrength`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public HatredStrengthType currentStrength { get; set; }` |  |
| **`disableEndNotification`** | `public bool disableEndNotification { get; set; }` |  |
| **`disableStartNotification`** | `public bool disableStartNotification { get; set; }` |  |
| **`progressType`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public QuestProgressType progressType { get; set; }` |  |
| **`requiredAmount`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int requiredAmount { get; set; }` |  |

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (31)

*Classes and systems that invoke, reference, or depend on `CurseStatusEffect`:*

`ACH_EMBRACE_MORTALITY` · `ACH_EMPRESS_OF_PAIN` · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `NodeListExtensions` · `Quest_KillToLiftCurse` · `Se_Curse_AmplifiedPain` · `Se_Curse_AnchorOfMind` · `Se_Curse_BlissOfIgnorance` · `Se_Curse_BrainFog` · `Se_Curse_DarkUrge` · `Se_Curse_DreamAfflictionDissociative` · `Se_Curse_DreamAfflictionHallucinatory` · `Se_Curse_DreamAfflictionInductive` · `Se_Curse_DreamAfflictionParalytic` · `Se_Curse_Electrified` · `Se_Curse_EternalLoop` · `Se_Curse_FaintMemory` · `Se_Curse_FateOfGreed` · `Se_Curse_Fragility` · `Se_Curse_FragmentedBeing` · `Se_Curse_GuidingCompass_CripplingAnxiety` · `Se_Curse_IntermittentExplosion` · `Se_Curse_Lethargy` · `Se_Curse_LossOfIdentity` · `Se_Curse_SilentNight` · `Se_Curse_SoftSkin` · `Se_Curse_Somnambulism` · `Se_Curse_UnstableEnergy` · `Se_Curse_VainDream` · `UI_InGame_CurseNotifications`

### Dependencies (23)

*Types and components that `CurseStatusEffect` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [ActorCheck](/api/Global.ActorCheck) · `ArrayGetClampedExtensions` · [ChatManager](/api/Global.ChatManager) · [DewLocalization](/api/Global.DewLocalization) · [DewQuest](/api/Global.DewQuest) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [EventInfoKill](/api/Global.EventInfoKill) · [EventInfoLoadRoom](/api/Global.EventInfoLoadRoom) · [EventInfoLoadZone](/api/Global.EventInfoLoadZone) · `HatredStrengthTypeExtensions` · [InGameUIManager](/api/Global.InGameUIManager) · [KillTracker](/api/Global.KillTracker) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [QuestManager](/api/Global.QuestManager) · `Quest_KillToLiftCurse` · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [StatusEffect](/api/Global.StatusEffect) · [ZoneManager](/api/Global.ZoneManager) · `Mirror.GeneratedNetworkCode`

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`HatredStrengthType`](/enums#hatredstrengthtype) · [`QuestProgressType`](/enums#questprogresstype) · [`SaveVarFlags`](/enums#savevarflags)

:::
