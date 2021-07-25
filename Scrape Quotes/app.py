import bs4
import requests
import pandas as pd

data_dict = {}
index=1

url = "http://quotes.toscrape.com"
copy_of_url = url

while True:
    response = requests.get(url)

    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('div', {"class": "quote"})

    for tag in tags:
        quote = tag.span.text
        author = "-" + tag.small.text
        data_dict[index] = [quote,author]
        index += 1

    next_page = soup.find('li', {'class': 'next'}) 

    if next_page:
        url = copy_of_url + next_page.a['href']
    
    else:
        break

data_dict_df = pd.DataFrame.from_dict(data_dict, orient='index', columns=['QUOTE','AUTHOR'])

data_dict_df.to_csv("data.csv")





