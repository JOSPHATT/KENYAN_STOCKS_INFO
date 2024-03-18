from bs4 import BeautifulSoup
import sys,re,subprocess,requests

base_url='https://www.tradingview.com/markets/kenya/'
response = requests.get(base_url)
response.raise_for_status() # ensure we notice bad responses
with open("kenyan_stocks_info.html", "w") as file:
    file.write(response.text)

html_doc="kenyan_stocks_info.html"
with open(html_doc) as f:
    soup = BeautifulSoup(f, "html.parser")
all_lnks=[]
for a in soup.find_all('a', href=True):
    print(a)
