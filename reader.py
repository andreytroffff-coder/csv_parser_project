import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def read_csv(file_path: str | Path, delimiter: str = ",") -> list[dict[str, str]]:
    """Read a CSV file and return rows as dictionaries."""
    try:
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            return list(reader)
    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
        return []
    except Exception as e:
        logger.error("Error reading CSV file: %s", e)
        return []
