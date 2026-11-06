# Class: ClientEventManager

- **Category:** <span class="cat-dot" style="--cat-color: #ef4444" data-cat="Combat & Abilities"></span> Combat & Abilities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ClientEventManager](/api/Global.ClientEventManager)

```csharp
public class ClientEventManager : NetworkedManagerBase<ClientEventManager>, ILogicUpdate
```

## Fields (30)

::: details Click to expand Fields (30)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`OnApplyElemental`** | `public SafeAction<EventInfoApplyElemental> OnApplyElemental` |  |
| **`OnAttackHit`** | `public SafeAction<EventInfoAttackHit> OnAttackHit` |  |
| **`OnAttackMissed`** | `public SafeAction<EventInfoAttackMissed> OnAttackMissed` |  |
| **`OnCastComplete`** | `public SafeAction<EventInfoCast> OnCastComplete` |  |
| **`OnChaosUsed`** | `public SafeAction<DewPlayer> OnChaosUsed` |  |
| **`OnDamageNegated`** | `public SafeAction<EventInfoDamageNegatedByImmunity> OnDamageNegated` |  |
| **`OnDamageNegatedByShield`** | `public SafeAction<EventInfoDamageNegatedByShield> OnDamageNegatedByShield` |  |
| **`OnDeath`** | `public SafeAction<EventInfoKill> OnDeath` |  |
| **`OnDismantled`** | `public SafeAction<Hero, NetworkBehaviour> OnDismantled` |  |
| **`OnGemMergeUpgraded`** | `public SafeAction<Hero, Gem> OnGemMergeUpgraded` |  |
| **`OnGetManaSpent`** | `public SafeAction<EventInfoSpentMana> OnGetManaSpent` |  |
| **`OnGiveCurrency`** | `public SafeAction<DewPlayer, DewPlayer, int, int> OnGiveCurrency` |  |
| **`OnHeroKnockedOut`** | `public SafeAction<Hero> OnHeroKnockedOut` |  |
| **`OnHeroRevive`** | `public SafeAction<Hero> OnHeroRevive` |  |
| **`OnHideOnScreenTimer`** | `public SafeAction<OnScreenTimerHandle> OnHideOnScreenTimer` |  |
| **`OnHideStatusEffectIcon`** | `public SafeAction<StatusEffect> OnHideStatusEffectIcon` |  |
| **`OnIgnoreCC`** | `public SafeAction<Entity> OnIgnoreCC` |  |
| **`OnItemBought`** | `public SafeAction<Hero, NetworkBehaviour> OnItemBought` |  |
| **`OnItemCleansed`** | `public SafeAction<Hero, NetworkBehaviour> OnItemCleansed` |  |
| **`OnItemSold`** | `public SafeAction<Hero, NetworkBehaviour> OnItemSold` |  |
| **`OnItemUpgraded`** | `public SafeAction<Hero, NetworkBehaviour> OnItemUpgraded` |  |
| **`OnLocalHeroAbilityChanged`** | `public SafeAction<Hero, HeroSkillLocation> OnLocalHeroAbilityChanged` |  |
| **`OnLocalHeroGemChanged`** | `public SafeAction<Hero, GemLocation> OnLocalHeroGemChanged` |  |
| **`OnRefreshEntityHealthbar`** | `public SafeAction<Entity> OnRefreshEntityHealthbar` |  |
| **`OnShowOnScreenTimer`** | `public SafeAction<OnScreenTimerHandle> OnShowOnScreenTimer` |  |
| **`OnShowStatusEffectIcon`** | `public SafeAction<StatusEffect> OnShowStatusEffectIcon` |  |
| **`OnTakeDamage`** | `public SafeAction<EventInfoDamage> OnTakeDamage` |  |
| **`OnTakeHeal`** | `public SafeAction<EventInfoHeal> OnTakeHeal` |  |
| **`OnTakeManaHeal`** | `public SafeAction<EventInfoHeal> OnTakeManaHeal` |  |
| **`OnTakeShield`** | `public SafeAction<EventInfoShield> OnTakeShield` |  |

:::

## Methods (15)

::: details `AddEvents(Actor)`

```csharp
public virtual void AddEvents(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::

::: details `InvokeOnApplyElemental(EventInfoApplyElemental)`

```csharp
public void InvokeOnApplyElemental(EventInfoApplyElemental info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [`EventInfoApplyElemental`](/api/Global.EventInfoApplyElemental) |  |

:::

::: details `InvokeOnCastComplete(EventInfoCast)`

```csharp
public void InvokeOnCastComplete(EventInfoCast eventInfo)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventInfo` | [`EventInfoCast`](/api/Global.EventInfoCast) |  |

:::

::: details `InvokeOnChaosUsed(DewPlayer)`

```csharp
public void InvokeOnChaosUsed(DewPlayer p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [`DewPlayer`](/api/Global.DewPlayer) |  |

:::

::: details `InvokeOnDismantled(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnDismantled(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

:::

::: details `InvokeOnGemMergeUpgraded(Hero, Gem)`

```csharp
public void InvokeOnGemMergeUpgraded(Hero h, Gem g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `g` | [`Gem`](/api/Global.Gem) |  |

:::

::: details `InvokeOnIgnoreCC(Entity)`

```csharp
public void InvokeOnIgnoreCC(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `InvokeOnItemBought(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemBought(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

:::

::: details `InvokeOnItemCleansed(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemCleansed(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

:::

::: details `InvokeOnItemSold(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemSold(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

:::

::: details `InvokeOnItemUpgraded(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemUpgraded(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [`Hero`](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

:::

::: details `InvokeOnRefreshEntityHealthbar(Entity)`

```csharp
public void InvokeOnRefreshEntityHealthbar(Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [`Entity`](/api/Global.Entity) |  |

:::

::: details `OnDestroy()`

```csharp
protected override void OnDestroy()
```

:::

::: details `OnStart()`

```csharp
public override void OnStart()
```

:::

::: details `RemoveEvents(Actor)`

```csharp
public virtual void RemoveEvents(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (16)

*Classes and systems that invoke, reference, or depend on `ClientEventManager`:*

[AbilityTrigger](/api/Global.AbilityTrigger) · `Ai_RandomGemUpgrade` · [Dew](/api/Global.Dew) · [Gem](/api/Global.Gem) · [HeroSkill](/api/Global.HeroSkill) · [Knockback](/api/Global.Knockback) · [PropEnt_Merchant_Base](/api/Global.PropEnt_Merchant_Base) · `Shrine_AltarOfCleansing` · `Shrine_Chaos` · `Shrine_CorruptedChaos` · `Shrine_Entanglement` · `Shrine_MawOfDoom` · `Shrine_ScaredMaw` · `Shrine_UpgradeWell` · [SkillTrigger](/api/Global.SkillTrigger) · [StatusEffect](/api/Global.StatusEffect)

### Dependencies (23)

*Types and components that `ClientEventManager` references or depends upon:*

[Actor](/api/Global.Actor) · [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) · [DewPlayer](/api/Global.DewPlayer) · [Entity](/api/Global.Entity) · [EventInfoApplyElemental](/api/Global.EventInfoApplyElemental) · [EventInfoAttackHit](/api/Global.EventInfoAttackHit) · [EventInfoAttackMissed](/api/Global.EventInfoAttackMissed) · [EventInfoCast](/api/Global.EventInfoCast) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoDamageNegatedByImmunity](/api/Global.EventInfoDamageNegatedByImmunity) · [EventInfoDamageNegatedByShield](/api/Global.EventInfoDamageNegatedByShield) · [EventInfoHeal](/api/Global.EventInfoHeal) · [EventInfoKill](/api/Global.EventInfoKill) · [EventInfoShield](/api/Global.EventInfoShield) · [EventInfoSpentMana](/api/Global.EventInfoSpentMana) · [Gem](/api/Global.Gem) · [Hero](/api/Global.Hero) · [NetworkedManagerBase`1](/api/Global.NetworkedManagerBase`1) · [SafeAction`1](/api/Global.SafeAction`1) · [SafeAction`2](/api/Global.SafeAction`2) · [SafeAction`3](/api/Global.SafeAction`3) · [SafeAction`4](/api/Global.SafeAction`4) · `Mirror.GeneratedNetworkCode`

### Related Enums (1)

*Enumerations referenced in fields, properties, or method signatures:*

<a href="/enums#heroskilllocation" class="enum-link" data-tooltip="Q=0 · W=1 · E=2 · R=3 · Identity=4 (+1 more)">HeroSkillLocation</a>

:::
