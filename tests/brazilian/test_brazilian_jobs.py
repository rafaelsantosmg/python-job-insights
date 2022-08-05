from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    report = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for item in report:
        assert "title" in item
        assert "salary" in item
        assert "type" in item
