import sys
from PyQt5.QtWidgets import QWidget
import requests

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
        
