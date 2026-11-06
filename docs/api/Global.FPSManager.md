# Class: FPSManager

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FPSManager](/api/Global.FPSManager)

```csharp
public class FPSManager : ManagerBase<FPSManager>, ILogicUpdate, ISettingsChangedCallback
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

:::

## Methods (4)

::: details `OnDisable()`

```csharp
protected override void OnDisable()
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

::: details `UpdateFPSLimit()`

```csharp
public void UpdateFPSLimit()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `FPSManager`:*

[InGameUIManager](/api/Global.InGameUIManager)

### Dependencies (4)

*Types and components that `FPSManager` references or depends upon:*

[ISettingsChangedCallback](/api/Global.ISettingsChangedCallback) · [InGameUIManager](/api/Global.InGameUIManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [UIManager](/api/Global.UIManager)

:::
