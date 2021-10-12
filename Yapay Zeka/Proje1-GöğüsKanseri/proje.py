# -*- coding: utf-8 -*-

#Gerekli kütüphanelerin eklenmesi
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis, LocalOutlierFactor
from sklearn.decomposition import PCA

#warning library
import warnings
warnings.filterwarnings("ignore")


#Veri setini yüklemek
data = pd.read_csv("data.csv")

#veri setinden sütun silme
data.drop(['Unnamed: 32','id'],inplace=True,axis=1)

#diagnosis sütununu target olarak değştirmek
data=data.rename(columns={"diagnosis":"target"})

#veriyi görselleştirme
sns.countplot(data["target"])
print(data.target.value_counts()) #veriye yazdırma

data["target"] = [1 if i.strip() =="M" else 0 for i in data.target] #Eğer datamız kötü huyluysa 1 olarak değilse 
#0 olarak değiştir.

#datamızdaki toplam sample sayısı
print(len(data))

#datamızın ilk 5 satırına hızlıca göz atmak
print(data.head())

#datanın boyutuna bakmak
print("Data Shape = ",data.shape)

#data ile ilgili bilgilere ulaşma
data.info()

#describe
describe = data.describe()

"""
standardization
missin value:none //yani kayıp değerler bu veride yok
"""











