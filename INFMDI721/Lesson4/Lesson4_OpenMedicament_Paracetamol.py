
# coding: utf-8

# # <center>Contrôle Continue MDI721</center>

# ### Exercice:
# Construire une base de données propre de conditionnement pour chaque vendeurs depuis open medicaments et à chaque fois extraire son dosage, sa forme galénique, sa posologie... afin de comparer les traitements.

# In[1]:


# coding: utf-8
# Imports:
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import json
import re


# In[2]:


url = "https://www.open-medicaments.fr/api/v1/medicaments?query=paracetamol&limit=100"
#url = "https://www.open-medicaments.fr/api/v1/medicaments?query=paracetamol%20500"


# In[3]:


page = get(url)
df = pd.read_json(page.content)


# In[4]:


df.head()


# In[5]:


# Pour extraire la forme galénique:
regex_forme = r",([\w\s]*)"
denomination = "PARACETAMOL ZYDUS 500 mg, gélule"
forme = re.findall(regex_forme, denomination)
print(f"Forme galénique : {forme}")


# In[6]:


# Pour extraire toutes les informations :
regex = r"([\D]*)(\d+)(.*),(.*)"
denomination = "PARACETAMOL ZYDUS 500 mg, gélule"
res = re.findall(regex, denomination)
print(f"Résultat : {res}")


# In[7]:


# Application sur toute la série
serie = df["denomination"]
res = serie.str.extract(regex)
res.head()


# In[8]:


res["mul"] = 1000
res["mul"] = res["mul"].where(res[2].str.strip() == "g", 1)
res["dosage"] = res[1].fillna(0).astype(int) * res["mul"]
res.head()


# In[9]:


res = res.drop(columns=["mul"])
res.head()


# In[19]:


# Mise en forme de la dataframe:
res = res.drop(columns=[1, 2])
res["grammage"] = "mg"
res = res.rename(columns = {0: "Nom medicaments", 3: "Forme"})
res.head()


# In[20]:


def main():
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(res)

if __name__ == '__main__':
    main()

