# Struct: EventInfoDamageNegatedByShield

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public struct EventInfoDamageNegatedByShield
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`actor`** | `public Actor actor` | The actor who started the damage. |
| **`damage`** | `public FinalDamageData damage` |  |
| **`negatedAmount`** | `public float negatedAmount` |  |
| **`shield`** | `[NonSerialized]
public ShieldEffect shield` | The shield effect responsible for this event. Only available on server. |
| **`victim`** | `public Entity victim` |  |
