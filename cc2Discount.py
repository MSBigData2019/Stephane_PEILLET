#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:35:05 2018

@author: stephanepeillet
"""

from requests import get
from bs4 import BeautifulSoup
import pandas as pd


#Qui est possède la meilleur réduction entre acer et dell.
url = "https://www.darty.com/nav/achat/informatique/ordinateur_portable/marque__dell__DELL.html"
url2 = "https://www.darty.com/nav/achat/informatique/ordinateur_portable/marque__acer__ACER.html" 


#trouver le nombre de reduction chez dell
page = get(url)
soup = BeautifulSoup(page.content, 'html.parser')
reducContainer = soup.find_all('p', class_ = "darty_prix_barre_remise darty_small separator_top")


page = get(url2)
soup = BeautifulSoup(page.content, 'html.parser')
reducContainer2 = soup.find_all('p', class_ = "darty_prix_barre_remise darty_small separator_top")
