import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.chrome.options import Options

url = 'https://amazon.jobs/en/search?base_query=&loc_query=South+Africa&country=ZAF'

# get the soup
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
sleep(1)
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.close()

job_title = []
job_id = []
location = []
job_category = []
description = []
date_listed = []

# date listed   # store this as a date
for date in soup.find_all("h2", {"class": "posting-date"}):
    date_listed.append(date.text)

# click into job tiles
for job_tile in soup.find_all("a", {"class": "job-link"}):
    job_link = 'https://amazon.jobs' + str(job_tile["href"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(job_link)
    sleep(1)
    tile_soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()

    # scrape all relevant page fields
    # job title
    job_title.append(tile_soup.find("h1", {"class": "title"}).text)
    # job id
    job_id.append(tile_soup.find("p", {"class": "meta"}).text.split(": ")[1].split(" |")[0])
    # location
    location.append(tile_soup.find("div", {"class": "association-content"}).text)
    # job category
    job_category.append(tile_soup.find_all("div", {"class": "association-content"})[1].text)

    # description
    desc_text = ""
    for item in tile_soup.find_all("div", {"class": "section"}):
        if "<h2>" in str(item.find('h2')):
            desc_text += str(item.text)
    description.append(desc_text)

# make a dictionary
data = {}
data["Job Title"] = job_title
data["Job ID"] = job_id
data["Location"] = location
data["Job Category"] = job_category
data["Description"] = description
data["Date Listed"] = date_listed

# dataframe
df = pd.DataFrame.from_dict(data)