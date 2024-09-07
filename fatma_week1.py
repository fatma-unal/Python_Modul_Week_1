# SORU - 1

for i in range(1, 10):
    print(i)



#SORU - 2

#for dongusu kullanilarak yapilan cozum

sayi = int(input("Bir sayi girin: "))

for i in range(0, sayi, 2):
    print(i)

# while dongusu kullanilarak yapilan cozum

sayi = int(input("Bir sayi girin: "))
i = 0
while i < sayi:
    print(i)
    i += 2



#SORU - 3

ilk_sayi = int(input("Ilk sayiyi giriniz: "))
son_sayi = int(input("Son sayiyi giriniz: "))

for sayi in range(ilk_sayi + 1, son_sayi + 1):
    print(sayi)



#SORU - 4

sayi = int(input("Bir sayi giriniz: "))

if sayi % 2 == 0:
    print(f"{sayi} bir cift sayidir.")

else:
    print(f"{sayi} tek sayidir.")



#SORU - 5

import math

sayi = int(input("Pozitif bir sayi giriniz: "))

result = math.factorial(sayi)
print(f"{sayi}! = {result}")



#SORU - 6

bolen_sayisi = 0
for i in range(2, sayi + 1):
    if sayi % i == 0:
        bolen_sayisi += 1

if bolen_sayisi == 1:
     print(f"{sayi} asal bir sayidir")

else:
    print(f"{sayi} asal degildir")

