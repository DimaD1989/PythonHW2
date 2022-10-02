# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number


# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum


# num = InputNumbers("Введите число: ")
# print(f"Сумма цифр = {sumNums(num)}")

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите число: "))
 
# factorial = 1
 
# for i in range(2, n+1):
#     factorial *= i
 
# print(factorial)

# Задайте список из n чисел последовательности (1+1/n ) ** n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# arr = [int(input('Введите элементы списка: ')) 
# for i in range(int(input('Введите длину списка: ')))]


# n = int(input('Введите количество чисел в последовательности: '))

# # Сразу же считаем сумму
# sum = 0
# for i in range(0, n):
#     # Запрашиваем число
#     input_value = int(input(f'Введите число #{i}: '))
#     # Сразу же прибавляем его к сумме
#     sum += input_value 

# print('Сумма всех чисел последовательности:', sum)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# arr = [int(input('Введите элемент списка: ')) 
# for i in range(int(input('Введите длину списка: ')))]
 
# mult = 1
# for i in arr:
#     mult *= i
 
# print(f'Весь список: {arr}')
# print(f'Произведение элементов списка: {mult}')

# arr = [int(input('Введите элемент списка: ')) 
# for i in range(int(input('Введите длину списка: ')))]
    
# for j in range(i):
#      if arr[i]>arr[i+1]:
        
#         arr[i],arr[i+1]=arr[i+1],arr[i]
        
#         print(arr)