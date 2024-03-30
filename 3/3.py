import requests
import bs4
import json
html=requests.get('https://tagildrama.ru/afisha/').text
soup=bs4.BeautifulSoup(html,'html.parser')
article=soup.find_all('div',class_='one-poster')
d=[]
for i in article:
    name=i.find('a').text
    date=str(i.find('h2',class_='font-title center').text)+' '+str(i.find('p',class_='center').text)
    day=i.find('div',class_='col s6 m6 xl2 day-time').find('p').text
    yearcategory=i.find('p',class_='bronze-color').text
    link=i.find('h4',class_='font-title').find('a').get('href')
    d.append({'name':name, 'date':date,'day':day,'yearcategory':yearcategory,'link':link})
with open ('spisok.json','w',encoding='utf-8') as f:
    f.write(json.dumps(d,ensure_ascii=False,indent=4))
print(d)