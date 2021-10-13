from bs4 import BeautifulSoup
from selenium import webdriver

import requests
import re


def extract_data():
    """
    extract data from text file
    """
    print("..................Loading.......................")
    company_list = []
    with open('companies.txt') as fobj:
        lines = fobj.readlines()
    for line in lines:
        company_list.append(line.rstrip())
    return company_list


def search_google():
    """
    return result URLs for the companies
    """
    companies = extract_data()
    company_urls = []
    for company in companies:
        payload = {'q': company}
        URL = 'https://www.google.com/search?'
        get_results = requests.get(URL, params=payload) 
        soup = BeautifulSoup(get_results.content,"html.parser")
        tags=soup.find_all("a")
        
        for tag in tags:
            my_dict = {
                "company": company,
                "company_url": tag.get('href')
            }
            company_urls.append(my_dict)

    return company_urls


def pick_twitter_url():
    """
    pick corresponding twitter urls for companies
    """
    company_urls = search_google()
    twitter_urls = []

    for company in company_urls:
        expression = r'https:\/\/twitter.com\/[A-Za-z0-9-]+'
        
        match = re.findall(expression, company['company_url'])
        if match:
            for lnk in match:
                twitter_link = {}
                twitter_link['company_name'] = company['company']
                twitter_link['link'] = lnk
                if twitter_link not in twitter_urls:
                    twitter_urls.append(twitter_link)

    return twitter_urls  


def scrape_twitter():
    """
    scrape twitter function
    """
    twitter_urls = pick_twitter_url()
    output_company = []
    
    for twitter_url in twitter_urls:
        driver = webdriver.Chrome()
        driver.get(twitter_url["link"])
        html_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(html_source, 'html.parser')
        
        try:
            main_div = soup.find('div', {'class': 'css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-56xrmm r-bcqeeo r-qvutc0'})
            company_tag = main_div.find('a', {'class': 'css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1cvl2hr r-1loqt21 r-4qtqp9 r-poiln3 r-1b7u577 r-bcqeeo r-qvutc0'})
            company_link = company_tag.get('href')
            
            my_dict = {}
            my_dict["company_name"] = twitter_url["company_name"]
            my_dict['twitter_url'] = twitter_url["link"]
            my_dict["company_url"] = company_link    
            output_company.append(my_dict)

        except:
            print('Company URL not found...')
            my_dict = {}
            my_dict["company_name"] = twitter_url["company_name"]
            my_dict['twitter_url'] = twitter_url["link"]
            my_dict["company_url"] = "Error processing"
            output_company.append(my_dict)

    print(output_company)
    return output_company


def check_company_website():
    company_links = scrape_twitter()
    emails = []
    for company in company_links:
        if company['company_url'] != "Error processing":
            URL = company['company_url']
            get_results = requests.get(URL, params='')
            
            new_emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                    get_results.text))

            for email in new_emails:                
                new_str = str(email)                    
                if company['company_name'].lower() in new_str.lower():
                    new_dict = {
                        "company_name": company['company_name'],
                        "email_address": new_str
                    }
                    emails.append(new_dict)
                         
        else:
            new_dict = {
                "company_name": company['company_name'],
                "email_address": "failed to process email"
            }
            emails.append(new_dict)

    return emails 


def write_to_file(filename):
    scraped_data = check_company_website()
    
    with open(filename, 'w') as file_object:
        for obj in scraped_data:
            if obj["email_address"] != "failed to process email":
                file_object.write("{0}: {1}  \n".format(obj["company_name"], obj["email_address"]))
            else:
                file_object.write("{0}: {1}  \n".format(obj["company_name"], obj["email_address"]))
    
    print("Finished writing to file "+filename+".....")
    return "Completed writing to file"