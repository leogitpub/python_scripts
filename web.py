from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.google.com').text
soap = BeautifulSoup(source,"html5lib")
article = soap.find('html')
print(article)

