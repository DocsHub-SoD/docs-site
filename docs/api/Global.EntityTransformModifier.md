# Class: EntityTransformModifier

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class EntityTransformModifier
```

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`localOffset`** | `public Vector3 localOffset { get; set; }` |  |
| **`rotation`** | `public Quaternion rotation { get; set; }` |  |
| **`scaleMultiplier`** | `public Vector3 scaleMultiplier { get; set; }` |  |
| **`worldOffset`** | `public Vector3 worldOffset { get; set; }` |  |

:::

## Methods (1)

::: details `Stop()`

Remove this transform modifier from its parent.

```csharp
public void Stop()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (27)

*Classes and systems that invoke, reference, or depend on `EntityTransformModifier`:*

`Ai_C_Whirlwind` · `Ai_E_WinterDive` · `Ai_Mon_Despair_BossAzurak_Roll` · `Ai_Mon_Ink_BossDarkMoon_Hammer` · `Ai_Mon_LavaLand_BossInfernus_Jump` · `Ai_Mon_SnowMountain_BossSkoll_DeathFromAbove` · `Ai_Mon_SnowMountain_BossSkoll_Whirlwind` · `Ai_Mon_Special_BossObliviax_TurnAtk` · `Ai_Q_MoonlightPact` · [EntityVisual](/api/Global.EntityVisual) · [FlavourManager](/api/Global.FlavourManager) · [FxEntityShake](/api/Global.FxEntityShake) · [FxEntityTransform](/api/Global.FxEntityTransform) · [ISpawnableAsMiniBoss](/api/Global.ISpawnableAsMiniBoss) · `Mon_Ink_EgoSword` · `Mon_Special_AmbushSpawner` · [PropEnt_Stone_DreamDust](/api/Global.PropEnt_Stone_DreamDust) · `RoomMod_Hunted` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · `Se_Mon_Despair_BossAzurak_Hide` · `Se_MorasDomain_AppearFromGround` · `Se_ObliviaxKidnap` · `Se_PureDream_Statue` · `Se_Q_Discipline_Jump` · `Se_R_SerpentineBlessing_Buff` · `Se_Shrine_Despair_Teleport`

### Dependencies (2)

*Types and components that `EntityTransformModifier` references or depends upon:*

[Entity](/api/Global.Entity) · [EntityVisual](/api/Global.EntityVisual)

:::
