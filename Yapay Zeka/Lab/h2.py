# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:00:17 2021

@author: azder
"""

#%% Uyg-1
"""
Kullanıcıdan 3 adet integer türünde değer alınız. Almış olduğunuz bu değerler bir üçgenin
açılarını ifade edecektir. Bu açı değerlerine göre bu üçgenin dik, geniş ya da dar üçgen olup
olmadığını belirleyen programı yazınız (20p).
"""

val1 = int(input("Değeri giriniz: "))
val2 = int(input("Değeri giriniz: "))
val3 = int(input("Değeri giriniz: "))
toplam = val1+val2+val3
# Üç açısının ölçüsü de 90° den küçük olan üçgenlere dar açılıüçgen denir.
if(toplam<=180 and val1<90 and val2<90 and val3<90):
    print("Dar Açılı Üçgen")
    
# Bir açısının ölçüsü 90° ye eşit olan üçgenlere denir.
elif(toplam<=180 and val1==90 or val2==90 or val3==90):
    print("Dik Açılı Üçgen")

# Bir açısının ölçüsü 90° den büyük olan üçgenlere denir.
elif( toplam<=180 and val1>90 or val2>90 or val3>90):
    print("Geniş Açılı Üçgen")

else:
    print("Girdiğiniz değerler bir üçgene ait değildir.")
    
#%% Uyg-2
