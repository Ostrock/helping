import requests
from bs4 import BeautifulSoup as bs

def parseVIX():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get('https://br.investing.com/currencies/us-dollar-index', headers= headers)
    soup = bs(r.text, 'html.parser')
    variation = soup.find("div", {"class": "top bold inlineblock"})
    variation = variation.find_all('span') 
    vix = float('.'.join(variation[3].text[1:-1].split(',')))

    return vix
