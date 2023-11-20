# SytaxError

# if True:
#     print("Syntax Error")

# if True:
# print("Syntax Error")

# print "Hello World"

# result = 10+*5

# my_list = [1,2,3
           
#Name Error

# istek = kumas_tipi + kumas_boyutu

#Type Error

# test = 123+ 'abc'


# number = 123
# print(number.split())


# value = 42

# element = value[0]


# FileNotFoundError

# with open('test.txt', 'r') as dosya:
#     icerik = dosya.read()


#Index Error 
# my_list = [1,2,3,4,5]

# print(my_list[10])

# cities = {'Adana': '01', 'İstanbul': '34', 'Ankara': '06'}

# print(cities['İzmir'])


# div = 100/0
# print(div)

try:
    print("Yapılacak işlemler")
except:
    print("Bir hata oluştu")

try: 
    cities = {'Adana': '01', 'İstanbul': '34', 'Ankara': '06'}

    print(cities['İzmir'])
except:
    print("KeyError")



try: 
    cities = {'Adana': '01', 'İstanbul': '34', 'Ankara': '06'}

    print(cities['İzmir'])
except KeyError:
    print("KeyError")
except NameError:
    print("NameError")
    print("Her şey yolunda gitti")
finally:
    print("Kaydınız başarıyla oluşturuldu.")

try:
    test = int("test")
    print(test)
except Exception as e:
    print(e)
