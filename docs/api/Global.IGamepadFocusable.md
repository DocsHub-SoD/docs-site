# Interface: IGamepadFocusable

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`

```csharp
public interface IGamepadFocusable : IGamepadFocusListener
```

## Methods (5)

::: details `CanBeFocused()`

```csharp
bool CanBeFocused()
```

**Returns:** `bool`

:::

::: details `CanHoldConfirmToRepeat()`

```csharp
bool CanHoldConfirmToRepeat()
```

**Returns:** `bool`

:::

::: details `GetBehavior()`

```csharp
FocusableBehavior GetBehavior()
```

**Returns:** `FocusableBehavior`

:::

::: details `GetSelectionDisplayType()`

```csharp
SelectionDisplayType GetSelectionDisplayType()
```

**Returns:** `SelectionDisplayType`

:::

::: details `GetTransform()`

```csharp
RectTransform GetTransform()
```

**Returns:** `UnityEngine.RectTransform`

:::
