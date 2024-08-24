# Пользователь вводит целое положительное число.Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.



while True:
     user_number = int(input("Введите целое положительное число. \n"))
     if user_number <= 0:
        print("Попробуйте еще раз")
     else:
        break
user_number = str(user_number)
result = max(str(user_number))
print(result)
