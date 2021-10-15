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


#%% Outlier
y=data.target
x=data.drop(["target"],axis=1) 
columns = x.columns.tolist()

clf = LocalOutlierFactor()
y_pred = clf.fit_predict(x) # -1 ve 1
X_score = clf.negative_outlier_factor_

outlier_score=pd.DataFrame()
outlier_score["score"] = X_score

# threshold
threshold = -2.5
filtre=outlier_score["score"]<threshold
outlier_index=outlier_score[filtre].index.tolist()

plt.figure()
plt.scatter(x.iloc[outlier_index,0], x.iloc[outlier_index,1], color="blue", s=50, label = "Outliers")
plt.scatter(x.iloc[:,0], x.iloc[:,1], color="k", s=3 , label= "Data Points")

radius = (X_score.max() - X_score)/(X_score.max() - X_score.min()) #Normalizasyon işlemi
outlier_score["raidus"] = radius
plt.scatter(x.iloc[:,0], x.iloc[:,1], s=1000*radius, edgecolors="r", facecolors="none", label="Outlier Scores")
plt.legend()#labelların görünmesi için gerekli komut
plt.show()

#drop outliers
x = x.drop(outlier_index)
y = y.drop(outlier_index).values

# %% train test split

test_size=0.3
X_train, X_test, Y_train, Y_test =  train_test_split(x,y,test_size=test_size, random_state = 42)

#%% 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train_df = pd.DataFrame(X_train,columns=columns)
X_train_df_describe = X_train_df.describe()

X_train_df["target"]=Y_train
#boxplot
data_melted = pd.melt(X_train_df, id_vars="target",
                      var_name="features",
                      value_name="value")

plt.figure()
sns.boxplot(x="features", y = "value", hue = "target" , data = data_melted)
plt.xticks(rotation = 90)
plt.show()

#pair plot
sns.pairplot(X_train_df[corr_features], diag_kind = "kde", markers = "+", hue="target")
plt.show()

#%% Basic KNN Method

knn = KNeighborsClassifier(n_neighbors= 2) #defalut değeri 5 tir.
knn.fit(X_train, Y_train)
y_pred = knn.predict(X_test)
cm  = confusion_matrix( Y_test, y_pred)
acc = accuracy_score(Y_test, y_pred)
score =knn.score(X_test, Y_test)
print("Score: ",score)
print("CM: ",cm)
print("Basic KNN Acc: ",acc)

#%% Choose best parameters
def KNN_Best_Params(x_train,x_test,y_train,y_test):
    k_range = list(range(1,31))
    weight_options = ["uniform","distance"]
    print()
    param_grid = dict(n_neighbors = k_range, weights = weight_options)
    
    knn = KNeighborsClassifier()
    grid = GridSearchCV(knn, param_grid, cv = 10, scoring = "accuracy")
    grid.fit(x_train, y_train)
    
    print("Best training score : {} with parameters {}".format(grid.best_score_, grid.best_params_))
    print()
    
    knn = KNeighborsClassifier(**grid.best_params_)
    knn.fit(x_train, y_train)
    
    y_pred_test = knn.predict(x_test)
    y_pred_train = knn.predict(x_train)

    cm_test = confusion_matrix(y_test, y_pred_test)
    cm_train = confusion_matrix(y_train, y_pred_train)

    acc_test = accuracy_score(y_test, y_pred_test)
    acc_train = accuracy_score(y_train, y_pred_train)
    print("Test Score : {}, Train Score : {}".format(acc_test, acc_train))
    print()
    print("CM Test : ",cm_test)
    print("CM Train : ",cm_train)
    
    return grid

grid = KNN_Best_Params(X_train, X_test, Y_train, Y_test)













