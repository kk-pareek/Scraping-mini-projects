import bs4
import requests

url = "http://quotes.toscrape.com/"

while True:
    response = requests.get(url)

    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('div', {"class": "quote"})

    for tag in tags:
        print("=="*50)
        print(tag.span.text)
        print("- " + tag.small.text)

    nav = soup.find('nav') 

    if nav and nav.a['href']:
        url = url + nav.a['href']
    
    else:
        break





