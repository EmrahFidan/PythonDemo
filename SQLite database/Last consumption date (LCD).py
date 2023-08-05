import datetime
import time

date = input("ürünün son tüketim tarihini giriniz: ")
print("Calculating...")
time.sleep(1.5)

LCD = date.split("/")

a = int(LCD[0])
b = int(LCD[1])
c= int(LCD[2])


guncel_tarih = datetime.datetime.now()
guncel_yil = guncel_tarih.year
guncel_ay = guncel_tarih.month
guncel_gun = guncel_tarih.day

year = c - guncel_yil
month = b - guncel_ay
day = a - guncel_gun

if(year < 0):
    print("this product has expired")
else:
    if(month < 0 and year == 0):
        print("this product has expired")

    elif(month < 0 and year > 0):
        year = year -1

        if(day < 0):
            month = month -1

            year = abs(year)
            day = 30 - abs(day)
            if (day > 29):
                y = month // 30
                day = day % 30
                month = month +y
            month = 12 - abs(month)
            if (month > 11):
                x = month // 12
                month = month % 12
                year = year + x
            print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

        elif(day >= 0):
            year = abs(year)
            day = 30 - abs(day)
            if (day > 29):
                y = month // 30
                day = day % 30
                month = month + y
            month = 12 - abs(month)
            month = 30 - abs(month)
            if (month > 11):
                x = month // 12
                month = month % 12
                year = year + x
            print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

    else:
        if(day < 0 and month == 0 and year == 0):
            print("this product has expired")

        elif(day < 0 and month == 0):
            year = year -1

            year = abs(year)
            month = abs(month)
            day = abs(day)
            print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

        elif(day < 0 and month > 0):

            month = month -1

            year = abs(year)
            day = 30 - abs(day)
            if (day > 29):
                y = month // 30
                day = day % 30
                month = month + y
            month = 12 - abs(month)
            month =12 - abs(month)
            if (month > 11):
                x = month // 12
                month = month % 12
                year = year + x
            print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year, month, day))

        else:
            year = abs(year)
            month = abs(month)
            day = abs(day)
            print("Son tüketim tarihi = {} yıl, {} ay, {} gün sonra ".format(year,month,day))