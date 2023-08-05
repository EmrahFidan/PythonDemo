from datetime import datetime

print (datetime.now()) # 2022-09-19 16:14:44.878615

su_an = datetime.now()

print(su_an.year) # 2022

print(su_an.month) # 9

print(su_an.microsecond) # 416645

print(su_an.day) # 19

print(su_an.second) # 57

print(su_an.hour) # 16

print(su_an.minute) # 18

print(datetime.ctime(su_an)) # Mon Sep 19 16:19:22 2022
# Şu anki tarihi daha güzel göstermek için kullanılır.

# en çok kullanılan strftime
print(datetime.strftime(su_an,"%Y")) # 2022

print(datetime.strftime(su_an,"%B")) # September

print(datetime.strftime(su_an,"%B %Y")) # September 2022

print(datetime.strftime(su_an,"%A")) # Monday

print(datetime.strftime(su_an,"%X")) # 16:23:19

print(datetime.strftime(su_an,"%D")) # 09/19/22

import locale # konuma özel yapmak için

print(locale.setlocale(locale.LC_ALL,""))

print(datetime.strftime(su_an,"%B %A"))

# locale ile bulunduğumuz yerin diline çevirebiliyoruz.

# çok fazla kullanılırlar.
su_an = datetime.now()
# şu anki zamanın saniye cinsinden değeri ne
saniye = datetime.timestamp((su_an))
print(saniye) # 1663594619.855004

# saniyeyi datetime objesine çevirme
su_an2 = datetime.fromtimestamp(saniye)
print(su_an2) # 2022-09-19 16:38:32.839097

su_an = datetime.fromtimestamp(0)
print(su_an) # 1970-01-01 03:00:00
# bilgisayarlar belli bir zamanı sayarken 1970'i baz almışlar
# milat olarak kabul etmişler. Bilgisayarlarımız aslında saniyeyi
# sayar ve buna göre şu anki zamanı verirler. 1970'ten hesaplayarak


#belli 2 tarih arasındaki farkı bulma
# sadece yıl ay gün girersen de olur, herşeyi girersen de olur.
tarih = datetime(2023,8,15)

şu_an = datetime.now()

fark =  tarih - şu_an

print(fark.days) # 329

print(fark.seconds) # 25990

print(fark.microseconds) # 647871