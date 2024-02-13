sayilar = [100,200,300,"Merhaba",True,15.5]
#programcılar saymaya sıfırdan başlar
print(sayilar[0])
print(sayilar)

sayilar.append(400)
print(sayilar)

sayilar.remove("Merhaba") #değere göre
print(sayilar)

sayilar.pop() #indexe göre siler (default son index) - girilme sırası heralde
print(sayilar)

add = [700,800,900]
sayilar.extend(add)
print(sayilar)

sayilar.clear() #listenin içini boşaltıyoruz
print(sayilar)

