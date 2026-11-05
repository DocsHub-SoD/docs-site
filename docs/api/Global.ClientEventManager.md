# Class: ClientEventManager

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** [DewNetworkBehaviour](/api/Global.DewNetworkBehaviour) → `NetworkedManagerBase` → [ClientEventManager](/api/Global.ClientEventManager)

```csharp
public class ClientEventManager : NetworkedManagerBase<ClientEventManager>, ILogicUpdate
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`OnApplyElemental`** | `public SafeAction&lt;EventInfoApplyElemental&gt; OnApplyElemental` |  |
| **`OnAttackHit`** | `public SafeAction&lt;EventInfoAttackHit&gt; OnAttackHit` |  |
| **`OnAttackMissed`** | `public SafeAction&lt;EventInfoAttackMissed&gt; OnAttackMissed` |  |
| **`OnCastComplete`** | `public SafeAction&lt;EventInfoCast&gt; OnCastComplete` |  |
| **`OnChaosUsed`** | `public SafeAction&lt;DewPlayer&gt; OnChaosUsed` |  |
| **`OnDamageNegated`** | `public SafeAction&lt;EventInfoDamageNegatedByImmunity&gt; OnDamageNegated` |  |
| **`OnDamageNegatedByShield`** | `public SafeAction&lt;EventInfoDamageNegatedByShield&gt; OnDamageNegatedByShield` |  |
| **`OnDeath`** | `public SafeAction&lt;EventInfoKill&gt; OnDeath` |  |
| **`OnDismantled`** | `public SafeAction&lt;Hero, NetworkBehaviour&gt; OnDismantled` |  |
| **`OnGemMergeUpgraded`** | `public SafeAction&lt;Hero, Gem&gt; OnGemMergeUpgraded` |  |
| **`OnGetManaSpent`** | `public SafeAction&lt;EventInfoSpentMana&gt; OnGetManaSpent` |  |
| **`OnGiveCurrency`** | `public SafeAction&lt;DewPlayer, DewPlayer, int, int&gt; OnGiveCurrency` |  |
| **`OnHeroKnockedOut`** | `public SafeAction&lt;Hero&gt; OnHeroKnockedOut` |  |
| **`OnHeroRevive`** | `public SafeAction&lt;Hero&gt; OnHeroRevive` |  |
| **`OnHideOnScreenTimer`** | `public SafeAction&lt;OnScreenTimerHandle&gt; OnHideOnScreenTimer` |  |
| **`OnHideStatusEffectIcon`** | `public SafeAction&lt;StatusEffect&gt; OnHideStatusEffectIcon` |  |
| **`OnIgnoreCC`** | `public SafeAction&lt;Entity&gt; OnIgnoreCC` |  |
| **`OnItemBought`** | `public SafeAction&lt;Hero, NetworkBehaviour&gt; OnItemBought` |  |
| **`OnItemCleansed`** | `public SafeAction&lt;Hero, NetworkBehaviour&gt; OnItemCleansed` |  |
| **`OnItemSold`** | `public SafeAction&lt;Hero, NetworkBehaviour&gt; OnItemSold` |  |
| **`OnItemUpgraded`** | `public SafeAction&lt;Hero, NetworkBehaviour&gt; OnItemUpgraded` |  |
| **`OnLocalHeroAbilityChanged`** | `public SafeAction&lt;Hero, HeroSkillLocation&gt; OnLocalHeroAbilityChanged` |  |
| **`OnLocalHeroGemChanged`** | `public SafeAction&lt;Hero, GemLocation&gt; OnLocalHeroGemChanged` |  |
| **`OnRefreshEntityHealthbar`** | `public SafeAction&lt;Entity&gt; OnRefreshEntityHealthbar` |  |
| **`OnShowOnScreenTimer`** | `public SafeAction&lt;OnScreenTimerHandle&gt; OnShowOnScreenTimer` |  |
| **`OnShowStatusEffectIcon`** | `public SafeAction&lt;StatusEffect&gt; OnShowStatusEffectIcon` |  |
| **`OnTakeDamage`** | `public SafeAction&lt;EventInfoDamage&gt; OnTakeDamage` |  |
| **`OnTakeHeal`** | `public SafeAction&lt;EventInfoHeal&gt; OnTakeHeal` |  |
| **`OnTakeManaHeal`** | `public SafeAction&lt;EventInfoHeal&gt; OnTakeManaHeal` |  |
| **`OnTakeShield`** | `public SafeAction&lt;EventInfoShield&gt; OnTakeShield` |  |

## Methods

### `AddEvents(Actor)`

```csharp
public virtual void AddEvents(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |

### `InvokeOnApplyElemental(EventInfoApplyElemental)`

```csharp
public void InvokeOnApplyElemental(EventInfoApplyElemental info)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `info` | [EventInfoApplyElemental](/api/Global.EventInfoApplyElemental) |  |

### `InvokeOnCastComplete(EventInfoCast)`

```csharp
public void InvokeOnCastComplete(EventInfoCast eventInfo)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `eventInfo` | [EventInfoCast](/api/Global.EventInfoCast) |  |

### `InvokeOnChaosUsed(DewPlayer)`

```csharp
public void InvokeOnChaosUsed(DewPlayer p)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `p` | [DewPlayer](/api/Global.DewPlayer) |  |

### `InvokeOnDismantled(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnDismantled(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [Hero](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

### `InvokeOnGemMergeUpgraded(Hero, Gem)`

```csharp
public void InvokeOnGemMergeUpgraded(Hero h, Gem g)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [Hero](/api/Global.Hero) |  |
| `g` | [Gem](/api/Global.Gem) |  |

### `InvokeOnIgnoreCC(Entity)`

```csharp
public void InvokeOnIgnoreCC(Entity ent)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `ent` | [Entity](/api/Global.Entity) |  |

### `InvokeOnItemBought(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemBought(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [Hero](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

### `InvokeOnItemCleansed(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemCleansed(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [Hero](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

### `InvokeOnItemSold(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemSold(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [Hero](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

### `InvokeOnItemUpgraded(Hero, NetworkBehaviour)`

```csharp
public void InvokeOnItemUpgraded(Hero h, NetworkBehaviour nb)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `h` | [Hero](/api/Global.Hero) |  |
| `nb` | `Mirror.NetworkBehaviour` |  |

### `InvokeOnRefreshEntityHealthbar(Entity)`

```csharp
public void InvokeOnRefreshEntityHealthbar(Entity e)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `e` | [Entity](/api/Global.Entity) |  |

### `OnDestroy()`

```csharp
protected override void OnDestroy()
```

### `OnStart()`

```csharp
public override void OnStart()
```

### `RemoveEvents(Actor)`

```csharp
public virtual void RemoveEvents(Actor actor)
```

**Parameters:**
| Name | Type | Description |
| :--- | :--- | :--- |
| `actor` | [Actor](/api/Global.Actor) |  |
