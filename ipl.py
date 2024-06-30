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
"""
output : 
['Chennai Super Kings', '₹2,95,00,000', '8', '25']
['Delhi Capitals', '₹10,00,000', '7', '24']
['Gujarat Titans', '₹15,00,000', '8', '23']
['Kolkata Knight Riders', '₹45,00,000', '8', '25']
['Lucknow Super Giants', '₹0', '7', '21']
['Mumbai Indians', '₹10,00,000', '8', '25']
['Punjab Kings', '₹3,45,00,000', '7', '25']
['Rajasthan Royals', '₹95,00,000', '8', '24']
['Royal Challengers Bangalore', '₹1,55,00,000', '8', '22']
['Sunrisers Hyderabad', '₹10,00,000', '8', '23']
                          TEAM FUNDS REMAINING OVERSEAS PLAYERS  TOTAL PLAYERS
0          Chennai Super Kings    ₹2,95,00,000                 8            25
1               Delhi Capitals      ₹10,00,000                 7            24
2               Gujarat Titans      ₹15,00,000                 8            23
3        Kolkata Knight Riders      ₹45,00,000                 8            25
4         Lucknow Super Giants              ₹0                 7            21
5               Mumbai Indians      ₹10,00,000                 8            25
6                 Punjab Kings    ₹3,45,00,000                 7            25
7             Rajasthan Royals      ₹95,00,000                 8            24
8  Royal Challengers Bangalore    ₹1,55,00,000                 8            22
9          Sunrisers Hyderabad      ₹10,00,000                 8            23
PS C:\Users\Mahendra Reddy\git_web_scrap> 
"""