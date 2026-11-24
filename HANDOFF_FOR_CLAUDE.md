# NEXORA AI — Handoff for Claude / ChatGPT (continue from this snapshot)

**Project:** NEXORA AI 2.0
**Owner:** spetthayn
**Public review repo:** https://github.com/spetthayn/NEXORA-AI-PUBLIC
**Archive:** NEXORA_AI_COMPLETE_RELEASE.zip
**Last status date:** 2026-11-24
**Implemented phases:** 0 → 8

Do not rewrite from scratch. Read this file + phase docs before changing architecture.

## 1. What this product is

Crypto market analysis platform with:
- Public market data (Bybit / Binance adapters + Mock)
- Quant indicators + multi-layer Vetter audit
- Hybrid AI analysis (Mock LLM + optional Grok via env key)
- Indicator Studio + historical backtests (no look-ahead)
- Adaptive Intelligence (review, drift, HITL parameter proposals)
- Paper trading + historical replay
- Controlled PAPER → LIVE gate (HITL phrase, env secrets)

Default is always simulation / PAPER. Real exchange order submit was not enabled in sandbox Phase 8.1.

Never promise guaranteed profit. Never invent prices when data is missing (no_data / insufficient_data).

## 2. Stack (fixed)

| Layer | Technology |
|-------|------------|
| Web | Vite + React 18 + TypeScript strict + Tailwind |
| Desktop | Tauri 2 foundation |
| Backend | Python, FastAPI (modular monolith) |
| Contracts | Pydantic → FastAPI OpenAPI → openapi_app.json |
| DB (Phase 0) | PostgreSQL / TimescaleDB + append-only candle triggers |
| Charts | TradingView Lightweight Charts |

## 3. Monorepo layout

```
nexora-ai/
  apps/web/
  apps/desktop/
  backend/app/           # FastAPI main
  backend/modules/       # domain modules
  packages/api_contracts/
  database/migrations/
  scripts/
  tests/
  documentation/
  .github/workflows/ci.yml
```

### Frontend routes
/, /charts, /analytics, /ai, /studio, /adaptive, /paper, /monitoring, /settings

### Backend key APIs
/health, /version,
/api/v1/instruments|candles|providers/status,
/api/v1/quant/indicators|audit,
/api/v1/ai/status|analyze,
/api/v1/studio/presets,
/api/v1/research/backtest|experiments,
/api/v1/adaptive/review|proposals,
/api/v1/paper/*, /api/v1/replay/*,
/api/v1/execution/mode, /api/v1/monitoring/metrics

## 4. Hard rules

1. No private keys in source, logs, API JSON, or AI prompts. Env only.
2. PAPER is default. LIVE needs checklist + phrase ENABLE LIVE TRADING + keys + min paper trades + kill switch clear.
3. AI must not override Vetter rejected. Insufficient data → explicit refuse.
4. No look-ahead in backtest/replay.
5. Candle versioning append-only (SQL triggers).
6. Mock / SIMULATION badges when using mock data.
7. Do not expand architecture without user approval.
8. Do not claim CI/Playwright/Tauri/live exchange success without actual runs.

## 5. How to run

```bash
cd nexora-ai
export PYTHONPATH=.
uvicorn backend.app.main:app --reload --port 8000

cd apps/web && npm ci && npm run dev
```

## 6. Verification

```bash
ruff check backend packages tests
pytest tests/unit -q
cd apps/web && npx tsc --noEmit && npx vitest run && npm run build
```

Last known audit (2026-11-24): 126 unit tests, 45 vitest, ruff/tsc/vite OK, ASGI smoke 200 on major routes.

## 7. Residual debt

1. Full GitHub Actions green on complete tree
2. Live Bybit public API (region blocks possible)
3. WebSocket streams
4. Playwright e2e completeness
5. Tauri Windows build
6. Real LIVE order submit only after explicit approval

## 8. Suggested next work

1. CI green
2. Live public data + Mock fallback
3. WebSocket with reconnect
4. Playwright critical paths
5. Tauri Windows build
6. Only then extend LiveExecutionAdapter for real orders

## 9. Module map

- data_adapters, quant, llm_gateway, ai_cost_manager
- indicator_studio, experiment_manager
- adaptive_intelligence, paper_trading, execution, monitoring
