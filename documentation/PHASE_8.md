# NEXORA AI — Phase 8 Performance, Monitoring & PAPER→LIVE Gate

**Status:** Steps 8.1 + 8.2 delivered for review
**Updated:** 2026-11-24

## Step 8.1 — Backend

Live gate, env-only secrets, monitoring metrics, redact filter, no real sandbox orders.

## Step 8.2 — Monitoring UI + Release checklist

| Item | Path |
|------|------|
| Page | apps/web/src/pages/Monitoring.tsx |
| Route | /monitoring |
| Types | api/executionTypes.ts |
| Release | documentation/RELEASE_CHECKLIST.md |

### UI

- Mode banner PAPER / LIVE
- LIVE readiness checklist (trades, kill switch, limits, keys status only)
- LIVE button disabled until exact phrase ENABLE LIVE TRADING
- One-click return to PAPER
- Metrics: latency, provider errors, AI budget, kill switch

## Verification (last known)

| Check | Result |
|-------|--------|
| pytest unit | 126 passed |
| ruff | passed |
| ASGI execution/monitoring | 200 |
| tsc --noEmit | exit 0 |
| vitest | 45 passed |
| vite build | exit 0 |

## Residual debt

GitHub Actions full tree, live Bybit, WS, Playwright, Tauri — see RELEASE_CHECKLIST.md.
