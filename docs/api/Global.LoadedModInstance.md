# Class: LoadedModInstance

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class LoadedModInstance
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`container`** | `public GameObject container` |  |
| **`isAlteringGameplay`** | `public bool isAlteringGameplay` | This must be set to true, if this mod is altering gameplay in any way. This will show mod icon in the lobby list to let the clients know prior to joining your game.This is automatically set to true if the mod contains any JSON overrides. |
| **`mod`** | `public ModItem mod` |  |
| **`registeredCommands`** | `public List&lt;string&gt; registeredCommands` |  |
