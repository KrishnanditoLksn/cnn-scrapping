import requests
from bs4 import BeautifulSoup

all_urls  =[]
url = "https://www.cnn.com"

data = requests.get(url).text
soup = BeautifulSoup(data,features="html.parser")
for a in soup.find_all('a',href=True):
    if a['href'] and a['href'][0] == '/' and a['href'] != '#':
        a['href'] = url + a['href']
    all_urls.append(a['href'])


print(all_urls)


def url_is_article(url):    
    if url:
        if 'cnn.com/' in url:
            if 'climate' in url.lower():
                return True
    return False


article_urls = [url for url in all_urls if url_is_article(url)]
print(article_urls)