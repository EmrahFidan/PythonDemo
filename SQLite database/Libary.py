import sqlite3
import time  # sleep fonksiyonuyla kodumuza gerçekçilik katacağız.
# 2 sınıf  oluşturacağız kitap ve kütüphane. Kütüphane  sınıfının içinde sqlite veritabanına bağlanarak
# kitap objelerini sqlite veri tabanına kaydetmeye çalışacağım.
class Kitap():

    def __init__(self,isim,yazar,yayınevi,tür,sayfa_sayısı):

        self.isim = isim
        self.yazar = yazar
        self.yayınevi =yayınevi
        self.tür = tür
        self.sayfa_sayısı = sayfa_sayısı

    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nSayfa Sayısı: {}\n".format(self.isim, self.yazar,self.yayınevi,self.tür,self.sayfa_sayısı)

class Kütüphane():

    def __init__(self):
        self.baglantı_olustur()
        # Sqlite veritabanına bağlantı_oluştur fonksiyonla bağlanacağız.
        # daha sonra bu fonksiyonu oluşturmalıyız.
        # ilk önce init fonksiyonu çalışacağı için burada da baglantı_olustur fonksiyonu çalışacak ve bizim tablomuz oluşacak.

    def baglantı_olustur(self):
        self.baglanti = sqlite3.connect("kütüphane.db") # kütüphane adında veritabanı oluşturduk

        self.cursor = self.baglanti.cursor() # veritabanı üzerinde işlem gerçekleştirmek için cursor oluşturuyoruz.
        # tablo oluşturmalıyız

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,sayfa_sayısı INT)" # kolay anlaşılması için
        # tablomuzun ismine "kitaplar" adını verdik
        self.cursor.execute(sorgu)
        self.baglanti.commit()  # yaptığımız işlemin veritabanı üzerinde aktif olması için

    def baglantı_kes(self):
        self.baglanti.close() # veritabanı üzerinde işlemlerimizin bittiğini gösterecek

    def kitapları_göster(self):

        sorgu = "Select * from kitaplar"
        # kitaplar tablosundaki tüm bilgileri çekmek için kullandığımız komut
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        # kitaplarımız liste içinde demt halinde bulunacaklar , unutma !!!!!

        if (len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                # eğer kitap varsa buradaki i bizim demetlerimizi gösterecek yani demetler üzerinde işlem yapmak için onların indekslerini yazmalıyız
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        self.cursor.execute("Select * From kitaplar where isim = ?", (isim,))
        # verilen isime göre veriyi çekeceğiz
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor.....")
        else:
            # listem tek elemanlı olacağı için (eğer kitap veri tabnına kayıtlıysa) o listenin ilk elemanını alacağım (0. indeks)
            # ve elimde bir demet olacak demetin elemanlarını sırayla yazmak için sırayla indekslerini alacağım
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitap_ekle(self, kitap):
    # burada yazdığımız "kitap" nesnesine göre işlemler yapacağım
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim, kitap.yazar, kitap.yayınevi, kitap.tür, kitap.sayfa_sayısı))
        # 5 tane eleman bulunduran demet oluşrumalıyım. Kitap nesnesinden sırasıyla değişkenlerimi aldım

        self.baglanti.commit() # bilginin tablo üzerinde geçerli olması için , bilginin güncellenmesi için

    def kitap_sil(self, isim):
# isime göre kitabı sileceğim
        self.cursor.execute("Delete From kitaplar where isim = ?",(isim,))
        self.baglanti.commit() # bilginin tablo üzerinde geçerli olması için , bilginin güncellenmesi için

    def sayfa_sayısı_yükselt(self,isim):
        # baskı yükselt olarak alternatiflenebilir
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            # bulunan kitabın 4. indeksi bize sayfa sayısını verecek
            sayfa_sayısı = kitaplar[0][4]
            sayfa_sayısı += 10

            sorgu2 = "Update kitaplar set sayfa_sayısı = ? where isim = ?"
            self.cursor.execute(sorgu2,(sayfa_sayısı,isim))

            self.baglanti.commit() # bilginin tablo üzerinde geçerli olması için , bilginin güncellenmesi için
# bu dosyayı modül olarak kullanacağız ve modül olarak kullanacağımız için buradaki kitap ve kütüphane sınıflarına erişebiliyor olacağız.