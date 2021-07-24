import bs4
import requests
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/list/ls063784435/'
res = requests.get(url)

data = res.text
soup = bs4.BeautifulSoup(data, 'html.parser')

tags = soup.find_all('a')

for tag in tags:
    link = tag.get('href')

    if type(link) == (str) and "https://" in link:
        print(link)
