import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://greenbelarus.info/'
URL = 'https://greenbelarus.info/news/nature'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


def get_html(url, params = ''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='media')
    news = []

    for item in items:
        name = item.find('div', class_='media-body').get_text(strip=True).lower()
        if 'поселил' in name or 'замечен'in name or 'впервые отметили'in name or 'обнаруженный'in name or 'обнаружен новый'in name:
            news.append(
                {
                    'title': item.find('div', class_='media-body').find('h3').get_text(strip=True),
                    'date': item.find('span', class_='datetime').get_text(strip=True),
                    'link': HOST + item.find('div', class_='media-body').find('a').get('href')

                }
            )
        else:
            continue

    return news


def parser():
    pages = 88
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for page in range(1, pages):
            print(f'Парсинг страницы{page}')
            html = get_html(URL, params={'page': page})
            news.extend(get_content(html.text))

        with open('data.json', 'w') as file:
            json.dump(news, file, indent=4)
    else:
        print('Error')

parser()

