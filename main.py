print("Merhaba Tobeto Test Ekibi")

#degiskenler
#metinsel - numerik - obje

text = "Merhaba "
kullaniciAdi = "Oğuz"
print(text+kullaniciAdi)

studentCount = "45" #string
print(studentCount +"5") #455

studentCount = 5 #integer => tam sayı
print(studentCount +5) #10

averagePoint = 25.5 # double - decimal - float => ondalıklı sayı
print(averagePoint + 5)

isVerified = True # boolean
print(isVerified)

print(type(text)) # degisken tiplerini ögrenmek icin yazabiliriz
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))

# matematiksel - mantıksal
number = 10
print(10 + 10)
print(number + number)

print(10 - 5)
print(number -5)

print(number /2)

print(number * 3)

print(number % 3) #mod:

#mantıksal operatörler => karşılaştırma operatörleri

print(number == 10) #true
print(number == 11) #false

print(number != 10) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

#string interpolation =>metin birleştirme
text = "Merhaba"
kullaniciAdi = "Oğuz"
totalText = text+" "+kullaniciAdi
print(totalText)

totalText = "{message} Sayın {name}".format(message=text,name=kullaniciAdi)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {kullaniciAdi}"
print(totalText)

print(type(totalText))

