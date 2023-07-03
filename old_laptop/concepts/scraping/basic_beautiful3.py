

import urllib.request
import requests
import urllib3
import certifi
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


given_url2 = 'https://insights.blackcoffer.com/solution-for-contact-centre-problems/'
http = urllib3.PoolManager(ca_certs=certifi.where())
page = http.request('GET', given_url2)
print(page)
print(type(page))

print()
hd = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0.1) Gecko/20100101 Firefox/101.0.1'}

r = requests.get(given_url2, headers=hd)
html_content = r.content
print('html_content :', html_content)

soup02 = bs(html_content, "html.parser")
print('soup02 =', soup02)
print('soup02 type:', type(soup02))

t0t = soup02.get_text()
print('tt =', t0t)
print('tt == "" :', t0t == "")
print('soup02 text(tt) type:', type(t0t))

print()
soup = bs(page, "html.parser")
print('soup =', soup)
print('soup type:', type(soup))

tt = soup.get_text()
print('tt =', tt)
print('tt == "" :', tt == "")
print('soup text(tt) type:', type(tt))

fd = soup.find_all('p')
print('fd =', fd)
print('fd type:', type(fd))

'''#page = urllib.request.urlopen("https://www2.census.gov/topics/genealogy/1990surnames/dist.all.last")
#print(page)
#print()
#soup = bs(page, features='lxml')
#print(soup)
#tt = soup.find_all('p')
tt = soup.get_text()
s = (tt[0:99])
s = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", s)
#for i in p:
    #print('i ==', i)
print(s)

top = list(tt[0:99])
print(top)
'''
