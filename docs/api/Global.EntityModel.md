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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (23)

*Classes and systems that invoke, reference, or depend on `EntityModel`:*

`Accessory_AttachPoint` · `Ai_Mon_Special_BossMaw_AnnihilationStance` · `Ai_Mon_Special_BossMaw_Cataclysm_Spawner` · `Ai_Mon_Special_BossMaw_ChainReaction` · `Ai_Mon_Special_BossMaw_MoonlightPact` · `Ai_Mon_Special_BossMaw_PrecisionShot` · [CharacterModelDisplay](/api/Global.CharacterModelDisplay) · [EntityAnimation](/api/Global.EntityAnimation) · [EntityVisual](/api/Global.EntityVisual) · `Hero_Aurena` · `Hero_Bismuth_BookController` · `Hero_Husk` · `Hero_Lacerta` · `Mon_DarkCave_CaveSpider` · `Mon_Despair_BossAzurak` · `Mon_Despair_WretchedArtillery` · `Mon_Ink_Archer` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossDarkMoonHallucination` · `Mon_Ink_BossWhiteNight` · `Mon_Ink_EgoSword` · `Mon_Primus_BossPrimusAeron` · `Mon_Special_BossPolaris`

### Dependencies (3)

*Types and components that `EntityModel` references or depends upon:*

[AnimationClipWithSpeed](/api/Global.AnimationClipWithSpeed) · [DewPool](/api/Global.DewPool) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1)

:::
