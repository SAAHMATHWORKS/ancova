# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:29:48 2018

@author: smooth computers llc
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from sklearn import linear_model
from sklearn.model_selection import train_test_split

plt.clf()
#Lecture du data frame
house_data = pd.read_csv('house_data.csv')

#Nettoyage du dataframe
house_data1=house_data.dropna(axis = 0, how = 'any')


Facteur=house_data1.iloc[0:len(house_data1),2]
typ_regions= np.unique(Facteur)
Nombre_regions=len(typ_regions)
Facteur[Facteur==1]="region_1"
Facteur[Facteur==2]="region_2"
Facteur[Facteur==3]="region_3"
Facteur[Facteur==4]="region_4"
Facteur[Facteur==10]="region_10"
house_data1.arrondissement=Facteur

dummies = pd.get_dummies(house_data1["arrondissement"])
house_data1 = pd.concat([house_data1, dummies], axis=1)
house_data1.head()
X = house_data1[["surface", "region_1", "region_2", "region_3","region_4","region_10"]]
X = sm.add_constant(X) # une autre façons d'ajouter une constante
y = house_data1["price"]

model = est = smf.ols(formula='price ~ surface * arrondissement', data=house_data1)
results = model.fit()
print(results.summary())

