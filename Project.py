#1.Give the url of the webside,2.HTML parsing,3.start a loop

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as rq

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=rq.get(url)


soup=bs(page.text,"html.parser")

star_table=soup.find("table")

temp_list=[]
table_rows=star_table.find_all("tr")


for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]

    temp_list.append(row)




Star_name = []
Distance = []
Radius = []
Mass = []

for i in range(1,len(temp_list)):

    Star_name.append(temp_list[i][1])
    Distance.append(temp_list[i][5])
    Radius.append(temp_list[i][9])
    Mass.append(temp_list[i][8])
    

df2=pd.DataFrame(list(zip(Star_name,Distance,Radius,Mass)),columns=["Star_name","Distance","Radius","Mass"])



df2.to_csv("final.csv")