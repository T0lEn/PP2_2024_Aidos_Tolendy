import re


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()


pattern = re.compile(r'ab*')


matches = pattern.findall(data)
print("Найденные соответствия:", matches)

#ex2

import re

def match_pattern(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

if match_pattern(data):
    print(f"Строка из файла соответствует паттерну '{data}'")
else:
    print(f"Строка из файла не соответствует паттерну '{data}'")


#ex3


import re

def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, string)
    return sequences


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

sequences = find_sequences(data)
if sequences:
    print("Найдено:")
    for sequence in sequences:
        print(sequence)
else:
    print("Нету")


#ex4

import re

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, string)
    return sequences


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

sequences = find_sequences(data)
if sequences:
    print("Найдено:")
    for sequence in sequences:
        print(sequence)
else:
    print("Нету")



# ex5

import re

def match_pattern(string):
    pattern = r'a.*b$'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

# Открываем файл .txt для чтения с указанием кодировки 'utf-8'
with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

if match_pattern(data):
    print(f"Строка из файла соответствует паттерну '{data}'")
else:
    print(f"Строка из файла не соответствует паттерну '{data}'")



#ex 6

def replace_with_colon(string):
    modified_string = string.replace(' ', ':').replace(',', ':').replace('.', ':')
    return modified_string


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

modified_string = replace_with_colon(data)
print("Строка после замены:")
print(modified_string)


#ex7


import re

def snake_to_camel(snake_case_string):
    camel_case_string = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case_string)
    return camel_case_string


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

camel_case_output = snake_to_camel(data)
print("Строка в стиле верблюжьего регистра:")
print(camel_case_output)


#ex8

import re

def split_at_uppercase(string):
    splitted_strings = re.findall(r'[A-ZА-Я]?[a-zа-я]*', string)
    return splitted_strings


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

splitted_strings = split_at_uppercase(data)
print("Результат разделения:")
print(splitted_strings)


#ex9


import re

def insert_spaces(string):
    modified_string = re.sub(r'([a-zа-я])([A-ZА-Я])', r'\1 \2', string)
    return modified_string


with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

modified_output = insert_spaces(data)
print("Строка с пробелами:")
print(modified_output)


#ex10


import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-ZА-Я])', '_', camel_case_string).lower()
    return snake_case_string

with open('lab5/row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

snake_case_output = camel_to_snake(data)
print("Строка в стиле змеиного регистра:")
print(snake_case_output)







