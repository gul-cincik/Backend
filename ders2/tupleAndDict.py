# my_tuple = ('Ali',)

# print(my_tuple)
# print(type(my_tuple))

# # farklı bir tanımlama şekli
# second_tuple = tuple()
# print(second_tuple)


# my_tuple = ('Oğuzhan', 'Berkay', 'Mehmet', 'Mert', 
#             'Gülten', 'Buse', 'Kutlay', 'Medet')
# my_list = list(my_tuple)
# print(my_list)

# print(my_list[2:5])
# print(my_list[:])
# print(my_list[3:])
# print(my_list[3:6])
# print(my_list[0:7:3])
# print(my_list[:3])

# print(my_list[-2])

# my_tuple = tuple('Türkiye',)
# print(my_tuple)

# my_dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': 'value4',
# }

# state_capitals = {
#     'Türkiye': 'Ankara',
#     'Almanya': 'Berlin',
#     'Fransa': 'Paris'
# }

# print(state_capitals)
# print(state_capitals['Fransa'])
# state_capitals['Fransa'] = 'Marsilya'
# print(state_capitals['Fransa'])

# state_capitals['İspanya'] = 'Madrid'
# print(state_capitals)

# car = {
#     'uretici': 'Honda',
#     'model': 'Civic',
#     'yil' : 2016,
#     'stoktaMi': True
# }


# coffee = {
#     'Name': 'Iced Americano',
#     'Description': 'Sade Soğuk Amerikano',
#     'Price': 79.00
# }

# coffee['Milk'] = False

# print(coffee)

# mix_values = {
#     'animal': ('dog', 'cat'),
#     'planet': ['Neptun', 'Saturn', 'Jupiter'],
#     'number': 40,
#     'pi': 3.14,
#     'is_good': True
# }

student = {
    'Name': ('John', 'Wick'),
    'Schools': ['İstanbul Teknik Üniversitesi', 'Dokuz Eylül Lisesi'],
    'Graduation': 2025,
    'GPA': 3.54,
    'Active': True 
}

#TODO tuple değiştirildi. Araştır.
# print(type(student['Name']))
# print(student['Name'])

#TODO neden alta yazmadı bak.
print(student.items(), "\n")
print(student.keys(), '\n')
print(student.values())


student.update({'Active': False})

#delete in kısaltması. silme için kullanılıyor.
# del student['Graduation']

print(student)

print('Name' in student)
print('Age' not in student)