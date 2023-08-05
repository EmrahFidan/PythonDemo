# işletim sisteminde işlemler gerçekleştirmek için kullanıyoruz

import os
from datetime import datetime

# çoook kapsamlı bir modül burada sadece temelleri göreceğiz.

# print(os.getcwd()) # bu dosyanın nerede olduğunu gösteriyor.
# C:\Users\20180\PycharmProjects\KE\İleri Seviye Modüller

# os.chdir("D:\Masaüstü") # change director (konum değiiştirme)
# print(os.getcwd()) # D:\Masaüstü

# print(os.listdir())
# ['Datetime.py', 'Os.py', 'SOn tüketim tarihi gelişmiş.py']
"""
for i in os.listdir():
    print(i)
    Datetime.py
    Os.py
    SOn
    tüketim
    tarihi
    gelişmiş.py
"""

# bulunduğum dizinde bir tane klasör , dosya oluşturmak için
print(os.getcwd())
# os.mkdir("DENEME 1") # make directory

# os.mkdir("Deneme2/Deneme3") # bunu yappınca sistem belirtilen yolu bulamıyor ama bunu yapmak için bir tane fonksiyonumuz var.
#os.makedirs("Deneme2/Deneme3")

# deneme 2 nin altındaki deneme 3 ü silmek için
 # os.rmdir("Deneme2/Deneme3")
# os.mkdir("Deneme2/Deneme3") # tekrar geri yükledim.

# os.rmdir("DENEME 1")

# os.removedirs("Deneme2/Deneme3") # bütün alt klasörleride siler.

# os.rename("test.txt","yeni.txt") # dosya adı değiştirmek için

# dosyanın özelliklerini almak için
# print(os.stat("yeni.txt"))
# s.stat_result(st_mode=33206,
# st_ino=4222124650707507,
# st_dev=4169844856,
# st_nlink=1,
# st_uid=0,
# st_gid=0,
# st_size=34,
# st_atime=1663700297,
# st_mtime=1663700262 (saniye cinsinden dosyanın değiştirilme zamanı
# st_ctime=1663700244)

# print(os.stat("yeni.txt").st_atime) # 1663700297.063755
# bunu saate çevirmek için
# print(datetime.fromtimestamp(os.stat("yeni.txt").st_atime))
# 2022-09-20 21:58:17.063755

print(os.walk("D:\Masaüstü"))
# masaüstünün altındaki bütün dosya ve klasörleri tek tek gez.
# <generator object _walk at 0x000001C29BDF9A10>
# görmek için for döngüsü kullanacağız.
# for i in os.walk("D:\Masaüstü"):
  #   print(i)
    # çoook fazla dosya var...

# Ben burada extradan güzel bir şekilde göstermek için
"""
for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("D:\Masaüstü\ÖZGÜR UYSAL"):
   print("Klasör Yolu = ",klasör_yolu)
   print("Klasör İsimleri = ", klasör_isimleri)
   print("Dosya İsimleri = ", dosya_isimleri)
"""
# ÇÜnkü bize dönen değer dmet halindeydi.

# eğer ben sadece dosya isimlerini almak istiyorum dersem ne yapacağım.
"""
for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("D:\Masaüstü\ÖZGÜR UYSAL"):
    for i in dosya_isimleri:
        print(i)
"""
# ben şimdi bu dosyalardan sadece txt olanları almak istersem

for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("D:\Masaüstü"):
    for i in dosya_isimleri:
        if(i.endswith(".pdf")):
            print(i)
