# Struct: ReactionChain

- **Category:** <span class="cat-dot" style="--cat-color: #22c55e" data-cat="Actors & Entities"></span> Actors & Entities
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct ReactionChain
```

## Methods (5)

::: details `DidReact(Actor, bool)`

Check if the actor has already contributed to this reaction chain.

```csharp
public bool DidReact(Actor actor, bool checkOnlyType = false)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |
| `checkOnlyType` | `bool` |  |

**Returns:** `bool`

:::

::: details `Equals(ReactionChain)`

```csharp
public bool Equals(ReactionChain other)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `other` | [`ReactionChain`](/api/Global.ReactionChain) |  |

**Returns:** `bool`

:::

::: details `Equals(object)`

```csharp
public override bool Equals(object obj)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `obj` | `object` |  |

**Returns:** `bool`

:::

::: details `GetHashCode()`

```csharp
public override int GetHashCode()
```

**Returns:** `int`

:::

::: details `New(Actor)`

Returns new reaction chain with given actor in contribution.

```csharp
public ReactionChain New(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [`Actor`](/api/Global.Actor) |  |

**Returns:** `ReactionChain`

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (39)

*Classes and systems that invoke, reference, or depend on `ReactionChain`:*

[AbilityInstance](/api/Global.AbilityInstance) · [Actor](/api/Global.Actor) · [DamageData](/api/Global.DamageData) · [EventInfoAttackEffect](/api/Global.EventInfoAttackEffect) · [EventInfoDamage](/api/Global.EventInfoDamage) · [EventInfoHeal](/api/Global.EventInfoHeal) · [EventInfoShield](/api/Global.EventInfoShield) · `Gem_C_Charcoal` · `Gem_C_Guidance` · `Gem_E_Blossom` · `Gem_E_Clemency` · `Gem_E_Fever` · `Gem_E_Pain` · `Gem_E_Twilight` · `Gem_E_Umbra` · `Gem_L_Embertail` · `Gem_R_Abyss` · `Gem_R_Accuracy` · `Gem_R_Blade` · `Gem_R_Control` · `Gem_R_Glass` · `Gem_R_Mortality` · `Gem_R_Ricochet` · `Gem_R_Rigidity` · `Gem_R_Wound` · `Gem_U_GlacialCore` · [HealData](/api/Global.HealData) · [ReactionChainComparer](/api/Global.ReactionChainComparer) · `Se_D_BeautifulThreat` · `Se_D_IcyVeins` · `Se_GenericShield_Stacking` · `Se_MirageSkin_Pulverization` · `Se_R_UnbreakableDetermination` · `Se_Star_Aurena_L_ShareHeal` · `Se_Star_Cetus_L_HealOnApDamage` · `Se_Star_Husk_D_DamageOverTimeCritWithPenalty` · [ShieldEffect](/api/Global.ShieldEffect) · `St_D_DisintegratingClaw` · `Mirror.GeneratedNetworkCode`

### Dependencies (1)

*Types and components that `ReactionChain` references or depends upon:*

[Actor](/api/Global.Actor)

:::
