from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Safari()
search_item = 'books on programming'

def get_url(search_item):

	'''get url from search item'''
	template = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss_2'
	search_item = search_item.replace(' ','+')
    # add term query to url
    url = template.format(search_item)

    # add page_no quesry to  url
    url += '&page={}'
	return url

x= get_url(search_item)

driver.get(x)
driver.maximize_window()
time.sleep(5)

## EXTRACT TH ECOLLECTIONS ###

soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.find_all('div',{'data-component-type':'s-search-result'})

print(len(results))


### PROTOTYPE OF THE SINLE EXTRACTION OF THE RECORD  ###


item = results[0]

# atag = item.h2.a

# description = atag.text.strip()

# url = 'https://www.amazon.in//'+atag.get('href')

# price_parent = item.find('span', 'a-price')

# price = price_parent.find('span', 'a-price-whole').text

# star_rating = item.i.text

# review_count = item.find('span', {'class': 'a-size-base',  'dir': 'auto'}).text


##### GENERALISE THE PATTERN -- FOR ALL ITEMS ####

def extract_record(item):

	# description
	atag = item.h2.a
	description = atag.text.strip()
	url = 'https://www.amazon.in//'+atag.get('href')

	#price
	try:
		price_parent = item.find('span', 'a-price')
		price = price_parent.find('span', 'a-price-whole').text
	except AttributeError:
		return


	# star -rating
	try:
		star_rating = item.i.text
		review_count = item.find('span', {'class': 'a-size-base',  'dir': 'auto'}).text
	except AttributeError:
		star_rating = ' '
		review_count = ' '


	product_result = (description, price, star_rating, review_count, url)

	return product_result


records = []
# results = soup.find_ll('div',{'data-component-type':'s-search-result'})

for item in results:
	record =  extract_record(item)
	if record:
		records.append(record)

print(records[0])

for row in records:
    print(row[1])