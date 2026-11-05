# Struct: EventInfoLoadRoom

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoLoadRoom
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`fromIndex`** | `public int fromIndex` |  |
| **`isLoadingFromSave`** | `public bool isLoadingFromSave` |  |
| **`isSidetrackTransition`** | `public bool isSidetrackTransition` |  |
| **`isTraveling`** | `public bool isTraveling` | Is this load result of traveling through a rift? (including the start of the game)This is true if:We just started the gameWe moved through the rift to visit a new / previously visited locationWe are loading from save, which were done in the middle of traveling.This is false if:We are loading from save, which were done after clearing the room. |
| **`toIndex`** | `public int toIndex` |  |
