# Class: EntityModel

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class EntityModel : MonoBehaviour
```

## Fields (26)

::: details Click to expand Fields (26)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bodyRenderers`** | `[Title("General", null, TitleAlignments.Left, true, true)] public Renderer[] bodyRenderers` |  |
| **`customMappings`** | `[Title("Custom Mappings", null, TitleAlignments.Left, true, true)] public List<EntityModelCustomMapping> customMappings` |  |
| **`death`** | `public AnimationClipWithSpeed death` |  |
| **`deathBehavior`** | `public EntityVisual.EntityDeathBehavior deathBehavior` |  |
| **`dissolveDelay`** | `[ShowIf("@deathBehavior == EntityVisual.EntityDeathBehavior.Dissolve", true)] public float dissolveDelay` |  |
| **`dissolveDuration`** | `[ShowIf("@deathBehavior == EntityVisual.EntityDeathBehavior.Dissolve", true)] public float dissolveDuration` |  |
| **`fxDeath`** | `public GameObject fxDeath` |  |
| **`fxLoop`** | `[Title("Effects", null, TitleAlignments.Left, true, true)] public GameObject fxLoop` |  |
| **`fxTakeDamage`** | `public GameObject fxTakeDamage` |  |
| **`hasGoldDissolve`** | `public bool hasGoldDissolve` |  |
| **`healthBarPosition`** | `public Transform healthBarPosition` |  |
| **`holsteredWeapon`** | `public Transform holsteredWeapon` |  |
| **`idle`** | `[Title("Animations", null, TitleAlignments.Left, true, true)] public AnimationClipWithSpeed idle` |  |
| **`lobby`** | `[Title("Hero", null, TitleAlignments.Left, true, true)] public AnimationClipWithSpeed lobby` |  |
| **`locomotion`** | `public EntityAnimation.LocomotionType locomotion` |  |
| **`runBackwardClip`** | `[ShowIf("support4Directions", true)] public AnimationClip runBackwardClip` |  |
| **`runBackwardLeftClip`** | `[ShowIf("support8Directions", true)] public AnimationClip runBackwardLeftClip` |  |
| **`runBackwardRightClip`** | `[ShowIf("support8Directions", true)] public AnimationClip runBackwardRightClip` |  |
| **`runForwardClip`** | `public AnimationClip runForwardClip` |  |
| **`runForwardLeftClip`** | `[ShowIf("support8Directions", true)] public AnimationClip runForwardLeftClip` |  |
| **`runForwardRightClip`** | `[ShowIf("support8Directions", true)] public AnimationClip runForwardRightClip` |  |
| **`runLeftClip`** | `[ShowIf("support4Directions", true)] public AnimationClip runLeftClip` |  |
| **`runRightClip`** | `[ShowIf("support4Directions", true)] public AnimationClip runRightClip` |  |
| **`stagger`** | `public AnimationClipWithSpeed stagger` |  |
| **`walkAnimationSpeed`** | `public float walkAnimationSpeed` |  |
| **`weapon`** | `public Transform weapon` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isInitialized`** | `public bool isInitialized { get; }` |  |
| **`support4Directions`** | `public bool support4Directions { get; }` |  |
| **`support8Directions`** | `public bool support8Directions { get; }` |  |

:::

## Methods (4)

::: details `ContainsCustomMappingKey(string)`

```csharp
public bool ContainsCustomMappingKey(string key)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |

**Returns:** `bool`

:::

::: details `GetCustomMapping&lt;T&gt;(string)`

```csharp
public T GetCustomMapping<T>(string key) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetCustomMappingArray&lt;T&gt;(string)`

```csharp
public T[] GetCustomMappingArray<T>(string key) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `` | `T` |  |

**Returns:** `T[]`

:::

::: details `TryGetCustomMapping&lt;T&gt;(string, out T)`

```csharp
public bool TryGetCustomMapping<T>(string key, out T target) where T : class
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `target` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::
