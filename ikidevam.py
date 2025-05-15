#setler indexli değildir.sırasızdır 
'''my_set = {1,1,2,2,3,3,4,4,5,5,6,6}
print(my_set)
# index kontrolü yapılamıyor

set1 = {"Elif","arı",1,2,3}
print(set1)'''
#tuplelar sıralıdır, indexlerden etk,leşim sağlanabilir
#DEĞİŞTİRİLEMEZLER
'''
my_tuple =(10,20,30,40,20)
print(my_tuple[0])'''

kisi = {
    "name" : "Elif",
    "surname" : "Arı",
    "diller" : ["python","java","C#"]
}
'''
print(kisi.keys())
print(kisi.values())

print(kisi.items())     #tuplelara ayırdı

dil = kisi.get("diller")
print(dil)

yas = kisi.get("yas","Bilinmiyor")
print(yas)'''
'''
kisi.update({"meslek":"yazılım geliştirici","Şehir":"Denizli"})
print(kisi)

kisi.update({"Şehir":"Uşak"})
print(kisi)'''

'''phone_book = {
    "Ahmet Kaya":"05554455556", 
    "Elif Arı" : "05321978399",
    "Tahsin B" : "05456891578"
}

isim = input("aramak istediğiniz kişinin adını yazınız :")

tel_no = phone_book.get(isim,"aradığınız kişi yok")
print(tel_no)'''

stock = {
    "kiwi":50,
    "elma":100,
    "muz":36,
    "portakal":20
}

meyve_adi = input("hagi meyve: ")
meyve_miktar = int(input("kaç kg: "))
if meyve_miktar > stock[meyve_adi]:
    print(f"{meyve_adi} meyvesinden maximum {stock[meyve_adi]}kg alabilirsiniz")
else :
    stock[meyve_adi] -= meyve_miktar
    print(stock)
