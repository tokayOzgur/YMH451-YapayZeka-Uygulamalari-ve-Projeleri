# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:30:06 2021

@author: Özgür Tokay
"""

#%% YSA ile cep telefonu fiyatlarının artışının belirlenmesi

#kütüphanlerin yüklenmesi
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#h4-telefon_fiyat_değişimi.csv
#veri setinin yüklenmesi
veri = pd.read_csv("h4-diyabet.csv")

#sınıf sayısının belirlenmesi
label_encoder = LabelEncoder().fit(veri.output)
labels = label_encoder.transform(veri.output)
classes = list(label_encoder.classes_)

#girdi ve çıktı verilerinin hazırlanması
X = veri.drop(["output"],axis=1)
y = labels

#verilerin standartlaştırılması
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#eğitim ve test verilerinin hazırlanması
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

#çıktı değerlerinin kategorileştirilmesi
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#YSA modelinin oluşturulması
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model= Sequential()
model.add(Dense(8,input_dim=8,activation="relu")) # Girdi Katmanı
model.add(Dense(10,activation="relu")) # Ara Katmanı
model.add(Dense(2,activation="softmax")) # Çıktı Katmanı
model.summary()

#tahmin değerlerin çekilmesi
tahmin = model.predict(X_test)

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


#%% Uyg-5 
"""

"""
# plt.figure()
# lw = 2
# plt.plot(
#     fpr[2],
#     tpr[2],
#     color="darkorange",
#     lw=lw,
#     label="ROC curve (area = %0.2f)" % roc_auc[2],
# )
# plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel("False Positive Rate")
# plt.ylabel("True Positive Rate")
# plt.title("Receiver operating characteristic example")
# plt.legend(loc="lower right")
# plt.show()




#%% Örnek Uygulama
from sklearn.metrics import roc_curve,auc
import matplotlib.pyplot as plt

gercek_degerler = [1,1,0,1,0,0,0,1,0,1,1,1]
tahminler = [0.98,0.43,0.3,0.55,0.35,0.2,0.1,0.60,0.03,0.85,0.35,0.58]
tahminler_2 = [0.63,0.54,0.4,0.7,0.4,0.66,0.51,0.4,0.3,0.8,0.71,0.4]

ypo, duyarlilik, esik_degerleri = roc_curve(gercek_degerler,tahminler)
auc_1 = auc(ypo,duyarlilik)

ypo_2, duyarlilik_2, esik_degerleri_2 = roc_curve(gercek_degerler,tahminler_2)
auc_2 = auc(ypo_2,duyarlilik_2)


plt.plot(ypo,duyarlilik,label="Model 1 AUC = %0.3f" %auc_1)
plt.plot(ypo_2,duyarlilik_2,label="Model 2 AUC = %0.3f" %auc_2)

plt.xlabel("Yanlış Pozitif Oranı")
plt.ylabel("Duyarlılık")

plt.legend(loc='lower right')

plt.show()