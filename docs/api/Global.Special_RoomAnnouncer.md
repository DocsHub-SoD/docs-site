# Class: Special_RoomAnnouncer

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Inheritance / Derived:** `SingletonBehaviour` → [Special_RoomAnnouncer](/api/Global.Special_RoomAnnouncer)

```csharp
public class Special_RoomAnnouncer : SingletonBehaviour<Special_RoomAnnouncer>
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`announceEvent`** | `[Space]
public bool announceEvent` |  |
| **`color`** | `[ShowIf("announceEvent", true)]
public Color color` |  |
| **`key`** | `public string key` |  |
| **`setRoomName`** | `[Space]
public bool setRoomName` |  |
| **`showZoneIndex`** | `[ShowIf("setRoomName", true)]
public bool showZoneIndex` |  |
| **`sprite`** | `[ShowIf("announceEvent", true)]
public Sprite sprite` |  |
| **`spriteScale`** | `[ShowIf("announceEvent", true)]
public float spriteScale` |  |
| **`zoneIndexOffset`** | `[ShowIf("@showZoneIndex && setRoomName", true)]
public int zoneIndexOffset` |  |
