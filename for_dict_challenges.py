# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from itertools import count

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
counter = {}

for row in students:
    names = row['first_name']
    if names in counter:
        counter[names] += 1
    else:
        counter[names] = 1
for key, value in counter.items():
    print(f'{key}: {value}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
#
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
counter = {}

for row in students:
    names = row['first_name']
    if names in counter:
        counter[names] += 1
    else:
        counter[names] = 1
max_name = max(counter, key=counter.get)
print(f'Самое частое имя среди учеников: {max_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
     [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

i = 0
for row in school_students:
    counter = {}
    i += 1
    for sub in row:
        names = sub['first_name']
        if names in counter:
            counter[names] += 1
        else:
            counter[names] = 1
    max_name = max(counter, key=counter.get)
    print(f'Самое частое имя среди учеников {i} класса: {max_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for row1 in school:
    counter = {'девочки': 0, 'мальчики': 0}
    class_name = row1['class']
    for row2 in row1['students']:
        names = row2['first_name']
        if is_male[names] == True:
            counter['мальчики'] += 1
        else:
            counter['девочки'] += 1
    print(f"Класс {class_name}: девочки {counter['девочки']}, мальчики {counter['мальчики']}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for row1 in school:
    counter = {'девочки': 0, 'мальчики': 0}
    class_name = row1['class']
    max_boys = 0
    max_girls = 0
    for row2 in row1['students']:
        names = row2['first_name']
        if is_male[names] == True:
            counter['мальчики'] += 1
        else:
            counter['девочки'] += 1
        if max_girls < counter['девочки']:
            output_girls = f'Больше всего девочек в классе {class_name}'
        elif max_boys < counter['мальчики']:
            output_boys = (f'Больше всего мальчиков в классе {class_name}')
print(output_boys, output_girls, sep='\n')

