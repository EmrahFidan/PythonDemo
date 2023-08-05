from Libary import *

print("""
----------------------------------------------------------------
Kütüphane Programına Hoşgeldiniz

İşlemler: 
1. Kitapları göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Sayfa Sayısı Yükselt

Çıkış yapmak istiyorsan "q" bas.
----------------------------------------------------------------
""")

# sqlite veritabanını oluşturmak için kütüphane classımı çağırdım
kütüphane = Kütüphane()

while True:
    işlem = input("Yapacağınız işlem = ")
    if(işlem == "q"):
        print("Program Sonlandırılıyor....")
        print("Yine Bekleriz")
        break
    else:
        işlem = int(işlem)

        if(işlem == 1):
            kütüphane.kitapları_göster()

        elif(işlem == 2):
            isim = input("Hangi Kitabı İstiyorsunuz : ")
            print("Kitap Sorgulanıyor...")
            time.sleep(2)
            kütüphane.kitap_sorgula(isim)

        elif (işlem == 3):
            isim = input("isim: ")
            yazar = input("Yazar: ")
            yayınevi = input("Yayınevi: ")
            tür = input("Türü: ")
            sayfa_sayısı = int(input("Sayfa Sayısı: "))

            yeni_kitap = Kitap(isim, yazar, yayınevi, tür, sayfa_sayısı)
            print("Kitap Ekleniyor...")
            time.sleep(2)
            kütüphane.kitap_ekle(yeni_kitap)
            print("Kitap Eklendi")

        elif (işlem == 4):
            isim = input("Hangi Kitabı Silmek İstiyorsunuz: ")
            cevap = input("Emin misiniz ? (E/H)")
            if (cevap == "E"):
                print("Kitap Siliniyor..")
                time.sleep(2)

                kütüphane.kitap_sil(isim)
                print("Kitap Silindi")


        elif (işlem == 5):
            isim = input("Hangi Kitabın Sayfa Sayısını Yükseltmek İstiyorsunuz :")
            print("Sayfa Sayısı Yükseltiliniyor....")
            time.sleep(2)

            kütüphane.sayfa_sayısı_yükselt(isim)
            print("Sayfa Sayısı Yükseltildi...")
        else:
            print("Geçersiz İşlem...")
