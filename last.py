from bs4 import BeautifulSoup
import requests 
import re

search term = input("What product do you want to search for? ")

url= f"https://www.newegg.ca/p/pl?d={search term}&N=4131"
page= requests.get(url).text

doc = Beautiful5oup(page, "html.parser")

page_text = doc.find(class="list-tool-pagination-text").strong pages = int(str(page_text).split("/")[-2].split("")[-][:-11)

items found = {}

for page in range(1, pages + 1):
    url = "https://www.newegg.ca/p/pl?d={search_term}&N=4131&page=[page}" page= requests.get(url), text
    doc BeautifulSoup(page. "html.parser")
    div= doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell") items = div.find_all(text=re.compile(search term))
    for item in items:

        parent = item.parent if parent.name = "a":
            continue
        link = parent["href"]

        next_parent = item.find_parent(class_="item-container")

        try:

            price = next_parent.find(class="price-current").find("strong").string items_found[item] = {"price": int(price.replace(",", "")), "Link": link)

        except:

            pass

sorted_items sorted (items found.items(), key-lambda x: x[1]['price'])

for item in sorted items:

    print(item [0]) print (f"$(item[1]['price'])")

    print(item[1]['link'])