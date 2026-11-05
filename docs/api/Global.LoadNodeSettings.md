# Class: LoadNodeSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class LoadNodeSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`advanceTurn`** | `public bool advanceTurn` | Advances hunters, room index and turn index. |
| **`dontDoRiftTransition`** | `public bool dontDoRiftTransition` | Skip animation of moving players, like sidetrack rifts. |
| **`dontStopLoading`** | `public bool dontStopLoading` | For Primus sequence. Does not do SetLoadingStatus after loading is done. |
| **`from`** | `public int from` |  |
| **`isLoadingFromSave`** | `public bool isLoadingFromSave` |  |
| **`isSidetrackTransition`** | `public bool isSidetrackTransition` |  |
| **`isTravelingRoom`** | `public bool isTravelingRoom` | Set this false only if we are loading from save, and the players were already in this room when the save was made. |
| **`isTravelingZone`** | `public bool isTravelingZone` | Set this false only if we are loading from save, and the players were already in this zone when the save was made. |
| **`isWhiteTransition`** | `public bool isWhiteTransition` | For Primus sequence. Fades out in white instead of normal loading screen. Unused. |
| **`newZone`** | `public Zone newZone` |  |
| **`newZoneNoAdvance`** | `public bool newZoneNoAdvance` | This is only used in development / testing context. Replaces the current zone, instead of advancing zone index. |
| **`to`** | `public int to` |  |

## Methods

### `Clone()`

```csharp
public LoadNodeSettings Clone()
```

**Returns:** `LoadNodeSettings`
