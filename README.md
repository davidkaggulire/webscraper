[![Build Status](https://app.travis-ci.com/davidkaggulire/webscraper.svg?branch=main)](https://app.travis-ci.com/davidkaggulire/webscraper)

[![Coverage Status](https://coveralls.io/repos/github/davidkaggulire/webscraper/badge.svg?branch=main)](https://coveralls.io/github/davidkaggulire/webscraper?branch=main)

# Webscraper
Python Webscraper that fetches a list of companies from a text file and scrapes Twitter using the given company names

# Functionality
The Python webscraper uses the requests library to get the google search results of the company name. Based on this company name, it returns all result URLs, from which it automatically picks the Twitter URL with regex.
After picking the URL, it surfs the Twitter page of the given company and picks out the number of people the company is following.

On completion all this output is written into a text file.

# Installing dependencies
To install dependencies needed, use the following command

 `pip install -r requirements.txt`

# Running Unit Tests
You can run unit tests using this command 
`pytest --cov=tests/` 

Check the **coverage** report using this command.
`pytest tests --cov=tests/ --cov-report term-missing`

# Author:
David Kaggulire