# NEXORA AI 2.0 — Temporary Public Snapshot

**Status:** Phase 0–8 complete snapshot for external review (ChatGPT / Claude).
**Visibility:** public (temporary — switch back to private after review).

## Start here

1. [CLAUDE_START_HERE.md](./CLAUDE_START_HERE.md)
2. [HANDOFF_FOR_CLAUDE.md](./HANDOFF_FOR_CLAUDE.md) — full technical handoff
3. [CHATGPT_PROMPT.md](./CHATGPT_PROMPT.md) — copy-paste prompt
4. [documentation/RELEASE_CHECKLIST.md](./documentation/RELEASE_CHECKLIST.md)
5. [documentation/PHASE_8.md](./documentation/PHASE_8.md)

## Full application source

If this repo only contains docs, attach or download:

- `NEXORA_AI_COMPLETE_RELEASE.zip` (full tree: backend, apps/web, tests, …)

SHA-256 of the release ZIP:

```
c8a06375aa4580113a07c19b5920aab56539ca060956371dbecf28643d09b39d
```

Related private repos (owner only):
- https://github.com/spetthayn/NEXORAI (Phase 0 partial)
- https://github.com/spetthayn/NEXORA-AI-RELEASE (release notes)

## Rules for reviewers

- Default mode: **PAPER / SIMULATION**
- LIVE requires phrase `ENABLE LIVE TRADING` + checklist + env keys
- Do not invent market data; respect `no_data` / `insufficient_data`
- No secrets in repo; keys only via environment variables
