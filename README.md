# Multi-asset crypto trading platform

A fresh-start project for researching, testing and eventually executing trading strategies across multiple cryptocurrencies.

**Status: planning baseline. The new application has not been implemented.** The repository contains the project plan and contributor guidance for a new implementation. The previous implementation has been removed from the current source tree.

## Direction

Build a system that can monitor multiple markets, compare opportunities, manage a shared portfolio and explain its decisions. Use numerical models for market predictions, language models for research and explanations, and deterministic code for portfolio limits and order execution.

Sophistication is a development goal; profitability is an unproven hypothesis that must be evaluated after costs and against simple benchmarks.

## Proposed first release

These are working defaults, not final investment or deployment decisions:

- Simulated spot trading on one exchange.
- A fixed initial universe of roughly 20–30 sufficiently liquid trading pairs, with adequate historical data.
- A shared portfolio budget across all pairs; observing a coin does not require holding it.
- A simple moving-average baseline, a machine-learning challenger and passive benchmarks.
- Historical evaluation followed by forward testing with live market data and simulated orders.
- A dashboard for signals, decisions, positions, execution, costs and portfolio performance.
- Explicit limits enforced outside all models; keeping funds unallocated is a valid outcome.

The exchange, exact markets, budget, risk thresholds, model providers, hosting and eventual trade-approval mode remain open. No live trading or funded exchange integration is part of this reset.

## Read next

| Document | Purpose |
| --- | --- |
| [Project brief](docs/PROJECT_BRIEF.md) | Product direction, proposed scope, trade-offs and unresolved decisions |
| [Architecture](docs/ARCHITECTURE.md) | Component responsibilities, data flow and candidate foundations |
| [Roadmap](docs/ROADMAP.md) | Ordered implementation milestones and acceptance criteria |
| [Contributor instructions](AGENTS.md) | Guidance for implementing the fresh application |

## Getting started

There is no new installation or start command yet. The first implementation milestone is the foundation and exchange-capability evaluation described in the roadmap. Add working setup instructions when that milestone lands.

Keep credentials, local configuration, account data, trained models and downloaded datasets out of Git. The project licence has not been selected.
