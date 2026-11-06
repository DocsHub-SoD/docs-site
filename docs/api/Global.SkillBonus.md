# Class: SkillBonus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class SkillBonus
```

## Fields (1)

::: details Click to expand Fields (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ignoreReceiveCooldownReductionFlag`** | `public bool ignoreReceiveCooldownReductionFlag` |  |

:::

## Properties (4)

::: details Click to expand Properties (4)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedCharge`** | `public int addedCharge { get; set; }` |  |
| **`cooldownMultiplier`** | `public float cooldownMultiplier { get; set; }` |  |
| **`cooldownOffset`** | `public float cooldownOffset { get; set; }` |  |
| **`parent`** | `public SkillTrigger parent { get; }` |  |

:::

## Methods (2)

::: details `Clone()`

```csharp
public SkillBonus Clone()
```

**Returns:** `SkillBonus`

:::

::: details `Stop()`

```csharp
public void Stop()
```

:::
