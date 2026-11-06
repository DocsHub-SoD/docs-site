# Class: DewControlSettings_Platform

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewControlSettings_Platform : IInitializableSettings, IValidatableSettings
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`controllerButtonType`** | `public ControllerButtonType controllerButtonType` |  |
| **`joystick0Dead`** | `public float joystick0Dead` |  |
| **`joystick0Max`** | `public float joystick0Max` |  |
| **`joystick1Dead`** | `public float joystick1Dead` |  |
| **`joystick1Max`** | `public float joystick1Max` |  |

:::

## Methods (3)

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

::: details `Validate()`

```csharp
public void Validate()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (2)

*Classes and systems that invoke, reference, or depend on `DewControlSettings_Platform`:*

[DewPlatformSettings](/api/Global.DewPlatformSettings) · `UI_Settings_View`

### Dependencies (2)

*Types and components that `DewControlSettings_Platform` references or depends upon:*

[IInitializableSettings](/api/Global.IInitializableSettings) · [IValidatableSettings](/api/Global.IValidatableSettings)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#controllerbuttontype" class="enum-link" data-tooltip="Xbox=1 · PlayStation=2 · Generic=3">ControllerButtonType</a>

:::
