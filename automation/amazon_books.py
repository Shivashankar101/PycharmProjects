import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import time


template = 'https://www.amazon.in/s?k={}g&ref=nb_sb_noss'

def get_url(search_item):

    search_item = search_item.replace(' ', '+')
    url = template.format(search_item) # search query
    url += '&page={}' # page querry
    return url

def get_record(item):

    try:
        # descriptin
        description = item.h2.a.text.strip()
        url = 'https://www.amazon.in//' + item.h2.a.get('href')
        author_line = item.find('div', {'class': 'a-row a-size-base a-color-secondary'})
        author = author_line.a.text.strip()
        # star-rating
        rating = item.i.text
        reviews = author_line.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
        # price
        price = item.find('span', {'class': 'a-price'}).text
    except AttributeError:
        description = ' '
        author = ' '
        rating = ' '
        reviews = ' '
        price = ' '

    result = (description, author, rating, reviews, price, url)
    return result

def scrap_data(search_item):

    url = get_url(search_item)
    driver = webdriver.Safari()
    records = []
    for page in range(1, 21):
        driver.get(url.format(page))
        driver.maximize_window()
        driver.implicitly_wait(10)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        res = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in res:
            time.sleep(1)
            record = get_record(item)
            if record:
                records.append(record)

    driver.quit()

    ## saving data to .CSV file
    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['description', 'author', 'rating', 'reviews', 'price', 'url'])
        writer.writerows(records)


scrap_data('books on programming')








