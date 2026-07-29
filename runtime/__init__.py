"""Runtime services: per-run context and file-based state.

* :class:`RunContext` stamps every pipeline run with a ``run_id`` and
  ``batch_id`` and owns the run's output directory + lineage record.
* :class:`FileState` persists the baselines the stateful quality checks need
  (schema snapshots for schema-drift, row-count history for volume-drift) as
  plain files — no database, per the "files only" decision.
"""

from runtime.run_context import RunContext
from runtime.state import FileState

__all__ = ["RunContext", "FileState"]
