# Implementation roadmap

The owner requested a fresh start and a multi-asset direction. Milestones below are proposed implementation steps; completion must be backed by working code and evidence.

## Milestone 0 — Reset and project record

- [x] Record the multi-asset product direction and unresolved decisions.
- [x] Define proposed components, evaluation standards and implementation milestones.
- [x] Preserve the complete original prototype under legacy/coinbase-pro/.
- [x] Replace the root README and add contributor guidance.

Result: a documented starting point. No new trading application is implemented.

## Milestone 1 — Foundation and capability evaluation

- [ ] Evaluate candidate exchange/API and framework compatibility with the proposed spot-market scope.
- [ ] Record the framework choice, alternatives and evidence in a short architecture decision.
- [ ] Establish the supported runtime, dependency management, formatting and test tooling.
- [ ] Add validated configuration with paper execution as the default.
- [ ] Implement a first vertical slice: ingest or replay candles for at least two pairs, validate timestamps, generate a baseline signal and record a simulated decision.
- [ ] Document local setup and useful commands.

Acceptance: a reproducible local run using fixtures or public market data, with no funded account required. Two pairs share the same simulated budget. Replaying the same decision does not create a duplicate order. Missing/stale data produces a visible rejection. No live order client is invoked.

## Milestone 2 — Reproducible historical evaluation

- [ ] Store validated history, source metadata and point-in-time universe definitions where available.
- [ ] Implement common simulation accounting across all pairs.
- [ ] Model fees, spread, slippage and order-size constraints.
- [ ] Implement the moving-average baseline and predefined passive benchmarks.
- [ ] Add chronological evaluation and checks for future-data leakage.
- [ ] Produce an experiment report including assumptions, costs, returns, drawdown, exposure and trade count.
- [ ] Exercise simultaneous signals, insufficient funds, missing candles and execution failures.

Acceptance: the same data and configuration reproduce the same result. Future data cannot influence earlier decisions. Portfolio totals reconcile and aggregate allocations cannot exceed the available budget. Assumptions and data coverage gaps are included in the report.

## Milestone 3 — Multi-asset paper trading and dashboard

- [ ] Select a fixed initial universe of approximately 20–30 eligible pairs, reducing it if history or liquidity is inadequate.
- [ ] Add live market ingestion with data freshness and quality checks.
- [ ] Implement durable decisions, order intents, balance reservations and simulated fills.
- [ ] Implement portfolio constraints and restart/recovery behaviour.
- [ ] Show market eligibility, signals, decisions, positions, costs, equity and operational health.
- [ ] Compare forward results with historical assumptions.

Acceptance: the system recovers without duplicate orders, respects a shared budget and pauses new entries when data or state is uncertain. Dashboard balances and metrics reconcile with the event/order records. Everything is labelled as simulated.

## Milestone 4 — Numerical model challenger

- [ ] Define the prediction target, horizon and feature set.
- [ ] Train on chronological history with appropriate separation between labels and evaluation periods.
- [ ] Evaluate walk-forward performance and calibration against the baseline.
- [ ] Log experiments, versions and training intervals; retain an untouched final evaluation period.
- [ ] Compare results after trading and operating costs.
- [ ] Test staged retraining and rollback before model replacement.

Acceptance: report both improvements and failures. Promote a model only if it meets predefined evaluation criteria; otherwise retain the simpler baseline. No claim that machine learning must outperform it.

## Milestone 5 — Optional news and automated research

- [ ] Select sources/provider only after establishing a concrete use case and operating-cost budget.
- [ ] Store source links, publication times, ingestion times and deduplication decisions.
- [ ] Keep source content isolated from execution and configuration authority.
- [ ] Evaluate incremental value against the numerical-only system.
- [ ] Run generated strategies as versioned experiments; require evaluation before promotion.
- [ ] Measure latency and provider/data costs.

Acceptance: news-derived claims are traceable, hindsight limitations are disclosed and prospective results support any decision to retain the feature. Failure of a language-model service cannot bypass trading limits.

## Milestone 6 — Optional live pilot

This milestone requires a separate owner decision on live execution, capital, numeric limits and whether trades need individual approval. The documentation reset is not that authorisation.

- [ ] Agree the exchange/account, eligible assets, budget and operating limits.
- [ ] Implement and verify the chosen account's product/permission support.
- [ ] Reconcile balances, open orders, fills and restarts with the exchange.
- [ ] Exercise ambiguous submissions, partial fills, cancellations, outages and manual pause/recovery.
- [ ] Validate the pilot's monitoring, reporting and stop procedure.

Acceptance: enable only the explicitly chosen scope, with recorded operational checks and visibility into actual fees and fills. Successful simulation does not establish future profitability.

## First implementation task

Start with Milestone 1. Keep the delivery small enough to review: document the stack choice and produce a working multi-pair paper decision loop, with accounting and idempotency checks. Update the README to reflect what actually runs. Do not attempt every future capability in the first change.
