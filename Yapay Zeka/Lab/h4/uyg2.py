# -*- coding: utf-8 -*-

#%% YSA ile cep telefonu fiyatlarının artışının belirlenmesi

#kütüphanlerin yüklenmesi
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis, LocalOutlierFactor
from sklearn.decomposition import PCA

#h4-telefon_fiyat_değişimi.csv
#veri setinin yüklenmesi
veri = pd.read_csv("h4-telefon_fiyat_değişimi.csv")

#sınıf sayısının belirlenmesi
label_encoder = LabelEncoder().fit(veri.price_range)
labels = label_encoder.transform(veri.price_range)
classes = list(label_encoder.classes_)

#girdi ve çıktı verilerinin hazırlanması
X = veri.drop(["price_range"],axis=1)
y = labels

#verilerin standartlaştırılması
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#%% eğitim ve test verilerinin hazırlanması
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

"""
*********************** UYG-2 *****************************************
Verilen kodu inceleyerek çapraz doğrulama işlemi yapınız ve buna göre başarımı değerlendiriniz.
"""
#%% Basic KNN Method

knn = KNeighborsClassifier(n_neighbors= 2) #defalut değeri 5 tir.
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
cm  = confusion_matrix( y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
score =knn.score(X_test, y_test)
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

grid = KNN_Best_Params(X_train, X_test, y_train, y_test)

#%%

#çıktı değerlerinin kategorileştirilmesi
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#YSA modelinin oluşturulması
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model= Sequential()
model.add(Dense(16,input_dim=20,activation="relu")) # Girdi Katmanı
model.add(Dense(12,activation="relu")) # Ara Katmanı
model.add(Dense(4,activation="softmax")) # Çıktı Katmanı
model.summary()


#modelin derlenmesi
model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

#modelin eğitilmesi
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=150)

#eğitiim ve doğrulama başarımlarının gösterilmesi
import matplotlib.pyplot as plt
plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Başarımları")
plt.ylabel("Başarım")
plt.xlabel("Epok Sayısı")
plt.legend(["Eğitim","Test"],loc="upper left")
plt.show()

plt.plot(model.history.history["loss"])
plt.plot(model.history.history["val_loss"])
plt.title("Model Kayıpları")
plt.ylabel("Kayıp")
plt.xlabel("Epok Sayısı")
plt.legend(["Eğitim","Test"],loc="upper left")
plt.show()











