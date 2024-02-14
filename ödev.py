# 1. Soru
kilo = float(input("Lütfen kilonuzu kg cinsinden girin: "))
boy = float(input("Lütfen boyunuzu metre cinsinden girin: "))
 
vki = kilo / (boy ** 2)
 
if vki < 18.5:
    print("Zayıf")
elif vki >= 18.5 and vki < 24.9:
    print("Normal")
elif vki >= 25 and vki < 29.9:
    print("Kilolu")
else:
    print("Obez")
 
print("Vücut kitle indeksiniz: " "{:.2f}".format(vki))

# 2. Soru
maas = float(input("Lütfen maaşınızı giriniz: "))
zam = float(input("Lütfen zam oranınızı(%) giriniz: "))
zamliMaas = (maas + maas * zam/100)
print("Zamlı maaş miktarınız: " , zamliMaas)

# 3. Soru
sayi1 = float(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))
sayi3 = float(input("Lütfen üçüncü sayıyı giriniz: "))
text = "En büyük sayı: "

if sayi1 >= sayi2 and sayi1 >= sayi3:
    print("{message} {sonuc}".format(message=text, sonuc=sayi1))
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    print("{message} {sonuc}".format(message=text, sonuc=sayi2))
else:
    print("{message} {sonuc}".format(message=text, sonuc=sayi3))

# 3. Soru if, elif, else olmadan
sayi1 = float(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))
sayi3 = float(input("Lütfen üçüncü sayıyı giriniz: "))

sonuç = {sayi1 >= sayi2 and sayi1>=sayi3: "En büyük sayı ilk sayıdır.",
        sayi2 >= sayi1 and sayi2 >= sayi3: "En büyük sayı ikinci sayıdır."}.get(
    True, "En büyük sayı üçüncü sayıdır.")

print(sonuç)

# 3. Soru Alternatif (Zor)
def en_büyük_sayi_bul(sayi1, sayi2, sayi3):
    if sayi1 >= sayi2 and sayi1 >= sayi3:
        return sayi1
    elif sayi2 >= sayi1 and sayi2 >= sayi3:
        return sayi2
    else:
        return sayi3
def kullanicidan_bilgi_al():
    try:
        sayi1 = float(input("Lütfen ilk sayıyı giriniz: "))
        sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))
        sayi3 = float(input("Lütfen üçüncü sayıyı giriniz: "))
        return sayi1, sayi2, sayi3
    except ValueError:
        print("Yanlış veri girişi. Lütfen geçerli sayılar giriniz.")
        return kullanicidan_bilgi_al()

sayi1, sayi2, sayi3 = kullanicidan_bilgi_al()
en_büyük_sayi = en_büyük_sayi_bul(sayi1, sayi2, sayi3)
print(f"En büyük sayı: {en_büyük_sayi}")

# 3. Soru Alternatif
sayi_listesi =[]
sayi_listesi.append(float(input("Lütfen birinci sayıyı giriniz: ")))
sayi_listesi.append(float(input("Lütfen ikinci sayıyı giriniz: ")))
sayi_listesi.append(float(input("Lütfen üçüncü sayıyı giriniz: ")))

print("En büyük sayı: ",max(sayi_listesi))

# 4. Soru
import math
r = float(input("Lütfen r yarıçapını giriniz: "))
alan = math.pi*r**2
cevre = 2*math.pi*r
print("Kürenin alanı: ", "{:.4f}".format(alan))
print("Kürenin çevresi: ", "{:.4f}".format(cevre))

# 5. Soru
sayi = input("Lütfen bir sayı giriniz: ")
if sayi == sayi[::-1]:
    print("Evet sayı bir palindromdur.")
else:
    print("Hayır, sayı bir palindrom değildir.")

# 5. Soru Alternatif
sayi = input("Lütfen bir sayı giriniz: ")
sayiTersi = sayi[::-1]
print("Sayının tersi: ", sayiTersi)
if sayi == sayiTersi:
    print("Evet sayı bir palindromdur.")
else:
    print("Hayır, sayı bir palindrom değildir.")