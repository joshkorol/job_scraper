#!/miniconda3/bin/python
from selenium import webdriver
from bs4 import BeautifulSoup
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
    # TODO keep in mind the strings will need %20 instead of spcaes
    driver = webdriver.Chrome()
    driver.get('https:/www.dice.com')
    # find releveant elements
    input_element = driver.find_element_by_id('typeaheadInput')
    input_element.send_keys('Software Engineer')
    button_element = driver.find_element_by_id('submitSearch-button')
    button_element.click()

    driver.quit()