# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

lengthOfChocolate = int(input("Введите длину шоколадки (количество долек): "))
widthOfChocolate = int(input("Введите ширину шоколадки (количество долек): "))
requiredPart = int(input("Сколько долек вы хотите отломить одним разломом: "))

if requiredPart <= lengthOfChocolate * widthOfChocolate and (requiredPart % lengthOfChocolate == 0 or requiredPart % widthOfChocolate == 0):
  print("Yes - вы можете отломить столько долек одним разломом")
else:
  print("No - вы не сможете отломить столько долек одним разломом")

