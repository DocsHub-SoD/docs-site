# Class: FxSelectiveVisibility

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DisallowMultipleComponent]
public class FxSelectiveVisibility : MonoBehaviour
```

## Fields (6)

::: details Click to expand Fields (6)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`forceFail`** | `public static bool forceFail` |  |
| **`hideOnSummons`** | `[ShowIf("@visibleTo != EffectVisibility.Everyone", true)] public bool hideOnSummons` |  |
| **`invertVisibility`** | `public bool invertVisibility` |  |
| **`parent`** | `[HideInInspector] public Actor parent` |  |
| **`visibleTo`** | `[InfoBox("@_helpText", InfoMessageType.Info, null)] public EffectVisibility visibleTo` |  |
| **`wasDisabled`** | `[HideInInspector] public bool wasDisabled` |  |

:::

## Methods (3)

::: details `IsVisibleLocally()`

```csharp
public bool IsVisibleLocally()
```

**Returns:** `bool`

:::

::: details `OnAfterDeserialize()`

```csharp
public void OnAfterDeserialize()
```

:::

::: details `OnBeforeSerialize()`

```csharp
public void OnBeforeSerialize()
```

:::
