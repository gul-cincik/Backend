# if kosul:
#     process
# else:
#     process

# #Temel if-elif-else örneği
# sayi = int(input("Lütfen bir sayi giriniz: "))

# if(sayi < 20):
#     print("Sayiniz 20den küçük")

# elif(sayi==20):
#     print("Sayiniz 20ye eşittir.")

# else:
#     print("Sayınız 20den büyük")

grade = int(input("Sınavdan aldığınız notu giriniz: "))

four_grade = float(grade / 25)

print(f"Dörtlük ortalamada notunuz: {four_grade}")

#3.5 ile 4 arası aa
if (3.5 < four_grade <= 4):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: AA")

#3 ile 3.5 arası ise ba
elif(3 < four_grade <= 3.5):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: BA")

#2.5 ile 3 arası ise bb
elif(2.5 < four_grade <= 3):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: BB")

elif(2 < four_grade <= 2.5):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: CB")

elif(1.5 < four_grade <= 2):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: CC")

elif(1 < four_grade <= 1.5):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: DC")

elif(four_grade < 1):
    print(f"Dörtlük sistemdeki {four_grade} notunuzun harf karşılığı: FF. Kaldınız! Sınava tekrar girin.")


#order dict oluşturun.
#product(ürün), color, stock, price
# kargo ücreti delivery_price
#kullanıcıya bu üründen kaç tane almak istiyorsunuz diye sorun.
#eğer kargo ücretini tamamlamışsa ücretsiz kargo için ürün ekleyin yazın.


order = {
    'product' : 'Saat',
    'color': 'Siyah',
    'stock': True,
    'price': 250
}

delivery_price = 1000


