# #strip() fonksiyonu stringdeki boşlukları kaldırır.
# space_str = "      listen spotify     "
# print(space_str.strip())

# #AŞ. kısmını stringden kaldıracak
# company_name = "Casper AŞ."
# print(company_name.strip("AŞ."))

# r_space_str = "      listen spotify     "
# print(r_space_str.lstrip())
# print(r_space_str.rstrip())

# #Mantık operatörleri
# #and, or, not

# #evli ve 25-35 yaş aralığındaki müşteriye reklam göst.
# age_feature = True #25--35 yaş aralığı
# married_feature = False # bekar
# gender = True # erkek

# ad = age_feature and married_feature
# print(ad)

# ad = age_feature or married_feature
# print(ad)

# # age_feature = not age_feature
# # print(age_feature)

# #1- 35 yaşından büyük ve evli erkek 
# man = ((not age_feature and not married_feature) and gender)
# print('Bu müşteri sizin reklam kitleniz içinde mi? ', man)

# #2- 25-35 yaş aralığında veya bekar kadın
# woman = age_feature or married_feature and not gender
# print(woman)

# # iki öğrencinin bir sınavdan aldığı notlar var.
# student1 = 'Ali'
# student2 = 'Fatma'

# ali_grade = 75
# fatma_grade = 75

# print("Ali'nin notu Fatma'nın notundan yüksek mi? ", ali_grade <= fatma_grade) #küçük eşit mi
# print("Ali'nin notu Fatma'nın notundan yüksek mi? ", ali_grade >= fatma_grade) #büyük eşit mi
# print("Ali'nin notu Fatma'nın notundan yüksek mi? ", ali_grade == fatma_grade) #eşit mi
# print("Ali'nin notu Fatma'nın notundan yüksek mi? ", ali_grade != fatma_grade) # farklı mı

# #string listesi
# countries = ['Turkey', 'Germany', 'Italy', 'Spain', 'Poland', 'Russia']

# print(countries)

# country_str = 'Turkey'
# listed_country = list(country_str)
# print(listed_country)

# #int listesi
# surfaces = [5420, 8756, 7854, 2500, 65874, 5600] 

# mixed_list = ['Turkey', 84.75, 783562, ['Adana', 'İstanbul', 'İzmir', 'Mersin', 'Ankara', 'Diyarbakır'], True]
# print(mixed_list)

# print(mixed_list[0])
# print(mixed_list[1])
# print(mixed_list[2])
# print(mixed_list[3])
# print(mixed_list[3][0])
# print(mixed_list[4])


colors = []
print("İlk tanımlanan liste: ", colors)

#listeye Mavi Kırmızı renklerini ekliyorum
colors.append('Blue')
colors.append('Red')
colors.append('White')
colors.append('Orange')
print('Appen fonksiyonu ile eklenen renklerden sonra oluşan liste: ', colors)

colors.insert(1, 'Black')
print('insert fonksiyonu ile ikinci elemana siyah eklendi: ', colors)

#remove fonksiyonu
colors.remove('White')
print('Silmek istediğiniz renk silindi: ', colors)

list_len = len(colors)
print(list_len)
print(len(colors))

mixed_list = ['Turkey', 84.75, 783562, ['Adana', 'İstanbul', 'İzmir', 'Mersin', 'Ankara', 'Diyarbakır'], True]
print(len(mixed_list))

cities = mixed_list[3]
cities.sort()
print('Sıralanan şehirler: ', cities)

sorted_cities = sorted(cities)
print(cities)
print(sorted_cities)

