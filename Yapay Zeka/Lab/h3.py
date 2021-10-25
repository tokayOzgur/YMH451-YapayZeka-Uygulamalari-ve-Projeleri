# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:26:29 2021

@author: baris
"""

#Kullanıcıdan integer türünde bir değer isteyiniz. İstemiş olduğunuz bu değerin çarpım tablosu
#değerlerini gösteren kodu for döngüsü ile gerçekleştiriniz (10p).

sayi = int(input("Bir sayi girin : "))
for i in range(11):
    print(i*sayi)
    
#Girilen bir sayının kaç basamaklı olduğunu belirleyen programı while döngüsü ile gerçekleştiriniz (10p)


a = int(input("Bir sayı girin basamak : "))
say = 0
while a > 0:
    a = a // 10
    say = say + 1
print("bu kadar basamaklı : ",say)


#Aşağıda bir listeye ait sayısal değerler verilmiştir. 
#sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#Bu listedeki 5’e bölünen sayıları çıktı olarak veren programı hem for hem de while döngüsü ile 
#gerçekleştiriniz. 150’den büyük değerleri dikkate almayınız (20p).

sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in sayısalDeğerler:
    if(i%5==0):
        print(i)
        
index = 0
while(index <len(sayısalDeğerler)):
    
    if(sayısalDeğerler[index]%5==0):
        print(sayısalDeğerler[index])
    index+=1
    
    
#Kullanıcıdan 3 adet (a, b ve c) değer alınız. a (dahil) ve b (dahil) arasında kaç sayının c’ye 
#bölünebildiğini belirleyen programı yazınız (20p).
#Örnek: a = 20, b = 40, c = 5 ise Çıktı: 5 

birincisayi= int(input("Birinci sayıyı gir : "))
ikincisayi= int(input("İkinci sayıyı gir : "))
ucuncusayi= int(input("Ucuncu sayıyı gir : "))
sayac=0
if (birincisayi<ikincisayi):
    
    for i in range(birincisayi,ikincisayi+1):
        if(i % ucuncusayi==0):
            sayac+=1
elif(birincisayi>ikincisayi):
    for i in range(ikincisayi,birincisayi+1):
        if(i % ucuncusayi==0):
            sayac+=1
            
print(sayac)
    

#diğer soru


for i in range(1,100):
    print(i ,"-",(100-i))
    
    
#son soru Kullanıcıdan bir IP adresi isteyiniz. İstediğiniz bu IP adresinden sonraki 5 değeri çıktı olarak 
#veren programı yazınız (30p)


ornekıp = []
for x in range(4):
    gelenip = int(input("İp nizin {} indeks değerini girin : ".format(x))) 
    if (gelenip<0):
        print("ıp değeri 0 dan küçük sayı olamaz.")
        break
    #ornekıp.append(gelenip)
    ornekıp.insert(x, gelenip)
sayac =0   
while sayac<4:
    ornekıp[3]+=1
    if(ornekıp[3]>255):
        ornekıp[3]=0
        ornekıp[2]+=1
    elif(ornekıp[2]>255):
        ornekıp[2]=0
        ornekıp[1]+=1
    elif(ornekıp[1]>255):
        ornekıp[1]=0
        ornekıp[0]+=1
    elif(ornekıp[0]>255):
        print("ip nizin ilk indeksi 255 ten büyük olamaz")
        break

        
    sayac+=1
    print(ornekıp)
    
        

    
        
    














 