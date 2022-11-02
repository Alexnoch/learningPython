test = ['test','test2']; 
numbers = [1,2,3,4,5,6]; # Список
constantNumbers = (6,5,4,3,2,1) # Кортеж значения которого нельзя изменять, хотя можно переопределять сам кортеж
test.append('test3'); # В конец списка
test.insert('test 0'); # В начало списка

print(max(numbers)) # Выводим максимальное число в списке
# Цикл
for key in test:
    print(key)

# 
squares = [value**2 for value in range(1,11)]
print(squares)

slice = numbers[1:4] # [1:]  Получение элементов с 1 по 4
copy = numbers[:] # копирует массив 

print(slice)