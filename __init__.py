# csv_parser package
from .reader import read_csv
from .analyzer import csv_analyzer, get_size
from .logging_conf import configure_logging

__all__ = ['read_csv', 'csv_analyzer', 'get_size', 'generate_content', 'configure_logging']


def __getattr__(name):
    if name == "generate_content":
        from .llm import generate_content

        return generate_content
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
