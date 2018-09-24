from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
# url = base_url + his[-1]
# html = urlopen(url).read().decode('utf-8')
# soup = BeautifulSoup(html, features='html.parser')
# description = soup.find("meta", {
#     "name": "description"
#     })
# print(soup.find('h1').get_text(), description)


for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='html.parser')
    description = soup.find("meta", {
    "name": "description"
    })
    print(i, soup.find('h1').get_text(), '\n    description: ', description)

    # find valid urls
    sub_urls = soup.find_all("a", {
    	"target": "_blank", 
    	"href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()

