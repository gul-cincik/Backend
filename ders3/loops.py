# #while
# #for
# #do while

# # while(kosul):
# #     işlemler

# number = 1

# while(number < 6):

#     print(number)

#     # number = number +1 ile aynı şey
#     number += 1


# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# # index olarak kullanacağız.
# i = 0

# while(i < len(my_list)):

#     print(my_list[i])

#     i += 1

# ####### ATM EXAMPLE ######

# # bakiye sorgulama 1
# # para çekme 2
# # para yatırma 3
# # çıkış 4


# bakiye = float(12000)

# secenek = int(input("Yapmak istediğiniz işlemi seçiniz: \n 1-Bakiye Sorgulama \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçimiz: "))

# #Çıkış
# while(secenek != 4):

#     #Bakiye sorgula
#     if(secenek == 1):

#         print(f"Toplam bakiyeniz {bakiye}")
#         secenek = int(input("Yapmak istediğiniz işlemi seçiniz: \n 1-Bakiye Sorgulama \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçiminiz: "))

    
#     #Para çekme
#     elif(secenek == 2):

#         para_cek = int(input(f"Toplam bakiyeniz {bakiye}. Çekmek istediğiniz para miktarını girin: "))

#         if(para_cek > bakiye):

#             print("Hesabınızda yeterli para bulunmamakta.")
        
#         else:

#             bakiye = bakiye - para_cek
#             print(f"Kalan bakiyeniz {bakiye}")
        
#         secenek = int(input("Yapmak istediğiniz işlemi seçiniz: \n 1-Bakiye Sorgulama \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçimiz: "))
    
#     #para yatırma
#     elif(secenek == 3):

#         para_yatir = int(input("Yatırmak istediğiniz miktarı giriniz: "))

#         bakiye = bakiye + para_yatir

#         print(f"Toplam bakiyeniz: {bakiye}")

#         secenek = int(input("Yapmak istediğiniz işlemi seçiniz: \n 1-Bakiye Sorgulama \n 2-Para Çekme \n 3-Para Yatırma \n 4-Çıkış \n Seçimiz: "))

#     else:
#         print("Yanlış tuşlama yaptınız: ")


# # break konusu
# count = 150

# i = 1

# limit = int(input("Sınırlandırmak istediğiniz sayıyı giriniz: "))

# while(i < count):

#     if(i == limit):

#         print(i)
#         print("Break ile döngü kırıldı.")
#         break

#     print(i)

#     i += 1


# #sayi tahmin oyunu

# import random

# number = random.randint(0,100)

# print("Sayı tahmin oyununa hoş geldiniz! ")

# while True:

#     tahmin = int(input("1-100 arasında bir sayı tahmin ediniz: "))

#     if(tahmin < number):
#         print("Daha büyük bir sayı deneyin! ")
    
#     elif(tahmin > number):
#         print("Daha küçük bir sayı tahmin edin! ")

#     else:
#         print("Bravo!")
#         break

# #for syntax
# for var in list:
#     işlemler

# numbers = [0,1,2,3,4,5,6,7,8,9,10]

# for number in numbers:

#     print(number)

# mevsimler = ['Sonbahar', 'Kış', 'İlkbahar', 'Yaz']

# for mevsim in mevsimler:

#     print(mevsim)

# ilkbahar = mevsimler[2]
# for harf in ilkbahar:
#     print(harf)

# times = int(input("Kaç kere bu mesajı göndermek istiyorsunuz: "))

# for i in range(times):

#     print("İyi haftasonları")

# import time

# names = ['Ali', 'Ayşe', 'Ahmet']
# moods = ['Mutlu', 'Üzgün', 'Kırgın']

# one_for_start = time.time()

# for name in names:
#     print(name)

# one_for_end = time.time()

# print("First loop execution time:", one_for_end - one_for_start)

# inner_for_start = time.time()

# for name in names:
#     for mood in moods:
#         print(name + " " + mood)

# inner_for_end = time.time()
# print("Inner loop execution time:", inner_for_end - inner_for_start)

# # # 100e kadar olan sayıların toplamını hesaplayan program
# # sum_num = 0

# # for i in range(1,101):

# #     sum_num = sum_num + i

# # print(sum_num)


# asal_sayilar = []

# for sayi in range(25,101): # sayi = 12

#     asalMi = True

#     for j in range(2, sayi): # j = 4

#         if(sayi % j == 0):

#             asalMi = False
#             break

#     if asalMi:
#         asal_sayilar.append(sayi)

# print(asal_sayilar)

# cift_sayilar = []

# for sayi in range(0,101):

#     if(sayi % 2 == 0):

#         cift_sayilar.append(sayi)

# print(cift_sayilar)

