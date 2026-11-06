# Class: ImageComponent

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [ImageComponentAnimated](/api/Global.ImageComponentAnimated)

```csharp
public abstract class ImageComponent : MonoBehaviour
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`image`** | `public Image image { get; }` |  |
| **`material`** | `public Material material { get; }` |  |

## Methods

### `Init()`

It's guaranteed image and material to be non-null when this is called.

```csharp
public virtual void Init()
```

### `OnDestroy()`

```csharp
public void OnDestroy()
```

### `Start()`

```csharp
public virtual void Start()
```

### `Tick()`

It's guaranteed image and material to be non-null when this is called.

```csharp
public virtual void Tick()
```

### `Update()`

```csharp
public virtual void Update()
```
