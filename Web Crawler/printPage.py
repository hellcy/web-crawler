from bs4 import BeautifulSoup
from urllib.request import urlopen

path = 'E:/Web Crawler/simple webpage.html'

htmlfile = open(path, 'r', encoding='utf-8').read()

print(htmlfile)

soup = BeautifulSoup(htmlfile)

print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')

all_href = [l['href'] for l in all_href]

print('\n', all_href)

# if has Chinese, apply decode()
html = urlopen("https://www.seek.com.au/").read().decode('utf-8')
print(html)