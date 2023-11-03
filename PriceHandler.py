#interface_modul_imports
from PyQt5.QtWidgets import QWidget

#rest_api_modul_imports
import requests
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#data_model

class Item:
    
    _name=''
    _price_list=[]
    _cur_price={}
    
    #name
    def set_name(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    #price
    def update_price(self, new_price, date):
        self._cur_price = {date, new_price}
        self._price_list.append(self._cur_price)
        
    def clear_price_list(self):
        self._cur_price={}
        self._price_list=[]

class Site:
    
    _name=''
    _url=''
    _list_items=[]
    
    #name
    def set_name(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    #url
    def set_url(self, url):
        self._url=url
    
    def get_url(self):
        return self._url
    
    #items
    def add_item(self, item):
        self._list_items.append(item)
        
    def set_items(self, items=[]):
        self._list_items.clear()
        self._list_items = items
        
    def get_items(self):
        return self._list_items
    
    def add_items(self, items=[]):
        if items:
            for item in items:
                self._list_items.append(item)
                
#interface

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('PriceHandler')
        self.show()
        
#rest_api
class RestAPI_dns:
    
    def get_products(self, search: str) -> list:
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        url = f'https://www.dns-shop.ru/search/?q={search}&p=1&order=popular&stock=all'
        session = requests.session()
        session.headers.update(headers)

        rs = session.get(url)
        data = json.loads(rs.text)

        root = BeautifulSoup(data['html'], 'html.parser')

        items = []

        for a in root.select('.product-info__title-link > a'):
            items.append(
                (a.get_text(strip=True), urljoin(rs.url, a['href']))
            )

        return items
    
    def test_search(self, name):
        self.get_products()
        for title, url in items:
            print(f'    {title!r}: {url}')
        