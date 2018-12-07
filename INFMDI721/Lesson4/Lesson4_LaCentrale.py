
# coding: utf-8

# # <center>DM La Centrale MDI720</center>

# L'objectif est de générer un fichier de données sur le prix des Renault Zoé sur le marché de l'occasion en Ile de France, PACA et Aquitaine. On fera le scrap sur le site Lacentrale Le fichier doit être propre et contenir les infos suivantes : version, année, kilométrage, prix, téléphone du propriétaire, est ce que la voiture est vendue par un professionnel ou un particulier.
# 
# Rem :Les données quanti (prix, km notamment) devront être manipulables (pas de string, pas d'unité). On ajoute une colonne si la voiture est plus chère ou moins chère que sa côte moyenne.

# In[2]:


# Imports 
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[3]:


def getLinksForOffers(website):
    linksArray=[]
    for i in range(1,3):
        url= website.format(i)
        result = requests.get(url)
        if result.status_code == 200:
            soup= BeautifulSoup(result.content,"html.parser")
            links=soup.findAll("a", "linkAd ann")
            for link in links:
                linksArray.append(link["href"])
        else :
            print(result.status_code)
    return linksArray
        
def getInfosFromLinks(links):
    for link in links: 
        result = requests.get(website+link)
        if result.status_code == 200:
            soup= BeautifulSoup(result.content, "html.parser")
            getInfosFromLink(soup)
        else :
            print(result.status_code)

def getInfosFromLink(soup):
    global df
    global arr
    price=soup.find("div", "gpfzj").find("strong").text.strip()
    price1=price.replace(" ","").replace('€',"").replace(u'\xa0',"")
    infos=soup.find("ul", "infoGeneraleTxt").findAll("li")
    annee=infos[0].find("span").text
    kilometrage=infos[1].find("span").text.replace("km","").replace(" ","").replace("-","")
    modele= soup.findAll("h3","mL20")[0].find("span").text.strip()
    arr.append([price1,annee, kilometrage, modele])


# In[4]:


website="https://www.lacentrale.fr"
websiteformat = "https://www.lacentrale.fr/listing?makesModelsCommercialNames=RENAULT%3AZOE&options=&page={}"
offers=getLinksForOffers(websiteformat)
arr=[]
getInfosFromLinks(offers)
df = pd.DataFrame(data=arr,columns=('price', 'annee','kilometrage','modele'))
print(df)


# In[5]:


df


# In[7]:


def main():
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)

if __name__ == '__main__':
    main()

