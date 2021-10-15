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


#%% PCA Analysis

#PCA'ye başlamadan önce verimizin scaler etmemiz lazım
scaler = StandardScaler()
x_scaled  = scaler.fit_transform(x)

pca = PCA(n_components=2 ) #normalde 30 tane var biz bunu 2'ye düşürmüş olduk
pca.fit(x_scaled)
X_reduced_pca = pca.transform(x_scaled)
pca_data = pd.DataFrame(X_reduced_pca, columns=["p1","p2"])
pca_data["target"] = y
sns.scatterplot(x = "p1", y = "p2", hue = "target", data = pca_data)
plt.title ("PCA : p1 vs p2")


X_train_pca, X_test_pca, Y_train_pca, Y_test_pca = train_test_split(X_reduced_pca, y, test_size = test_size, random_state=42)

grid_pca  = KNN_Best_Params(X_train_pca, X_test_pca, Y_train_pca, Y_test_pca)


#visualize
cmap_light = ListedColormap(['orange', 'cornflowerblue'])
cmap_bold = ListedColormap(['darkorange','darkblue'])

h = .05
X = X_reduced_pca
x_min, x_max = X[:,0].min() -1, X[:,0].max() +1
y_min, y_max = X[:,1].min() -1, X[:,1].max() +1
xx, yy = np.meshgrid(np.arange(x_min,x_max,h),
                    np.arange(y_min,y_max,h))

Z = grid_pca.predict(np.c_[xx.ravel(),yy.ravel()])

#Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,Z , cmap = cmap_light)

#Plot also the training points
plt.scatter(X[:,0], X[:,1], c=y, cmap=cmap_bold,
            edgecolors='k', s =20)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("%i-Class classification (k = %i, weights = '%s')"
          % (len(np.unique(y)), grid_pca.best_estimator_.n_neighbors, grid_pca.best_estimator_.weights))

#%% NCA Analysis

nca = NeighborhoodComponentsAnalysis(n_components=2, random_state=42 )
nca.fit(x_scaled, y)
X_reduced_nca = nca.transform(x_scaled)
nca_data = pd.DataFrame(X_reduced_nca, columns = ["p1","p2"])
nca_data ["target"] = y
sns.scatterplot(x = "p1", y ="p2", hue = "target", data = nca_data) 
plt.title("NCA : p1 vs p2 ")



X_train_nca, X_test_nca, Y_train_nca, Y_test_nca = train_test_split(X_reduced_nca, y, test_size = test_size, random_state=42)

grid_nca  = KNN_Best_Params(X_train_nca, X_test_nca, Y_train_nca, Y_test_nca)


#visualize
cmap_light = ListedColormap(['orange', 'cornflowerblue'])
cmap_bold = ListedColormap(['darkorange','darkblue'])

h = .2 #step size in the mesh
X = X_reduced_nca
x_min, x_max = X[:,0].min() -1, X[:,0].max() +1
y_min, y_max = X[:,1].min() -1, X[:,1].max() +1
xx, yy = np.meshgrid(np.arange(x_min,x_max,h),
                    np.arange(y_min,y_max,h))

Z = grid_nca.predict(np.c_[xx.ravel(),yy.ravel()])

#Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,Z , cmap = cmap_light)

#Plot also the training points
plt.scatter(X[:,0], X[:,1], c=y, cmap=cmap_bold,
            edgecolors='k', s =20)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("%i-Class classification (k = %i, weights = '%s')"
          % (len(np.unique(y)), grid_nca.best_estimator_.n_neighbors, grid_nca.best_estimator_.weights))





























