import json
import requests
from bs4 import BeautifulSoup

start_url = 'https://ru.wikipedia.org/wiki/%D0%9F%D1%81%D0%B5%D0%B2%D0%B4%D0%BE%D0%BD%D0%B8%D0%BC'

data = []

def crawl(url, depth):
    try:
        print('Кравлим url %s и depth %d' % (url, depth))
        response = requests.get(url)
    except:
        print("Невозможно сделать запрос на '%s'\n" % url)
        return

    content  = BeautifulSoup(response.text, 'lxml')

    title = content.find('title').text
    description = content.get_text()

    if description is None:
        description = ''
    else:
        description = description.strip().replace('\n', ' ')

    result = {
        'url': url,
        'title': title,
        'description': description
    }

    data.append(result)

    if depth == 0:
        return

    try:
        links = content.findAll('a')
    except:
        return

    for link in links:
        try:            
            if 'http' not in link['href']:
                follow_url = url + link['href']
            else:
                follow_url = link['href']

            crawl(follow_url, depth - 1)
        except KeyError:
            pass
    
    return result

crawl(start_url, 2)
print(len(data))
