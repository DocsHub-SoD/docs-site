# Struct: AssetRef&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public struct AssetRef<T> where T : Object
```

## Fields (5)

::: details Click to expand Fields (5)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`guid`** | `public string guid` |  |
| **`isActor`** | `public bool isActor` |  |
| **`isMonoBehaviour`** | `public bool isMonoBehaviour` |  |
| **`typeAssemblyQualifiedName`** | `public string typeAssemblyQualifiedName` |  |
| **`typeName`** | `public string typeName` |  |

:::

## Properties (2)

::: details Click to expand Properties (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`asset`** | `[JsonIgnore] [JsonIgnore] public T asset { get; set; }` |  |
| **`lightAsset`** | `[JsonIgnore] [JsonIgnore] public T lightAsset { get; }` |  |

:::

## Methods (5)

::: details `ClearCache()`

```csharp
public void ClearCache()
```

:::

::: details `Equals(AssetRef&lt;T&gt;)`

```csharp
public bool Equals(AssetRef<T> other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | `AssetRef<T>` |  |

**Returns:** `bool`

:::

::: details `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

:::

::: details `GetType()`

```csharp
[Obsolete("Using GetType() on AssetRefs is typically a mistake", true)]
public Type GetType()
```

**Returns:** `System.Type`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (56)

*Classes and systems that invoke, reference, or depend on `AssetRef<T>`:*

`AbilityAnimationReplacementPair` · [AbilityTrigger](/api/Global.AbilityTrigger) · `Ai_Mon_Special_AmbushSpawner_Projectile` · `AssetRefExtensions` · [EntityAbility](/api/Global.EntityAbility) · [EntityAnimation](/api/Global.EntityAnimation) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · [MirageSkinDecoObject](/api/Global.MirageSkinDecoObject) · `Mon_Despair_AzurakMonsterSpawner` · `Mon_Special_BossMaw` · [Monster](/api/Global.Monster) · [MusicManager](/api/Global.MusicManager) · `NetworkReaderWriterExtensions` · `NextZoneOverrideTreasure` · [PreloadInterface](/api/Global.PreloadInterface) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · [Room](/api/Global.Room) · `RoomMod_Ambush` · `RoomMod_DistantMemories` · `RoomMod_PureDream` · [RoomMonsters](/api/Global.RoomMonsters) · [RoomProps](/api/Global.RoomProps) · `Se_Mon_Special_BossPolaris_Holy_PhaseShifter` · `Shrine_ArtifactGiver` · `Shrine_Hatred` · [SkillTrigger](/api/Global.SkillTrigger) · `St_Q_Laceration` · `TravelerStoryNodeDef` · `TravelerStoryPresenter` · [TriggerConfig](/api/Global.TriggerConfig) · `UI_Collectables_MainView` · `UI_Collectables_ObjectItem` · `UI_DifficultyIcon` · `UI_EmoteList_PreviewWindow` · `UI_InGame_FloatingWindow_ChoiceShrine_Item` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_Skills_ContextMenu` · `UI_Lobby_Constellations_Skills_ContextMenu_Item` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_DejavuWindow` · `UI_Lobby_DejavuWindow_Item` · `UI_Lobby_HeroList` · `UI_Lobby_HeroList_Item` · `UI_Lobby_Loadout_ComponentBase` · `UI_Lobby_Loadout_SkillSlot` · `UI_Lobby_SelectedHeroInfo_Base` · `UI_Lobby_SelectedHeroInfo_HeroStat` · `UI_LucidDreamIcon` · `UI_StarIcon` · [UI_StationaryEmote](/api/Global.UI_StationaryEmote) · `UI_TravelerStoryDetailContainer` · `UI_TravelerStory_DetailPanel` · [Zone](/api/Global.Zone) · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (2)

*Types and components that `AssetRef<T>` references or depends upon:*

`AssetRefTypeResolver` · [DewResources](/api/Global.DewResources)

:::
