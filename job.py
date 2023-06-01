from enum import Enum
#  TODO: outline requirements for job class
"""
Universal Job class used in list returned by scraper
"""
class Job:
    """
    Enum for Job type
    """
    class Type(Enum):
        ONSITE = 1
        HYBRID = 2
        REMOTE = 3

    """
    Constructor for Job

    Parameters:
    title (string): the title of the job
    salary (int): the salary of the job
    company (str): the comapny of the job
    location (str): the location of the job
    type (Type Enum): onsite, hybrid, remote
    desc (str): the description of the job

    Returns:
    Job: a Job object
    """
    def __init__(self, role: str, salary: int, comapny: str, location: str, type: Type, desc: str):
        self.title = role
        self.salary = salary
        self.company = comapny
        self.location = location
        self.type = type
        self.desc = desc