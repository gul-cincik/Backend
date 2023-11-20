# [1,2,3,4]

# şifrenin özelliklerini bir dictionaryde tutalım.
# 1->büyük harf
# 2->küçük harf
# 3->noktalama
# 4-> rakamlar
# pass_ozellik = {'1': 'ABCDEF....', '2': 'abcdf', '3': '.<>....'}

# kaç karakter, uzunluk


# Kullanıcıya seçenekleri tek tek sor.

#Kullanıcı 0 girerse istemiyorum, 1 girerse istiyorum. 

# 1 dediklerini bi listeye ekle.
# pass_secenek = [] #1,2,3
# pass_secenek.append()

#Kullanıcı şifrenin özelliklerini belirledikten sonra kaç karakter diye soracak.

# for ile dönerken listedeki seçeneğe dictionaryden ulaşın.

# random kütüphanesini kullanarak istenilen uzunlukta şifre oluşturulacak.

# Kullanıcıdan kayıt etmek istediği dosya yolunu alın.

# Alınan dosya yoluna sifre.txt eklesin.

# Oluşturulan şifreyi bu dosyaya kaydetsin


import random
import string

pass_ozellik = {1: string.ascii_uppercase, 2: string.ascii_lowercase, 3: string.punctuation, 4: string.digits}

pass_secenek = []

for ozellik in pass_ozellik:
    secenek = input(f"{pass_ozellik[ozellik]} özelliğini istiyor musunuz? (0: Hayır, 1: Evet): ")
    if secenek == '1':
        pass_secenek.append(pass_ozellik[ozellik])

uzunluk = int(input("Şifrenin kaç karakter uzunluğunda olmasını istersiniz?: "))       

pass_rand = ""

for i in pass_secenek:

    pass_rand = pass_rand + i

print(pass_rand)

