import json
import csv

with open('stocks.json') as f:
    j=json.load(f)

field_names=['stock_name','stock_category','price']

stocks=[]
for k,v in j.items():
    c_k=k.replace('"', "")
    c_v=[i.replace('"', "") for i in v]
    entry=list(zip(c_v[::2], c_v[1::2]))
    #stock={}
    for i in entry:
        stock={}
        p=i[1].split(" ")
        stock['stock_name']=i[0]
        stock['stock_category']=c_k
        st=p[0]
        stp=st.encode("ascii", "ignore")
        stpr=stp.decode()
        stpra=stpr.split(",")
        print(stpra)
        if len(stpra)>1:
            stock['price']=float(stpra[0]+stpra[1])
        elif len(stpra[0])==0:
            stock['price']=0
        else:
            stock['price']=float(stpra[0])
        stocks.append(stock) 
print(stocks)

with open('stocks.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(stocks)
