class Popularity():
    popular_domains = [
        'https://en.wikipedia.org/',
        'https://www.python.org/',
        'https://www.rottentomatoes.com/',
        'https://pypi.org/', 
        'https://www.indiatoday.in/',
        'https://www.geeksforgeeks.org/',
        'https://stackoverflow.com/',
        'https://google.com/',
        'https://www.ozon.ru/',
        'https://ru.wikipedia.org/',
        'https://google.ru/',
        'https://leetcode.com/',
        'https://mail.ru/',
        'https://www.avito.ru/',
        'https://telegram.org/',
        'https://github.com/',
        'https://mail.google.com/',
        'https://www.apple.com/',
        'https://www.spotify.com/',
        'https://hh.ru',
        'https://www.youtube.com/',
        'https://aliexpress.ru/',
        'https://www.gosuslugi.ru/',
        'https://www.microsoft.com/ru-ru/',
        'https://www.kinopoisk.ru/',
        'https://www.bbc.com/',
        'https://www.rbc.ru/',
        'https://translate.google.com/',
        'https://yandex.ru/',
        'https://ru.wiktionary.org/',
        'https://www.amazon.com/',
        'https://gb.ru/'
    ]

    ps = 0

    def __init__(self, url):
        self.url = url

    def popularity_score(self):
        for domain in self.popular_domains:
            if domain == self.url:
                self.ps += 100 / len(self.popular_domains)
            if domain in self.url:
                self.ps += 100 / len (self.popular_domains)

        return self.ps