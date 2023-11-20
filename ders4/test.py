# def meyveci(meyve1, meyve2):
#     print(meyve1, 've', meyve2, 'den satın almak istiyorum.' )

# meyveci('portakal', 'elma')

# def meyveci(*meyve):

#     print('Almak istediklerim: ')

#     for i in meyve:
#         print('-', i)

# meyveci('portakal', 'elma', 'mandalina')

# def animals(**kwargs):

#     print('Baskent\t\t', 'Ulke')
#     for key,value in kwargs.items():
#         print(f"{value}\t\t{key}")

# animals(Turkiye="Istanbul", Italya="Roma", Almanya="Berlin", Fransa="Paris")

# def brothers(bro1, bro2, bro3):
#     print('Kardeşlerin adları : ')
#     print(bro1, bro2, bro3)

# family = ['ayşe', 'ali', 'mehmet']

# brothers(*family)


# def generation(y,z):

#     print(y, "Y kuşağından")
#     print(z, "Z kuşağından")

# gene_dictionary = {'y':"Ayşe", 'z': "Ali"}

# generation(**gene_dictionary)

# def generation(y='Test',z='Test'):

#     print(y, "Y kuşağından")
#     print(z, "Z kuşağından")

# generation()

# text = "Global değişken"

# def global_func():
#     print(text)

# text = "Bu bir global değişken."

# global_func()

# def local_func():

#     local_text = "Bu bir lokal değişken."

#     print(local_text)

# local_func()
# # print(local_text)

# # # ERRORS

# # # SyntaxError
# # if True 
# #     print("Syntax Error")

# # if True:
# # print("Syntax Error")

# # print "Hello World"

# # result = 10 +* 5


# # my_list = [1, 2, 3

# # #NameError

# # print(undefined_variable)

# #TypeError

# result = "Hello " + 42

# numbers = 123

# parts = numbers.split()

# value = len()

# value = 42
# element = value[0]

# #Value Error
# test = "test"
# number = int(test)

# #FileNotFound Error
# with open('nonexistent_file.txt', 'r') as file:
#     content = file.read()

# # Index Error
# my_list = [1, 2, 3]
# print(my_list[5])


# my_dict = {'Adana': '01', 'İstanbul': '34', 'Ankara': '06'}
# print(my_dict[''])

# #Zero division
# result = 10 / 0


# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#     numerator = 10
#     denominator = 0

#     result = numerator/denominator

#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")
    
# finally:
#     print("This is finally block.")


try:
   test = int("test")
except Exception as e:
   print(e)

