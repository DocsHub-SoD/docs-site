# Class: DewPool

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewPool
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`_clearAction`** | `public static Dictionary<Type, Action<object>> _clearAction` |  |

:::

## Methods (4)

::: details `ClearEventsAndProcessors(Component)`

```csharp
public static void ClearEventsAndProcessors(Component obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Component` |  |

:::

::: details `GetArray&lt;T&gt;(out ArrayReturnHandle&lt;T&gt;, int)`

```csharp
public static T[] GetArray<T>(out ArrayReturnHandle<T> handle, int minSize = 128)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ArrayReturnHandle<T>` |  |
| `minSize` | `int` |  |
| `` | `T` |  |

**Returns:** `T[]`

:::

::: details `GetDictionary&lt;TKey, TValue&gt;(out DictionaryReturnHandle&lt;TKey, TValue&gt;)`

Get an empty dictionary of TKey, TValue.You do not need to clear the dictionary before returning.

```csharp
public static Dictionary<TKey, TValue> GetDictionary<TKey, TValue>(out DictionaryReturnHandle<TKey, TValue> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `DictionaryReturnHandle<TKey, TValue>` |  |
| `` | `TKey` |  |
| `` | `TValue` |  |

**Returns:** `System.Collections.Generic.Dictionary<TKey, TValue>`

:::

::: details `GetList&lt;T&gt;(out ListReturnHandle&lt;T&gt;)`

Get an empty list of T.You do not need to clear the list before returning.

```csharp
public static List<T> GetList<T>(out ListReturnHandle<T> handle)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<T>` |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.List<T>`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (44)

*Classes and systems that invoke, reference, or depend on `DewPool`:*

`ACH_M_M_M_MONSTER_KILL` · [Actor](/api/Global.Actor) · `Ai_Mon_Ink_BossWhiteNight_Cataclysm_SafeZone` · `Ai_Mon_Sky_BigBaam_BeamAtk` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_R_Inspire_Roar` · [AttachToFace](/api/Global.AttachToFace) · [CameraManager](/api/Global.CameraManager) · [Dew](/api/Global.Dew) · [DewCollider](/api/Global.DewCollider) · [DewEffect](/api/Global.DewEffect) · [DewPhysics](/api/Global.DewPhysics) · [DewProfileStats](/api/Global.DewProfileStats) · [DewResources](/api/Global.DewResources) · [Entity](/api/Global.Entity) · [EntityComponent](/api/Global.EntityComponent) · [EntityModel](/api/Global.EntityModel) · [EntityStatus](/api/Global.EntityStatus) · [EntityVisual](/api/Global.EntityVisual) · [FxSelectiveQuality](/api/Global.FxSelectiveQuality) · `Gem_R_Ricochet` · `GetComponentsNonAllocExtension` · [GlobalUIManager](/api/Global.GlobalUIManager) · `Hero_Bismuth` · `Hero_Yubar_ScrollTexture` · `Ink_ScrollingInkAnimation` · `Mon_Special_BossMaw` · [Projectile](/api/Global.Projectile) · [Room](/api/Global.Room) · [RoomModifierBase](/api/Global.RoomModifierBase) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · [SafeAction`4](/api/Global.SafeAction`4) · `Se_Mon_DarkCave_BossSeeker_Blink` · `Se_R_BaptismOfSun_Buff` · `Se_RoomMod_UnstableVeilOfTime_ModifyCooldowns` · `Shrine_FallenStar` · [StatusEffect](/api/Global.StatusEffect) · `ToListNonAllocExtensions` · `UI_InGame_TimerDisplay_Item` · `UI_TravelerStory_HeroConstellation` · `UI_World_FollowAndFaceCamera`

### Dependencies (4)

*Types and components that `DewPool` references or depends upon:*

[Actor](/api/Global.Actor) · [EntityComponent](/api/Global.EntityComponent) · `IPoolClearable` · [ManagerBase`1](/api/Global.ManagerBase`1)

:::
