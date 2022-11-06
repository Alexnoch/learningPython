# print
#alien_0 = {'color': 'green', 'points': 5}
#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " points!")

                # STRINGS
# str() - преобразование типов
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

                # NUMBERS
#int() - преобразование типов

                # LISTS 

# test = ['test','test2']; 
#numbers = [1,2,3,4,5,6]; # Список
# constantNumbers = (6,5,4,3,2,1) # Кортеж значения которого нельзя изменять, хотя можно переопределять сам кортеж
#test.append('test3'); # В конец списка
#test.insert('test 0'); # В начало списка
#squares = [value**2 for value in range(1,11)]  
#print(max(numbers)) # Выводим максимальное число в списке

# Доступ к элементам списка

#slice = numbers[1:4] # [1:]  Получение элементов с 1 по 4
#copy = numbers[:] # копирует массив 

                # Условия
# if name in friends:  - проверка на наличие в списке 

# if 'erin' not in favorite_languages.keys():   - проверка есть ли ключ в словаре по строке
    # print("Erin, please take our poll!")



#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#x_increment = 2
#else:
# Пришелец двигается быстро.
#x_increment = 3
# Новая позиция равна сумме старой позиции и приращения


                # Цикл
#for key in test:
#    print(key)


#for alien_number in range(30): - функция рэндж заставляет отработать цикл 30 раз
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#aliens.append(new_alien)

# Вывод первых 5 пришельцев:
#  for alien in aliens[:5]:
# print(alien)
# print("...")

    # Цикл while - работает пока условие верно

    # while current_number <= 5:
    # print(current_number)
    # current_number += 1

# Чтобы немедленно прервать цикл while без выполнения оставшегося кода в цикле
# независимо от состояния условия, используйте команду break .

# Вместо того чтобы полностью прерывать выполнение цикла без выполнения остав-
# шейся части кода, вы можете воспользоваться командой continue для возвращения
# к началу цикла и проверке условия

# Удаление всех cat в списке в цикле    
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
# pets.remove('cat')
# print(pets)

    # Задаем вопросы, записываем в словари, при необходимости выходим
# responses = {}
# # Установка флага продолжения опроса.
# polling_active = True
# while polling_active:
# # Запрос имени и ответа пользователя.
# 
# name = input("\nWhat is your name? ")
# response = input("Which mountain would you like to climb someday? ")
# 
# # Ответ сохраняется в словаре:
# responses[name] = response
# # Проверка продолжения опроса.Использование цикла while со списками и словарями   133
# 
# repeat = input("Would you like to let another person respond? (yes/ no) ")
# if repeat == 'no':
# polling_active = False
# # Опрос завершен, вывести результаты.
# print("\n--- Poll Results ---")
#  for name, response in responses.items():
# print(name + " would like to climb " + response + ".")

                #СЛОВАРИ 

#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points']) 

#del alien_0['points'] - delete key

    # Перебор только ключей
#for name in favorite_languages.keys():
#    print(name.title())

    #Обход словаля ключ - значение
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }

# newItem = [];

# for key, value in user_0.items():    
#     print("\nKey: " + key +  ": " + value)
#     newItem.append({key : value})

# print(newItem)

# for language in favorite_languages.values():  - только значения   

# for language in set(favorite_languages.values()): - получение только уникальных значений из словаря


# users = {
# 'aeinstein': {
    # 'first': 'albert',
    # 'last': 'einstein',
    # 'location': 'princeton',
# },
# 'mcurie': {
    # 'first': 'marie',
    # 'last': 'curie',
    # 'location': 'paris',
# },
# }


# print(users['mcurie']['first'])



#                                          INPUT


# mytext = input('Input text:')

# print(mytext)

    # Программа будет выполняться до тех пор, пока пользователь не введёт нужные данные циклу while, он так и будет крутить кусок кода
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""

# while message != 'quit':
#     message = input(prompt)
#     print(message)


                                        # Числовые операции

# Оператор вычисления остатка
# При работе с числовыми данными может пригодиться оператор вычисления остатка ( % ), который делит одно число на другое и возвращает остаток:
# 1
# 4 % 3
# 5 % 3
# 6 % 3 

# >>>
# 1
# >>>
# 2
# >>>
# 0
# >>>
    # Проверка на четность, если есть остаток оно не четное

#             if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
# print("\nThe number " + str(number) + " is odd.")                         



    
                                    # ФУНКЦИИ
#  Определение функции
# def greet_user():
    # """Выводит простое приветствие."""
    # print("Hello!")
   
#Вызов функции
# greet_user()

# Именнованые параметры для функции
# describe_pet(animal_type='hamster', pet_name='harry')

# Чтобы передать функции копию списка, можно поступить так:
# имя_функции(имя_списка[:])

# def make_pizza(*toppings):
#     """Вывод списка заказанных дополнений."""
# print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# Звездочка в имени параметра *toppings приказывает Python создать пустой кор-
# теж с именем toppings и упаковать в него все полученные значения.

# Сначала идут именные параметры потом общие, по другому не работает
# def make_pizza(size, *toppings):

                                    #Модули  
# import module;

# text = module.returnData()

# print(text)

# from имя_модуля import функция_0, функция_1, функция_2

# from pizza import make_pizza as mp   - псевдоним для функции модуля
# import pizza as p  - псевдоним для самого модуля
# from pizza import * - импорт всех функций модуля

# from car import Car  - импорт класса Команда import в точке  приказывает Python открыть модуль car и импорти-
# ровать класс Car .
# from car import Car, ElectricCar - импорт нескольких классов из модуля

# Также возможно импортировать весь модуль, а потом обращаться к нужным клас-
# сам с использованием точечной записи.  
# my_cars.py
# import car
#  my_beetle = car.Car('volkswagen', 'beetle', 2016)
# from имя_модуля import *


# Импортирование модуля в модуль
# electric_car.py
# """Набор классов для представления электромобилей."""
#  from car import Car
# class Battery():
# ...
# class ElectricCar(Car):



                                    # API 
# Пакет requests предоставляет удобные средства для запроса информации с сайтов
# из программ Python и анализа полученных ответов. Чтобы установить requests ,
# введите команду следующего вида:
# $ pip install --user requests

# https://bootstrap.pypa.io/get-pip.py  - установка самого пайпа, созранение его на комп и инсталяция этого файла через команду sudo python get-pip.py

# pip list


# import requests
# import tkinter as tk


# def getMockData():
#     # url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#     url = 'http://alexnoch-blog.ru'
#     r = requests.get(url)
#     print("Status code:", r.status_code)
    
#     # response_dict = r.json()
#     # response_dict.split(',')
#     label = tk.Label(window,text=r.text, wraplength=500)
#     label.pack()

# window = tk.Tk()
# window.geometry(f"400x500+100+200");

# btn1 = tk.Button(window,text='Get Data', command=getMockData)
# btn1.pack()

# window.mainloop()

                    # CLASSES

# class Car():
#     def __init__(self, make, model, year):
# """Инициализирует атрибуты описания автомобиля."""
# self.make = make
# self.model = model
# self.year = year
# 
#   self.odometer_reading = 0    // Параметр по умолчанию
# def get_descriptive_name(self):
# ...
# 
# def read_odometer(self):
# """Выводит пробег машины в милях."""
# print("This car has " + str(self.odometer_reading) + " miles on it.")     
# 
# 
# my_new_car.odometer_reading = 23  - изменить параметр по умолчанию
# 
# 
# class Car():

#  - Обновление параметра по умолчанию класс через метод класса
# def update_odometer(self, mileage):
# """Устанавливает заданное значение на одометре."""
# self.odometer_reading = mileage
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
#  my_new_car.update_odometer(23)
# my_new_car.read_odometer()  
# 
# 
# 
# 
# def increment_odometer(self, miles):
# """Увеличивает показания одометра с заданным приращением."""
# self.odometer_reading += miles        
# 
# 
# 
        #Наследование класса
        # 
# class ElectricCar(Car):
#     """Представляет аспекты машины, специфические для электромобилей."""
#     def __init__(self, make, model, year):
#         """Инициализирует атрибуты класса-родителя."""
#         super().__init__(make, model, year)


# my_tesla = ElectricCar('tesla', 'model s', 2016)  
# 
# 
# 
#  Наследуемся от машины, но вызываем в классе машини, класс батарейка и используем методы батарейки в классе машини
# class Battery():
# """Простая модель аккумулятора электромобиля."""

# def __init__(self, battery_size=70):
# """Инициализирует атрибуты аккумулятора."""
# self.battery_size = battery_size
# def describe_battery(self):
# """Выводит информацию о мощности аккумулятора."""
# print("This car has a " + str(self.battery_size) + "-kWh battery.")
# class ElectricCar(Car):
# """Представляет аспекты машины, специфические для электромобилей."""
# def __init__(self, make, model, year):
# """
# Инициализирует атрибуты класса-родителя.
# Затем инициализирует атрибуты, специфические для электромобиля.
# """
# super().__init__(make, model, year)
# 
# self.battery = Battery()
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()  
                      
class Auto():
    def __init__(self,color,speed):
        """auto claaa"""
        self.color = color
        self.speed = speed
    
    def gas(self):
        print(self.color + ' auto run ' + str(self.speed) + ' hour')


mycar = Auto('Red', 200)
run = mycar.gas()

