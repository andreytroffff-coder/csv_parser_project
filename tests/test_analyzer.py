from csv_parser.analyzer import csv_analyzer, get_size


def test_csv_analyzer_counts_values(tmp_path):
    file_path = tmp_path / "cities.csv"
    file_path.write_text("city\nMoscow\nParis\nMoscow\n", encoding="utf-8")

    result = csv_analyzer(file_path, "city")

    assert result is not None
    assert result["rows"] == 3
    assert result["columns"] == ["city"]
    assert result["value_counts"]["Moscow"] == 2


def test_csv_analyzer_returns_none_for_unknown_column(tmp_path):
    file_path = tmp_path / "cities.csv"
    file_path.write_text("city\nMoscow\nParis\n", encoding="utf-8")

    result = csv_analyzer(file_path, "country")

    assert result is None


def test_get_size_returns_file_size(tmp_path):
    file_path = tmp_path / "sample.csv"
    file_path.write_text("name\nAlice\n", encoding="utf-8")

    size = get_size(file_path)

    assert size > 0
