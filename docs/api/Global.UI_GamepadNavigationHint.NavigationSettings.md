# Struct: UI_GamepadNavigationHint.NavigationSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
[InlineProperty]
public struct UI_GamepadNavigationHint.NavigationSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`canFallbackToGeneric`** | `[ShowIf("@navigation != GamepadNavigation.Generic \|\| limitToChildren", true)]
[ToggleLeft]
public bool canFallbackToGeneric` |  |
| **`customTarget`** | `[ShowIf("@navigation == GamepadNavigation.Custom", true)]
public GameObject customTarget` |  |
| **`limitToChildren`** | `[ShowIf("@navigation != GamepadNavigation.Custom", true)]
[ToggleLeft]
public bool limitToChildren` |  |
| **`navigation`** | `[EnumToggleButtons]
[HideLabel]
public GamepadNavigation navigation` |  |
