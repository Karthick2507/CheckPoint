"""Create the quick-start sqlite database.

Builds a small `orders` source and an empty `orders_clean` target, seeded so the
demo pipeline shows every part of the framework working:

* today's batch (B2) is mostly good, so the pipeline runs end to end;
* it contains one NULL customer and one negative amount, so the validation
  gates produce real failures and quarantine files;
* an earlier batch (B1) exists, so batch-scoping is visibly doing something.

Run:  python examples/quickstart/seed.py
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path(__file__).parent / "quickstart.db"


def main() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    now = datetime.now()
    recent = (now - timedelta(hours=1)).isoformat(timespec="seconds")
    older = (now - timedelta(days=3)).isoformat(timespec="seconds")

    con = sqlite3.connect(DB_PATH)
    con.execute(
        """
        CREATE TABLE orders (
            order_id     INTEGER,
            customer_id  TEXT,
            amount       REAL,
            created_at   TEXT,
            batch_id     TEXT
        )
        """
    )
    con.execute(
        """
        CREATE TABLE orders_clean (
            id        INTEGER,
            customer  TEXT,
            amount    REAL,
            loaded_at TEXT
        )
        """
    )
    con.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
        [
            # yesterday's batch — clean
            (1, "C001", 100.0, older, "B1"),
            (2, "C002", 250.0, older, "B1"),
            (3, "C003", 175.5, older, "B1"),
            # today's batch — two deliberate defects
            (4, "C004", 300.0, recent, "B2"),
            (5, None, 120.0, recent, "B2"),      # NULL customer  -> completeness fails
            (6, "C006", -50.0, recent, "B2"),    # negative amount -> range fails
            (7, "C007", 410.0, recent, "B2"),
        ],
    )
    con.commit()
    con.close()

    print(f"Created {DB_PATH}")
    print("  orders:       7 rows (batch B1 = 3 clean, batch B2 = 4 with 2 defects)")
    print("  orders_clean: empty (the pipeline fills it)")
    print("\nNext:")
    print("  python -m cli run-pipeline \\")
    print("    --pipeline examples/quickstart/pipeline.yml \\")
    print("    --connections-dir examples/quickstart/connections \\")
    print("    --state-dir examples/quickstart/state")


if __name__ == "__main__":
    main()
