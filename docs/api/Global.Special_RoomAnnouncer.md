# Class: Special_RoomAnnouncer

- **Category:** <span class="cat-dot" style="--cat-color: #3b82f6" data-cat="Managers & Systems"></span> Managers & Systems
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [Special_RoomAnnouncer](/api/Global.Special_RoomAnnouncer)

```csharp
public class Special_RoomAnnouncer : SingletonBehaviour<Special_RoomAnnouncer>
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`announceEvent`** | `[Space] [Space] public bool announceEvent` |  |
| **`color`** | `[ShowIf("announceEvent", true)] public Color color` |  |
| **`key`** | `public string key` |  |
| **`setRoomName`** | `[Space] [Space] public bool setRoomName` |  |
| **`showZoneIndex`** | `[ShowIf("setRoomName", true)] public bool showZoneIndex` |  |
| **`sprite`** | `[ShowIf("announceEvent", true)] public Sprite sprite` |  |
| **`spriteScale`** | `[ShowIf("announceEvent", true)] public float spriteScale` |  |
| **`zoneIndexOffset`** | `[ShowIf("@showZoneIndex && setRoomName", true)] public int zoneIndexOffset` |  |

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (0)

*No incoming dependencies recorded.*

### Dependencies (1)

*Types and components that `Special_RoomAnnouncer` references or depends upon:*

[SingletonBehaviour`1](/api/Global.SingletonBehaviour`1)

:::
