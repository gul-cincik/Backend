country_detail = []

#ülke adı, nüfus, yüzölçümü, başkent

country = input("Lütfen bir ülke adı giriniz:")
population = float(input("Lütfen ülkenin nüfusunu giriniz: ")) 
yuzolcumu = int(input("Lütfen ülkenin yüzölçümünü giriniz: "))
capital = input("Başkenti giriniz: ")


country_detail.append(country)
country_detail.append(population)
country_detail.append(yuzolcumu)
country_detail.append(capital)

print("Listeniz oluşturuldu: ", country_detail)

# country_detail.remove(capital) #country_detail.remove(country_detail[3])

# print("Listenizden başkent çıkartıldı: ", country_detail)


eleman = int(input("Kaçıncı elemanı silmek istiyorsunuz? "))
country_detail.remove(country_detail[eleman-1])
print(country_detail)