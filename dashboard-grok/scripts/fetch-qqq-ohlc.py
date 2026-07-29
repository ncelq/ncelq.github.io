#!/usr/bin/env python3
"""Fetch QQQ daily OHLC from Yahoo and write dashboard-grok/qqq-ohlc.json."""

from __future__ import annotations

import argparse
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# dashboard-grok/scripts/ → repo root
ROOT_DEFAULT = Path(__file__).resolve().parents[2]
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def fetch_yahoo(range_: str = "6mo") -> dict:
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/QQQ?interval=1d&range={range_}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    result = payload["chart"]["result"][0]
    ts = result["timestamp"]
    quote = result["indicators"]["quote"][0]
    days = []
    for t, o, h, low, c, v in zip(
        ts,
        quote["open"],
        quote["high"],
        quote["low"],
        quote["close"],
        quote["volume"],
    ):
        if o is None or c is None:
            continue
        day = datetime.fromtimestamp(t, timezone.utc).astimezone(
            ZoneInfo("America/New_York")
        ).strftime("%Y-%m-%d")
        days.append(
            {
                "date": day,
                "open": float(o),
                "high": float(h) if h is not None else float(o),
                "low": float(low) if low is not None else float(c),
                "close": float(c),
                "volume": int(v) if v is not None else 0,
            }
        )
    return {
        "symbol": "QQQ",
        "source": "yahoo-finance-chart",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "days": days,
    }


def write_ohlc(repo_root: Path, range_: str = "6mo") -> Path:
    out = repo_root / "dashboard-grok" / "qqq-ohlc.json"
    data = fetch_yahoo(range_=range_)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT_DEFAULT)
    parser.add_argument("--range", default="6mo")
    args = parser.parse_args()
    path = write_ohlc(args.root.resolve(), range_=args.range)
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"Wrote {path} ({len(data['days'])} days)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
