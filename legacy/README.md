# Original Coinbase Pro prototype

This directory preserves the original project as a historical reference. It is not the new application's entry point and is not a runnable foundation for live trading.

The complete tracked tree from commit [3d411ec868e9b179789bb449c328e1674decc8a1](https://github.com/StephenCon/bitcoin-trading-bot/commit/3d411ec868e9b179789bb449c328e1674decc8a1) is retained unchanged in [coinbase-pro](coinbase-pro/), including its original README, empty test files and ignore rule. Untracked local credentials were not part of the repository.

## Original behaviour

The prototype fetches hourly Coinbase Pro candles, calculates a 20-period simple moving average, checks the most recent crossing and attempts one fixed-size market order. It runs once and exits.

## Findings from static review

- The executor passes an order dictionary to a request-signing helper that concatenates it with strings, causing a TypeError before submission.
- Buy/sell direction is calculated but never included as the order's side field.
- The signing helper and request-body serialisation do not consistently use identical bytes.
- requirements.txt is empty despite pandas and requests imports.
- config/settings.py is intentionally ignored and absent; the README example also omits API_PASSPHRASE.
- There is no processed-candle/order persistence, so repeated runs can repeat a trade signal.
- There are no account/position checks, fill reconciliation, paper-trading engine or performance evaluation.
- The test modules and base-strategy file are empty.
- The historical-data function accepts a lookback argument without using it.
- The README contains malformed Markdown, a placeholder clone URL and an unsupported reference to a missing MIT licence file.

The code was inspected rather than executed. These notes are not an exhaustive security audit or proof of strategy performance.

Reimplement any useful strategy ideas against the new project's interfaces and evaluation rules. The archived setup instructions and API details are historical.
