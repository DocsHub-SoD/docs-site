# Class: RoomModifierBase

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier)

```csharp
public class RoomModifierBase : Actor, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IExcludeFromPool
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowedZones`** | `[ShowIf("@chance &gt; 0.000001f", true)]
[InfoBox("All zones will be allowed to have this modifier", InfoMessageType.Info, "@allowedZones == null \|\| allowedZones.Length == 0")]
[InfoBox("@GetZoneValidationMessage(allowedZones)", InfoMessageType.Error, "@GetZoneValidationMessage(allowedZones) != null")]
public string[] allowedZones` |  |
| **`chance`** | `[LabelText("@spawnType.ToString()")]
public float chance` |  |
| **`difficultyScaling`** | `[ShowIf("@chance &gt; 0.000001f", true)]
public ScaleWithDifficultyMode difficultyScaling` |  |
| **`disableOtherEnvParticles`** | `[ToggleLeft]
public bool disableOtherEnvParticles` |  |
| **`disallowOtherModifiers`** | `[ShowIf("@chance &gt; 0.000001f", true)]
[ToggleLeft]
public bool disallowOtherModifiers` |  |
| **`enableInnerDecorations`** | `[Title("Decorations", null, TitleAlignments.Left, true, true)]
[ToggleLeft]
public bool enableInnerDecorations` |  |
| **`enableOuterDecorations`** | `[ToggleLeft]
public bool enableOuterDecorations` |  |
| **`excludeFromPool`** | `public bool excludeFromPool` |  |
| **`fxLoop`** | `[Title("Effects", null, TitleAlignments.Left, true, true)]
public GameObject fxLoop` |  |
| **`hiddenOnVisitedNode`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)]
public bool hiddenOnVisitedNode` |  |
| **`innerDecorations`** | `[BoxGroup("Inner Decorations", true, false, 0)]
[InlineProperty]
[HideLabel]
[ShowIf("enableInnerDecorations", true)]
public DecorationSettings innerDecorations` |  |
| **`isMain`** | `[Title("General", null, TitleAlignments.Left, true, true)]
[FormerlySerializedAs("showOnTopRight")]
public bool isMain` | Main modifiers will print notification when user enters the node.A node can only have a single main modifier. |
| **`mainColor`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)]
public Color mainColor` |  |
| **`mapSprite`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)]
public Sprite mapSprite` |  |
| **`mapSpriteScale`** | `[ShowIf("@isMain \|\| visibilityOnWorld != NodeModifierVisibility.Hidden", true)]
public float mapSpriteScale` |  |
| **`modifiesRewards`** | `[ShowIf("@chance &gt; 0.000001f", true)]
[ToggleLeft]
public bool modifiesRewards` |  |
| **`outerDecorations`** | `[BoxGroup("Outer Decorations", true, false, 0)]
[InlineProperty]
[HideLabel]
[ShowIf("enableOuterDecorations", true)]
public DecorationSettings outerDecorations` |  |
| **`removeModifierWhenOverrideOverwritten`** | `[ToggleLeft]
[ShowIf("@!string.IsNullOrEmpty(roomOverride)", true)]
public bool removeModifierWhenOverrideOverwritten` |  |
| **`roomOverride`** | `public string roomOverride` |  |
| **`spawnedDecorations`** | `public readonly List&lt;GameObject&gt; spawnedDecorations` |  |
| **`spawnOncePerLoop`** | `[ShowIf("@chance &gt; 0.000001f", true)]
[ToggleLeft]
public bool spawnOncePerLoop` |  |
| **`spawnType`** | `[Title("Natural Spawn Settings", null, TitleAlignments.Left, true, true)]
public ModifierSpawnType spawnType` |  |
| **`visibilityOnWorld`** | `public NodeModifierVisibility visibilityOnWorld` |  |
| **`zoneIndexRange`** | `[ShowIf("@chance &gt; 0.000001f", true)]
public Vector2Int zoneIndexRange` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`id`** | `[SaveVar(SaveVarFlags.Default)]
public int id { get; }` | Modifier id of this modifier instance. |
| **`isDestroyedOnRoomChange`** | `public override bool isDestroyedOnRoomChange { get; }` |  |
| **`modData`** | `public ModifierData modData { get; }` |  |

## Methods

### `CanSpawnAtNode(int)`

Checked on server, on the modifier prefab, when generating the world.It will be called in the middle of generating the world, but essential things like basic node positions and distances will be provided.

```csharp
public virtual bool CanSpawnAtNode(int nodeIndex)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `nodeIndex` | `int` |  |

**Returns:** `bool`

### `GetScaledChance()`

```csharp
public float GetScaledChance()
```

**Returns:** `float`

### `IsAvailableInGame()`

Is this modifier available in game? If false, this modifier will not be applied to nodes.Checked on server everytime when generating world.NOTE that in-game constellation registration happens AFTER first world generation!!!!

```csharp
public virtual bool IsAvailableInGame()
```

**Returns:** `bool`

### `ModifyEntities(Action&lt;Entity&gt;, Action&lt;Entity&gt;)`

Modify all entities.onStart is called on all existing entities and entities spawned in the future.onStop is called on all existing entities when modifier stops.

```csharp
public void ModifyEntities(Action<Entity> onStart, Action<Entity> onStop)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `onStart` | [System.Action&lt;T&gt;&lt;Entity&gt;](/api/Global.Entity) |  |
| `onStop` | [System.Action&lt;T&gt;&lt;Entity&gt;](/api/Global.Entity) |  |

### `OnCreate()`

```csharp
protected override void OnCreate()
```

### `OnDestroyActor()`

```csharp
protected override void OnDestroyActor()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `PlaceDecorations(DecorationSettings, IReadOnlyList&lt;(int, int)&gt;)`

```csharp
public static List<GameObject> PlaceDecorations(DecorationSettings s, IReadOnlyList<(int, int)> indices)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `s` | [DecorationSettings](/api/Global.DecorationSettings) |  |
| `indices` | `System.Collections.Generic.IReadOnlyList&lt;T&gt;&lt;(int,int)&gt;` |  |

**Returns:** `System.Collections.Generic.List&lt;T&gt;&lt;UnityEngine.GameObject&gt;`

### `PlaceShrine&lt;T&gt;(PlaceShrineSettings)`

Places a shrine on random position.This function properly handles revisits.Warning: does not support multiple shrines of same type

```csharp
public void PlaceShrine<T>(PlaceShrineSettings settings) where T : Shrine
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [PlaceShrineSettings](/api/Global.PlaceShrineSettings) |  |
| `` | `T` |  |

### `RemoveModifier()`

Remove and destroy this modifier.

```csharp
public void RemoveModifier()
```

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`
