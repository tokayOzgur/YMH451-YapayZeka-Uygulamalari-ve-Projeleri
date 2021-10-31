# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:07:34 2021

@author: Özgür Tokay
"""


#%% YSA ile cep telefonu fiyatlarının artışının belirlenmesi

#kütüphanlerin yüklenmesi
import numpy as py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

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

#eğitim ve test verilerinin hazırlanması
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#çıktı değerlerinin kategorileştirilmesi
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

""" ***************************** UYG-1 **************************
#YSA modelinin oluşturulması
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model= Sequential()
model.add(Dense(16,input_dim=20,activation="relu")) # Girdi Katmanı
model.add(Dense(12,activation="relu")) # Ara Katmanı
model.add(Dense(4,activation="softmax")) # Çıktı Katmanı
model.summary()
"""
#Uyg-1 Verilen Kodu inceleyerek kendi modelinizi oluşturunuz(10p)
#YSA modelinin oluşturulması
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model= Sequential()
model.add(Dense(16,input_dim=20,activation="relu")) # Girdi Katmanı
model.add(Dense(12,activation="relu")) # Ara Katmanı
model.add(Dense(6,activation="relu")) # Ara Katmanı
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



















