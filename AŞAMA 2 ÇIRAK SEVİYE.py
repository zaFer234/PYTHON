#SORU 1-2
x = float(input("İlk sayıyı giriniz:"))
y = float(input("İkinci sayıyı giriniz:"))
v = x*y

def tekçift():
    if v % 2 == 0 :
        print("SAYILARIN ÇARPIMI ÇİFTTİR.")

    else:
        print("SAYILARIN ÇARPIMI TEKTİR.")
    return

def degerlik():
    if 0 > v:
        print("SAYI NEGATİF.")

    else:
        print("SAYI POZİTİFTİR.")
    return

tekçift()
degerlik()



'''
SORU 3

İvme Nedir?

Çizgide hareket eden bir nokta ya da nesne, hızlanırsa veya yavaşlarsa ivme değişkenlik gösteriyor demektir.
Bir daire üzerindeki hareket sistemi, hızı sabit olsa dahi hızlanır. Çünkü yön sürekli olarak değişir. 
Diğer tüm hareket türleri bakımından, her iki efekt hızlanmaya katkı sunar.
İvme, bir zaman aralığında hız vektöründeki değişimin zaman aralığına bölümü olarak tanımlanır. Anlık ivme kesin 
bir anda ve konumda belirli bir zaman aralığı boyunca hızdaki değişimin zaman aralığı sıfıra giderken zaman 
aralığına oranının limiti ile verilir.
Örnek vermek gerekirse, hız saniyede metre olarak ifade edildiğinde hızlanma saniyede metre cinsinden ifade 
edilecektir

İvme Formülü ve İvme Hesaplama

İvme, hızdaki değişim ile aynı yöndeki bir vektördür. Δ v yani hız bir vektör olduğu için yönde değişim yaşayabilir.
Dolayısıyla hızlanma, hızda, yönde veya her ikisinde birden bir değişiklik görülmesi doğal karşılanır. Bir nesne
yavaşladığında, ivmesi hareketinin yönünün tersidir. Bu yavaşlama olarak bilinir.
İvme aşağıdaki formül kullanılarak hesaplanır.

İvme (a) = Hız (v)/ Zaman (t)

Hız, konum vektörünün bir türevi olduğundan, ivme vektörünün bileşenleri, sistemin koordinatlarının ikinci türevleri
şeklinde ifade edilebilir.
Kısa zaman aralıkları ise anlık hızlanma ile bulunur. Burada payda sıfıra yaklaştıkça bir oranın sınırına türev denir
Anlık ivme, bu durumda, zaman aralığı sıfıra yaklaştıkça ortalama ivmenin sınırıdır ya da alternatif olarak ivme
hızın türevidir.
Anlık hızlanma süresini şu şekilde hesaplayabilirsiniz.

a= lim ∆ v/ ∆ t = dv/ dt
∆ t → 0


Hız Nedir?

Herhangi bir objenin birim zamanda yaptığı yer değiştirme miktarına hız denir. Yani herhangi bir cisim bir noktadan
başka bir noktaya yaptığı hareket ile beraber hız gerçekleştirir. Tabii bu hareket hızın değişimine bağlı olarak 
birçok değişik unsurun sürecin içerisine girmesine olanak vermektedir.
Belirli bir noktadan başka bir noktaya hareket ile beraber, hız hesaplaması yapılabilmektedir. Tabii bunun 
sağlanabilmesi için ise mutlaka değişkenlerin bilinmesi gerekir.

Hız Nasıl Hesaplanır?

Alınan toplam yol miktarının süreye bölünmesi ile hız hesaplanabilmektedir. O yüzden matematiksel hesaplama 
konusunda hız, yol ve zamanın arasında orantı bulunmaktadır. Yani hız, yol ile doğru orantılı ancak zaman 
ile ters orantılıdır. Genel olarak ise fizikte ve matematikte hız şu şekilde hesaplanır;

X = V x T
X = Kat edilen mesafe
V = Hız
T = Alınan süre

Bu değişkenler ele alınmak suretiyle herhangi bir canlı ya da cansız varlığın hızı hesaplanabilmektedir. 
Tabii bu hesaplama içerisinde ivmelenme ile beraber birçok doğal unsur da sürecin içerisinde yer alabilmektedir
Elbette bu da çok daha hassas bir hesaplama imkanı tanır. Ancak genel olarak hız yukarıdaki formül altıda hesaplanır.

Yukarıda yazdığımız gibi hız X = V x T üzerinden hesaplanmaktadır.



Kuvvet Nedir ve Nasıl Oluşur?

Kuvvet: Hareket halinde olan bir cismi durduran yahut duran bir cismi hareket ettiren etki kuvvet olarak 
adlandırılmaktadır. Kuvvetin, ayrıca bir cismin şekil değişikliğine neden olabilen bir etki olduğu da ifade
edilebilir. İnsan için çok önemli olan pek çok farklı makinenin ve farklı sistemlerin temelinde kuvvet yatmaktadır.
Kuvvet ile birlikte hareket eden bütün cisimler, görevini yerine getirmek amacıyla gerekli olan enerjiyi ortaya 
çıkarır. Bu enerjiyle birlikte elde edilen güç üzerinden günlük yaşamda kullanılan birçok unsur ortaya çıkmaktadır.

Hareket ve kuvvetle ilgili en temel formül Fnet = m.a eşitliğidir. Bu formül mekanik fiziğin temelini oluşturmaktadır
Burada F kuvvet, m kütle ve a ivme olmaktadır. Formülü izah edersek bir cisme kuvvet etki ederse cisim ivmeli hareket 
eder.
'''

b = float(input("Geçen zamanı  giriniz:"))
d = float(input("Alınan yolu giriniz:"))
m = float(input("Kütle giriniz:"))

f = d / b
def hız():
    f = d / b
    print("{} hız".format(f))
    return

c = f / b
def ivme():
    c = f / b
    print("{} ivme".format(c))
    return

def kuvvet():
    n = m * c
    print("{} kuvvet".format(n))

hız()
ivme()
kuvvet()



#SORU 4

p = float(input("Kısa kenarı giriniz:"))
l = float(input("Uzun kenarı giriniz:"))

def alan():
    al = p * l
    print("{} alan".format(al))
    return

def çevre():
    çe = (2 * p) + (2 * l)
    print("{} çevre".format(çe))
    return

alan()
çevre()



#SORU 5
for i in range(3,501):
    if i%5==0 and i%7==0:
        print(i)


#SORU 6
w = float(input("Yaşınızı giriniz:"))
if w > 18:
    print("EHLİYET ALABİLİRSİNİZ.")
else:
    print("DAHA YAŞINIZ EHLİYET ALMAYA UYGUN DEĞİL.")
