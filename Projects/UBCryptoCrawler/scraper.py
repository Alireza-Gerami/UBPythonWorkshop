import json
import sys
import time

from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://arzdigital.com'
COINS_LIST_SLUG = '/coins'


def get_all_coins():
    coins_list = {}
    response = requests.get(url=BASE_URL + COINS_LIST_SLUG)
    if response.status_code == 200:
        body = BeautifulSoup(response.content, 'html.parser')
        pagination_list = body.find('ul', attrs={'class': 'arz-coin-pagination__list'})
        pagination_li_list = pagination_list.find_all('li')
        start_page_number = pagination_li_list[0].text.strip()
        end_page_number = pagination_li_list[-2].text.strip()
        for i in range(int(start_page_number), int(end_page_number) + 1):
            print(f'__________ Page {i} __________')
            PAGE_NUMBER_SLUG = f'/page-{i}'
            response = requests.get(url=BASE_URL + COINS_LIST_SLUG + PAGE_NUMBER_SLUG)
            if response.status_code == 200:
                body = BeautifulSoup(response.content, 'html.parser')
                for tr in body.table.tbody.find_all('tr'):
                    coin_name = tr['data-name']
                    coin_slug = tr['data-slug']
                    coin_symbol = tr['data-symbol']
                    coins_list[coin_symbol] = {'coin_name': coin_name, 'coin_slug': coin_slug}
                    print(f'{coin_name:<30} | {coin_symbol:<10} | {coin_slug:<30}')
            time.sleep(2)
        with open('coins.json', 'w') as f:
            json.dump(coins_list, f)
        return coins_list


def load_coins_list():
    with open('coins.json', 'r') as f:
        return json.load(f)


def get_coin_date(coin_slug):
    response = requests.get(url=BASE_URL + COINS_LIST_SLUG + f'/{coin_slug}')
    if response.status_code == 200:
        body = BeautifulSoup(response.content, 'html.parser')
        market_info = body.find('div', attrs={'class': 'arz-row-sb arz-coin-page-data__coin-market-info'})
        all_market_info_span = market_info.find_all('span',
                                                    attrs={'class': 'arz-coin-page-data__coin-market-info-value'})
        market_cap = all_market_info_span[1].text.strip()
        coin_price_box = body.find('div', attrs={'class': 'arz-coin-page-data__coin-price-box'})
        usd_price = coin_price_box.find('div', attrs={'class': 'arz-coin-page-data__coin-price'}).text.strip()
        toman_price = coin_price_box.find('div',
                                          attrs={'class': 'arz-coin-page-data__coin-toman-price'}).span.text.strip()
        return {'market_cap': market_cap, 'usd_price': usd_price, 'toman_price': toman_price}


if __name__ == '__main__':
    coins = load_coins_list()
    symbol = sys.argv[1]
    if symbol in coins.keys():
        coin_data = get_coin_date(coins[symbol]['coin_slug'])
        print(coin_data)
    else:
        print(f'{symbol} dose not exists.')
