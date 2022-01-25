from random import randint

print('''
***KURALLAR***
1-KULLANICI GİRİŞİ DÜZGÜN YAPILMALI.
2-OYUN 5 RAUNDDAN OLUŞMAKTADIR.
3-HER HANGİ BİR SAYI GİRİP ŞANS HASSARI ALINIR.
4-20 ÜZERİ SAYI GİRİLİRSE DAHA FAZLA HASAR VERME İHTİMALİ YĞKSEKTİR.
5-20 SAYISI YAZILIRSA OYUNCUYA HASAR VEREMEZSİN.
6-KİMSENİN CANI BİTMEZSE OYUN BERABERE BİTER.
7-OYUN SONU TEPKİ GELMEZ İSE BERABERE BİTMİŞTİR.
''')




kadı = input("Oyunda kayıtlı kullannıcı adlarını giriniz:(İKİ AD ARASI BOŞLUK BIRAKIN!)")
şifre = input("Oyunda kayıtlı şifreyi giriniz:(BOŞLUK BIRAKIN!)")
dkkullanıcı = "zafer ömer"
dşifre = "12345 98745"
oyuncu1 = "ömer"
oyuncu2 = "zafer"
oyuncu1can = 100
oyuncu2can = 100

if kadı == dkkullanıcı and şifre == dşifre:
    if oyuncu1can or oyuncu2can < 101:


        print("BAŞARILI")
        print('''}\n\n\n
    *****OYUN BAŞLADI*****
    ''')

        print("\n\n\n ROUND 1")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        print("1.OYUNCU (ZAFER) SIRASI")

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu2can  = oyuncu2can - hasar1
        elif x > 20:
            oyuncu2can = oyuncu2can - hasar2




        print("2.OYUNCU (ÖMER) SIRASI")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu1can = oyuncu1can - hasar1
        elif x > 20:
            oyuncu1can = oyuncu1can - hasar2


        print("\n\n\n ROUND 1 SONU\n ZAFER : can {}\n ÖMER: can {}".format(oyuncu1can,oyuncu2can))








        print("\n\n\n ROUND 2")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        print("1.OYUNCU (ZAFER) SIRASI")

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu2can = oyuncu2can - hasar1
        elif x > 20:
            oyuncu2can = oyuncu2can - hasar2

        print("2.OYUNCU (ÖMER) SIRASI")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu1can = oyuncu1can - hasar1
        elif x > 20:
            oyuncu1can = oyuncu1can - hasar2

        print("\n\n\n ROUND 2 SONU\n ZAFER : can {}\n ÖMER: can {}".format(oyuncu1can, oyuncu2can))





        print("\n\n\n ROUND 3")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        print("1.OYUNCU (ZAFER) SIRASI")

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu2can = oyuncu2can - hasar1
        elif x > 20:
            oyuncu2can = oyuncu2can - hasar2

        print("2.OYUNCU (ÖMER) SIRASI")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu1can = oyuncu1can - hasar1
        elif x > 20:
            oyuncu1can = oyuncu1can - hasar2

        print("\n\n\n ROUND 3 SONU\n ZAFER : can {}\n ÖMER: can {}".format(oyuncu1can, oyuncu2can))





        print("\n\n\n ROUND 4")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        print("1.OYUNCU (ZAFER) SIRASI")

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu2can = oyuncu2can - hasar1
        elif x > 20:
            oyuncu2can = oyuncu2can - hasar2

        print("2.OYUNCU (ÖMER) SIRASI")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu1can = oyuncu1can - hasar1
        elif x > 20:
            oyuncu1can = oyuncu1can - hasar2

        print("\n\n\n ROUND 4 SONU\n ZAFER : can {}\n ÖMER: can {}".format(oyuncu1can, oyuncu2can))



        print("\n\n\n ROUND 5")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        print("1.OYUNCU (ZAFER) SIRASI")

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))

        if x < 20:
            oyuncu2can = oyuncu2can - hasar1
        elif x > 20:
            oyuncu2can = oyuncu2can - hasar2

        print("2.OYUNCU (ÖMER) SIRASI")
        hasar1 = randint(15, 20)
        hasar2 = randint(20, 24)

        x = int(input("Hasar vereceğiniz sayıyı giriniz:"))
        if x < 20:
            oyuncu1can = oyuncu1can - hasar1
        elif x > 20:
            oyuncu1can = oyuncu1can - hasar2


        if oyuncu1can or oyuncu2can < 0:
            if oyuncu1can < 0:
                print("\n\nOYUN BİTTİ")
                print("\nOYUNCU 2 (ÖMER) KAZANMIŞTIR.")
                print("\n\n*****TEBRİKLER*****")
            elif oyuncu2can < 0:
                print("\n\nOYUN BİTTİ")
                print("\nOYUNCU 1 (ZAFER) KAZANMIŞTIR.")
                print("\n\n*****TEBRİKLER*****")

        elif oyuncu1can and oyuncu2can < 0:
            print("OYUN BERABERE BİTMİŞTİR.")

        else:
            print("OYUN BERABERE BİTMİŞTİR.")


elif kadı == dkkullanıcı:
    print("ŞİFRE HATALI!.")
elif şifre == dşifre:
    print("KULLANICI ADI HATALI!")
else:
    print("HATALI GİRİŞ YAPTINIZ!")