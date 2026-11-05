# Class: EntityVisual

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [EntityComponent](/api/Global.EntityComponent)

```csharp
[HideMonoScript]
[RequireComponent(typeof(EntityHighlightProvider))]
[LogicUpdatePriority(-299)]
public class EntityVisual : EntityComponent, ILogicUpdate, ICleanup
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`accessoryInstances`** | `[NonSerialized]
public List&lt;Accessory&gt; accessoryInstances` |  |
| **`ClientEvent_OnGroundMarkerHiddenChanged`** | `public SafeAction&lt;bool&gt; ClientEvent_OnGroundMarkerHiddenChanged` |  |
| **`ClientEvent_OnModelLoaded`** | `public SafeAction ClientEvent_OnModelLoaded` |  |
| **`ClientEvent_OnRendererEnabledChanged`** | `public SafeAction&lt;bool&gt; ClientEvent_OnRendererEnabledChanged` |  |
| **`ClientEvent_OnSpawnComplete`** | `public SafeAction ClientEvent_OnSpawnComplete` | Called when the entity finishes spawning or spawning is skipped. |
| **`dazeAfterSpawnDuration`** | `public float dazeAfterSpawnDuration` |  |
| **`delayLoopEffectTilSpawned`** | `[LabelText("Delay Loop Effect Until Spawned")]
[FormerlySerializedAs("delayStartEffectTilSpawned")]
[ToggleLeft]
public bool delayLoopEffectTilSpawned` |  |
| **`delaySpawnEffectOnGroundTilSpawned`** | `[LabelText("Delay Until Spawned")]
[ShowIf("@spawnEffectOnGround != null", true)]
public bool delaySpawnEffectOnGroundTilSpawned` |  |
| **`delaySpawnEffectUntilSpawned`** | `[LabelText("Delay Until Spawned")]
[ShowIf("@spawnEffect != null", true)]
public bool delaySpawnEffectUntilSpawned` |  |
| **`disableModelTransformUpdate`** | `[NonSerialized]
public bool disableModelTransformUpdate` |  |
| **`doPositionOffset`** | `public bool doPositionOffset` |  |
| **`doScaling`** | `public bool doScaling` |  |
| **`invisibleByDefault`** | `[NonSerialized]
public bool invisibleByDefault` | Set this true on before spawn to make entities invisible by default, appearing after EnableRenderers is called. |
| **`invulnerableWhileSpawning`** | `public bool invulnerableWhileSpawning` |  |
| **`mirageSkinObjects`** | `public Dictionary&lt;string, List&lt;GameObject&gt;&gt; mirageSkinObjects` |  |
| **`model`** | `[NonSerialized]
public EntityModel model` |  |
| **`modelTransform`** | `[NonSerialized]
public Transform modelTransform` |  |
| **`renderers`** | `[NonSerialized]
public List&lt;Renderer&gt; renderers` |  |
| **`skipSpawning`** | `[NonSerialized]
public bool skipSpawning` | Set this true on before spawn to make entities pop in instead of play its spawning effects, voices and animations. |
| **`solidRenderers`** | `[NonSerialized]
public List&lt;Renderer&gt; solidRenderers` |  |
| **`spawnAnim`** | `public DewAnimationClip spawnAnim` |  |
| **`spawnDuration`** | `[Title("Spawn", null, TitleAlignments.Left, true, true)]
public float spawnDuration` |  |
| **`spawnEffect`** | `[Title("Effects", null, TitleAlignments.Left, true, true)]
public GameObject spawnEffect` |  |
| **`spawnEffectOnGround`** | `public GameObject spawnEffectOnGround` |  |
| **`spawnXOffset`** | `[ShowIf("doPositionOffset", true)]
public AnimationCurve spawnXOffset` |  |
| **`spawnXScale`** | `[ShowIf("doScaling", true)]
[LabelText("@useSeparateAxis ? \"Spawn X Scale\" : \"Spawn Scale\"")]
public AnimationCurve spawnXScale` |  |
| **`spawnYOffset`** | `[ShowIf("doPositionOffset", true)]
public AnimationCurve spawnYOffset` |  |
| **`spawnYScale`** | `[ShowIf("@doScaling && useSeparateAxis", true)]
public AnimationCurve spawnYScale` |  |
| **`spawnZOffset`** | `[ShowIf("doPositionOffset", true)]
public AnimationCurve spawnZOffset` |  |
| **`spawnZScale`** | `[ShowIf("@doScaling && useSeparateAxis", true)]
public AnimationCurve spawnZScale` |  |
| **`useSeparateAxis`** | `[ShowIf("doScaling", true)]
public bool useSeparateAxis` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`currentYOffset`** | `public float currentYOffset { get; }` |  |
| **`currentYVelocity`** | `public float currentYVelocity { get; }` |  |
| **`etLocalOffset`** | `public Vector3 etLocalOffset { get; }` |  |
| **`etRotation`** | `public Quaternion etRotation { get; }` |  |
| **`etScaleMultiplier`** | `public Vector3 etScaleMultiplier { get; }` |  |
| **`etWorldOffset`** | `public Vector3 etWorldOffset { get; }` |  |
| **`genericStackIndicatorMax`** | `public int genericStackIndicatorMax { get; set; }` |  |
| **`genericStackIndicatorValue`** | `public int genericStackIndicatorValue { get; set; }` |  |
| **`highlight`** | `public EntityHighlightProvider highlight { get; }` |  |
| **`isGroundMarkerHidden`** | `public bool isGroundMarkerHidden { get; }` |  |
| **`isRendererOff`** | `public bool isRendererOff { get; }` |  |
| **`isSpawning`** | `public bool isSpawning { get; }` |  |
| **`materials`** | `public IReadOnlyList&lt;Material&gt; materials { get; }` | List of this entity's materials. (Instantiated) |

## Methods

### `AddSharedMaterialLocal(Material)`

Locally add a material to all mesh renderers of this entity.

```csharp
public void AddSharedMaterialLocal(Material material)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `material` | `UnityEngine.Material` |  |

### `Awake()`

```csharp
protected override void Awake()
```

### `DisableRenderers()`

Make this entity invisible by turning off all renderers everywhere.

```csharp
public void DisableRenderers()
```

### `DisableRenderersLocal()`

Locally make this entity invisible by turning off all renderers.

```csharp
public void DisableRenderersLocal()
```

### `EnableRenderers()`

Undo this entity'sDisableRenderers()and make it visible again everywhere.

```csharp
public void EnableRenderers()
```

### `EnableRenderersLocal()`

Locally undo this entity'sDisableRenderers()and make it visible again.

```csharp
public void EnableRenderersLocal()
```

### `FixClothes()`

```csharp
public void FixClothes()
```

### `FixTails()`

```csharp
public void FixTails()
```

### `FixTailsAndClothes()`

Reset tails and clothes.

```csharp
public void FixTailsAndClothes()
```

### `FrameUpdate()`

```csharp
public override void FrameUpdate()
```

### `GetAbovePosition()`

```csharp
public Vector3 GetAbovePosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetBasePosition()`

```csharp
public Vector3 GetBasePosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetBodyBounds()`

Get bounds of renderers specified as "body" of this entity.

```csharp
public Bounds GetBodyBounds()
```

**Returns:** `UnityEngine.Bounds`

### `GetBonePosition(HumanBodyBones)`

This will return center position if the bone couldn't be found.

```csharp
public Vector3 GetBonePosition(HumanBodyBones bone)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bone` | `UnityEngine.HumanBodyBones` |  |

**Returns:** `UnityEngine.Vector3`

### `GetBoneRotation(HumanBodyBones)`

This will return entity's rotation if the bone couldn't be found.

```csharp
public Quaternion GetBoneRotation(HumanBodyBones bone)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `bone` | `UnityEngine.HumanBodyBones` |  |

**Returns:** `UnityEngine.Quaternion`

### `GetCenterPosition()`

```csharp
public Vector3 GetCenterPosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetMuzzlePosition()`

```csharp
public Vector3 GetMuzzlePosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetMuzzleRotation()`

```csharp
public Quaternion GetMuzzleRotation()
```

**Returns:** `UnityEngine.Quaternion`

### `GetNewColorModifier()`

Gets a new color modifier for this entity. The color is applied locally.

```csharp
public EntityColorModifier GetNewColorModifier()
```

**Returns:** `EntityColorModifier`

### `GetNewShellModifier()`

Gets a new color modifier for this entity. The color is applied locally.

```csharp
public EntityShellModifier GetNewShellModifier()
```

**Returns:** `EntityShellModifier`

### `GetNewTransformModifier()`

Gets a new transform modifier for this entity. The transform is applied locally to its model.

```csharp
public EntityTransformModifier GetNewTransformModifier()
```

**Returns:** `EntityTransformModifier`

### `GetRenderBounds()`

Get bounds of all solid renderers.

```csharp
public Bounds GetRenderBounds()
```

**Returns:** `UnityEngine.Bounds`

### `GetWeaponPosition()`

```csharp
public Vector3 GetWeaponPosition()
```

**Returns:** `UnityEngine.Vector3`

### `GetWeaponRotation()`

```csharp
public Quaternion GetWeaponRotation()
```

**Returns:** `UnityEngine.Quaternion`

### `HideGroundMarker()`

```csharp
public void HideGroundMarker()
```

### `HideGroundMarkerLocal()`

```csharp
public void HideGroundMarkerLocal()
```

### `KnockUp(KnockUpStrength, bool)`

Knock up this entity everywhere.

```csharp
public void KnockUp(KnockUpStrength strength, bool isFriendly)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | [KnockUpStrength](/api/Global.KnockUpStrength) |  |
| `isFriendly` | `bool` |  |

### `KnockUp(float, bool)`

Knock up this entity everywhere. Strength: 0.8(Small), 1.1(Normal), 1.5(Big)

```csharp
public void KnockUp(float strength, bool isFriendly)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `strength` | `float` |  |
| `isFriendly` | `bool` |  |

### `LoadModelDefault()`

```csharp
public void LoadModelDefault()
```

### `LoadModelDefaultLocal()`

```csharp
public void LoadModelDefaultLocal()
```

### `LoadModelLocal(EntityModel)`

Locally change model of this entity. You can provide either a model in a prefab, or the default one in the spawned entity.The provided model must be fresh; it must never be the already initialized instance of EntityModel.

```csharp
public void LoadModelLocal(EntityModel m)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `m` | [EntityModel](/api/Global.EntityModel) |  |

### `LogicUpdate(float)`

```csharp
public override void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `OnLateStartServer()`

```csharp
public override void OnLateStartServer()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `OnStartClient()`

```csharp
public override void OnStartClient()
```

### `OnStartServer()`

```csharp
public override void OnStartServer()
```

### `OnStop()`

```csharp
public override void OnStop()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```

### `RemoveMaterialLocal(Material)`

Locally remove a material from all mesh renderers of this entity.

```csharp
public void RemoveMaterialLocal(Material material)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `material` | `UnityEngine.Material` |  |

### `SetShaderProperty(string, float)`

```csharp
public void SetShaderProperty(string key, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `float` |  |

### `SetShaderProperty(string, Color)`

```csharp
public void SetShaderProperty(string key, Color value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `UnityEngine.Color` |  |

### `SetShaderPropertyLocal(int, float)`

```csharp
public void SetShaderPropertyLocal(int propertyId, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `propertyId` | `int` |  |
| `value` | `float` |  |

### `SetShaderPropertyLocal(int, Color)`

```csharp
public void SetShaderPropertyLocal(int propertyId, Color value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `propertyId` | `int` |  |
| `value` | `UnityEngine.Color` |  |

### `SetShaderPropertyLocal(string, float)`

```csharp
public void SetShaderPropertyLocal(string key, float value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `float` |  |

### `SetShaderPropertyLocal(string, Color)`

```csharp
public void SetShaderPropertyLocal(string key, Color value)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `key` | `string` |  |
| `value` | `UnityEngine.Color` |  |

### `SetYOffset(float)`

```csharp
public void SetYOffset(float offset)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `offset` | `float` |  |

### `SetYOffsetLocal(float)`

```csharp
public void SetYOffsetLocal(float offset)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `offset` | `float` |  |

### `SetYVelocity(float)`

```csharp
public void SetYVelocity(float velocity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `velocity` | `float` |  |

### `SetYVelocityLocal(float)`

```csharp
public void SetYVelocityLocal(float velocity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `velocity` | `float` |  |

### `ShowGroundMarker()`

```csharp
public void ShowGroundMarker()
```

### `ShowGroundMarkerLocal()`

```csharp
public void ShowGroundMarkerLocal()
```

### `SkipSpawning()`

Cancels ongoing spawn animation of this entity.

```csharp
public void SkipSpawning()
```
