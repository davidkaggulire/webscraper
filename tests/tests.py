"""tests.py"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import unittest
import requests

from web_scraper import extract_data, search_google, pick_twitter_url, scrape_twitter, write_to_file


class TestScrapping(unittest.TestCase):

    def test_extract_data(self):
        company_list = []
        file_path = '/home/dkaggs/Desktop/scrapping/companies.txt'
        with open(file_path) as fobj:
            lines = fobj.readlines()
        for line in lines:
            company_list.append(line.rstrip())
        self.assertEqual(extract_data(), company_list)
        self.assertIsInstance(extract_data(), list)


    def test_google_search(self):
        self.assertIsInstance(search_google(), list)


    def test_pick_twitter_url(self):
        self.assertIsInstance(pick_twitter_url(), list)


    def test_scrape_twitter(self):        
        self.assertIsInstance(scrape_twitter(), list)


    def test_write_to_file(self):
        self.assertEqual(write_to_file('alice.txt'), "Completed writing to file")


if __name__ == '__main__':
    unittest.main()