from bs4 import BeautifulSoup
import requests
import re

url = "https://www.goodhousekeeping.com/food-recipes/healthy/g807/vegan-recipes/ "


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

price = doc.find_all(text =re.compile(input("Masukkan Kata = ")))
#for tag in price :   
    #print("_______________________")
   # print(tag)
print(price)