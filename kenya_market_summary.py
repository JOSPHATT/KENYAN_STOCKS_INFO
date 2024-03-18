import json
import requests

r = requests.get('https://live.mystocks.co.ke/m/', stream=True)
page_lines=[]
for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        page_lines.append(json.dumps(decoded_line))

c=0
toppers_table=[]
titles=["Top Gainers", "Top Losers", "Top Movers", "row r0", "row r1"]
for i in page_lines:
    if any(x in i for x in titles):
        toppers_table.append(i)
    else:
        continue

print(toppers_table)

#CODE TO CHECK FOR MATCHES IN PAGE LINES LIST
"""matches = ["BAMB","EABL","SASINI LTD"]
l=["SASN","NCBA","SCOM","WTK","EVRD","KCB","ABSA","CTUM","UMME","SLAM","SGL","SCBK","LKL","LBTY","ABSA","KCB","Military Expenditure","Inflation Rate MoM","Inflation Rate","Producer Prices Index YoY","Food Inflation YoY","Consumer Price Index"]

for i in page_lines:
    if any(x in i for x in matches):
        print(i)
    else:
        continue
"""

    
