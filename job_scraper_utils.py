#!/usr/bin/env python
import requests
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

    # send get req
    response = requests.get(url)
    # create object to parse htmld
    soup = BeautifulSoup(response.content, 'html.parser')
    job_elements = soup.find_all('div', class_='job-listing')

"""
TODO add documentation
"""
def scrape_dice():
    response = requests.get("dice.com")
    # create object to parse htmld
    soup = BeautifulSoup(response.content, 'html.parser')
    job_elements = soup.find_all('div', class_='job-listing')
