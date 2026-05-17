import logging
import os
from pathlib import Path

from .reader import read_csv

logger = logging.getLogger(__name__)


def csv_analyzer(
    file_path: str | Path,
    column_name: str,
    delimiter: str = ",",
) -> dict[str, object] | None:
    """Analyze a CSV file and return summary information."""
    data = read_csv(file_path, delimiter)
    if not data:
        logger.warning("No data found in the CSV file.")
        return None

    columns = list(data[0].keys())
    logger.info("Total rows: %s", len(data))
    logger.info("Columns: %s", ", ".join(columns))

    if column_name not in columns:
        logger.warning("Column '%s' not found in the CSV file.", column_name)
        return None

    value_counts: dict[str, int] = {}
    for row in data:
        value = row.get(column_name, "")
        value_counts[value] = value_counts.get(value, 0) + 1

    logger.info("Value counts for column '%s':", column_name)
    for value, count in value_counts.items():
        logger.info("%s: %s", value, count)

    return {
        "rows": len(data),
        "columns": columns,
        "value_counts": value_counts,
    }


def get_size(file_path: str | Path) -> int:
    """Return the CSV file size in bytes."""
    size = os.path.getsize(file_path)
    logger.info("File size: %s bytes", size)
    return size
