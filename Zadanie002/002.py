# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("Введите любое трехзначное число  ")
sumOfDigits = int(number[0]) + int(number[1]) + int(number[2])
print(f"Сумма цифр введенного числа = {sumOfDigits} ")

digit = int(number)
sumOfDigits2 = digit % 10 + digit//10 % 10 + digit // 100 % 10
print(f"Сумма цифр введенного числа вторым способом = {sumOfDigits2} ")
