# Class: SkillBonus

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[Serializable]
public class SkillBonus
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`ignoreReceiveCooldownReductionFlag`** | `public bool ignoreReceiveCooldownReductionFlag` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`addedCharge`** | `public int addedCharge { get; set; }` |  |
| **`cooldownMultiplier`** | `public float cooldownMultiplier { get; set; }` |  |
| **`cooldownOffset`** | `public float cooldownOffset { get; set; }` |  |
| **`parent`** | `public SkillTrigger parent { get; }` |  |

## Methods

### `Clone()`

```csharp
public SkillBonus Clone()
```

**Returns:** `SkillBonus`

### `Stop()`

```csharp
public void Stop()
```
