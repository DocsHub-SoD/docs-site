# Class: ImageComponent

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ImageComponentAnimated](/api/Global.ImageComponentAnimated)

```csharp
public abstract class ImageComponent : MonoBehaviour
```

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`image`** | `public Image image { get; }` |  |
| **`material`** | `public Material material { get; }` |  |

:::

## Methods (5)

::: details `Init()`

It's guaranteed image and material to be non-null when this is called.

```csharp
public virtual void Init()
```

:::

::: details `OnDestroy()`

```csharp
public void OnDestroy()
```

:::

::: details `Start()`

```csharp
public virtual void Start()
```

:::

::: details `Tick()`

It's guaranteed image and material to be non-null when this is called.

```csharp
public virtual void Tick()
```

:::

::: details `Update()`

```csharp
public virtual void Update()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (3)

*Classes and systems that invoke, reference, or depend on `ImageComponent`:*

`IMG_FireplaceAlpha` · `IMG_ScrollingTexture` · [ImageComponentAnimated](/api/Global.ImageComponentAnimated)

### Dependencies (0)

*No outgoing class dependencies recorded.*

:::
