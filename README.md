# CSV Parser

`csv_parser` is a small CLI project for reading CSV files, showing basic file statistics, and generating a short AI summary from the first rows of the dataset.

## Features

- Reads CSV files with a configurable delimiter
- Shows row count, columns, and file size
- Calculates value counts for a selected column
- Sends the first rows of the dataset to Groq for a text summary

## Project Structure

```text
csv_parser/
|-- __init__.py
|-- analyzer.py
|-- llm.py
|-- logging_conf.py
|-- main.py
|-- reader.py
|-- requirements.txt
|-- tests/
```

## Requirements

- Python 3.10+
- A Groq API key stored in an environment variable

## Installation

```bash
python -m venv .venv
pip install -r csv_parser/requirements.txt
```

## Environment Variables

Create a `.env` file in the `csv_parser` folder and add:

```env
GROQ_API_KEY=your_api_key_here
# Optional:
GROQ_MODEL=llama-3.3-70b-versatile
```

## Run

From the parent directory of `csv_parser`, run:

```bash
python -m csv_parser.main path/to/file.csv --column city
```

Useful options:

- `--delimiter ";"` for custom CSV delimiters
- `--limit 10` to change how many rows are sent to Groq

### Main Examples

Run with a regular comma-separated CSV:

```bash
python -m csv_parser.main data.csv --column city
```

Run with a semicolon-separated CSV:

```bash
python -m csv_parser.main data.csv --column city --delimiter ";"
```

Run with a different row limit for Groq:

```bash
python -m csv_parser.main reports/sales.csv --column region --limit 10
```

Run with all main options together:

```bash
python -m csv_parser.main reports/sales.csv --column region --delimiter ";" --limit 15
```

## Example Workflow

1. Start the program with `python -m csv_parser.main data.csv --column city`
2. Review the row count, columns, and value counts in the terminal
3. Review logs in `csv_reader.log`
4. Review the AI summary in `groq_analysis_response.txt`

## Tests

Run tests from the parent directory:

```bash
pytest csv_parser/tests
```

### Test Examples

Run all tests:

```bash
python -m pytest csv_parser/tests
```

Run only reader tests:

```bash
python -m pytest csv_parser/tests/test_reader.py
```

Run only analyzer tests:

```bash
python -m pytest csv_parser/tests/test_analyzer.py
```

Run one group of tests by name:

```bash
python -m pytest csv_parser/tests -k analyzer
```

## Notes

- Do not commit real API keys to the repository.
- Groq summary generation requires `GROQ_API_KEY`, but CSV parsing and analysis logic are testable separately.
