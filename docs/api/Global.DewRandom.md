# Class: DewRandom

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewRandom
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`initialSeed`** | `public uint initialSeed` |  |
| **`instance`** | `public static DewRandom instance` |  |
| **`s0`** | `public uint s0` |  |
| **`s1`** | `public uint s1` |  |
| **`s2`** | `public uint s2` |  |
| **`s3`** | `public uint s3` |  |

## Methods

### `ColorHSV(float, float, float, float, float, float, float, float)`

```csharp
public Color ColorHSV(float hueMin = 0, float hueMax = 1, float satMin = 0, float satMax = 1, float valMin = 0, float valMax = 1, float alphaMin = 1, float alphaMax = 1)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `hueMin` | `float` |  |
| `hueMax` | `float` |  |
| `satMin` | `float` |  |
| `satMax` | `float` |  |
| `valMin` | `float` |  |
| `valMax` | `float` |  |
| `alphaMin` | `float` |  |
| `alphaMax` | `float` |  |

**Returns:** `UnityEngine.Color`

### `GetRandomSeed()`

```csharp
public static uint GetRandomSeed()
```

**Returns:** `uint`

### `InsideUnitCircle()`

```csharp
public Vector2 InsideUnitCircle()
```

**Returns:** `UnityEngine.Vector2`

### `InsideUnitSphere()`

```csharp
public Vector3 InsideUnitSphere()
```

**Returns:** `UnityEngine.Vector3`

### `NextDouble()`

```csharp
public double NextDouble()
```

**Returns:** `double`

### `NextFloat()`

```csharp
public float NextFloat()
```

**Returns:** `float`

### `NextFloat(float, float)`

```csharp
public float NextFloat(float min, float max)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `min` | `float` |  |
| `max` | `float` |  |

**Returns:** `float`

### `NextUInt32()`

```csharp
public uint NextUInt32()
```

**Returns:** `uint`

### `OnUnitSphere()`

```csharp
public Vector3 OnUnitSphere()
```

**Returns:** `UnityEngine.Vector3`

### `Range(int, int)`

```csharp
public int Range(int minInclusive, int maxExclusive)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `minInclusive` | `int` |  |
| `maxExclusive` | `int` |  |

**Returns:** `int`

### `Range(float, float)`

```csharp
public float Range(float min, float max)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `min` | `float` |  |
| `max` | `float` |  |

**Returns:** `float`

### `Rotation()`

```csharp
public Quaternion Rotation()
```

**Returns:** `UnityEngine.Quaternion`

### `RotationUniform()`

```csharp
public Quaternion RotationUniform()
```

**Returns:** `UnityEngine.Quaternion`

### `SetSeed(uint)`

```csharp
public void SetSeed(uint seed)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `seed` | `uint` |  |

### `ToString()`

```csharp
public override string ToString()
```

**Returns:** `string`

### `Value()`

```csharp
public float Value()
```

**Returns:** `float`
