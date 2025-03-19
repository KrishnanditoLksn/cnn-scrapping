import requests
from bs4 import BeautifulSoup

all_urls  =[]
url = "https://edition.cnn.com/search?q=climate+change+&from=0&size=10&page=1&sort=relevance&types=all&section="

data = requests.get(url).text
soup = BeautifulSoup(data,features="html.parser")
for a in soup.find_all('a',href=True):
    if a['href'] and ['href'][0] == '/climate'  and a['href'] != '#':
        a['href'] = url + a['href']
    all_urls.append(a['href'])


print(all_urls)