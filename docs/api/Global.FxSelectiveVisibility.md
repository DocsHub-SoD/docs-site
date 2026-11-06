# Class: FxSelectiveVisibility

- **Category:** <span class="cat-dot" style="--cat-color: #64748b" data-cat="Misc & Utility"></span> Misc & Utility
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[DisallowMultipleComponent]`

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
| **`parent`** | `[HideInInspector] [HideInInspector] public Actor parent` |  |
| **`visibleTo`** | `[InfoBox("@_helpText", InfoMessageType.Info, null)] public EffectVisibility visibleTo` |  |
| **`wasDisabled`** | `[HideInInspector] [HideInInspector] public bool wasDisabled` |  |

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


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (1)

*Classes and systems that invoke, reference, or depend on `FxSelectiveVisibility`:*

[DewEffect](/api/Global.DewEffect)

### Dependencies (8)

*Types and components that `FxSelectiveVisibility` references or depends upon:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [CameraManager](/api/Global.CameraManager) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [ManagerBase`1](/api/Global.ManagerBase`1) · [StatusEffect](/api/Global.StatusEffect) · `TransformGetScenePathExtension`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#effectvisibility" class="enum-link" data-tooltip="Everyone=0 · Caster=1 · Target=2 · Victim=3 · Owner=4">EffectVisibility</a>

:::
