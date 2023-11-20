def func(*args):
    print("test")

def meyveci(meyve1, meyve2):
    print(meyve1, 've', meyve2, 'satın almak istiyorum')

meyveci('portakal', 'elma')

# *args ile yapalım.

def meyveci(*meyve):

    print("Almak istediklerim: ")

    for i in meyve:
        print("-", i)

meyveci('portakal', 'elma', 'mandalina')

meyveci(1, 'str', 0.75, True)

# **kwargs -> keyword args

def ulkeler(**kwargs):

    print('Ulke\t\tBaskent')

    for key, value in kwargs.items():
        print(f"{key}\t\t{value}")

#escape karakterleri -> \t (tab)

ulkeler(Turkiye="Istanbul", Italya="Roma", Almanya="Berlin", Fransa= "Paris")

def brothers(bro1, bro2, bro3):

    print('Broların adları: ')
    print(bro1, bro2, bro3)

family = ['Ali', 'Ahmet', 'Mehmet']

brothers(*family)

def generation(y="Test",z="Test"):

    print(y, 'Y kuşağından')
    print(z, "Z kuşağından")

gene_dictionary = {'y': "Ayşe", 'z': "Ali"}

# generation(**gene_dictionary)

generation()

#GLOBAL LOCAL VARIABLES

text = "Global değişken"

def global_func():
    print(text)


def local_func():

    local_text = "Bu bir local değişken."

    print(local_text)

# print(local_text)
global_func()
local_func()



