# Class: DewEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewEffect
```

## Fields (2)

::: details Click to expand Fields (2)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disablePlay`** | `public static bool disablePlay` |  |
| **`disablePlayNew`** | `public static bool disablePlayNew` |  |

:::

## Methods (28)

::: details `ApplySpeedMultiplier(GameObject, float)`

```csharp
public static void ApplySpeedMultiplier(GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

:::

::: details `ApplySpeedMultiplierNetworked(NetworkIdentity, GameObject, float)`

```csharp
public static void ApplySpeedMultiplierNetworked(NetworkIdentity parent, GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

:::

::: details `ChangeColorObject(object, float?, float, float, float)`

```csharp
public static void ChangeColorObject(object obj, float? hue = null, float saturationMult = 1, float valueMult = 1, float alphaMult = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |
| `hue` | `float?` |  |
| `saturationMult` | `float` |  |
| `valueMult` | `float` |  |
| `alphaMult` | `float` |  |

:::

::: details `ChangeColorRecursively(GameObject, float?, float, float, float)`

```csharp
public static void ChangeColorRecursively(GameObject gameObject, float? hue = null, float saturationMult = 1, float valueMult = 1, float alphaMult = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |
| `hue` | `float?` |  |
| `saturationMult` | `float` |  |
| `valueMult` | `float` |  |
| `alphaMult` | `float` |  |

:::

::: details `GetPath(Transform, Transform)`

```csharp
public static string GetPath(Transform root, Transform target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `root` | `UnityEngine.Transform` |  |
| `target` | `UnityEngine.Transform` |  |

**Returns:** `string`

:::

::: details `Play(GameObject, Entity, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void Play(GameObject effect, Entity attach, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `Play(GameObject, Entity, Vector3, Quaternion?, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void Play(GameObject effect, Entity attach, Vector3 position, Quaternion? rotation, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `Play(GameObject, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void Play(GameObject effect, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `Play(GameObject, Vector3, Quaternion?, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void Play(GameObject effect, Vector3 position, Quaternion? rotation, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `PlayCastEffect(GameObject, CastInfo, CastMethodType, float, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void PlayCastEffect(GameObject effect, CastInfo info, CastMethodType method, float duration = -1, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `method` | [`CastMethodType`](/api/Global.CastMethodType) |  |
| `duration` | `float` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `PlayCastEffectNetworked(NetworkIdentity, GameObject, CastInfo, CastMethodType, float)`

```csharp
public static void PlayCastEffectNetworked(NetworkIdentity parent, GameObject effect, CastInfo info, CastMethodType method, float duration = -1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `info` | [`CastInfo`](/api/Global.CastInfo) |  |
| `method` | [`CastMethodType`](/api/Global.CastMethodType) |  |
| `duration` | `float` |  |

:::

::: details `PlayNetworked(NetworkIdentity, GameObject, Entity, Vector3, Quaternion?)`

```csharp
public static void PlayNetworked(NetworkIdentity parent, GameObject effect, Entity entity, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `PlayNetworked(NetworkIdentity, GameObject, Entity)`

```csharp
public static void PlayNetworked(NetworkIdentity parent, GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `PlayNetworked(NetworkIdentity, GameObject, Vector3, Quaternion?)`

```csharp
public static void PlayNetworked(NetworkIdentity parent, GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `PlayNetworked(NetworkIdentity, GameObject)`

```csharp
public static void PlayNetworked(NetworkIdentity parent, GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `PlayNew(GameObject, Entity, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void PlayNew(GameObject effect, Entity attach, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `PlayNew(GameObject, Entity, Vector3, Quaternion?, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void PlayNew(GameObject effect, Entity attach, Vector3 position, Quaternion? rotation, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `PlayNew(GameObject, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void PlayNew(GameObject effect, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `PlayNew(GameObject, Vector3, Quaternion?, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void PlayNew(GameObject effect, Vector3 position, Quaternion? rotation, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

:::

::: details `PlayNewNetworked(NetworkIdentity, GameObject, Entity, Vector3, Quaternion?)`

```csharp
public static void PlayNewNetworked(NetworkIdentity parent, GameObject effect, Entity entity, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `PlayNewNetworked(NetworkIdentity, GameObject, Entity)`

```csharp
public static void PlayNewNetworked(NetworkIdentity parent, GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `PlayNewNetworked(NetworkIdentity, GameObject, Vector3, Quaternion?)`

```csharp
public static void PlayNewNetworked(NetworkIdentity parent, GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

:::

::: details `PlayNewNetworked(NetworkIdentity, GameObject)`

```csharp
public static void PlayNewNetworked(NetworkIdentity parent, GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `ResolvePath(Transform, string, bool)`

```csharp
public static GameObject ResolvePath(Transform root, string path, bool warnOnFail = true)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `root` | `UnityEngine.Transform` |  |
| `path` | `string` |  |
| `warnOnFail` | `bool` |  |

**Returns:** `UnityEngine.GameObject`

:::

::: details `Stop(GameObject)`

```csharp
public static void Stop(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `StopNetworked(NetworkIdentity, GameObject)`

```csharp
public static void StopNetworked(NetworkIdentity parent, GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |

:::

::: details `TintObject(object, Color, bool)`

Tint color of the object. (Multiply given color to its color)

```csharp
public static void TintObject(object obj, Color color, bool dontLogWarning = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |
| `color` | `UnityEngine.Color` |  |
| `dontLogWarning` | `bool` |  |

:::

::: details `TintRecursively(GameObject, Color)`

```csharp
public static void TintRecursively(GameObject gameObject, Color color)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |
| `color` | `UnityEngine.Color` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (76)

*Classes and systems that invoke, reference, or depend on `DewEffect`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · [Actor](/api/Global.Actor) · `Ai_Atk_HuskSword` · `Ai_Atk_HuskSword_Crit` · `Ai_Mon_Ink_BossWhiteNight_AltAtk_Ready` · `Ai_Mon_Primus_BossPrimusAeron_Adaptation_Orb` · `Ai_Mon_Special_BossPolaris_Holy_CounterSpell_SkillProjectile` · `Ai_QR_Innocence_Explosion` · `Ai_QR_Innocence_Projectile` · `Ai_Q_CruelSun` · `Ai_Q_CruelSun_Shockwave` · [ArtifactWorldModel](/api/Global.ArtifactWorldModel) · [CameraManager](/api/Global.CameraManager) · [CharacterModelDisplay](/api/Global.CharacterModelDisplay) · [ChargingChannel](/api/Global.ChargingChannel) · [DamageInstance](/api/Global.DamageInstance) · [DewBeamRenderer](/api/Global.DewBeamRenderer) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewNetworkManager](/api/Global.DewNetworkManager) · [DewResources](/api/Global.DewResources) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · [Emote](/api/Global.Emote) · [EntitySound](/api/Global.EntitySound) · [EntityVisual](/api/Global.EntityVisual) · `Extras_CharacterPoser` · [FeedbackManager](/api/Global.FeedbackManager) · [FlavourManager](/api/Global.FlavourManager) · [FocusedLobbyCharacterEffect](/api/Global.FocusedLobbyCharacterEffect) · `Forest_DayNight_Effect` · [FxEffect](/api/Global.FxEffect) · [FxNetworkedEffect](/api/Global.FxNetworkedEffect) · [FxRepeatedEffect](/api/Global.FxRepeatedEffect) · `GameCover_Animator` · `Ge_Obliviax_InterruptTravelAndKidnap` · [GlobalUIManager](/api/Global.GlobalUIManager) · `ItemWorldModel` · [LobbyUIManager](/api/Global.LobbyUIManager) · [PingInstance](/api/Global.PingInstance) · [PlayLobbyManager](/api/Global.PlayLobbyManager) · [PlayLobby_Character](/api/Global.PlayLobby_Character) · `PlayTutorial_Tutorial_Hunt` · `PlayTutorial_Tutorial_Intro` · `Primus_PureWhiteOpenEffect` · [Projectile](/api/Global.Projectile) · [RoomMonsters](/api/Global.RoomMonsters) · `Se_Q_CruelSun_Armored` · `Shrine_BossSoul` · `Shrine_Chaos` · `Shrine_Destiny` · `Shrine_HeroSoul` · [SkillVisualOverrideItem](/api/Global.SkillVisualOverrideItem) · `Sky_NightWaterEffect` · [SpawnManager](/api/Global.SpawnManager) · [TransitionManager](/api/Global.TransitionManager) · `UI_ButtonEffect` · `UI_Constellations` · `UI_Constellations_CategoryGroup` · [UI_EmoteWheel](/api/Global.UI_EmoteWheel) · `UI_GamepadShoulderControls` · `UI_InGame_CurrentArtifact` · `UI_InGame_FloatingWindow_Base` · `UI_Lobby_AccList` · `UI_Lobby_Constellations` · `UI_Lobby_Constellations_StarList` · `UI_Lobby_ExpandableStory` · `UI_Lobby_ReverieButton` · `UI_Reveries_SlotBase` · `UI_Reveries_SpecialSlot` · `UI_Title_LizardSmoothie` · `UI_Title_SplashView` · `UI_TravelerStory` · `UI_TravelerStory_ColorizeByHeroColor` · `UI_TravelerStory_Details_Story` · `UI_TravelerStory_IllustrationPopup` · `UI_TravelerStory_StoryViewer` · [View](/api/Global.View)

### Dependencies (29)

*Types and components that `DewEffect` references or depends upon:*

[Actor](/api/Global.Actor) · [CameraManager](/api/Global.CameraManager) · [CastInfo](/api/Global.CastInfo) · [DewPlayer](/api/Global.DewPlayer) · [DewPool](/api/Global.DewPool) · [DewResources](/api/Global.DewResources) · [EffectAutoDestroy](/api/Global.EffectAutoDestroy) · [Entity](/api/Global.Entity) · [EntityCheck](/api/Global.EntityCheck) · [FxCastTelegraph](/api/Global.FxCastTelegraph) · [FxInterpolatedEffectBase](/api/Global.FxInterpolatedEffectBase) · `FxParticleSystemCacheData` · `FxPlayPlan` · [FxSelectiveQuality](/api/Global.FxSelectiveQuality) · [FxSelectiveVisibility](/api/Global.FxSelectiveVisibility) · [GameSettingsManager](/api/Global.GameSettingsManager) · `GetComponentsNonAllocExtension` · `GraphicsManager` · [IAttachableToEntity](/api/Global.IAttachableToEntity) · [IEffectComponent](/api/Global.IEffectComponent) · [IEffectSetupComponent](/api/Global.IEffectSetupComponent) · [IEffectWithOwnerContext](/api/Global.IEffectWithOwnerContext) · [IEffectWithSpeed](/api/Global.IEffectWithSpeed) · [ListReturnHandle`1](/api/Global.ListReturnHandle`1) · [ManagerBase`1](/api/Global.ManagerBase`1) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · `ParticleSystemExtensions` · [SafeAction](/api/Global.SafeAction) · [SafeAction`1](/api/Global.SafeAction`1)

### Related Enums (2)

*Enumerations referenced in fields, properties, or method signatures:*

[`CastMethodType`](/enums#castmethodtype) · [`Quality3Levels`](/enums#quality3levels)

:::
