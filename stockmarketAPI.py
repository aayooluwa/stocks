# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:28:52 2021

@author: AyoOluwa
"""

import bs4
import requests
from bs4 import BeautifulSoup

query =str(input('Input stock symbol:\t'))

r=requests.get('https://finance.yahoo.com/quote/{}?p={}'.format(query.upper(),query.lower()))

soup=bs4.BeautifulSoup(r.text,"lxml")

stock_name=soup.find_all('h1',{'class':'D(ib) Fz(18px)'})[0].text

print("\n" + stock_name)

seems_useful=soup.find_all('div',{'class':'C($tertiaryColor) Fz(12px)'})[0].find('span').text

print(seems_useful)

price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

time_stamp=soup.find_all('div',{'class':'C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm'})[0].find('span').text

print("---------------------------\n")

print("Price:\t" + price)

print(time_stamp)

current_price=soup.find_all('p',{'class':'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)'})[0].find('span').text

time_stamp_2=soup.find_all('span',{'class':'C($tertiaryColor) Fz(12px) smartphone_Fz(xs)'})[0].text

print("\nCurrent price:\t" + current_price)

print(time_stamp_2)
