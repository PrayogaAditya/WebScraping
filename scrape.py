from bs4 import BeautifulSoup
import requests
from selenium import webdriver
url = input("masukkan URL : ")
browser = webdriver.firefox()
browser.get(url)

#doc = BeautifulSoup(result.text, "html.parser")
#tag = doc.find_all(text="Kebab Vegetarian")
#parent = tag[0].parent
#print(doc.find_all())