# Минимальный делитель
# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input("Введите число N: "))
flag = True
i = 2
while flag:
    if n % i == 0:
        print(i)
        flag = False
    i += 1

# n = int(input("Введите число N: "))

# for i in range (2, n + 1):
#     if n % i == 0:
#         print(i)
#         break






