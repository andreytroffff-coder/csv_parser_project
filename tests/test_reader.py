from csv_parser.reader import read_csv


def test_read_csv_with_default_delimiter(tmp_path):
    file_path = tmp_path / "people.csv"
    file_path.write_text("name,age\nAlice,20\nBob,25\n", encoding="utf-8")

    rows = read_csv(file_path)

    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
    assert rows[1]["age"] == "25"


def test_read_csv_with_custom_delimiter(tmp_path):
    file_path = tmp_path / "cities.csv"
    file_path.write_text("city;country\nMoscow;Russia\nParis;France\n", encoding="utf-8")

    rows = read_csv(file_path, delimiter=";")

    assert len(rows) == 2
    assert rows[0]["country"] == "Russia"


def test_read_csv_returns_empty_list_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.csv"

    rows = read_csv(missing_file)

    assert rows == []
