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
