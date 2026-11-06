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
| **`maxTotalUseCount`** | `[SaveVar(SaveVarFlags.Default)] [FormerlySerializedAs("maxUseCount")] [BoxGroup("Shrine Settings", true, false, 0)] public int maxTotalUseCount` |  |
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
| **`isAvailable`** | `[SaveVar(SaveVarFlags.Default)] public bool isAvailable { get; set; }` |  |
| **`isLocked`** | `[SaveVar(SaveVarFlags.Default)] public bool isLocked { get; set; }` |  |
| **`isOnCooldown`** | `public bool isOnCooldown { get; }` |  |
| **`isRegularReward`** | `public virtual bool isRegularReward { get; }` |  |
| **`scaleSpawnRateWithPlayers`** | `public bool scaleSpawnRateWithPlayers { get; }` |  |
| **`totalUseCount`** | `[SaveVar(SaveVarFlags.Default)] public int totalUseCount { get; set; }` |  |

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
