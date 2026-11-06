# Interface: ISpawnableAsMiniBoss

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ISpawnableAsMiniBoss
```

## Methods (3)

::: details `GiveGenericMiniBossBonus(Entity, float)`

```csharp
public static void GiveGenericMiniBossBonus(Entity entity, float postDelayMultiplier = 0.5)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `postDelayMultiplier` | `float` |  |

:::

::: details `OnBeforeSpawnAsMiniBoss()`

Called on server before being spawned as an elite.

```csharp
void OnBeforeSpawnAsMiniBoss()
```

:::

::: details `OnCreateAsMiniBoss()`

Called everywhere after being spawned as an elite.

```csharp
void OnCreateAsMiniBoss()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (25)

*Classes and systems that invoke, reference, or depend on `ISpawnableAsMiniBoss`:*

`Mon_DarkCave_DarkElemental` · `Mon_DarkCave_Oppressor` · `Mon_Despair_Displacer` · `Mon_Despair_DreadBug` · `Mon_Despair_ParalyticFly` · `Mon_Despair_WretchedArtillery` · `Mon_Forest_Hound` · `Mon_Forest_SpiderSpitter` · `Mon_Forest_SpiderWarrior` · `Mon_Ink_Archer` · `Mon_Ink_DivineAnimal` · `Mon_Ink_GhostBlade` · `Mon_Ink_GhostSpear` · `Mon_LavaLand_FireElemental` · `Mon_LavaLand_InfernoSpider` · `Mon_LavaLand_Magmadon` · `Mon_LavaLand_SuperheatedWolf` · `Mon_Sky_Baam` · `Mon_Sky_BigBaam_Regular` · `Mon_Sky_BigBaam_Rooter` · `Mon_Sky_StarSeed` · `Mon_SnowMountain_IceElemental` · `Mon_SnowMountain_Scavenger` · `Mon_SnowMountain_SnowWolf` · [RoomMonsters](/api/Global.RoomMonsters)

### Dependencies (8)

*Types and components that `ISpawnableAsMiniBoss` references or depends upon:*

[Actor](/api/Global.Actor) · [Entity](/api/Global.Entity) · [EntityAbility](/api/Global.EntityAbility) · [EntityControl](/api/Global.EntityControl) · [EntityStatus](/api/Global.EntityStatus) · [EntityTransformModifier](/api/Global.EntityTransformModifier) · [EntityVisual](/api/Global.EntityVisual) · [StatBonus](/api/Global.StatBonus)

:::
