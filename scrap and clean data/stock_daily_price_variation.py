import requests
from bs4 import BeautifulSoup

def parseVIX():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get('https://br.investing.com/currencies/us-dollar-index', headers= headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    variation = soup.find("div", {"class": "top bold inlineblock"})
    variation = variation.find_all('span')  
    vix = float((variation[3].text).replace(',','.').replace('%','').replace('+',''))
    
    vix = (((vix)/100*-1)+1 )

    return vix 

print(parseVIX())
