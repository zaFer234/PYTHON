#SORU 1
a = input("7 basamaklı sayı giriniz:")
toplam = 0
carpim = 1

for rakam in a:
    toplam += int(rakam)

print("Sayının rakamları toplamı:", toplam)

for rakam in str(a):
    if int(rakam) != 0:
        carpim *= int(rakam)

print("sayının rakamları çarpımı:", carpim)




#SORU2
b = float(input("1 Sayı giriniz:"))
c = float(input("2 Sayı giriniz:"))
v = float(input("3 Sayı giriniz:"))
d = float(input("4 Sayı giriniz:"))
s = float(input("5 Sayı giriniz:"))

f = [b,c,v,d,s]
list.sort(f)

h = f[0:2]
k = f[3:5]

A = (h[0] + h[1]) * f[2]
B = k[0] + k[1]

C = A / B
print(C)