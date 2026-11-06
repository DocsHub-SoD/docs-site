# Class: DewEffect

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public static class DewEffect
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`disablePlay`** | `public static bool disablePlay` |  |
| **`disablePlayNew`** | `public static bool disablePlayNew` |  |

## Methods

### `ApplySpeedMultiplier(GameObject, float)`

```csharp
public static void ApplySpeedMultiplier(GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

### `ApplySpeedMultiplierNetworked(NetworkIdentity, GameObject, float)`

```csharp
public static void ApplySpeedMultiplierNetworked(NetworkIdentity parent, GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

### `ChangeColorObject(object, float?, float, float, float)`

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

### `ChangeColorRecursively(GameObject, float?, float, float, float)`

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

### `GetPath(Transform, Transform)`

```csharp
public static string GetPath(Transform root, Transform target)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `root` | `UnityEngine.Transform` |  |
| `target` | `UnityEngine.Transform` |  |

**Returns:** `string`

### `Play(GameObject, Entity, NetworkIdentity)`

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

### `Play(GameObject, Entity, Vector3, Quaternion?, NetworkIdentity)`

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

### `Play(GameObject, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void Play(GameObject effect, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

### `Play(GameObject, Vector3, Quaternion?, NetworkIdentity)`

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

### `PlayCastEffect(GameObject, CastInfo, CastMethodType, float, NetworkIdentity)`

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

### `PlayCastEffectNetworked(NetworkIdentity, GameObject, CastInfo, CastMethodType, float)`

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

### `PlayNetworked(NetworkIdentity, GameObject, Entity, Vector3, Quaternion?)`

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

### `PlayNetworked(NetworkIdentity, GameObject, Entity)`

```csharp
public static void PlayNetworked(NetworkIdentity parent, GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

### `PlayNetworked(NetworkIdentity, GameObject, Vector3, Quaternion?)`

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

### `PlayNetworked(NetworkIdentity, GameObject)`

```csharp
public static void PlayNetworked(NetworkIdentity parent, GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |

### `PlayNew(GameObject, Entity, NetworkIdentity)`

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

### `PlayNew(GameObject, Entity, Vector3, Quaternion?, NetworkIdentity)`

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

### `PlayNew(GameObject, NetworkIdentity)`

Provide parent if the effect originates from an entity and needs GameBoss/GameSelf/GameOthers clarifications.

```csharp
public static void PlayNew(GameObject effect, NetworkIdentity parent = null)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `parent` | `Mirror.NetworkIdentity` |  |

### `PlayNew(GameObject, Vector3, Quaternion?, NetworkIdentity)`

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

### `PlayNewNetworked(NetworkIdentity, GameObject, Entity, Vector3, Quaternion?)`

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

### `PlayNewNetworked(NetworkIdentity, GameObject, Entity)`

```csharp
public static void PlayNewNetworked(NetworkIdentity parent, GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [`Entity`](/api/Global.Entity) |  |

### `PlayNewNetworked(NetworkIdentity, GameObject, Vector3, Quaternion?)`

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

### `PlayNewNetworked(NetworkIdentity, GameObject)`

```csharp
public static void PlayNewNetworked(NetworkIdentity parent, GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |

### `ResolvePath(Transform, string, bool)`

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

### `Stop(GameObject)`

```csharp
public static void Stop(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `StopNetworked(NetworkIdentity, GameObject)`

```csharp
public static void StopNetworked(NetworkIdentity parent, GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `parent` | `Mirror.NetworkIdentity` |  |
| `effect` | `UnityEngine.GameObject` |  |

### `TintObject(object, Color, bool)`

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

### `TintRecursively(GameObject, Color)`

```csharp
public static void TintRecursively(GameObject gameObject, Color color)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `gameObject` | `UnityEngine.GameObject` |  |
| `color` | `UnityEngine.Color` |  |
