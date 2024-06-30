import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
url="https://www.iplt20.com/auction/2022"
page=requests.get(url,headers=headers)
pp=BeautifulSoup(page.text,'html.parser')
#print(pp)
coll=pp.find('table',class_="ih-td-tab auction-tbl")
columns=coll.find_all('th')
head=[]
for cc in columns:
    #print(cc.text)
    head.append(cc.text)
import pandas as pd
df=pd.DataFrame(columns=head)
#print(df)
rows=coll.find_all('tr')
i=0
for rr in rows[1:]:
    ll=[]
    #print(rr.find('h2'))
    tdat=rr.find_all('td')
    for dd in tdat:
        ll.append(dd.text.strip())
    df.loc[i]=ll
    i=i+1
    print(ll)
print(df)