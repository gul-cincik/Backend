#csv
import csv

class Urun:

    indirim_orani = 0.5

    tum_objeler = []

    def __init__(self, ad: str, fiyat: int, adet: int):
        
        assert fiyat >= 0, f"Gelen fiyat bilgisi 0'dan küçük olamaz! Girdiğiniz değer: {fiyat}"
        assert adet >= 0, f"Gelen adet bilgisi 0'dan küçük olamaz! Girdiğiniz değer: {adet}"

        self.ad = ad
        self.fiyat = fiyat
        self.adet = adet

        Urun.tum_objeler.append(self)

    def toplam_fiyat_hesapla(self):

        return self.fiyat * self.adet
    
    def indirim_uygula(self):
        return self.fiyat * self.indirim_orani

    @classmethod
    def csv_oku(cls):

        with open('ders6\\data.csv', 'r') as data_dosya:

            okuyucu = csv.DictReader(data_dosya)

            urunler = list(okuyucu)

            for urun in urunler:

                print(urun)

                Urun(
                    ad = urun.get('ad'),
                    fiyat = int(urun.get('fiyat')),
                    adet = int(urun.get('adet')),
                )

    def __repr__(self):
        return f"Urun('{self.ad}', {self.fiyat}, {self.adet})"
    
    #self kavramını statik methodlarda göndermemeniz gerek.
    @staticmethod
    def integer_mi(num):

        if(isinstance(num, int)):
            return True
        else:
            return False



# Urun.csv_oku()

urun1 = Urun("Telefon", 5000, 4)
# urun2 = Urun("Bilgisayar", 30000, 2)
# urun3 = Urun("Kulaklık", 1000, 2)
# urun4 = Urun("Televizyon", 10000, 1)

# urun1_fiyat = urun1.toplam_fiyat_hesapla()
# print(urun1_fiyat)

# print(Urun.tum_objeler)

# for i in Urun.tum_objeler:
#     print(i.ad)

# print(urun1.fiyat)
# print(urun1.indirim_uygula())
# print(urun2.indirim_uygula())

# urun3.indirim_orani = 0.2
# print(urun3.indirim_uygula())

#csv -> comma seperated values. virgülle ayrılmış olan data.


# class Musteri:
# ad,
# soyad, 
# email, 
# sehir, 
# cinsiyet


# kullanıcıdan aldığınız yukarıdaki inputları Musteri objesine dönüştürüp csv dosyasına kaydedin.
# muster.csv dosyası oluşturun.
