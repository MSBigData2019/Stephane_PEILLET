#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:58:33 2018

@author: stephanepeillet
"""


import requests
from bs4 import BeautifulSoup
import numpy as np

pageNum = ""
HP = f'https://www.darty.com/nav/achat/informatique/ordinateur_portable/portable/marque_{pageNum}_hp__HP.html'
DELL = f'https://www.darty.com/nav/achat/informatique/ordinateur_portable/portable/marque_{pageNum}_dell__DELL.html'
              
def getAVG(link) :
	pages = ["", "2", "3", "4", "6", "7"]
	discounts = []
	for page in pages :
		pageNum = page
		page = requests.get(link)
		soup = BeautifulSoup(page.text,'html.parser')
		remises = soup.find_all('span', class_ = "striped_price")
		discounts += [float(remise.text[2:-1]) for remise in remises]
	return sum(discounts)/len(discounts)

print('HP : ' + str(getAVG(HP)))
print('DELL : ' + str(getAVG(DELL)))



