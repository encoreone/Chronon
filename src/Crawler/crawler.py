import json
import threading
import requests
import pymongo
from bs4 import BeautifulSoup


class Crawler():
    try:
        connect_uri = 'mongodb://root:root@localhost:27017' #example
        client = pymongo.MongoClient(connect_uri)
        db = client.results
        print(db)
    except:
        print('Ошибка подключения к бд :(')
 

    search_results = []

    def crawl(self, url, depth):
        try:
            print("Кравлим url = %s  depth = %d" % (url, depth))
            response = requests.get(url, headers={'user-agent': 'glacier-crawler'})
        except:
            print("Невозможно сделать запрос на '%s'\n" % url)
            return

        content  = BeautifulSoup(response.text, 'html.parser')

        try:
            title = content.find('title').text
            description = ''
            score = 0
            popularity = ''

            for tag in content.findAll():
                if tag.name == 'p':
                    description += tag.text.strip().replace('\n', '')
        except:
            return

        result = {
            'url': url,
            'title': title,
            'description': description,
            'score': score,
            'popularity': popularity
        }

        self.search_results.append(result)

        if depth == 0:
            return

        links = content.findAll('a')

        for link in links:
            try:            
                if 'http' in link['href']:
                    self.crawl(link['href'], depth - 1)
            except KeyError:
                pass

    def insert_results(self):
        search_results = self.db.search_results
        search_results.insert_many(self.search_results)
        search_results.create_index([
            ('url', pymongo.TEXT),
            ('title', pymongo.TEXT),
            ('description', pymongo.TEXT),
            ('score', pymongo.TEXT),
            ('popularity', pymongo.TEXT)
        ], name='search_results', default_language='english')

    # def printData(self):
    #     for entry in self.search_results:
    #         print(json.dumps(entry))

    #     for entry in self.db.search_results.find({"$text": {"$search": "Welcome"}}):
    #         print(entry)


crawler = Crawler()
crawler.crawl("https://ru.wikipedia.org/wiki/Google_(%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F)", 1)
crawler.insert_results()
# crawler.printData()