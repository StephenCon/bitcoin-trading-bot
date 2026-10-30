# Proposed architecture

Status: design proposal. No new runtime or framework has been selected.

## Boundaries

The initial system should be a modular application with clear interfaces. Introduce separate services only when isolation, workload or deployment requirements justify them.

| Component | Responsibility | Boundary |
| --- | --- | --- |
| Exchange adapter | Discover products, ingest market data, expose balances and order operations where enabled. | Isolate exchange-specific authentication, precision, limits and API behaviour. |
| Data store | Persist candles, metadata, quality checks and source timestamps. | Distinguish event time, receipt time and the time information became usable. |
| Market universe | Track approved pairs, eligibility and reasons for exclusion. | Monitoring and trading eligibility are separate states. |
| Feature pipeline | Produce reproducible inputs from information available at decision time. | Identical definitions in research and forward operation. |
| Strategy/model layer | Produce signals, horizons and measured uncertainty. | Has no credentials or direct order-submission access. |
| Opportunity ranking | Compare eligible signals after expected costs. | Uses a common horizon or explicitly adjusts for differing horizons. |
| Portfolio/risk engine | Enforce balance reservations, exposure limits and trade eligibility. | Deterministic rules have final authority over proposed orders. |
| Paper/live executor | Apply a chosen execution mode, track order lifecycle and reconcile fills. | Paper trading is the default; live integration is a later milestone. |
| Audit log and dashboard | Explain decisions and display portfolio and system state. | Render recorded facts; distinguish simulation from real execution. |
| Optional research/news layer | Suggest experiments, extract cited events and explain existing records. | Untrusted source content cannot alter configuration or execute actions. |

## Decision cycle

1. Ingest market updates and reject stale, incomplete or inconsistent inputs.
2. Build features for eligible pairs using closed candles in the initial strategy.
3. Obtain numerical signals and estimates from the current approved model/strategy version.
4. Rank opportunities after estimated costs, considering existing portfolio exposure.
5. Evaluate portfolio limits and reserve available funds atomically.
6. Create a uniquely identified order intent, then submit through the configured executor.
7. Reconcile order status and fills, update accounting and release reservations as appropriate.
8. Persist the reason for every accepted and rejected decision.

The system may produce zero orders. A scanner must not create a requirement to deploy the entire budget.

## Shared portfolio

All pairs consume one capital pool. Independent per-coin loops must not each assume the full balance is available.

Portfolio accounting should include available and reserved cash, held assets, pending buys/sells, fees, realised profit/loss and marked-to-market equity. Handle precision and minimum-order rules without binary floating-point rounding errors in financial accounting.

Enforce configurable per-asset exposure, aggregate exposure, open-position and pending-order limits. Add measured correlation/group constraints to avoid repeatedly buying the same underlying market exposure.

Numeric risk limits require an explicit configuration and validation. A loss trigger stops new entries and follows a defined policy for pending orders and existing holdings; it is not a guaranteed loss ceiling.

## Persistence and execution

Record at least:

- Market-data timestamps, missing intervals, source and eligibility snapshots.
- Strategy/model versions, feature definitions and training/evaluation intervals.
- Decision IDs, signal inputs, exclusions and portfolio checks.
- Order intents, exchange IDs where relevant, reservations, partial fills, fees and final status.
- Portfolio snapshots and operational events.

Use stable decision/order identifiers to prevent duplicate submissions after retries or restarts. A timed-out submission has an unknown outcome until reconciled. Do not blindly retry it.

Pause new entries when inputs are stale or account/order state is uncertain. Define recovery and management of existing positions explicitly. Keep secrets outside Git and logs; future exchange credentials should have only the required permissions and no withdrawal authority.

## Historical and forward testing

Use common feature, signal and portfolio rules across historical simulation and forward paper trading. Execution adapters may differ, but assumptions must be explicit and versioned.

Historical evaluation must model fees, spread, slippage and capital contention. Model partial or rejected fills when data supports them, or disclose the simplified assumptions. Never execute a close-derived signal earlier than the data would have become available.

A paper-trading dashboard must label simulated balances and fills. Test portfolio-level behaviour when several pairs signal at the same time.

## Candidate foundations

### Freqtrade and FreqAI

Benefits: existing market-data handling, backtesting, dry-run operation and per-pair model training/retraining. This could shorten time to a useful research platform.

Trade-offs: strategy lifecycle, supported exchanges, data formats, portfolio behaviour and UI integration need evaluation against this brief. Verify the selected exchange and spot markets before committing to this stack.

Documented limitation at planning time: FreqAI does not support pair lists that dynamically add/remove assets during a running instance. It expects the required history and models to be available. A stable approved universe can still be ranked; adding assets needs a controlled download, training and activation workflow. Do not promise unrestricted automatic discovery as an existing framework feature.

### Custom Python application

Benefits: direct control over portfolio rules, exchange adapters and dashboard integration.

Trade-offs: data validation, simulation, persistence, order lifecycle, retries and reconciliation all need implementation and meaningful tests. Use maintained exchange SDKs where appropriate rather than copying legacy request-signing code.

Coinbase Advanced's official Python SDK is a candidate if Coinbase is selected. Its existence does not prove that a particular account, region or framework supports all desired products.

## Proposed layout after stack selection

Choose the actual layout during the foundation milestone. Expected responsibilities are configuration, market data, universe selection, features/models, strategies, portfolio/risk, execution, persistence, reporting and a dashboard.

Keep the new application separate from legacy/. Do not introduce empty packages, infrastructure or dependency files solely to imitate the old layout. Provide working setup and test commands with the first executable slice.
