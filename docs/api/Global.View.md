# Class: View

- **Category:** <span class="cat-dot" style="--cat-color: #ec4899" data-cat="User Interface"></span> User Interface
- **Namespace:** `Global`
- **Assembly:** `Dew.Core.dll`
- **Attributes:** `[ExecuteAlways] [RequireComponent] [RequireComponent]`

```csharp
[ExecuteAlways]
[RequireComponent(typeof(CanvasGroup))]
[RequireComponent(typeof(Canvas))]
public class View : MonoBehaviour
```

## Fields (13)

::: details Click to expand Fields (13)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`blockRaycastWhenShown`** | `[ToggleLeft] public bool blockRaycastWhenShown` |  |
| **`disableGameObjectWhenHidden`** | `[ToggleLeft] public bool disableGameObjectWhenHidden` |  |
| **`disablesInGamePlayingInput`** | `[ToggleLeft] public bool disablesInGamePlayingInput` |  |
| **`fadeTime`** | `public float fadeTime` |  |
| **`hideEffect`** | `public GameObject hideEffect` |  |
| **`ignoreOn`** | `[ShowIf("@showBehavior == View.ShowBehavior.UseState", true)] public List<string> ignoreOn` |  |
| **`instances`** | `public static List<View> instances` |  |
| **`interactableWhenShown`** | `[ToggleLeft] public bool interactableWhenShown` |  |
| **`onHide`** | `public UnityEvent onHide` |  |
| **`onShow`** | `public UnityEvent onShow` |  |
| **`showBehavior`** | `public View.ShowBehavior showBehavior` |  |
| **`showEffect`** | `public GameObject showEffect` |  |
| **`showOn`** | `[ShowIf("@showBehavior == View.ShowBehavior.UseState", true)] public List<string> showOn` |  |

:::

## Properties (1)

::: details Click to expand Properties (1)

| Name | Declaration | Description |
| :--- | :--- | :--- |
| **`isShowing`** | `public bool isShowing { get; }` |  |

:::

## Methods (10)

::: details `Awake()`

```csharp
protected virtual void Awake()
```

:::

::: details `Hide()`

Hide this view. ShowBehaviour must be set to Manually.

```csharp
public void Hide()
```

:::

::: details `OnDestroy()`

```csharp
protected virtual void OnDestroy()
```

:::

::: details `OnDisable()`

```csharp
protected virtual void OnDisable()
```

:::

::: details `OnEnable()`

```csharp
protected virtual void OnEnable()
```

:::

::: details `OnHide()`

```csharp
protected virtual void OnHide()
```

:::

::: details `OnShow()`

```csharp
protected virtual void OnShow()
```

:::

::: details `Show()`

Show this view. ShowBehaviour must be set to Manually.

```csharp
public void Show()
```

:::

::: details `Start()`

```csharp
protected virtual void Start()
```

:::

::: details `Update()`

```csharp
protected virtual void Update()
```

:::


## Architecture & Relationships

::: details Click to expand Architecture & Relationships

### Used By (33)

*Classes and systems that invoke, reference, or depend on `View`:*

[InGameUIManager](/api/Global.InGameUIManager) · `PlayTutorial_EditorOnlySkip` · `PlayTutorial_StartGameRift` · [TitleManager](/api/Global.TitleManager) · `UI_Achievements_View` · `UI_Collectables_MainView` · `UI_Common_MenuView` · `UI_Constellations` · `UI_CreditsView` · `UI_Guide_View` · `UI_InGame_ArtifactStoryView` · `UI_InGame_GiveCurrencyView` · `UI_InGame_LoopNotice` · `UI_InGame_ResultView` · `UI_InGame_ScoreboardView` · `UI_InGame_Scoreboard_PlayerItem` · `UI_InGame_Scoreboard_PlayerItem_Skill` · `UI_InGame_Scoreboard_PlayerItem_Skill_Gem` · `UI_InGame_WorldView` · `UI_Lobby_CharacterView` · `UI_Lobby_ObliterationView` · `UI_SelectControlPresetWindow` · `UI_Settings_View` · `UI_ShowIfTopmostView` · `UI_Title_CreateLobbyView` · `UI_Title_EULAView` · `UI_Title_FindLobbyView` · `UI_Title_LanguageSelectionView` · `UI_Title_MasteryRewardView` · `UI_Title_ProfileSelection` · `UI_Title_SplashView` · `UI_Title_TitleView` · `UI_TutorialDifficultyView`

### Dependencies (6)

*Types and components that `View` references or depends upon:*

[DewEffect](/api/Global.DewEffect) · [InGameUIManager](/api/Global.InGameUIManager) · [ManagerBase`1](/api/Global.ManagerBase`1) · [SafeAction](/api/Global.SafeAction) · [SafeAction`2](/api/Global.SafeAction`2) · [UIManager](/api/Global.UIManager)

:::
