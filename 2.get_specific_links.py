import bs4
import requests
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/list/ls063784435/'
res = requests.get(url)

data = res.text
soup = bs4.BeautifulSoup(data, 'html.parser')

tags = soup.find_all('h3', {"class": "lister-item-header"})


for tag in tags:
    link = tag.a.get('href')
    print("https://imdb.com" + link)

    

