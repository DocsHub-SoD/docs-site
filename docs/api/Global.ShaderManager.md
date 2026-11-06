# Class: ShaderManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[ExecuteAlways]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [ShaderManager](/api/Global.ShaderManager)

```csharp
[ExecuteAlways]
public class ShaderManager : ManagerBase<ShaderManager>, ILogicUpdate, ISettingsChangedCallback
```

## Methods (3)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::

::: details `UpdateRoomRotation()`

```csharp
public static void UpdateRoomRotation()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `ShaderManager`:*

[CameraManager](/api/Global.CameraManager)

### Dependencies (7)

*Types and components that `ShaderManager` references or depends upon:*

[CameraManager](/api/Global.CameraManager) · [Dew](/api/Global.Dew) · [DewShadingProfile](/api/Global.DewShadingProfile) · [FxCameraShake](/api/Global.FxCameraShake) · [ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
