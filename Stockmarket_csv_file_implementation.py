# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:04:08 2021

@author: AyoOluwa
"""

import csv
import bs4
import requests
from bs4 import BeautifulSoup

with open ('output_test.csv', 'w') as csv_file:
            fieldnames = ['Name of stock(SYMBOL)','CURRENT PRICE','UNITS OWNED','TOTAL VALUE($)']
            docs =csv.DictWriter(csv_file, fieldnames = fieldnames, delimiter=',',lineterminator='\r')
            docs.writeheader()

with open('input_test.csv', 'r') as csv_file:
    docs = csv.DictReader(csv_file,delimiter = ',')
    
    
    for k in docs:
        with open ('output_test.csv', 'a') as csv_file:
            fieldnames = ['Name of stock(SYMBOL)','CURRENT PRICE','UNITS OWNED','TOTAL VALUE($)']
            docs =csv.DictWriter(csv_file, fieldnames = fieldnames, delimiter=',',lineterminator='\r')
            
            b = k['STOCK SYMBOL']
           
            print(b)
            r=requests.get('https://finance.yahoo.com/quote/{}?p={}'.format(b.upper(),b.lower()))     
            soup=bs4.BeautifulSoup(r.text,"lxml")
            price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
            time_stamp=soup.find_all('div',{'class':'C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm'})[0].find('span').text
            a = k['UNITS OWNED']
            c = float(k['UNITS OWNED'])
            D = c * float(price)
            stock_name=soup.find_all('h1',{'class':'D(ib) Fz(18px)'})[0].text
            docs.writerow({'Name of stock(SYMBOL)':stock_name,'CURRENT PRICE':price,'UNITS OWNED':a,'TOTAL VALUE($)':D})
            print(price)
            
    with open ('output_test.csv', 'a') as csv_file:
        docs =csv.DictWriter(csv_file, fieldnames = fieldnames, delimiter=',')
        docs.writerow({'Name of stock(SYMBOL)':time_stamp})
 
        
       
          
           
            
            

'''  
    fieldnames = ['NAME OF STOCK', 'STOCK SYMBOL' , 'CURRENT PRICE']

    with open('test.csv','w') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter= '\t')
        
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames, delimeter = '\t')
        
        csv_writer.writeheader()
    
        for line in csv_reader:

            r=requests.get('https://finance.yahoo.com/quote/{}?p={}'.format(line['STOCK SYMBOL'].upper(),line['STOCK SYMBOL'].lower()))
        
            soup=bs4.BeautifulSoup(r.text,"lxml")

            stock_name=soup.find_all('h1',{'class':'D(ib) Fz(18px)'})[0].text

            seems_useful=soup.find_all('div',{'class':'C($tertiaryColor) Fz(12px)'})[0].find('span').text

            price=soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

            current_price=soup.find_all('p',{'class':'Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)'})[0].find('span').text

            time_stamp_2=soup.find_all('span',{'class':'C($tertiaryColor) Fz(12px) smartphone_Fz(xs)'})[0].text
        
        
'''
        
    
   