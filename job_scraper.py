#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
"""
Copyright 2023 Josh Korol
All Rights Reserved

Created: May 31, 2023

This script is a tool I use to scrape job listings across popular websites such as Linkedin, Wayup, Dice, and Indeed.

Usage:
- Run the script with the following command: python my_script.py
- Pass the input file path as a command-line argument.
"""

def scrape_job_listings():
    # TODO: handle 

    url = ''

    # send get req
    response = requests.get(url)
    # create object to parse htmld
    soup = BeautifulSoup(response.content, 'html.parser')
    job_elements = soup.find_all('div', class_='job-listing')

def query_dice():
