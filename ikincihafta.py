#1den 20ye kadar tüm sayıların bulunduğu listede sayı tek ise 
#tek sayı çift ise çift sayı yazdırsın

'''numbers = [i for i in range(21)]

for num in numbers :
    if num %2 == 0:
        print(f"çift sayı:  {num} ")
    else:
        print(f'tek sayı: {num} ')


'''

shopping_list = ["süt", "ekmek", "yumurta"]
urun_sayisi = int(input("kaç tane ürün eklemek istersiniz: "))

for i in range(urun_sayisi):
    eklenecek_urun= input(f"lütfen {i+1} . ürünü giriniz " )
    shopping_list.append(eklenecek_urun)

print(shopping_list)

silmek = input("ürün silmek ister misiniz (E: evet , H hayır)")
#flag yöntemi
isPresent = False

if silmek == 'E':
    silinecek_urun = input("lütfen silmekk istediğiniz ürünü yazınız")

    for urun in shopping_list:
        if urun == silinecek_urun:
            shopping_list.remove(urun)
            isPresent = True
            print(shopping_list)
            break
        else :
            isPresent = False
    if isPresent == False :
        print("aradığınız ürün bulunamadı.")
elif silmek == 'H':
    print('ürünlriniz şu şekildedir')
    for index, value in enumerate(shopping_list):
        print(f"{index+1}. ürün : {value}")
else :
    print("hatalı işlem")