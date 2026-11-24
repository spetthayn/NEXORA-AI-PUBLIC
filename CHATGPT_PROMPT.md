# Prompt for ChatGPT (copy-paste)

Repository (temporary public): https://github.com/spetthayn/NEXORA-AI-PUBLIC

Also attach if possible: NEXORA_AI_COMPLETE_RELEASE.zip from the project owner.

---

Продолжай проект NEXORA AI 2.0.

Сначала прочитай в репозитории / архиве:
1) CLAUDE_START_HERE.md
2) documentation/HANDOFF_FOR_CLAUDE.md (или HANDOFF_FOR_CLAUDE.md в корне)
3) documentation/RELEASE_CHECKLIST.md
4) documentation/PHASE_8.md

Контекст:
- Реализованы Phase 0–8 (foundation → market data → quant/AI → studio → adaptive → paper/replay → monitoring + PAPER→LIVE gate).
- Стек: Vite+React+TypeScript strict, FastAPI, Tauri foundation, PWA, Mock/Bybit/Binance public data.
- По умолчанию PAPER/SIMULATION. LIVE только через чек-лист + точную фразу ENABLE LIVE TRADING + ключи из env.
- Не переписывай архитектуру с нуля. Не выдумывай цены при no_data/insufficient_data. Секреты только из env.

Задачи:
1) Краткий аудит: что есть, что в residual debt (CI, live Bybit, WS, Playwright, Tauri).
2) Как прогнать: ruff, pytest tests/unit, apps/web tsc/vitest/vite build.
3) Предложи следующий конкретный шаг и жди моего подтверждения.

Отвечай на русском. Честно пиши, какие файлы реально видел.
