# Class: SingletonDewNetworkBehaviour&lt;T&gt;

- **Category:** <span class="cat-dot" style="--cat-color: #06b6d4" data-cat="Networking"></span> Networking
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → [Room](/api/Global.Room)

```csharp
public class SingletonDewNetworkBehaviour<T> : DewNetworkBehaviour, ILogicUpdate where T : MonoBehaviour
```

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`instance`** | `public static T instance { get; }` | If you expect the instance to be null, you MUST USE softInstance in Update loops.This will call FindObjectOfType if current instance is null, which can be very expensive. |
| **`softInstance`** | `public static T softInstance { get; }` |  |

## Methods

### `Awake()`

```csharp
protected override void Awake()
```
