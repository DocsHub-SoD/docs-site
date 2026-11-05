# Class: DewConversationSettings

- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewConversationSettings
```

## Fields

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`callFunctions`** | `[NonSerialized]
public Dictionary&lt;string, Action&gt; callFunctions` | This is not synced to clients. |
| **`onStop`** | `[NonSerialized]
public Action onStop` | This is not synced to clients. |
| **`player`** | `public DewPlayer player` |  |
| **`rotateTowardsCenter`** | `public bool rotateTowardsCenter` |  |
| **`speakers`** | `public Entity[] speakers` |  |
| **`startConversationKey`** | `public string startConversationKey` |  |
| **`variables`** | `public Dictionary&lt;string, string&gt; variables` |  |
| **`visibility`** | `public ConversationVisibility visibility` |  |

## Properties

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isLocalAuthority`** | `public bool isLocalAuthority { get; }` | Is local player authorized to advance the conversation? |
| **`isVisibleToLocal`** | `public bool isVisibleToLocal { get; }` | Can local player see this conversation? |
| **`seed`** | `public int seed { get; }` | Used for solving randomness consistently across clients. |
