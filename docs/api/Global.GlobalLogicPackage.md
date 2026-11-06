# Class: GlobalLogicPackage

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [LogicBehaviour](/api/Global.LogicBehaviour) → `ManagerBase` → [GlobalLogicPackage](/api/Global.GlobalLogicPackage)

```csharp
public class GlobalLogicPackage : ManagerBase<GlobalLogicPackage>, ILogicUpdate
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`showFps`** | `[NonSerialized] public bool showFps` |  |

:::

## Methods (2)

::: details `Awake()`

```csharp
protected override void Awake()
```

:::

::: details `CallOnReady(Action)`

Call the action after global package has been added. If the global package already exists, it will be called immediately.

```csharp
public static void CallOnReady(Action callback)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `callback` | `System.Action` |  |

:::
