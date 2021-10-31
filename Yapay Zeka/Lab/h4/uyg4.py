# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:30:06 2021

@author: Özgür Tokay
"""

#%% YSA ile cep telefonu fiyatlarının artışının belirlenmesi

#kütüphanlerin yüklenmesi
import numpy as py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#h4-telefon_fiyat_değişimi.csv
#veri setinin yüklenmesi
veri = pd.read_csv("h4-diyabet.csv")

#sınıf sayısının belirlenmesi
label_encoder = LabelEncoder().fit(veri.plasma)
labels = label_encoder.transform(veri.plasma)
classes = list(label_encoder.classes_)

#girdi ve çıktı verilerinin hazırlanması
X = veri.drop(["plasma"],axis=1)
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

#YSA modelinin oluşturulması
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model= Sequential()
model.add(Dense(16,input_dim=8,activation="relu")) # Girdi Katmanı
model.add(Dense(12,activation="relu")) # Ara Katmanı
model.add(Dense(4,activation="softmax")) # Çıktı Katmanı
model.summary()

#modelin derlenmesi
model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

#modelin eğitilmesi
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=50)

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
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.metrics import roc_auc_score

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_test[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_test.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

plt.figure()
lw = 2
plt.plot(
    fpr[2],
    tpr[2],
    color="darkorange",
    lw=lw,
    label="ROC curve (area = %0.2f)" % roc_auc[2],
)
plt.plot([0, 1], [0, 1], color="navy", lw=lw, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver operating characteristic example")
plt.legend(loc="lower right")
plt.show()





