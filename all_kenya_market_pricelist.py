import json
import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://live.mystocks.co.ke/m/pricelist', stream=True)
page_lines=[]
for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        page_lines.append(json.dumps(decoded_line))

raw_data=page_lines[45:201]
#print(raw_data)

stocks=[]
stock_name=[]
stock_price=[]
entry=[]
stocks_all={}

print(raw_data)
for i in raw_data:
    html_doc=i
    soup = BeautifulSoup(html_doc, 'html.parser')
    val=soup.get_text()
    #print(val)
    if "head" in i:
        title=val
        entry=[]
        continue
    elif val:
        entry.append(val)
        stocks_all[title]=entry
        continue
#print(stocks_all)

c_stocks_all = {key.replace('"', ''):val for key, val in stocks_all.items()}
with open('stocks.json', 'w') as f:
        json_data=json.dump(c_stocks_all, f, indent=8, ensure_ascii=True)

