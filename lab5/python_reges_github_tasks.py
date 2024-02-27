import re
#ex1
def match_pattern(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False


user_input = input("Введи строку: ")

if match_pattern(user_input):
    print(f"'{user_input}' соответствует паттерну")
else:
    print(f"'{user_input}' не соответствует паттерну");


#ex2

def match_pattern(string):
    pattern2 = r'ab{2,3}'
    if re.fullmatch(pattern2, string):
        return True
    else:
        return False


user_input = input("Введи строку: ")

if match_pattern(user_input):
    print(f"'{user_input}' соответствует паттерну")
else:
    print(f"'{user_input}' не соответствует паттерну");

#ex3


def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, string)
    return sequences


user_input = input("Введите строку: ")

sequences = find_sequences(user_input)
if sequences:
    print("Найдено:")
    for sequence in sequences:
        print(sequence)
else:
    print("Нету");

#ex4

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, string)
    return sequences


user_input = input("Введите строку: ")

sequences = find_sequences(user_input)
if sequences:
    print("Найдено:")
    for sequence in sequences:
        print(sequence)
else:
    print("Нету");


# ex5

def match_pattern(string):
    pattern = r'a.*b$'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False


user_input = input("Введи строку: ")

if match_pattern(user_input):
    print(f"'{user_input}' соответствует паттерну")
else:
    print(f"'{user_input}' не соответствует паттерну");


#ex 6

def replace_with_colon(string):
   
    modified_string = string.replace(' ', ':').replace(',', ':').replace('.', ':')
    return modified_string


user_input = input("Введите строку: ")


modified_string = replace_with_colon(user_input)
print("Строка после замены:")
print(modified_string)

#ex7


def snake_to_camel(snake_case_string):
    camel_case_string = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case_string)
    return camel_case_string

snake_case_input = input("Введите строку в стиле змеиного регистра: ")
camel_case_output = snake_to_camel(snake_case_input)
print("Строка в стиле верблюжьего регистра:")
print(camel_case_output)

#ex8

def split_at_uppercase(string):
    splitted_strings = re.findall(r'[A-ZА-Я]?[a-zа-я]*', string)
    return splitted_strings

user_input = input("Введите строку: ")
splitted_strings = split_at_uppercase(user_input)
print("Результат разделения:")
print(splitted_strings)

#ex9


def insert_spaces(string):
    modified_string = re.sub(r'([a-zа-я])([A-ZА-Я])', r'\1 \2', string)
    return modified_string

user_input = input("Введите строку: ")
modified_output = insert_spaces(user_input)
print("Строка с пробелами:")
print(modified_output)

#ex10


def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-ZА-Я])', '_', camel_case_string).lower()
    return snake_case_string

camel_case_input = input("Введите строку в стиле верблюжьего регистра: ")
snake_case_output = camel_to_snake(camel_case_input)
print("Строка в стиле змеиного регистра:")
print(snake_case_output)






