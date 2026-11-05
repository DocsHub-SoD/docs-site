# Class: DewNetworkBehaviour

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [Actor](/api/Global.Actor) → [DewAllHeroesPresentZone](/api/Global.DewAllHeroesPresentZone) → [DewCutsceneDirector](/api/Global.DewCutsceneDirector) → [DewPlayer](/api/Global.DewPlayer) → [EntityComponent](/api/Global.EntityComponent) → [EntityTransformSync](/api/Global.EntityTransformSync) → [GenericTransformSync](/api/Global.GenericTransformSync) → `NetworkedManagerBase&lt;T&gt;` → [Room_Barrier](/api/Global.Room_Barrier) → [Room_Shortcut](/api/Global.Room_Shortcut) → [Room_Trap_ActivatorBase](/api/Global.Room_Trap_ActivatorBase) → [Room_Waypoint](/api/Global.Room_Waypoint) → [RoomComponent](/api/Global.RoomComponent) → `SingletonDewNetworkBehaviour&lt;T&gt;`

```csharp
public class DewNetworkBehaviour : NetworkBehaviour, ILogicUpdate
```

## Methods

### `Awake()`

```csharp
protected virtual void Awake()
```

### `FrameUpdate()`

```csharp
public virtual void FrameUpdate()
```

### `FxApplySpeedMultiplier(GameObject, float)`

Change speed of an effect, affecting ParticleSystems and IEffectWithSpeed inheritors.

```csharp
public void FxApplySpeedMultiplier(GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

### `FxApplySpeedMultiplierNetworked(GameObject, float)`

Change speed of an effect, affecting ParticleSystems and IEffectWithSpeed inheritors.

```csharp
public void FxApplySpeedMultiplierNetworked(GameObject effect, float multiplier)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `multiplier` | `float` |  |

### `FxPlay(GameObject, Entity, Vector3, Quaternion?)`

Play effect locally attached to given entity, positioned.

```csharp
public void FxPlay(GameObject effect, Entity attach, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [Entity](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlay(GameObject, Entity)`

Play effect locally attached to given entity.

```csharp
public void FxPlay(GameObject effect, Entity attach)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [Entity](/api/Global.Entity) |  |

### `FxPlay(GameObject, Vector3, Quaternion?)`

Play effect locally at given position.

```csharp
public void FxPlay(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlay(GameObject)`

Play effect locally.

```csharp
public void FxPlay(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `FxPlayNetworked(GameObject, Entity, Vector3, Quaternion?)`

Play effect everywhere attached to given entity, positioned. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect, Entity entity, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [Entity](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlayNetworked(GameObject, Entity)`

Play effect everywhere attached to given entity. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [Entity](/api/Global.Entity) |  |

### `FxPlayNetworked(GameObject, Vector3, Quaternion?)`

Play effect everywhere. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlayNetworked(GameObject)`

Play effect everywhere. Only callable in server.

```csharp
public void FxPlayNetworked(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `FxPlayNew(GameObject, Entity, Vector3, Quaternion?)`

Instantiate and play effect locally attached to given entity, positioned.

```csharp
public void FxPlayNew(GameObject effect, Entity attach, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [Entity](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlayNew(GameObject, Entity)`

Instantiate and play effect locally attached to given entity.

```csharp
public void FxPlayNew(GameObject effect, Entity attach)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `attach` | [Entity](/api/Global.Entity) |  |

### `FxPlayNew(GameObject, Vector3, Quaternion?)`

Instantiate and play effect locally at given position.

```csharp
public void FxPlayNew(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlayNew(GameObject)`

Instantiate and play effect locally.

```csharp
public void FxPlayNew(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `FxPlayNewNetworked(GameObject, Entity, Vector3, Quaternion?)`

Instantiate and play effect everywhere attached to given entity, positioned. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect, Entity entity, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [Entity](/api/Global.Entity) |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlayNewNetworked(GameObject, Entity)`

Instantiate and play effect everywhere attached to given entity. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect, Entity entity)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `entity` | [Entity](/api/Global.Entity) |  |

### `FxPlayNewNetworked(GameObject, Vector3, Quaternion?)`

Instantiate and play effect everywhere at given position. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect, Vector3 position, Quaternion? rotation)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |
| `position` | `UnityEngine.Vector3` |  |
| `rotation` | `UnityEngine.Quaternion?` |  |

### `FxPlayNewNetworked(GameObject)`

Instantiate and play effect everywhere. Only callable in server.

```csharp
public void FxPlayNewNetworked(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `FxStop(GameObject)`

Stop effect locally.

```csharp
public void FxStop(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `FxStopNetworked(GameObject)`

Stop effect everywhere. Only callable in server. Use non-networked variant in DewEffect if you want to stop effect locally.

```csharp
public void FxStopNetworked(GameObject effect)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `effect` | `UnityEngine.GameObject` |  |

### `GetComponent&lt;T&gt;(out T)`

```csharp
protected void GetComponent<T>(out T comp)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `comp` | `T` |  |
| `` | `T` |  |

### `InvalidateInstance()`

Invalidate an instance from pool, preventing it from being reused.

```csharp
public void InvalidateInstance()
```

### `LogicUpdate(float)`

```csharp
public virtual void LogicUpdate(float dt)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `dt` | `float` |  |

### `OnDestroy()`

```csharp
protected virtual void OnDestroy()
```

### `OnLateStart()`

```csharp
public virtual void OnLateStart()
```

### `OnLateStartServer()`

```csharp
public virtual void OnLateStartServer()
```

### `OnStart()`

```csharp
public virtual void OnStart()
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
public virtual void OnStop()
```

### `OnStopClient()`

```csharp
public override void OnStopClient()
```

### `OnStopServer()`

```csharp
public override void OnStopServer()
```
