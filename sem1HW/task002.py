# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# num = input('Введите трехзначное число: ')
# sum = 0
# if len(num) == 3:
#     for i in num:
#        sum += int(i)
#     print(sum)
# else:
#     print('Не трехзначное число')



num = int(input('Введите трехзначное число: '))
if 99 < num < 1000:
    print(num // 100 + num // 10 % 10 + num % 10)