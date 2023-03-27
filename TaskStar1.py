# *****(3)Напишите программу, которая принимает на вход две строки и определяет, являются ли они анаграммами. 
# Знаки препинания, пробелы и регистр при этом игнорируются.
# Пример ввода:
# Цари, вино и сало.
# Лисица и ворона.
# Пример вывода:
# YES

import re

first_user_input = str(re.sub(r'[^\w\s]','', input("Введите первую строку: ")).replace(' ', '').upper())
second_user_input = str(re.sub(r'[^\w\s]','', input("Введите вторую строку: ")).replace(' ', '').upper())
print(first_user_input)

def string_comparison(string: str) -> int:
    string_price = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7,
                   'Ж': 8, 'З': 9, 'И': 10, 'Й': 11, 'К': 12, 'Л': 13, 'М': 14,
                   'Н': 15, 'О': 16, 'П': 17, 'Р': 18, 'С': 19, 'Т': 20, 'У': 21,
                   'Ф': 22, 'Х': 23, 'Ц': 24, 'Ч': 25, 'Ш': 26, 'Щ': 27, 'Ъ': 28,
                   'Ы': 29, 'Ь': 30, 'Э': 31, 'Ю': 32, 'Я': 33}

    comparison = 0
    for ch in string:
            if ch.isalpha():
                for keys in string_price:
                    if ch in keys:
                        comparison += string_price[keys]
    return comparison

if string_comparison(first_user_input) == string_comparison(second_user_input):
    print("Введенные строки являются анаграммами!!!")
else: print("Введенные строки не являются анаграммами")
