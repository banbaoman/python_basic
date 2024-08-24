# Узнайте упользователя числоn.Найдите сумму чисел n+nn+nnn.Например,пользователь
#ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input("Введите любое целое число. \n")
number_1 = user_number * 2
number_2 = user_number * 3
result = int(user_number) + int(number_1)+ int(number_2)
print(result)