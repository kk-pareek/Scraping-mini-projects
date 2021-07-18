import bs4
import requests
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.imdb.com/list/ls063784435/'
res = requests.get(url)

data = res.text
soup = bs4.BeautifulSoup(data, 'html.parser')

tags = soup.find_all('h3', {"class": "lister-item-header"})

data_dict = {}
index = 1

for tag in tags:
    rank = str(index)
    name = tag.a.text
    profile_link = "https://imdb.com" + tag.a.get('href')

    data_dict[rank] = [name, profile_link] 
    index += 1

data_dict_df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['NAME', 'PROFILE_LINK'])

data_dict_df.to_csv('data.csv')