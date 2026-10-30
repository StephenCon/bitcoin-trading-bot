# Project brief

Recorded: 30 October 2026.

## Confirmed direction

The owner wants to start again from the existing bitcoin-trading-bot repository and explore a substantially more capable system using advances in machine learning and language models. The scope includes multiple cryptocurrencies rather than a Bitcoin-only bot.

This commit records the direction and implementation plan. It does not establish that a strategy is profitable, select an exchange or authorise live orders.

## Product goal

Research and evaluate whether a system can select useful trading opportunities across a defined market universe while controlling total portfolio exposure and making decisions inspectable.

The product should answer:

- What markets are being monitored, and which are eligible to trade?
- Why did the system enter, exit or decline a trade?
- What information was actually available when it decided?
- What did fees, spread and execution differences cost?
- Did a strategy improve results over simple alternatives, and at what level of loss and volatility?
- Is a weak result caused by the strategy, a model, market data or order execution?

## Capabilities

| Capability | Intended behaviour |
| --- | --- |
| Market monitoring | Collect prices, candles, volume and market metadata; add order-book inputs only when justified by a tested strategy. |
| Eligibility filtering | Reject markets with inadequate history, stale data, insufficient liquidity, excessive spread or incompatible trading rules. |
| Predictive models | Estimate defined outcomes over an explicit horizon and measure accuracy and calibration on unseen data. |
| News analysis | Extract events and cited claims from timestamped sources; evaluate whether those features improve results. |
| Strategy research | Propose and compare strategies through recorded, reproducible experiments. |
| Opportunity ranking | Compare estimated returns after costs, uncertainty and portfolio constraints; allow no trade. |
| Portfolio management | Allocate one shared budget, account for open orders and positions, and limit concentration in related exposures. |
| Trade management | Validate, submit, track and reconcile orders, partial fills, cancellations and failures. |
| Dashboard | Show the watchlist, decisions, positions, balances, costs, performance and operational health. |

News analysis, automated strategy generation and advanced order-book features belong to later milestones. They are not requirements for the first usable paper-trading release.

## Proposed first-release scope

- One exchange and one settlement/quote currency, chosen after confirming accessible markets, API support and costs.
- Spot markets only; no borrowing, leverage, derivatives or cross-exchange arbitrage.
- Approximately 20–30 eligible pairs as an initial engineering target, subject to data coverage and available capital in simulation.
- A documented initial universe selected before evaluating results.
- Historical testing and simulated forward trading before considering live execution.
- A transparent moving-average baseline and one numerical machine-learning challenger.
- Shared portfolio accounting, persistent state and a decision log.
- A dashboard showing both individual trades and the whole portfolio.
- Core operation independent of a paid language-model service.

These are proposed defaults. The exact asset count is not an allocation recommendation or a claimed optimum.

## How the intelligence is divided

Numerical models produce explicit, testable market estimates. A language model may extract news events, suggest research hypotheses and explain recorded decisions with sources. It does not invent account balances, produce authoritative risk limits or bypass the execution rules.

Track whether a model's confidence corresponds to observed outcomes. Do not display a language model's self-reported confidence as a probability of trading success.

Model updates and generated strategies must pass evaluation before promotion. Retraining does not automatically justify replacing a model in production.

## Evaluation

Compare strategies over the same dates, starting funds, market universe and execution-cost assumptions:

1. Uninvested cash in the selected quote currency.
2. Buy-and-hold Bitcoin, where an accessible market and adequate data are available.
3. A predefined equal-weight buy-and-hold basket from the selected universe.
4. The original moving-average idea, reimplemented correctly.
5. A machine-learning challenger.

Report returns after fees, spread and slippage alongside maximum drawdown, volatility, turnover, exposure, trade count and execution failures. Include hosting, data and model costs in the operating-cost assessment. A higher gross return alone is insufficient evidence of improvement.

Use chronological training and evaluation windows. Keep future labels and unfinished candles out of decision inputs. Separate model tuning from final testing and prevent label horizons from overlapping evaluation boundaries. Record attempted experiments and reserve an untouched evaluation period to reduce selection bias.

Preserve point-in-time market eligibility where possible. Choosing today's survivors for every historical period can exaggerate results. State coverage gaps, including missing delisted assets. Historical news tests must use information available at the time and account for possible hindsight from a language model's training; prospective testing is required before trusting that feature.

Paper fills are simulations. Differences from real queue position, liquidity and execution must be visible in reports.

## Trade-offs and failure modes

- More assets expand the opportunity set and also increase training, storage, API and operational costs.
- Multiple holdings can behave like one concentrated position if they move together.
- Illiquid markets can erase a predicted advantage through spread and slippage.
- More strategies and parameter searches increase the chance of finding lucky historical results.
- Market behaviour can change after training; retraining may also make a model worse.
- Stale data, exchange outages, ambiguous order responses and restarts can cause unintended exposure without reconciliation.
- News can be false, duplicated, late or manipulative. Treat all retrieved content as untrusted input.
- Exit triggers and automatic pauses cannot guarantee a maximum realised loss during gaps or outages.
- Increased complexity must earn its place through measured improvements.

## Decisions still open

| Decision | Working position |
| --- | --- |
| Exchange and accessible products | Evaluate current support; Coinbase Advanced is a candidate because of the original project, not a commitment. |
| Framework | Compare Freqtrade/FreqAI with a smaller custom Python service before choosing. |
| Exact assets and quote currency | Decide from market availability, history, liquidity, cost and account constraints. |
| Model/provider | No provider selected; add a language model only for a measured use case. |
| Capital and numeric limits | Unspecified. Use clearly labelled simulated funds during development. |
| Eventual execution mode | Owner has not chosen autonomous trading within limits versus approval of individual trades. |
| Deployment and credentials | Unspecified; no production environment or funded account is configured. |
| Project name and licence | Existing repository name retained; choose branding and licence separately. |

## Reference material

Checked during planning on 30 October 2026; verify again when implementing integrations.

- [FreqAI documentation](https://docs.freqtrade.io/en/stable/freqai/)
- [Freqtrade market selection and filters](https://www.freqtrade.io/en/stable/plugins/)
- [Freqtrade backtesting](https://www.freqtrade.io/en/stable/backtesting/)
- [Freqtrade lookahead analysis](https://www.freqtrade.io/en/stable/lookahead-analysis/)
- [Coinbase Advanced Python SDK](https://coinbase.github.io/coinbase-advanced-py/index.html)
