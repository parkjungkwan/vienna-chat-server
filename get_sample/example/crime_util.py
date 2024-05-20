import json
import pandas as pd
from example.crime_abstract import PrinterBase, ReaderBase, ScraperBase
import googlemaps
from selenium import webdriver
from icecream import ic


class Printer(PrinterBase):

    def dframe(self, this: pd.DataFrame) -> None:
        print('-' * 100)
        ic(f'타입: {type(this)}')
        ic(f'컬럼: {this.columns}')
        ic(f'상위 1개행: {this.head(1)}')
        ic(f'null 갯수: {this.isnull().sum()} 개')
        print('-' * 100)


class Reader(ReaderBase):

    def __init__(self) -> None:
        pass

    def csv(self, file) -> object:
        return pd.read_csv(f'{file}.csv', encoding='UTF-8', thousands=',')
    
    def xls(self, file, header, usecols) -> object:
        return pd.read_csv(f'{file}.xls', header=header, usecols=usecols)
    
    def json(self, file) -> object:
        return json.load(open(f'{file}.json', encoding='UTF-8'))
    
    def gmaps(self, api_key: str) -> object:
        return googlemaps.Client(key=api_key)


class Scraper(ScraperBase):

    def __init__(self) -> None:
        pass

    def driver(self) -> object:
        return webdriver.Chrome('C:/Program Files/Google/Chrome/chromedriver.exe')
    
    def auto_login(self, driver, url, selector, data) -> None:
        driver.get(url)
        driver.find_element_by_css_selector(selector).send_keys(data)
        driver.find_element_by_css_selector(selector).submit()