import requests
 
from bs4 import BeautifulSoup


url = "https://www.mrasports.pk/"

req = requests.get(url)

content = req.content

soup = BeautifulSoup(content,'html.parser')

anchor = soup.find_all('a')

with open("text.txt","a") as a:
    for i in anchor:
        link = i.get('href')

        if link is not None and link != '#':
            print(link)
            
            a.write(link + '/n')
