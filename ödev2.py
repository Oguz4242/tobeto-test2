# 1. Soru
sayi1 = 1
sayi2 = 1

sayi_dizisi = [sayi1,sayi2]
for i in range(20):

    sayi1,sayi2 = sayi2, sayi1 + sayi2
    sayi_dizisi.append(sayi2)

print("Fibonacci serisi: ", sayi_dizisi)

# 2. Soru
sayi= int(input("Lütfen bir sayi giriniz: "))
carpanToplam=0
i=1
while i<sayi:
     if sayi%i==0:
          carpanToplam+=i
     i+=1
if sayi==carpanToplam:
     print("Tebrikler mükemmel sayıyı buldunuz.")
else:
     print ("Yeni bir sayı ile deneyiniz")

# 2.Soru Alternatif
sayi = int(input("Lütfen bir sayı giriniz:"))
toplam=0
 
for i in range(1,sayi):
    if(sayi%i == 0):
        toplam +=i

if(sayi == toplam):
    print("Mükemmel sayıdır.")
else:
    print("Mükemmel sayı değildir.")

# 3. Soru
import math
sayi1 = int(input("Lütfen birinci sayıyı giriniz : "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz : "))
 
ebob=math.gcd(sayi1,sayi2)
ekok=(sayi1*sayi2)/ebob
        
print ("EBOB:", ebob)
print ("EKOK:", ekok)


# 4. Soru
sayi = int(input("Lütfen bir sayı giriniz:"))
if sayi>1:   
    
    for i in range(2,sayi):
        if sayi%i == 0:
            print("Asal sayı değildir.")
            break
    else:
        print("Asal sayıdır.")
else:
    print("Asal sayı değildir.")

# 5. Soru
sayi = int(input("Lütfen asal çarpanlarına ayırmak istediğiniz sayıyı giriniz: "))
asal_carpanlar = []
i = 2
while sayi > 1:
    while sayi % i == 0:
            asal_carpanlar.append(i)
            sayi //= i
    i += 1

print("Asal Çarpanlar:", asal_carpanlar)