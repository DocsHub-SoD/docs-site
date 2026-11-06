# Class: EntityHighlightProvider

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → [HighlightProvider](/api/Global.HighlightProvider) → [MeshHighlightProvider](/api/Global.MeshHighlightProvider)

```csharp
public class EntityHighlightProvider : MeshHighlightProvider, ILogicUpdate
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disableHighlight`** | `public bool disableHighlight` |  |
| **`HitEffectDuration`** | `public const float HitEffectDuration = 0.1` |  |

:::

## Methods (6)

::: details `Awake()`

```csharp
protected override void Awake()
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

::: details `ShowHit()`

```csharp
public void ShowHit()
```

:::

::: details `Start()`

```csharp
protected override void Start()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `EntityHighlightProvider`:*

[EntityVisual](/api/Global.EntityVisual)

### Dependencies (6)

*Types and components that `EntityHighlightProvider` references or depends upon:*

[DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [HighlightProvider](/api/Global.HighlightProvider) · [ManagerBase`1](/api/Global.ManagerBase`1) · [MeshHighlightProvider](/api/Global.MeshHighlightProvider) · [SafeAction`1](/api/Global.SafeAction`1)

:::
