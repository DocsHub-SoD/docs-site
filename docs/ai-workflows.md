# Using This Documentation with AI Assistants

If you use an AI coding assistant (such as Cursor, GitHub Copilot, Claude, ChatGPT, or Antigravity) while developing mods for **Shape of Dreams**, this page explains how to get the most accurate code without polluting your context window.

---

## 1. The Core Problem with API Documentation

Shape of Dreams contains **897 types** and thousands of methods in a single assembly.

If you try to paste whole web pages or entire folders of documentation into an LLM:
- You burn tens of thousands of tokens per prompt.
- The model suffers from "attention degradation" (forgetting details in the middle).
- The model often hallucinates method names that exist in standard Unity or other games rather than Shape of Dreams.

---

## 2. Recommended Workflows

### Option A: Querying the SQLite Database (`api.db`) — Best for Coding Agents
For tool-assisted agents (Cursor with terminal/agent mode, Antigravity, Cline):

1. Download [`api.db`](https://github.com/DocsHub-SoD/docs-data/blob/main/api.db) and [`LLM_GUIDE.md`](https://github.com/DocsHub-SoD/docs-data/blob/main/LLM_GUIDE.md) from the [docs-data repository](https://github.com/DocsHub-SoD/docs-data).
2. Place them in your mod workspace.
3. Prompt your assistant:
   > *"Check `LLM_GUIDE.md` and query `api.db` using sqlite3 to find the exact method signatures and parameter types before writing patches."*
4. The assistant executes pinpoint SQL queries that cost under 50 tokens each and returns 100% verified C# signatures.

### Option B: Web & Chat-Based Assistants (ChatGPT, Claude Web)
If you are chatting with an AI in a browser:
1. Navigate to the class you need in this portal (e.g. [`AbilityTrigger`](/api/Global.AbilityTrigger) or [`Actor`](/api/Global.Actor)).
2. Copy only the specific method or field declaration you intend to hook or modify.
3. Provide that targeted signature in your prompt:
   > *"Here is the exact method signature from Shape of Dreams: `public virtual bool CanBeCast()`. Write a HarmonyPrefix patch in BepInEx 5 that checks my custom condition before calling this method."*

---

## 3. Need the Source Data?

All raw JSON models, the knowledge graph, and the SQLite database are open and maintained in the community repository:
👉 **[DocsHub-SoD/docs-data on GitHub](https://github.com/DocsHub-SoD/docs-data)**
