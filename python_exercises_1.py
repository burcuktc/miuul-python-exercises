# Python Alıştırmalar
# 1) Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
text = "The goal is to turn data into information, and information into insight."
text.upper().replace(',',' ').replace('.',' ').split()

# 2) Verilen liste için aşağıdaki görevleri yapınız.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
lst

# Adım 5: Yeni bir eleman ekleyin.
lst.append('B')
lst

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
lst.insert(8,'N')
lst

# 3) Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
 dict = {'Christian': ["America",18],
        'Daisy':["England",12],
         'Antonio':["Spain",22],
         'Dante':["Italy",25]}

 #  Adım 1: Key değerlerine erişiniz.
 dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict['Daisy'][1] = 13
dict
#veya
dict.update({'Daisy':["England",13] })
dict

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({'Ahmet': ["Turkey",24]})
dict

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
dict

# 4) Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonskiyon yazınız.
l = [2,13,18,93,22]
def func(list):
    a = []
    b = []
    for i in list:
        if i % 2 ==0:
            a.append(i)
        else:
            b.append(i)

    return(a,b)
func([2,13,18,93,22])

# 5) Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

# 6) Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
  print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")