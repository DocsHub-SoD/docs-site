# Class: MeshHighlightProvider

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [HighlightProvider](/api/Global.HighlightProvider) → [EntityHighlightProvider](/api/Global.EntityHighlightProvider) → [InteractableMeshHighlightProvider](/api/Global.InteractableMeshHighlightProvider)

```csharp
public class MeshHighlightProvider : HighlightProvider, ILogicUpdate
```

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`meshHighlight`** | `public HighlightEffect meshHighlight { get; }` |  |

:::

## Methods (6)

::: details `Awake()`

```csharp
protected virtual void Awake()
```

:::

::: details `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

:::

::: details `OnClickTimeUpdated()`

```csharp
protected override void OnClickTimeUpdated()
```

:::

::: details `OnCursorStatusUpdated()`

```csharp
protected override void OnCursorStatusUpdated()
```

:::

::: details `OnDestroy()`

```csharp
protected void OnDestroy()
```

:::

::: details `Start()`

```csharp
protected virtual void Start()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (5)

*Classes and systems that invoke, reference, or depend on `MeshHighlightProvider`:*

[EntityHighlightProvider](/api/Global.EntityHighlightProvider) · [EntityVisual](/api/Global.EntityVisual) · [InteractableMeshHighlightProvider](/api/Global.InteractableMeshHighlightProvider) · `UI_EntityHealthBar` · `UI_EntityHealthBarMain`

### Dependencies (3)

*Types and components that `MeshHighlightProvider` references or depends upon:*

[HighlightProvider](/api/Global.HighlightProvider) · [LogicBehaviour](/api/Global.LogicBehaviour) · [ObjectHighlightManager](/api/Global.ObjectHighlightManager)

:::
