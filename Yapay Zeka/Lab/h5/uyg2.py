# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 23:38:33 2021

@author: tokay
"""

import pandas as pd
import SimpSOM as sps
from sklearn.cluster import KMeans
import numpy as np

#Veri Setinin  yüklenmesi ve gerekli veriler ile kullanılması
veri = pd.read_csv("CC GENERAL.csv")
X= veri.drop(["CUST_ID","BALANCE"],axis=1)

#Ağın oluşturulması
net = sps.somNet(50, 50, X.values, PBC=True)

#Ağın Eğitilmesi
net.train(0.01, 1000)

#Veri noktalarının 2 boyutlu bir haritaya gömülmesi ve kümelemenin yapılması
hrt = np.array((net.project(X.values)))
kmeans=KMeans(n_clusters=3, max_iter=300, random_state=0)

#Kümeleme sonuçlarının gösterilmesi
y_kmeans = kmeans.fit_predict(hrt)

#Kümelerin etiketlerinin belirlenmesi
veri["kümeler"] = kmeans.labels_

#1 numaralı kümenin değerlerine bakılması
print(veri[veri["kümeler"]==0].head(5))

#2 numaralı kümenin değerlerine bakılması
print(veri[veri["kümeler"]==1].head(5))

#3 numaralı kümenin değerlerine bakılması
print(veri[veri["kümeler"]==2].head(5))

#Tüm sütünları gösterme
pd.set_option('display.max_columns', None)

