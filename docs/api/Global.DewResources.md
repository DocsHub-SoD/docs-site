# Class: DewResources

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewResources
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`EnableVerboseLogging`** | `public static bool EnableVerboseLogging` |  |
| **`onRepairMissingReferences`** | `public static SafeAction onRepairMissingReferences` |  |
| **`onVariantsCleared`** | `public static SafeAction onVariantsCleared` |  |
| **`variantsParent`** | `public static Transform variantsParent` |  |
| **`vOtherPlayersTonedDown`** | `public static int vOtherPlayersTonedDown` |  |
| **`vQualityAdjusted`** | `public static int vQualityAdjusted` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`database`** | `public static DewResourceDatabase database { get; }` |  |
| **`loadedGuids`** | `public static IReadOnlyCollection<string> loadedGuids { get; }` |  |
| **`transparentMat`** | `public static Material transparentMat { get; }` |  |

:::

## Methods (46)

::: details `AddPreloadRule(MonoBehaviour, Action&lt;PreloadInterface&gt;)`

```csharp
public static void AddPreloadRule(MonoBehaviour owner, Action<PreloadInterface> onPreload)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `owner` | `UnityEngine.MonoBehaviour` |  |
| `onPreload` | [`System.Action<T><PreloadInterface>`](/api/Global.PreloadInterface) |  |

:::

::: details `ClearAllVariants(bool)`

This will cause serious issues when used in the middle of a run! Use more selective ClearVariants variants to avoid issues.

```csharp
public static int ClearAllVariants(bool repairReferences)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `repairReferences` | `bool` |  |

**Returns:** `int`

:::

::: details `ClearVariantsOfAsset(string, VariantDef?, bool)`

Destroy loaded variants of the specified asset. This will also clear light version of assets if one exists.

```csharp
public static int ClearVariantsOfAsset(string guid, VariantDef? target, bool repairReferences)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `target` | [`VariantDef?`](/api/Global.VariantDef) |  |
| `repairReferences` | `bool` |  |

**Returns:** `int`

:::

::: details `ClearVariantsOfVarDef(VariantDef, bool)`

```csharp
public static int ClearVariantsOfVarDef(VariantDef target, bool repairReferences)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `target` | [`VariantDef`](/api/Global.VariantDef) |  |
| `repairReferences` | `bool` |  |

**Returns:** `int`

:::

::: details `Convert(Object, Type)`

```csharp
public static Object Convert(Object obj, Type type)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `type` | `System.Type` |  |

**Returns:** `UnityEngine.Object`

:::

::: details `Convert&lt;T&gt;(Object)`

```csharp
public static T Convert<T>(Object obj) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `FindAllByNameSubstring(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<Object> FindAllByNameSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><UnityEngine.Object>`

:::

::: details `FindAllByNameSubstring&lt;TFilter&gt;(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<TFilter> FindAllByNameSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><TFilter>`

:::

::: details `FindAllByType(Type, ResourceLoadSettings)`

```csharp
public static IEnumerable<Object> FindAllByType(Type type, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><UnityEngine.Object>`

:::

::: details `FindAllByType&lt;T&gt;(ResourceLoadSettings)`

```csharp
public static IEnumerable<T> FindAllByType<T>(ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T>`

:::

::: details `FindAllByTypeSubstring(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<Object> FindAllByTypeSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><UnityEngine.Object>`

:::

::: details `FindAllByTypeSubstring&lt;TFilter&gt;(string, ResourceLoadSettings)`

```csharp
public static IEnumerable<TFilter> FindAllByTypeSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `System.Collections.Generic.IEnumerable<T><TFilter>`

:::

::: details `FindOneByIdSubstring(string, ResourceLoadSettings)`

```csharp
public static Object FindOneByIdSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `FindOneByIdSubstring&lt;TFilter&gt;(string, ResourceLoadSettings)`

```csharp
public static TFilter FindOneByIdSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `TFilter`

:::

::: details `FindOneByTypeSubstring(string, ResourceLoadSettings)`

```csharp
public static Object FindOneByTypeSubstring(string substring, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `FindOneByTypeSubstring&lt;TFilter&gt;(string, ResourceLoadSettings)`

```csharp
public static TFilter FindOneByTypeSubstring<TFilter>(string substring, ResourceLoadSettings settings = default) where TFilter : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `substring` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `TFilter` |  |

**Returns:** `TFilter`

:::

::: details `FindRoomNameBySubstring(string)`

```csharp
public static string FindRoomNameBySubstring(string name)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |

**Returns:** `string`

:::

::: details `GetAllDependencies(out ListReturnHandle&lt;string&gt;, string)`

```csharp
public static List<string> GetAllDependencies(out ListReturnHandle<string> handle, string objName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `handle` | `ListReturnHandle<string>` |  |
| `objName` | `string` |  |

**Returns:** `System.Collections.Generic.List<T><string>`

:::

::: details `GetByGuid(string, ResourceLoadSettings)`

```csharp
public static Object GetByGuid(string guid, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `GetByGuid&lt;T&gt;(string, ResourceLoadSettings)`

```csharp
public static T GetByGuid<T>(string guid, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetByLinkTypeAndId&lt;T&gt;(ResourceLinkBy, string)`

```csharp
public static T GetByLinkTypeAndId<T>(ResourceLinkBy type, string id) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | [`ResourceLinkBy`](/api/Global.ResourceLinkBy) |  |
| `id` | `string` |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetByName(string, ResourceLoadSettings)`

```csharp
public static Object GetByName(string name, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `GetByName&lt;T&gt;(string, ResourceLoadSettings)`

```csharp
public static T GetByName<T>(string name, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetByShortTypeName(string, ResourceLoadSettings)`

```csharp
public static Object GetByShortTypeName(string name, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `GetByShortTypeName&lt;T&gt;(string, ResourceLoadSettings)`

```csharp
public static T GetByShortTypeName<T>(string name, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetByType(Type, ResourceLoadSettings)`

```csharp
public static Object GetByType(Type type, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `GetByType&lt;T&gt;(ResourceLoadSettings)`

```csharp
public static T GetByType<T>(ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetByType&lt;T&gt;(Type, ResourceLoadSettings)`

```csharp
public static T GetByType<T>(Type type, ResourceLoadSettings settings = default) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `type` | `System.Type` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |
| `` | `T` |  |

**Returns:** `T`

:::

::: details `GetGuidOfAsset(Object)`

```csharp
public static string GetGuidOfAsset(Object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |

**Returns:** `string`

:::

::: details `GetLinkId(Object)`

```csharp
public static string GetLinkId(Object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |

**Returns:** `string`

:::

::: details `GetLinkType(Type)`

```csharp
public static ResourceLinkBy GetLinkType(Type objType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `objType` | `System.Type` |  |

**Returns:** `ResourceLinkBy`

:::

::: details `GetNetworkedPrefab(uint, ResourceLoadSettings)`

```csharp
public static GameObject GetNetworkedPrefab(uint id, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `uint` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `GetNextVariantId()`

```csharp
public static int GetNextVariantId()
```

**Returns:** `int`

:::

::: details `GetSuggestedResourceLoadSettings(Actor, Type)`

```csharp
public static ResourceLoadSettings GetSuggestedResourceLoadSettings(Actor parentActor, Type childType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parentActor` | [`Actor`](/api/Global.Actor) |  |
| `childType` | `System.Type` |  |

**Returns:** `ResourceLoadSettings`

:::

::: details `GetSuggestedVarDef(Actor, Type)`

```csharp
public static VariantDef GetSuggestedVarDef(Actor parentActor, Type childType)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parentActor` | [`Actor`](/api/Global.Actor) |  |
| `childType` | `System.Type` |  |

**Returns:** `VariantDef`

:::

::: details `GetVariantIdForSkin(string)`

```csharp
public static int GetVariantIdForSkin(string skinName)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `skinName` | `string` |  |

**Returns:** `int`

:::

::: details `Load(string, ResourceLoadSettings)`

```csharp
public static Object Load(string guid, ResourceLoadSettings settings = default)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |
| `settings` | [`ResourceLoadSettings`](/api/Global.ResourceLoadSettings) |  |

**Returns:** `UnityEngine.Object`

:::

::: details `Preload(string)`

```csharp
public static void Preload(string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `guid` | `string` |  |

:::

::: details `RegisterVariantProcessor(int, ResourceVariantProcessor)`

```csharp
public static void RegisterVariantProcessor(int id, ResourceVariantProcessor processor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` |  |
| `processor` | [`ResourceVariantProcessor`](/api/Global.ResourceVariantProcessor) |  |

:::

::: details `RepairMissingReferences_Prepare()`

```csharp
public static void RepairMissingReferences_Prepare()
```

:::

::: details `RepairMissingReferences_Repair()`

```csharp
public static void RepairMissingReferences_Repair()
```

:::

::: details `TryConvert(Object, Type, out Object)`

```csharp
public static bool TryConvert(Object obj, Type type, out Object result)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `type` | `System.Type` |  |
| `result` | `UnityEngine.Object` |  |

**Returns:** `bool`

:::

::: details `TryConvert&lt;T&gt;(Object, out T)`

```csharp
public static bool TryConvert<T>(Object obj, out T result) where T : Object
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `result` | `T` |  |
| `` | `T` |  |

**Returns:** `bool`

:::

::: details `TryGetGuidOfAsset(Object, out string)`

```csharp
public static bool TryGetGuidOfAsset(Object obj, out string guid)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `UnityEngine.Object` |  |
| `guid` | `string` |  |

**Returns:** `bool`

:::

::: details `UnloadUnused()`

```csharp
public static void UnloadUnused()
```

:::

::: details `UnregisterVariantProcessor(int)`

```csharp
public static void UnregisterVariantProcessor(int id)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `id` | `int` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (171)

*Classes and systems that invoke, reference, or depend on `DewResources`:*

[Actor](/api/Global.Actor) · [ActorManager](/api/Global.ActorManager) · `Ai_Hatred_Curse` · `Ai_Hatred_InkMapCurse` · `Ai_Mon_Sky_BossNyx_Atk` · `Ai_Mon_Special_BossPolaris_Holy_Purgatory_Spawner` · `Ai_RandomGemUpgrade` · `Ai_Star_Cetus_F_BI_SelfDamageAoeCold_AOE` · `AssetRefTypeResolver` · [AssetRef`1](/api/Global.AssetRef`1) · [CharacterModelDisplay](/api/Global.CharacterModelDisplay) · [ChatManager](/api/Global.ChatManager) · [DevGameManager](/api/Global.DevGameManager) · [Dew](/api/Global.Dew) · `DewConsoleCommands` · [DewEffect](/api/Global.DewEffect) · `DewItem` · [DewMod](/api/Global.DewMod) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewPersistence](/api/Global.DewPersistence) · [DewPlayer](/api/Global.DewPlayer) · [DewProfile](/api/Global.DewProfile) · `DewProfileMerge` · [DewProfileStats](/api/Global.DewProfileStats) · [DewSave](/api/Global.DewSave) · [EntityVisual](/api/Global.EntityVisual) · [GameManager](/api/Global.GameManager) · [GameMod_Limbo](/api/Global.GameMod_Limbo) · [GameMod_MirageSkin](/api/Global.GameMod_MirageSkin) · [GameSettingsManager](/api/Global.GameSettingsManager) · [Hero](/api/Global.Hero) · [HeroLoadoutData](/api/Global.HeroLoadoutData) · [LootManager](/api/Global.LootManager) · `LucidDream_MarshOfDestiny` · `LucidDream_WILD` · `Mon_DarkCave_BossSeeker` · `Mon_DarkCave_CaveSpider` · `Mon_Despair_BossAzurak` · [Mon_DreamTeller](/api/Global.Mon_DreamTeller) · `Mon_Forest_SpiderWarrior` · `Mon_Ink_BossDarkMoon` · `Mon_Ink_BossWhiteNight` · `Mon_LavaLand_BossInfernus` · `Mon_Sky_BossNyx` · `Mon_SnowMountain_SnowWolf` · `Mon_Special_BossErebos` · `Mon_Special_BossLightElemental` · `Mon_Special_BossObliviax` · `MonsterAbilityPrewarmConfig` · [MonsterPool](/api/Global.MonsterPool) · [MusicManager](/api/Global.MusicManager) · `NextZoneOverrideTreasure` · [PingManager](/api/Global.PingManager) · [PlayGameManager](/api/Global.PlayGameManager) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · `PlayTutorialManager` · [PreloadInterface](/api/Global.PreloadInterface) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · [PropEnt_Merchant_Jonas](/api/Global.PropEnt_Merchant_Jonas) · [PropEnt_Merchant_Smoothie](/api/Global.PropEnt_Merchant_Smoothie) · `PropEnt_Stone_PitchBlackOre` · [QuestManager](/api/Global.QuestManager) · [Rift_Sidetrack](/api/Global.Rift_Sidetrack) · `Rift_Sidetrack_TheDream` · `RoomMod_Ambush` · `RoomMod_LeafPuppies` · `RoomMod_MeteoricLife` · `RoomMod_UnstableRatSwarm` · [RoomModifierBase](/api/Global.RoomModifierBase) · [RoomModifiers](/api/Global.RoomModifiers) · [RoomMonsters](/api/Global.RoomMonsters) · [RoomRifts](/api/Global.RoomRifts) · `Se_MirageSkin_Oblivion` · `Se_MirageSkin_Pulverization` · `Se_Star_Bismuth_I_KnowledgeBook` · `Se_Star_Cetus_I_ColdDiscountFireSurcharge` · `Se_Star_I_DismantleReroll` · `Shrine_Ascension` · `Shrine_BossSoul` · `Shrine_CallOfTheRavenous` · `Shrine_Destiny` · `Shrine_FallenStar` · `Shrine_Hatred` · `Shrine_Luck` · `Shrine_MarshOfDestiny_SeedOfTorment` · [SkillTrigger](/api/Global.SkillTrigger) · [SpawnManager](/api/Global.SpawnManager) · [SpecialEntityRoomModifier](/api/Global.SpecialEntityRoomModifier) · `St_Q_GoldenBurst` · `St_Q_Laceration` · `St_Q_Reduction` · [SyncableAssetRef](/api/Global.SyncableAssetRef) · `TestMapGameManager` · [TitleManager](/api/Global.TitleManager) · `TravelerStoryPresenter` · [TriggerConfig](/api/Global.TriggerConfig) · `UI_AccList` · `UI_AccList_Item` · `UI_AccList_PreviewWindow` · `UI_Achievement_Icon` · `UI_Collectables_MainView` · `UI_Common_ChatBox_Item` · `UI_Common_MenuView` · `UI_DifficultyIcon` · `UI_EmoteList` · `UI_EmoteList_Item` · `UI_HeroIcon` · `UI_InGame_AchievementNotifications` · `UI_InGame_ArtifactStoryView` · `UI_InGame_CurrentArtifact` · `UI_InGame_EmoteCanvas` · `UI_InGame_FloatingWindow_ChoiceShrine_Item` · `UI_InGame_FloatingWindow_CorruptedChaos_Item` · `UI_InGame_FloatingWindow_Shop_Item` · `UI_InGame_PartyDisplay_Item` · `UI_InGame_ResultView` · `UI_InGame_Result_Difficulty` · `UI_InGame_Result_HeroGemItem` · `UI_InGame_World_NodeItem` · `UI_ItemIcon` · `UI_LimboDepthIcon` · `UI_Lobby_AccList` · `UI_Lobby_Constellations_AlphaStar` · `UI_Lobby_Constellations_HeroConstellationBase` · `UI_Lobby_Constellations_HeroConstellation_StarSlot` · `UI_Lobby_Constellations_MiniAlphaStar` · `UI_Lobby_Constellations_Skills_Slot` · `UI_Lobby_Constellations_StarCount` · `UI_Lobby_Constellations_StarDetails` · `UI_Lobby_Constellations_StarItem` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_Constellations_TitleAndEmblem` · `UI_Lobby_DejavuButton` · `UI_Lobby_DejavuWindow` · `UI_Lobby_EmoteCanvas` · `UI_Lobby_HeroList` · `UI_Lobby_HeroList_Item` · `UI_Lobby_Loadout_ComponentBase` · `UI_Lobby_LucidDreamsWindow` · `UI_Lobby_ObliterationView_Item` · `UI_Lobby_Obliteration_BannedItems` · `UI_Lobby_Obliteration_BannedItems_Item` · `UI_Lobby_PlayerNametag` · `UI_Lobby_SelectedHeroInfo_Base` · `UI_Lobby_SelectedHeroInfo_StarDecoration` · `UI_Lobby_SkinList_Item` · `UI_LucidDreamIcon` · `UI_NametagList` · `UI_NametagList_Item` · `UI_NametagList_PreviewWindow` · `UI_ProfileStatistics_Item_FavouriteTraveler` · `UI_SkinList` · `UI_SkinList_Item` · `UI_SkinList_PreviewWindow` · `UI_StarIcon` · [UI_StationaryEmote](/api/Global.UI_StationaryEmote) · `UI_Title_FindLobby_LobbyItem` · `UI_TooltipManager` · `UI_Tooltip_CollectableTargetName` · `UI_Tooltip_EquippedGemDescriber_Item` · `UI_Tooltip_GemDescription` · `UI_Tooltip_GemTitle` · `UI_Tooltip_ObjIcon` · `UI_Tooltip_SkillStarDescriber` · `UI_Tooltip_WorldNode_Modifiers` · `UI_TravelerHeroTitle` · `UI_TravelerStory` · `UI_TravelerStory_ColorizeByHeroColor` · `UI_TravelerStory_HeroConstellation` · [WorldNodeData](/api/Global.WorldNodeData) · [ZoneManager](/api/Global.ZoneManager)

### Dependencies (19)

*Types and components that `DewResources` references or depends upon:*

`DewInternal.DewResourceDatabase` · [Actor](/api/Global.Actor) · [Dew](/api/Global.Dew) · [DewEffect](/api/Global.DewEffect) · [DewPool](/api/Global.DewPool) · [FxCameraShake](/api/Global.FxCameraShake) · `GetComponentsNonAllocExtension` · `GraphicsManager` · [ILinkedByGuid](/api/Global.ILinkedByGuid) · [IOtherPlayersTonedDownLimit](/api/Global.IOtherPlayersTonedDownLimit) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [PreloadInterface](/api/Global.PreloadInterface) · [ResourceLoadSettings](/api/Global.ResourceLoadSettings) · [ResourceVariantProcessor](/api/Global.ResourceVariantProcessor) · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1) · `ToListNonAllocExtensions` · [VariantDef](/api/Global.VariantDef)

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

[`ResourceLinkBy`](/enums#resourcelinkby)

:::
