import argparse

from .analyzer import csv_analyzer, get_size
from .llm import DEFAULT_PROMPT, generate_content
from .logging_conf import configure_logging
from .reader import read_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze CSV files and generate a Gemini summary."
    )
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument(
        "--column",
        required=True,
        help="Column name for frequency analysis",
    )
    parser.add_argument(
        "--delimiter",
        default=",",
        help="Delimiter used in the CSV file",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Number of rows to send to Gemini",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    configure_logging()

    result = csv_analyzer(args.file_path, args.column, args.delimiter)
    if not result:
        print("Could not analyze the CSV file. Check logs for details.")
        return 1

    size = get_size(args.file_path)
    print(f"Rows: {result['rows']}")
    print(f"Columns: {', '.join(result['columns'])}")
    print(f"Value counts for '{args.column}': {result['value_counts']}")
    print(f"File size: {size} bytes")

    data = read_csv(args.file_path, args.delimiter)[:args.limit]
    content = generate_content(DEFAULT_PROMPT, data)
    if content is None:
        print("AI summary was not generated. Check logs for details.")
        return 1

    print("AI summary saved to groq_analysis_response.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#example usage:
# python -m csv_parser.main .\exam_results.csv  --column score --delimiter ',' 
# python -m csv_parser.main .\exam_results.csv  --column score --delimiter ',' --limit 10
