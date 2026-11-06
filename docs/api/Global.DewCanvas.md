# Class: DewCanvas

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[LogicUpdatePriority]`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour)

```csharp
[LogicUpdatePriority(400)]
public class DewCanvas : LogicBehaviour, ILogicUpdate, ISettingsChangedCallback
```

## Methods (3)

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnEnable()`

```csharp
protected override void OnEnable()
```

:::

::: details `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (3)

*Types and components that `DewCanvas` references or depends upon:*

[ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
