#! /usr/bin/env python
import sys
import bs4
import requests

URL="https://www.archlinux.org/news/"
TABLE_ID="article-list"

r = requests.get(URL)
soup = bs4.BeautifulSoup(r.content, 'lxml')


article_table = soup.find(id=TABLE_ID)
articles = []
for row in article_table.find_all('tr')[1:16]:
    elems = row.find_all('td')
    item = {
        'date': elems[0].text,
        'title': elems[1].text,
    }
    articles.append(item)

for item in articles:
    print(f"{item['date']} - {item['title']}")
