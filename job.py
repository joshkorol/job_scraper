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
    salary (int): the salary of the job
    company (str): the comapny of the job
    location (str): the location of the job
    type (Type Enum): onsite, hybrid, remote

    Returns:
    Job: a Job object
    """
    def __init__(self, salary: int, comapny: str, location: str, type: Type):
        self.salary = salary
        self.company = comapny
        self.location = location
        self.type = type