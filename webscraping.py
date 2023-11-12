import requests
from bs4 import BeautifulSoup


url = "https://www.mrasports.pk/"
get =requests.get(url)

res = get.content

soup = BeautifulSoup(res,'html.parser')

# print(soup.prettify)

#Get the title

#print(soup.title)

#Get the anchor tag

#print(soup.find_all('a'))

#Get the paragraph

#print(soup.find_all('p'))

# links in achor tag

anchor = soup.find_all('a')


for link in anchor:
    if(link.get('href') != '#'):
        linkAdd = link.get('href')
        print(linkAdd)

img = soup.find_all('img')

for src in img:
    if(src.get('src') != '#'):
        imagelink = src.get('src')
        print(imagelink)