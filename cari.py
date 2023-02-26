from bs4 import BeautifulSoup
import requests
import re

url = "https://www.google.com/search?client=ms-android-oppo&tbs=lf:1,lf_ui:9&sxsrf=AOaemvJGk8SAqBAcktdLvqQAIUiDXtdENw:1633515673049&q=restauran&ibp=gwp;0,6&rflfq=1&num=10&sa=X&ved=2ahUKEwiC67SLyLXzAhXJWisKHQj6AWgQxMEEegUIBRCCAQ&biw=424&bih=885&dpr=1.7"


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
kelas = doc.find(class_= "kR1eme oz3cqf rOVRL rllt__wrapped lrl-obh")

#for i in range(0) :
#parent = kelas[0].parent
#span = parent.find("h2")
print (kelas)
    
 





