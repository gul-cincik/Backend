# file_path = "C:\\Users\\GC\\Projects\\Cosmios\\Files\\names.txt"

# example_file = "ders4/example.txt"

# with open(file_path, 'r') as file:

#     lines = file.readlines()

#     print(lines)

#     print("test")

# for line in lines:
#     print(line)
# with open(example_file, 'r') as ex_file:

#     content = ex_file.read()

#     print(content)

# file_path = "C:\\Users\\GC\\Projects\\Cosmios\\Files\\names.txt"

# with open(file_path, 'w') as file:

#     while(True):

#         name = input('Çıkış yapmak için qya basınız\nİsim giriniz: ')

#         if(name == 'q'):
#             break

#         line_name = name + '\n'
#         file.write(line_name)

import os

klasor_yolu = "C:/Users/GC/Projects/Cosmios/Files/products"

klasorler = os.listdir(klasor_yolu) #glasses, shoes

for klasor in klasorler:
    
    dosya_yolu = os.path.join(klasor_yolu, klasor)

    stok_yolu = os.path.join(dosya_yolu, 'stok.txt')

    if os.path.isfile(stok_yolu):

        with open(stok_yolu, 'r') as stok:

            content = stok.read()

            print(f"{klasor} ürünlerinin {content} adet stoğu bulunmakta")
    

# [1,2,3,4]

# 1->büyük harf
# 2->küçük harf
# 3->noktalama
# 4-> rakamlar
# kaç karakter, uzunluk


