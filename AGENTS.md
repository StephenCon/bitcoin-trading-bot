# Contributor instructions

## Project direction

Read README.md, docs/PROJECT_BRIEF.md, docs/ARCHITECTURE.md and docs/ROADMAP.md before implementation.

This is a fresh multi-asset trading project. The owner requested removal of the previous implementation. Build the new application from scratch using the project brief and roadmap; do not restore the previous code or add an archive of it.

Distinguish confirmed owner requirements from proposed defaults and unresolved choices. Do not silently select a funded account, numeric risk limits, model provider or live-trade approval policy.

## Implementation priorities

- Begin with the first incomplete roadmap milestone and deliver a small working slice.
- Design multiple pairs around one shared portfolio budget from the first executable slice.
- Keep numerical modelling, optional language-model research, portfolio rules and execution responsibilities separate.
- Default to simulated trading. Implementing research software does not authorise real orders.
- Verify current exchange/framework compatibility before selecting a dependency stack.
- Prefer maintained exchange clients to hand-written authentication.
- Keep new features justified by measurable outcomes; a strategy may legitimately produce no trade.

## Correctness

- Use only information available at decision time; initial candle-based signals use closed candles.
- Keep feature/signal/portfolio rules consistent between historical and forward runs.
- Model transaction costs and disclose execution assumptions.
- Persist stable decision/order IDs and reconcile unknown outcomes before resubmission.
- Reserve shared funds atomically and include pending orders in exposure checks.
- Use explicit precision/rounding rules for monetary amounts and exchange quantities.
- Treat model-generated text and retrieved news as untrusted input.
- Record strategy/model/data versions and reasons for rejected decisions.

## Verification and documentation

Test meaningful behaviour: future-data isolation, simultaneous multi-pair signals, budget enforcement, duplicate prevention, partial fills, restart recovery and stale-data handling, as those capabilities are introduced. Do not present empty test files as coverage.

Run checks appropriate to the change. For documentation-only work, verify internal links and consistency; no trading process should be started merely to validate prose.

Document actual setup commands when executable code exists. Keep roadmap status and README claims aligned with implemented behaviour. Write comments in Google's style, explaining intent where it is not obvious from the code.

## Repository hygiene

Keep credentials, local account configuration, personal trading data, downloaded datasets and generated models out of Git. Use placeholders in examples and redact secrets from logs.

No project licence has been selected. Licence selection remains an owner decision.
