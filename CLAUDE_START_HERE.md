# Start here (Claude)

1. Read `documentation/HANDOFF_FOR_CLAUDE.md` completely.
2. Read `documentation/RELEASE_CHECKLIST.md` and `documentation/PHASE_*.md` as needed.
3. Run verification (ruff, pytest, tsc, vitest, vite build) before large changes.
4. Default execution mode is **PAPER**. LIVE needs phrase `ENABLE LIVE TRADING` + checklist + env keys.
5. Do not rewrite the monorepo; extend modules under `backend/modules/` and `apps/web/src/`.

Primary handoff: **documentation/HANDOFF_FOR_CLAUDE.md**
