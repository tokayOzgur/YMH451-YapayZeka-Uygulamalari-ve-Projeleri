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
"""
İçinde uzaylı olan bir oyun geliştirdiğinizi düşünün. uzaylı_rengi isminde bir değişken oluşturun
ve bu değişken string türünde değerler alsın. Bu değişkene kırmızı, yeşil ya da sarı
değerlerinden birini klavyeden veriniz. 
Eğer uzaylının rengi yeşilse “Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız” şeklinde bir çıktı veriniz. 
Eğer rengi yeşil değilse "Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız" şeklinde çıktı veriniz.
 Senaryoya ait programı yazınız (20p).
"""

uzayli_rengi = str.upper(input("uzayli rengini girin : "))
# print(uzayli_rengi)
if (uzayli_rengi =="YEŞIL" or uzayli_rengi =="YEŞİL" or uzayli_rengi =="YESIL" ):
    print("Tebrikler, yesil uzaylıya ateş ettiğiniz için 5 puan kazandınız")

else:
    print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız")

#%% Uyg-3
"""
Bir önceki sorudaki örneğe dayanarak if-elif-else yapılarını kullanarak aşağıdaki soruları
cevaplayınız (20p).
a) Eğer uzaylı rengi yeşil ise "Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız",
b) Eğer uzaylı rengi sarı ise "Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız",
c) Eğer uzaylı rengi kırmız ise "Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız"
şeklinde çıktı veren programı yazınız.
"""

uzayli_rengii = str.upper(input("uzayli rengini girin : "))
if (uzayli_rengi =="YEŞIL" or uzayli_rengi =="YEŞİL" or uzayli_rengi =="YESIL"):
    print("Tebrikler, yesil uzaylıya ateş ettiğiniz için 5 puan kazand?n?z")
elif (uzayli_rengi =="KIRMIZI"):
    print("Tebrikler, kırmızi uzaylıya ateş ettiğiniz için 15 puan kazandınız")
elif (uzayli_rengi =="SARI"):
    print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız")
    
#%% Uyg-4
"""
if-elif-else yapılarını kullanarak bir insanın yaşam evreleri ile ilgili programı oluşturunuz. int
türünde, yaş isminde bir değişken oluşturup, bu değişken için gerekli olan değeri kullanıcıdan
isteyiniz (20p).
a) Eğer bir insanın yaşı 2 yaşından küçük ise, "Bu kişi bebektir",
b) Eğer bir insanın yaşı 2 ile 4 arasındaysa (2 dâhil) "Bu kişi yeni yürümeye başlayan çocuktur",
c) Eğer bir insanın yaşı 4 ile 13 arasındaysa (4 dâhil) "Bu kişi çocuktur",
d) Eğer bir insanın yaşı 13 ile 20 arasındaysa (13 dâhil) "Bu kişi ergendir",
e) Eğer bir insanın yaşı 20 ile 65 arasındaysa (20 dâhil) "Bu kişi yetişkindir",
f) Eğer bir insanın yaşı 65 ve üstü ise (65 dâhil) "Bu kişi yaşlıdır" şeklinde çıktı veriniz.
"""

yas = int(input("yaşı girin : "))
if 0<yas<2:
    print("Bu kişi bebeketir")
elif 2<=yas<4:
    print("Bu kişi yeni yürümeye ba?layan çocuktur")
elif 4<= yas <13:
    print("Bu kişi çocuktur.")
elif 13<= yas<20:
    print("Bu kişi ergendir")
elif 20<=yas<65:
    print("Bu kişi yetişkindir.")
else:
    print("Bu kişi Yaşlıdır.")
    
#%% Uyg-5
"""
Favori meyvelerinizin olduğu bir liste oluşturunuz ve bu listede 5 adet meyveniz bulunsun.
Listenin adı favori_meyveler şeklinde tanımlansın. if-else yapısını kullanarak örnekte verilen
meyvelerin favori listenizde olup olmadığını kontrol ediniz. Örnek meyveler; elma, armut,
karpuz, kavun, muz, portakal, çilek, vişne, kiraz ve mandalina (20p).
"""

favori_meyveler = ["armut","kiraz","çilek","muz","avokado"]

meyve_Sec = str(input("Listede aramak istediğiniz meyve : "))
for i in favori_meyveler:
    if i==meyve_Sec:
        print("Listede var") 
    
    
    
    
    