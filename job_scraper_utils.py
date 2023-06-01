#!/Users/joshkorol/miniconda3/bin/python3
import time
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
TODO add documentation
"""
def scrape_dice():
    # Create ChromeOptions object
    options = Options()
    #options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    options.add_experimental_option("detach", True)
    chrome_driver = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chrome_driver, service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.dice.com')

    # find releveant elements
    # TODO: implement location, job name config
    input_job_element = driver.find_element(By.ID, "typeaheadInput").send_keys("Software Engineering")
    input_location_element = driver.find_element(By.ID, "google-location-search").send_keys("Atlanta, GA, USA"+ Keys.ENTER)
    
    # - - - filter results - - -
    # TODO: implement control about hybrid/remote
    # exclude remote options
    time.sleep(3)
    exclude_remote_button = driver.find_element(By.XPATH, '//button[@aria-label="Filter Search Results by Exclude Remote"]')
    exclude_remote_button.click()

    work_from_home_button = driver.find_element(By.XPATH, '//button[@aria-label="Filter Search Results by Work From Home Available"]')
    work_from_home_button.click()
    print("Completed")
    # now search through query
    driver.quit()