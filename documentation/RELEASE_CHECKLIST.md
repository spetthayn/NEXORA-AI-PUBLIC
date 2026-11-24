# NEXORA AI — Release Checklist (PC)

## 1. Repository & CI

```bash
cd nexora-ai
git add .
git commit -m "Phase 8 complete"
git push -u origin main
```

Open GitHub Actions → NEXORA AI CI. Do not claim green without the Actions log.

## 2. Database (Phase 0 schema)

```bash
docker compose -f docker-compose.phase0.yml up -d
bash scripts/apply_schema.sh
bash scripts/verify_db_triggers.sh
```

## 3. Playwright E2E & Tauri (Windows)

```bash
cd apps/web && npm ci && npx playwright install && npx playwright test
# Tauri: apps/desktop src-tauri → npm run tauri build
```

## 4. Environment & safe start (always PAPER first)

```env
XAI_API_KEY=
BYBIT_API_KEY=
BYBIT_API_SECRET=
NEXORA_CORS_ORIGINS=http://localhost:5173
```

```bash
export PYTHONPATH=.
uvicorn backend.app.main:app --reload --port 8000
cd apps/web && npm run dev
```

1. Open UI → Monitoring
2. Confirm PAPER / SIMULATION
3. Enable LIVE only after checklist + phrase ENABLE LIVE TRADING

## 5. Residual tech debt

- Full green GitHub Actions on complete tree
- Live Bybit from regions without blocks
- WebSocket streaming
- Playwright coverage gaps
- Tauri MSI/NSIS on Windows

## 6. Safety

- No private keys in git, logs, API JSON, or AI prompts
- Kill switch and daily loss limits stay active
