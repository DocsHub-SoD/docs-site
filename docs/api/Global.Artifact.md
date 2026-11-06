# Class: Artifact

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DewResourceLink]`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor)

```csharp
[DewResourceLink(ResourceLinkBy.Type)]
public class Artifact : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, ICustomInteractable
```

## Fields (3)

::: details Click to expand Fields (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`icon`** | `public Sprite icon` |  |
| **`mainColor`** | `[ColorUsage] [ColorUsage(false)] public Color mainColor` |  |
| **`touchSound`** | `public DewAudioClip touchSound` |  |

:::

## Properties (11)

::: details Click to expand Properties (11)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`altInteractProgress`** | `public float? altInteractProgress { get; }` |  |
| **`canAltInteract`** | `public bool canAltInteract { get; }` |  |
| **`canInteractWithMouse`** | `public bool canInteractWithMouse { get; }` |  |
| **`cost`** | `public Cost cost { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`grantedStardust`** | `public int grantedStardust { get; }` |  |
| **`interactActionRawText`** | `public string interactActionRawText { get; }` |  |
| **`interactAltActionRawText`** | `public string interactAltActionRawText { get; }` |  |
| **`interactPivot`** | `public Transform interactPivot { get; }` |  |
| **`nameRawText`** | `public string nameRawText { get; }` |  |
| **`priority`** | `public int priority { get; }` |  |

:::

## Methods (4)

::: details `CanInteract(Entity)`

```csharp
public bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

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

::: details `OnInteract(Entity, bool)`

```csharp
public void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (22)

*Classes and systems that invoke, reference, or depend on `Artifact`:*

[ArtifactWorldModel](/api/Global.ArtifactWorldModel) · `Artifact_AStoryWorthKeeping` · `Artifact_ATaleOfTheChamber` · `Artifact_AnOldGratitude` · `Artifact_BouquetOfEyes` · `Artifact_EmblemOfSubjugation` · `Artifact_FirstMerchantsToken` · `Artifact_FoolsGold` · `Artifact_ForestHoundSeed` · `Artifact_MomentOfDistantMonologue` · `Artifact_NightmareCatalyst` · `Artifact_RememberanceOfTheFirstJonas` · `Artifact_StarBlossom` · `Artifact_TheLittleStarSanctuary` · `Artifact_TheStarlitStone` · `Artifact_ThoseWhoMayEnter` · `Artifact_TomeOfTheSeeker` · `Artifact_VoidWhisperer` · `Artifact_WatchersNote` · `Artifact_WeddingRing` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `UI_TooltipManager`

### Dependencies (14)

*Types and components that `Artifact` references or depends upon:*

[Actor](/api/Global.Actor) · [ArtifactWorldModel](/api/Global.ArtifactWorldModel) · [Cost](/api/Global.Cost) · [DewAudioClip](/api/Global.DewAudioClip) · [DewLocalization](/api/Global.DewLocalization) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [Entity](/api/Global.Entity) · [ICustomInteractable](/api/Global.ICustomInteractable) · [IExcludeFromPool](/api/Global.IExcludeFromPool) · [IInteractable](/api/Global.IInteractable) · [InGameUIManager](/api/Global.InGameUIManager) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [QuestManager](/api/Global.QuestManager) · [ZoneManager](/api/Global.ZoneManager)

:::
