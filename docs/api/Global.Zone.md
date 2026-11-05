# Class: Zone

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
[DewResourceLink(ResourceLinkBy.Name)]
public class Zone : MonoBehaviour
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`bossRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)]
public List&lt;string&gt; bossRooms` |  |
| **`combatRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)]
public List&lt;string&gt; combatRooms` |  |
| **`defaultMonsters`** | `public MonsterSpawnRule defaultMonsters` |  |
| **`defaultMusicRef`** | `[Header("Settings")]
[InfoBox("This music will be played on non-boss rooms.", InfoMessageType.Info, null)]
public AssetRef&lt;DewMusicItem&gt; defaultMusicRef` |  |
| **`defaultProps`** | `[InfoBox("This prop rule will be applied on combat rooms.", InfoMessageType.Info, null)]
public PropSpawnRule defaultProps` |  |
| **`disableRoomModifiers`** | `[Header("World Generation")]
public bool disableRoomModifiers` |  |
| **`eventRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)]
public List&lt;string&gt; eventRooms` |  |
| **`mainColor`** | `public Color mainColor` |  |
| **`numOfEvents`** | `[HideIf("useSpecialGeneration", true)]
public Vector2Int numOfEvents` |  |
| **`numOfMerchants`** | `[HideIf("useSpecialGeneration", true)]
public Vector2Int numOfMerchants` |  |
| **`numOfNodes`** | `[HideIf("useSpecialGeneration", true)]
public Vector2Int numOfNodes` |  |
| **`rooms`** | `[FoldoutGroup("Automatically Baked Data", 0)]
public List&lt;string&gt; rooms` |  |
| **`shopRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)]
public List&lt;string&gt; shopRooms` |  |
| **`specialNodes`** | `[ShowIf("useSpecialGeneration", true)]
public int specialNodes` |  |
| **`startRooms`** | `[FoldoutGroup("Automatically Baked Data", 0)]
public List&lt;string&gt; startRooms` |  |
| **`useSpecialGeneration`** | `public bool useSpecialGeneration` |  |
| **`zoneTier`** | `public int zoneTier` |  |
