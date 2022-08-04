from src.jobs import read


def get_unique_job_types(path):
    jobs_read = read(path)
    jobs_types = set()
    for job_type in jobs_read:
        jobs_types.add(job_type["job_type"])
    return list(jobs_types)


def filter_by_job_type(job, job_type):
    job_job_type = list()
    for type in job:
        if type["job_type"] == job_type:
            job_job_type.append(type)
    return job_job_type


def get_unique_industries(path):
    jobs_read = read(path)
    jobs_industry = set()
    for job_industry in jobs_read:
        if len(job_industry["industry"]) != 0:
            jobs_industry.add(job_industry["industry"])
    return list(jobs_industry)


def filter_by_industry(jobs, industry):
    job_industry = list()
    for job in jobs:
        if job["industry"] == industry:
            job_industry.append(job)
    return job_industry


def get_max_salary(path):
    jobs_read = read(path)
    max_salaries = list()
    for job_max_salary in jobs_read:
        if (
            len(job_max_salary["max_salary"]) != 0
            and job_max_salary["max_salary"] != "invalid"
        ):
            max_salaries.append(int(job_max_salary["max_salary"]))
    max_salary = max(max_salaries)
    return max_salary


def get_min_salary(path):
    jobs_read = read(path)
    min_salaries = list()
    for job_min_salary in jobs_read:
        if (
            len(job_min_salary["min_salary"]) != 0
            and job_min_salary["min_salary"] != "invalid"
        ):
            min_salaries.append(int(job_min_salary["min_salary"]))
    min_salary = min(min_salaries)
    return min_salary


def verify_matches_salary(min_salary, max_salary, salary):
    if not isinstance(salary, int):
        raise ValueError
    if not isinstance(min_salary, int) or not isinstance(max_salary, int):
        raise ValueError
    if min_salary > max_salary:
        raise ValueError


def matches_salary_range(job, salary):
    try:
        verify_matches_salary(job["min_salary"], job["max_salary"], salary)
        return job["min_salary"] <= salary <= job["max_salary"]
    except KeyError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    filter_jobs = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_jobs.append(job)
        except ValueError:
            continue
    return filter_jobs
