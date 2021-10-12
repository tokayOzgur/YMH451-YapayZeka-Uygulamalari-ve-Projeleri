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

# %% EDA 

#Correlation / Korelasyon
corr_matrix= data.corr()
sns.clustermap(corr_matrix, annot=True,  fmt=".2f")
plt.title("Correlation Between Features")
plt.show()


#
threshold = 0.75 # bu değerden yüksek olanları filtrelemek
filtre = np.abs(corr_matrix["target"]) > threshold
corr_features = corr_matrix.columns[filtre].tolist()
sns.clustermap(data[corr_features].corr() , annot=True, fmt=".2f")  
plt.title("Correlation Between Features with Corr Threshold 0.75")

"""
there are some  corrleted featrues
"""


#box plot
data_melted=pd.melt(data, id_vars="target",
                    var_name="features",
                    value_name="value")
plt.figure()#yeni figür oluştur
sns.boxplot(x = "features", y="value", hue="target", data=data_melted)
plt.xticks(rotation=90)#featuresların isimleri 90 derece dik olucaktır 
plt.show()

"""
Buradaki box_plottan anlaam çıkartabilmemiz için veri normalizasyonaa yada standardization'a
 tabi tutmamız lazım
"""

"""
standardization-normalization
"""

#pair plot
sns.pairplot(data[corr_features], diag_kind="kde", markers="+", hue="target")
plt.show()


"""
skewness (çarpıklık)
"""








