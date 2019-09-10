from pprint import pprint

import requests
import bs4


url = "https://www.tesco.com/groceries/en-GB/promotions/A32671682"

items = {}

page_no = 1

connection = requests.Session()
while True:
    page = connection.get(url, params={
        "page": str(page_no)})
    soup = bs4.BeautifulSoup(page.text)

    if page.status_code == 404:
        # This page doesn't exist - we have reached the end of the products
        break
    divs = soup.find_all(class_="tile-content")

    for i in divs:
        try:
            item = {
                "title": i.findAll(class_="sc-htoDjs")[0].string,
                "image": i.findAll(class_="product-image")[0].get('src'),
                "price": i.find(class_="price-control-wrapper").find(class_="value").string
            }
            items.update({str(i.get('data-auto-id')): item})
        except AttributeError:
            # The item does not have all of the required attributes - maybe it's out of stock?
            pass

    page_no = page_no+1
pprint(items)
