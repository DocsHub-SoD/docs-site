# Interface: ICustomInteractable

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface ICustomInteractable
```

## Properties (8)

::: details Click to expand Properties (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`altInteractProgress`** | `float? altInteractProgress { get; }` |  |
| **`canAltInteract`** | `bool canAltInteract { get; }` |  |
| **`cost`** | `Cost cost { get; }` |  |
| **`costAlt`** | `Cost costAlt { get; }` |  |
| **`interactActionRawText`** | `string interactActionRawText { get; }` |  |
| **`interactAltActionRawText`** | `string interactAltActionRawText { get; }` |  |
| **`nameRawText`** | `string nameRawText { get; }` |  |
| **`worldOffset`** | `Vector3 worldOffset { get; }` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (24)

*Classes and systems that invoke, reference, or depend on `ICustomInteractable`:*

[Artifact](/api/Global.Artifact) · `ConversationShrineBase` · [PingManager](/api/Global.PingManager) · [Room_Shortcut](/api/Global.Room_Shortcut) · `Shrine_AncientRemnants` · `Shrine_Anitya` · `Shrine_ArtifactGiver` · `Shrine_CallOfTheRavenous` · `Shrine_Destiny` · `Shrine_DreamdustBit` · `Shrine_DreamdustBox` · `Shrine_GoldBit` · `Shrine_GoldBox` · `Shrine_Guidance` · `Shrine_LoopCat` · `Shrine_Luck` · `Shrine_Merchant_Backpack` · `Shrine_MorasDomain_HerPresence` · `Shrine_Polaris_Teleporter` · `Shrine_PrimusDoor` · `Shrine_StarCookie` · `Shrine_TheConsortOfNight` · `Shrine_TheConsortOfNight_Rift` · `UI_InGame_Interact_Custom`

### Dependencies (1)

*Types and components that `ICustomInteractable` references or depends upon:*

[Cost](/api/Global.Cost)

:::
