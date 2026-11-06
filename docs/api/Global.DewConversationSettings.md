# Class: DewConversationSettings

- **Category:** <span class="cat-dot" style="--cat-color: #f97316" data-cat="Data & Core Math"></span> Data & Core Math
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public class DewConversationSettings
```

## Fields (8)

::: details Click to expand Fields (8)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`callFunctions`** | `[NonSerialized] public Dictionary<string, Action> callFunctions` | This is not synced to clients. |
| **`onStop`** | `[NonSerialized] public Action onStop` | This is not synced to clients. |
| **`player`** | `public DewPlayer player` |  |
| **`rotateTowardsCenter`** | `public bool rotateTowardsCenter` |  |
| **`speakers`** | `public Entity[] speakers` |  |
| **`startConversationKey`** | `public string startConversationKey` |  |
| **`variables`** | `public Dictionary<string, string> variables` |  |
| **`visibility`** | `public ConversationVisibility visibility` |  |

:::

## Properties (3)

::: details Click to expand Properties (3)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isLocalAuthority`** | `public bool isLocalAuthority { get; }` | Is local player authorized to advance the conversation? |
| **`isVisibleToLocal`** | `public bool isVisibleToLocal { get; }` | Can local player see this conversation? |
| **`seed`** | `public int seed { get; }` | Used for solving randomness consistently across clients. |

:::
