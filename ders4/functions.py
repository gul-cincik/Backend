
# def findMax(number_list):

#     x = max(number_list)

#     print('Max number of list is: ', x)

#     return x

# def findMin(number_list):

#     y = min(number_list)

#     print('Min number is: ', y)

#     return y

# num_list = [100, 587, 759, 450]

# max_number = findMax(number_list=num_list)

# min_number = findMin(num_list)

# print(max_number)
# print(min_number)

# def findMinAndMax(number_list):

#     x = max(number_list)

#     y = min(number_list)

#     return x, y


# num_list = [100, 587, 759, 450]

# max_number, min_number = findMinAndMax(num_list)

# print(f'Listenizdeki Max sayi: {max_number} \nListenizdeki min sayi: {min_number}')

# # bir listenin ilk elemanını dönen fonk.
# def numbers(number_list):

#     first_element = number_list[0] # 100

#     last_element = number_list[3] # 450

#     return first_element, last_element

# nums  = numbers(num_list)

# print(nums)


# #palindrome


# def is_palindrome(input_str):

#     clean_str = ''.join(input_str.split()).lower()

#     return clean_str[::-1]

# word = input('Enter a word or phrase: ')

# reversed_word = is_palindrome(word)

# if(word.lower() == reversed_word):
#     print(f"{word} is a palindrome! ")

# else:
#     print(f"{word} is not a palindrome! ")


import random

def generate_password():

    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    pass_len = 12

    password = "".join(random.sample(s, pass_len))

    return password

sifre = generate_password()

print('Oluşturulan şifre: ', sifre)