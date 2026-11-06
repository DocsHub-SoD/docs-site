# Class: Zone

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Zone : MonoBehaviour
```

## Fields (17)

::: details Click to expand Fields (17)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bossRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)] public List<string> bossRooms` |  |
| **`combatRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)] public List<string> combatRooms` |  |
| **`defaultMonsters`** | `public MonsterSpawnRule defaultMonsters` |  |
| **`defaultMusicRef`** | `[Header("Settings")] [InfoBox("This music will be played on non-boss rooms.", InfoMessageType.Info, null)] public AssetRef<DewMusicItem> defaultMusicRef` |  |
| **`defaultProps`** | `[InfoBox("This prop rule will be applied on combat rooms.", InfoMessageType.Info, null)] public PropSpawnRule defaultProps` |  |
| **`disableRoomModifiers`** | `[Header("World Generation")] public bool disableRoomModifiers` |  |
| **`eventRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)] public List<string> eventRooms` |  |
| **`mainColor`** | `public Color mainColor` |  |
| **`numOfEvents`** | `[HideIf("useSpecialGeneration", true)] public Vector2Int numOfEvents` |  |
| **`numOfMerchants`** | `[HideIf("useSpecialGeneration", true)] public Vector2Int numOfMerchants` |  |
| **`numOfNodes`** | `[HideIf("useSpecialGeneration", true)] public Vector2Int numOfNodes` |  |
| **`rooms`** | `[FoldoutGroup("Automatically Baked Data", 0)] public List<string> rooms` |  |
| **`shopRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)] public List<string> shopRooms` |  |
| **`specialNodes`** | `[ShowIf("useSpecialGeneration", true)] public int specialNodes` |  |
| **`startRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)] public List<string> startRooms` |  |
| **`useSpecialGeneration`** | `public bool useSpecialGeneration` |  |
| **`zoneTier`** | `public int zoneTier` |  |

:::
