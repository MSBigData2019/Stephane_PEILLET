#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:21:19 2018

@author: stephanepeillet
"""

from requests import get
from bs4 import BeautifulSoup
import pandas as pd

urls = ['https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA',
        'https://www.reuters.com/finance/stocks/financial-highlights/AIR.PA',
        'https://www.reuters.com/finance/stocks/financial-highlights/DANO.PA']

#Initialisation
company = ['LVMH', 'Airbus', 'Danone']
q_means = []
q_highs = []
q_lows = []
prices = []
changes = []
shares = []
d_companies = []
d_industries = []
d_sectors = []

#Fonction pour obtenir les ventes au quartier à fin décembre 2018.
def get_quarters(soup):
    quarter = soup.find_all('td', class_ = "data")
    q_mean = quarter[1].text.strip()
    q_high = quarter[2].text.strip()
    q_low  = quarter[3].text.strip()
    return [q_mean, q_high, q_low]

#Fonction pour obtenir le prix de l'action et son % de changement au moment du crawling.
def get_price(soup):
    sectionQuoteDetail = soup.find('div', class_ = "sectionQuoteDetail")
    price = sectionQuoteDetail.find_all('span')[1].text.strip()
    return price

def get_change(soup):
    change = soup.find_all('span', class_ = "valueContentPercent")[0].text.strip()
    return change

#Fonction pour parser la donnée de change.
def extract_change(change):
    return change.strip('()')

#Fonction pour obtenir le % Shares Owned des investisseurs institutionel.
def get_sharesOwned(soup):
    sharesContainer = soup.find_all('div', class_ = "moduleBody")
    sharesOwned = sharesContainer[13]
    share = sharesOwned.find('td', class_ = 'data').text.strip()
    return share

#Fonction pour obtenir le dividend yield de la company, le secteur et de l'industrie.
def get_dividends(soup):
    sharesContainer = soup.find_all('div', class_ = "moduleBody")
    dividend= sharesContainer[4]
    dividend2 = dividend.find_all('td', class_ = 'data')
    d_company = dividend2[0].text.strip()
    d_industry = dividend2[1].text.strip()
    d_sector = dividend2[2].text.strip()
    return [d_company, d_industry, d_sector]

# Création de la requête pour chacune des entreprises.
for url in urls:
    page = get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #Quarters
    quarters = get_quarters(soup)
    print("Quarters : ")
    print(quarters)
    q_means.append(quarters[0])
    q_highs.append(quarters[1])
    q_lows.append(quarters[2])
    
    #Price and change
    price = get_price(soup)
    change = get_change(soup)
    change = extract_change(change)
    print("prix : "+price)
    print("change : "+change)
    prices.append(price)
    changes.append(change)
    
    #SharesOwned
    share = get_sharesOwned(soup)
    print("Share : "+share)
    shares.append(share)

    #Dividends
    dividends = get_dividends(soup)
    print("Dividends : ")
    print(dividends)
    d_companies.append(dividends[0])
    d_industries.append(dividends[1])
    d_sectors.append(dividends[2])      
        
#Stockages des données dans une DataFrame
df = pd.DataFrame({'Company': company,
                   'Quarter Mean': q_means,
                   'Quarter High': q_highs,
                    'Quarter Low': q_lows,
                    'Price': prices,
                    '% Change' : changes,
                    '% Shares Owned' : shares,
                    'Dividend Company' : d_companies,
                    'Dividend Industry' : d_industries,
                    'Dividend Sector' : d_sectors})

print(df)
