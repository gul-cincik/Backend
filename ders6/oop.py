# Object Oriented Programming -> Nesne tabanlı programlama

class Urun:
    def toplam_fiyat_hesapla(self,x,y):
        return x*y #fiyat * adet dönecek.


urun = Urun()

urun.ad = "Telefon"
urun.fiyat = 5000
urun.adet = 4

print(type(urun))
print(type(urun.ad))
print(type(urun.fiyat))
print(type(urun.adet))


toplam_fiyat = urun.toplam_fiyat_hesapla(urun.fiyat, urun.adet)

print(toplam_fiyat)

urun2 = Urun()
urun2.ad = "Bilgisayar"
urun2.fiyat = 30000
urun2.adet = 2

print(urun2.toplam_fiyat_hesapla(urun2.fiyat, urun2.adet))


class Dog:

    sehir = "Adana"

    #Constructor
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def havla(self):
        print(f"{self.ad} havlıyor.")


my_dog = Dog("Karabaş", 3)
dog2 = Dog("Garip", 5)
my_dog.havla()

print(my_dog.ad)

print(f"{my_dog.ad} {my_dog.yas} yaşında.")

print(Dog.__dict__)
print(my_dog.__dict__)

print(dog2.__dict__)

print(my_dog.sehir)