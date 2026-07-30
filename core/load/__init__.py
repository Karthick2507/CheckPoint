"""Load stage: write into a target DataSource.

Two strategies:

* :class:`~core.load.loader.Loader` — row-based, for moving data *between*
  systems (Presto -> Snowflake).
* :class:`~core.load.pushdown.PushdownLoader` — ``INSERT … SELECT`` executed in
  the warehouse, for same-warehouse work at any scale.
"""

from core.load.loader import LoadResult, Loader
from core.load.pushdown import PushdownLoader, PushdownResult

__all__ = ["Loader", "LoadResult", "PushdownLoader", "PushdownResult"]
