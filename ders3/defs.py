# syntax
# def helloWorld():

#     print("Hello World")

# helloWorld()

def toplama(sayi1, sayi2):

    toplam = sayi1 + sayi2

    print(toplam)

def cikarma(sayi1: int, sayi2: int):
     
     sonuc = sayi1-sayi2

     print(sonuc)

def carpma(sayi1, sayi2):
     
     sonuc = sayi1 * sayi2

     print(f"{sayi1} ile {sayi2} nin çarpım sonucu {sonuc}")

def bolme(sayi1, sayi2):
     
     sonuc = sayi1 / sayi2

     print(sonuc)



# 1- Çarpma
#2-bölme
#3-çıkarma
#4-toplama
#5- çıkış

secim = 0

while(secim != 5):
    x = int(input("Bir sayı giriniz: "))
    y = int(input("Bir sayı giriniz: "))

    secim = int(input("Yapmak istediğiniz işlemi seçiniz: \n 1-Çarpma \n 2-Bölme \n 3-Çıkarma \n 4-Toplama \n 5-Çıkış \n Seçimiz: "))

    if(secim == 1):
         carpma(x,y)

    elif(secim == 2):
         bolme(x,y)

    elif(secim == 3): 
         cikarma(x,y)

    elif(secim == 4): 
         toplama(x,y)
    
    elif(secim == 5):
         break
    
    else:
         print("Geçerli bir işlem girmediniz.")

