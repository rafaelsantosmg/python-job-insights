from src.sorting import sort_by

JOBS = [
    {"min_salary": 3000, "max_salary": 9000, "date_posted": "2022-02-20"},
    {"min_salary": 5000, "max_salary": 15000, "date_posted": "2022-12-13"},
    {"min_salary": 2000, "max_salary": 6000, "date_posted": "2022-08-07"},
    {"min_salary": 4000, "max_salary": 12000, "date_posted": "2022-06-25"},
]

JOBS_SORT = [
    {"min_salary": 2000, "max_salary": 6000, "date_posted": "2022-08-07"},
    {"min_salary": 3000, "max_salary": 9000, "date_posted": "2022-02-20"},
    {"min_salary": 4000, "max_salary": 12000, "date_posted": "2022-06-25"},
    {"min_salary": 5000, "max_salary": 15000, "date_posted": "2022-12-13"},
]


def test_sort_by_criteria():
    sort_by(JOBS, "min_salary")
    assert JOBS_SORT == JOBS
