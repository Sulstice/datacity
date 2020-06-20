import sys
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

SCRAPE_LIST = [
    'https://communitycrimemap.com/'
]

#TODO make a util module add this in there
def get_page_as_html_request(as_selenium = False, custom_list = SCRAPE_LIST):
    res = []
    for site in custom_list:
        if as_selenium:
            path = '/usr/local/bin/chromedriver'

            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
            myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'ext-gen67')))
            html = myElem.page_source
        else:
            html = requests.get(site)
        res.append(html)
    return res


def get_column_headers(table):
    res = []
    th = table.find_all('th')
    a = table.find('th')
    for header in th:
        span = header.find('span')
        text = span.text
        if text in res:
            continue
        else:
            res.append(text)
    return res

def parse_table(soup):
    headers = get_column_headers(soup)

    pass

def parse_dallas(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    table = soup.find_all('hr')
#
#    parse_table(table)


def main():
    html = get_page_as_html_request(True)[0]
    #TODO have some code here to determine what type of scrping
    # opting to do austin hard code for now
    parse_dallas(html)

if __name__ == "__main__":
    main()
