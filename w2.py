#-*-coding:utf8;-*-
#qpy:console

from selenium import webdriver

PATH = "/storage/emulated/0/chromedriver.exe"
browser = webdriver.Chrome(PATH)

driver.get("google.com")
driver.quit()