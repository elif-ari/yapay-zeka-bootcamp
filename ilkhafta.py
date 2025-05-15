'''dogru_sifre = "1234"
sifre = None

while sifre!=dogru_sifre:
    sifre = input("parola giriniz: ")
    if sifre != dogru_sifre:
        print("şifre yanlıştır. \n tekrar deneyiniz")
    else :
        print("parola doğru...")
        break'''


#text = "gece GÜNDÜZ peşimdeler peşimde"
#print(text.swapcase())

'''s = 'Python'
print(s.rjust(19,'+'))'''

###parçalama ve bölme işlemleri
'''
meyve_string ="elma,çilek,armut,karpuz"

meyveler =meyve_string.split(',')
print(meyveler)
print(type(meyveler))

line_text = "bugün yapay zeka eğitiminin 2. günü \n konular: \n döngüler,fonksiyonlar, listeler"
print(line_text.splitlines())
#arama ve değiştirme

txt = "merhaba dünya ,dünya güzeldir."
baslangic_index=txt.find("dünya")
print (baslangic_index)

son_index=txt.rfind("dünya")
print (son_index)

degistirilmis= txt.replace('dünya', 'evren')
print(degistirilmis)

data = "covid.xlsx"
print('dosyanın sonu xlsx ile bitiyor mu: ', data.startswith('cvd'))
'''
#white space silme işlemi
'''white = '       python              '
print(white.strip())
print(white.lstrip())
print(white.rstrip())

#string içeriği kontrolleri

print('1233456avB.'.isalnum())
print('Merhaba.'.isalpha())

print("     ".isspace())

print('hEllo'.isupper())
print('Hello World'.istitle())


#format bir stringin içerisinde farklı değişkenler
name = "elif"
surname = 'arı'
age = 22
print('benim adım: {} ,soyadım: {} , yaşım: {}'.format(name,surname,age) )

print(f'benim adım: {name} ,soyadım: {surname} , yaşım: {age}')'''

num2 = [40,10,35,25,15,10,0,-85]

ascendind_list = list(sorted(num2))
print(ascendind_list)

descending_list = list(sorted)


