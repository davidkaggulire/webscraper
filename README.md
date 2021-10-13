[![Build Status](https://app.travis-ci.com/davidkaggulire/webscraper.svg?branch=main)](https://app.travis-ci.com/davidkaggulire/webscraper)

[![Coverage Status](https://coveralls.io/repos/github/davidkaggulire/webscraper/badge.svg?branch=main)](https://coveralls.io/github/davidkaggulire/webscraper?branch=main)

[![codecov](https://codecov.io/gh/davidkaggulire/webscraper/branch/main/graph/badge.svg?token=FK4L7HYDKH)](https://codecov.io/gh/davidkaggulire/webscraper)

# Webscraper
The Webscraper is built using python to fetch companies from a text file, search for each company's Twitter page, scrape the Twitter page and further navigate to the individual company site to get the company's email address. The email address together with the company name are then written to a file in a format of:
`{ company_name: email_address }`

# Functionality
The Python webscraper uses the requests library to get the google search results of the company name. Based on this company name, it returns all result URLs, from which it automatically picks the Twitter URL with regex.
After picking the URL, it surfs the Twitter page of the given company and picks the website link for the company. It then redirects to the company website and picks its email through regex and writes the content of both email and company name to a text file.

# Dependencies
attrs==21.2.0
beautifulsoup4==4.10.0
certifi==2021.5.30
charset-normalizer==2.0.6
coverage==5.5
coveralls==3.2.0
docopt==0.6.2
idna==3.2
iniconfig==1.1.1
packaging==21.0
pluggy==1.0.0
py==1.10.0
pyparsing==2.4.7
pytest==6.2.5
pytest-cov==3.0.0
requests==2.26.0
selenium==3.141.0
soupsieve==2.2.1
toml==0.10.2
tomli==1.2.1
urllib3==1.26.7

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