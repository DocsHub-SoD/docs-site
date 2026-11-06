# Class: Shrine

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [ChoiceShrine](/api/Global.ChoiceShrine) → [EditSkillShrine](/api/Global.EditSkillShrine)

```csharp
public abstract class Shrine : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IProp, IBanRoomNodesNearby
```

## Fields (16)

::: details Click to expand Fields (16)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`availableEffect`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject availableEffect` |  |
| **`baseGoldCost`** | `[BoxGroup("Shrine Settings", true, false, 0)] public int baseGoldCost` |  |
| **`ClientEvent_OnSuccessfulUse`** | `public SafeAction<Entity> ClientEvent_OnSuccessfulUse` | Called everywhere after an entity uses this shrine successfully. |
| **`interactableDelay`** | `[BoxGroup("Shrine Settings", true, false, 0)] public float interactableDelay` |  |
| **`lockedEffect`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject lockedEffect` |  |
| **`mapVisibility`** | `[BoxGroup("Shrine Settings", true, false, 0)] public MapItemVisibility mapVisibility` |  |
| **`maxTotalUseCount`** | `[SyncVar] [SaveVar] [FormerlySerializedAs] [SaveVar(SaveVarFlags.Default)] [FormerlySerializedAs("maxUseCount")] [BoxGroup("Shrine Settings", true, false, 0)] public int maxTotalUseCount` |  |
| **`maxUseCountPerPlayer`** | `[BoxGroup("Shrine Settings", true, false, 0)] public int maxUseCountPerPlayer` |  |
| **`model`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject model` |  |
| **`unavailableByDefault`** | `[ToggleLeft] [BoxGroup("Shrine Settings", true, false, 0)] public bool unavailableByDefault` |  |
| **`unavailableEffect`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject unavailableEffect` |  |
| **`unlockEffect`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject unlockEffect` |  |
| **`useCooldown`** | `[BoxGroup("Shrine Settings", true, false, 0)] public float useCooldown` |  |
| **`useEffect`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject useEffect` |  |
| **`useEffectLocal`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject useEffectLocal` |  |
| **`useLockedEffect`** | `[BoxGroup("Shrine Settings", true, false, 0)] public GameObject useLockedEffect` |  |

:::

## Properties (9)

::: details Click to expand Properties (9)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canInteractWithMouse`** | `public virtual bool canInteractWithMouse { get; }` |  |
| **`focusDistance`** | `public float focusDistance { get; }` |  |
| **`interactPivot`** | `public virtual Transform interactPivot { get; }` |  |
| **`isAvailable`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public bool isAvailable { get; set; }` |  |
| **`isLocked`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public bool isLocked { get; set; }` |  |
| **`isOnCooldown`** | `public bool isOnCooldown { get; }` |  |
| **`isRegularReward`** | `public virtual bool isRegularReward { get; }` |  |
| **`scaleSpawnRateWithPlayers`** | `public bool scaleSpawnRateWithPlayers { get; }` |  |
| **`totalUseCount`** | `[SaveVar] [SaveVar(SaveVarFlags.Default)] public int totalUseCount { get; set; }` |  |

:::

## Methods (15)

::: details `CanAfford(Entity)`

Checked everywhere.

```csharp
public AffordType CanAfford(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `AffordType`

:::

::: details `CanInteract(Entity)`

```csharp
public virtual bool CanInteract(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `DoPostUseRoutines(Entity)`

Deduct cost from the entity, increment use count and invoke callbacks.

```csharp
public void DoPostUseRoutines(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `GetClosestPointOnShrine(Vector3)`

```csharp
public Vector3 GetClosestPointOnShrine(Vector3 pos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `pos` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetCost(Entity)`

Get gold/health cost of this shrine for specified activator. This must return consistent values across server and clients.

```csharp
public virtual Cost? GetCost(Entity activator)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activator` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `Cost?`

:::

::: details `GetRandomSpawnPosition(Vector3)`

```csharp
public Vector3 GetRandomSpawnPosition(Vector3 activatorPos)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `activatorPos` | `UnityEngine.Vector3` |  |

**Returns:** `UnityEngine.Vector3`

:::

::: details `GetUseCountByPlayer(DewPlayer)`

```csharp
public int GetUseCountByPlayer(DewPlayer player)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `player` | [`DewPlayer`](/api/Global.DewPlayer) |  |

**Returns:** `int`

:::

::: details `MakeAvailable()`

Forcibly make the shrine available for use. Callable on server.

```csharp
[Button]
public void MakeAvailable()
```

:::

::: details `MakeUnavailable()`

Forcibly make the shrine unavailable for use. Callable on server.

```csharp
[Button]
public void MakeUnavailable()
```

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
public virtual void OnInteract(Entity entity, bool alt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `alt` | `bool` |  |

:::

::: details `OnUse(Entity)`

Called on server when an entity uses this shrine. Return value must indicate success of this use.Returning true will play use effect, increment use count, and deduct cost from entity.

```csharp
protected abstract bool OnUse(Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |

**Returns:** `bool`

:::

::: details `ResetUseCounts()`

```csharp
public void ResetUseCounts()
```

:::

::: details `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (67)

*Classes and systems that invoke, reference, or depend on `Shrine`:*

[ChoiceShrine](/api/Global.ChoiceShrine) · `ConversationShrineBase` · [EditSkillShrine](/api/Global.EditSkillShrine) · [FloatingWindowManager](/api/Global.FloatingWindowManager) · [PingManager](/api/Global.PingManager) · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_SkillsAndEssences` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomRewards](/api/Global.RoomRewards) · `Shrine_AncientRemnants` · `Shrine_Anitya` · `Shrine_ArtifactGiver` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_BrokenWoodenDoll` · `Shrine_CallOfTheRavenous` · `Shrine_Chaos` · `Shrine_Concept` · `Shrine_CookingPot` · `Shrine_CorruptedChaos` · `Shrine_DebugTeleport` · `Shrine_Despair` · `Shrine_Despair_Vestige` · `Shrine_Destiny` · `Shrine_Disintegration` · `Shrine_DreamdustBit` · `Shrine_DreamdustBox` · `Shrine_Entanglement` · `Shrine_FallenStar` · `Shrine_FragmentOfRadiance` · `Shrine_GoldBit` · `Shrine_GoldBox` · `Shrine_Guidance` · `Shrine_Hatred` · `Shrine_Hatred_Old` · `Shrine_Hatred_Reward` · `Shrine_HeroSoul` · `Shrine_HiddenStash` · `Shrine_InvitationOfJonasMeeting` · `Shrine_LoopCat` · `Shrine_Luck` · `Shrine_MarshOfDestiny_SeedOfTorment` · `Shrine_MawOfDoom` · `Shrine_Memory` · `Shrine_Merchant_Backpack` · `Shrine_MirrorOfRemorse` · `Shrine_MorasDomain_HerPresence` · `Shrine_PileOfSnow` · `Shrine_Polaris_Teleporter` · `Shrine_PotOfGreed` · `Shrine_PrimusDoor` · `Shrine_PrimusEndingLightPillar` · `Shrine_PyranasLove` · `Shrine_Se_Star_Bismuth_I_KnowledgeBook_Book` · `Shrine_SmallSoul` · `Shrine_StarCookie` · `Shrine_Stardust` · `Shrine_StarlessPath_EndingRift` · `Shrine_StrayMemory_StartProp` · `Shrine_TheConsortOfNight` · `Shrine_TheConsortOfNight_Rift` · `Shrine_WagesOfResolve` · `UI_InGame_FloatingWindow_ChoiceShrine` · `UI_InGame_Interact_Custom` · `UI_InGame_Interact_Shrine` · `UI_InGame_Map_Item_Shrine` · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (18)

*Types and components that `Shrine` references or depends upon:*

[Actor](/api/Global.Actor) · [Cost](/api/Global.Cost) · `CostExtensions` · [Dew](/api/Global.Dew) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [GameManager](/api/Global.GameManager) · `GetComponentsNonAllocExtension` · [Hero](/api/Global.Hero) · [IBanRoomNodesNearby](/api/Global.IBanRoomNodesNearby) · [IInteractable](/api/Global.IInteractable) · [IProp](/api/Global.IProp) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · `Vector3FlattenExtension`

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`AffordType`](/enums#affordtype) · [`MapItemVisibility`](/enums#mapitemvisibility) · [`SaveVarFlags`](/enums#savevarflags)

:::
