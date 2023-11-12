import requests
 
from bs4 import BeautifulSoup


url = "https://www.mrasports.pk/"

req = requests.get(url)

content = req.content

soup = BeautifulSoup(content,'html.parser')

anchor = soup.find_all('a')

for link in anchor:
    if(link.get('href') != '#'):
        linkadd = link.get('href')
        print(linkadd)
