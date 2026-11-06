# Class: Rift_Sidetrack

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Actor](/api/Global.Actor) → [Rift](/api/Global.Rift)

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Rift_Sidetrack : Rift, ILogicUpdate, ICleanup, ICustomDestroyRoutine, IInteractable, IBanRoomNodesNearby
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`allowedZones`** | `[InfoBox("All zones will be allowed to have this modifier", InfoMessageType.Info, "@allowedZones == null \|\| allowedZones.Length == 0")] [InfoBox("@GetZoneValidationMessage(allowedZones)", InfoMessageType.Error, "@GetZoneValidationMessage(allowedZones) != null")] [ShowIf("@spawnChance > 0", true)] public string[] allowedZones` |  |
| **`mainColor`** | `public Color mainColor` |  |
| **`manualRoomNames`** | `[HideIf("useWildcardPattern", true)] [LabelText("Room Names")] public List<string> manualRoomNames` |  |
| **`oncePerLoop`** | `[ShowIf("@spawnChance > 0", true)] public bool oncePerLoop` |  |
| **`softInstance`** | `public static Rift_Sidetrack softInstance` |  |
| **`spawnChance`** | `[Title("Natural Spawn Settings", null, TitleAlignments.Left, true, true)] public float spawnChance` |  |
| **`useWildcardPattern`** | `[Title("Destination", null, TitleAlignments.Left, true, true)] public bool useWildcardPattern` |  |
| **`wildcardPattern`** | `[ShowIf("useWildcardPattern", true)] public string wildcardPattern` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static Rift_Sidetrack instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`isValid`** | `public bool isValid { get; }` | Is this sidetrack rift valid for use? Sidetrack rifts with no rooms are invalid. |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```

### `GetConfirmMessage()`

```csharp
protected virtual string GetConfirmMessage()
```

**Returns:** `string`

### `OnInteractRift(Hero)`

```csharp
protected override bool OnInteractRift(Hero hero)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hero` | [`Hero`](/api/Global.Hero) |  |

**Returns:** `bool`

### `ShouldBeSavedWithRoom()`

```csharp
public override bool ShouldBeSavedWithRoom()
```

**Returns:** `bool`

### `TravelImmediately()`

```csharp
public virtual void TravelImmediately()
```
