#!/Users/joshkorol/miniconda3/bin/python3
import time
from typing import List, Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
"""
Copyright Josh Korol 2023
All Rights Reserved

This file will include helper functions for job_scraper.py

Usage:
- Run the script with the following command: python my_script.py
- Pass the input file path as a command-line argument.
"""

"""
TODO add documentation
"""
def scrape_job_listings():
    # TODO: handle params from config file, etc.
    print()

"""
Creates a Chrome driver object.

Args: 
    chrome_drive_directory (str): The directory to your chrome driver, default

Returns:

"""
def create_driver(chrome_driver_directory: str="/usr/local/bin/chromedriver", driver_options: List[List[Any]]=[["e","detach", True]]) -> webdriver:
    options = Options()
    for list in driver_options:
        params = list[1:]
        if list[0] == 'e':
            options.add_experimental_option(*params)
        else:
            options.add_argument(*params)
    return webdriver.Chrome(chrome_driver_directory, service=Service(ChromeDriverManager().install()), options=options)
 """
Calculates the square of a given number.

Args:
    query_options (Dict[str, List[str]]): The user's options for the query
        key (str): The name of the query option
        val (List[str]): The values for the query option

        REMOTE OPTIONS:
        "remote" -> [remote_only, exclude_remote, work_from_home]
        "employment_type" -> [full_time, part_time, contract, third_party]
Returns:
    
"""
def scrape_dice(query_options: List[Dict[str, List[str]]]=None):
    driver = create_driver()
    driver.get('https://www.dice.com')

    # find releveant elements
    # TODO: implement location, job name config
    input_job_element = driver.find_element(By.ID, "typeaheadInput").send_keys("Software Engineering")
    input_location_element = driver.find_element(By.ID, "google-location-search").send_keys("Atlanta, GA, USA"+ Keys.ENTER)
    
    # - - - filter results - - -
    # TODO: implement control about hybrid/remote
    # REMOTE OPTIONS
    """
    Helper function for clicking button
    
    Args:
        key (str): Option key
        by (By): By enum for the find_element() method
        value (str): Value of the find_element() method
    """
    def click_button(key: str, by: By, value: str):
        if key == "remote":
            driver.find_element(by, '//span[contains(text(), "{value}")]//button[@aria-label="Filter Search Results by {value}"]').click()
        elif key == "employment_type":
            driver.find_element(by, value)

    time.sleep(3)
    remote_only, exclude_remote, work_from_home = query_options["remote"]
    if remote_only:
        click_button(By.XPATH, "Remote Only")
    if exclude_remote:
         click_button(By.XPATH, "Exclude Remote")
    if work_from_home:
        click_button(By.XPATH, "Work From Home Available")

    print("Completed Remote Options")
    # EMPLOYMENT TYPE
    full_time, part_time, contract, third_party = query_options["employment_type"]



    # now search through query