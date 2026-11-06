# Class: DewGameplaySettings_User

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewGameplaySettings_User : IInitializableSettings
```

## Fields (15)

::: details Click to expand Fields (15)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`abbreviateBigDamageNumbers`** | `public bool abbreviateBigDamageNumbers` |  |
| **`confirmMemoryEditByHold`** | `public ConfirmMemoryEditBehavior confirmMemoryEditByHold` |  |
| **`cursorColor`** | `public float cursorColor` |  |
| **`cursorScale`** | `public float cursorScale` |  |
| **`damageNumberVisibility`** | `public DamageNumberVisibility damageNumberVisibility` |  |
| **`disableTutorial`** | `public bool disableTutorial` |  |
| **`enableProfanityFilter`** | `public bool enableProfanityFilter` |  |
| **`gamepadVibrationStrength`** | `public float gamepadVibrationStrength` |  |
| **`highlightCharactersOnMouseOver`** | `public bool highlightCharactersOnMouseOver` |  |
| **`killScreenEffectsStrength`** | `public float killScreenEffectsStrength` |  |
| **`reduceOtherPlayerEffectsStrength`** | `public ReduceOtherPlayerEffectsStrength reduceOtherPlayerEffectsStrength` |  |
| **`screenShakeStrength`** | `public float screenShakeStrength` |  |
| **`showHunterWarning`** | `public bool showHunterWarning` |  |
| **`uiScale`** | `public float uiScale` |  |
| **`unlockSkillsOutsideEditMode`** | `public bool unlockSkillsOutsideEditMode` |  |

:::

## Methods (2)

::: details `Clone()`

```csharp
public object Clone()
```

**Returns:** `object`

:::

::: details `Initialize()`

```csharp
public void Initialize()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `DewGameplaySettings_User`:*

[DewProfile](/api/Global.DewProfile) · `UI_Settings_View`

### Dependencies (1)

*Types and components that `DewGameplaySettings_User` references or depends upon:*

[IInitializableSettings](/api/Global.IInitializableSettings)

### Related Enums (3)

*Enumerations referenced in fields, properties, or method signatures:*

[`ConfirmMemoryEditBehavior`](/enums#confirmmemoryeditbehavior) · [`DamageNumberVisibility`](/enums#damagenumbervisibility) · [`ReduceOtherPlayerEffectsStrength`](/enums#reduceotherplayereffectsstrength)

:::
