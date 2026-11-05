# Class: FPSManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [FPSManager](/api/Global.FPSManager)

```csharp
public class FPSManager : ManagerBase<FPSManager>, ILogicUpdate, ISettingsChangedCallback
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`shouldRegisterUpdates`** | `public override bool shouldRegisterUpdates { get; }` |  |

## Methods

### `OnDisable()`

```csharp
protected override void OnDisable()
```

### `OnEnable()`

```csharp
protected override void OnEnable()
```

### `OnSettingsChanged()`

```csharp
public void OnSettingsChanged()
```

### `UpdateFPSLimit()`

```csharp
public void UpdateFPSLimit()
```
