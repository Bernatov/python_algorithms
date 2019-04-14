# #задача №1
# n=input()
# sum_num=0
# pr_num=1
# for i in n:
#     sum_num+=int(i)
# for i in n:
#     pr_num*=int(i)
#
# print(f'Сумма цифр{sum_num}')
# print(f'Произведение цифр {pr_num}')

# # задача №4
# import random
#
# diapozon1 = int(input())
# diapozon2= int(input())
#
# print(f'случайное целое число в диапозоне от {diapozon1} до {diapozon2} - {random.randint(diapozon1, diapozon2)}')
# print(f'случайное вещественное число в диапозоне от {diapozon1} до {diapozon2} - {random.uniform(diapozon1, diapozon2)}')
#
# diapozon_bukv=input()
# print(f'случайная буква в диапозоне {diapozon_bukv} - {diapozon_bukv[ random.randint(1,len(diapozon_bukv))]}')

# # задача №5
# alf = 'abcdefghijklmnopqrstuvwxyz'
# word1 = input()
# word2 = input()
# print(f'буква "{word1}" имеет порядковый номер - {alf.index(word1)+1}, буква "{word2}" имеет порядковый номер - {alf.index(word2)+1}, а между ними {abs(alf.index(word2) - alf.index(word1)) - 1} букв ')

# #№6
# alf = 'abcdefghijklmnopqrstuvwxyz'
# num_word=int(input())
# # не через встроенную функцию
# i=''
# for _ in range(num_word):
#    i=alf[_]
# print(f'искомая буква {i}')

# #№8
# year=int(input('введите год '))
#
# if year%400==0:
#     print('Год високосный')
# elif year%100==0:
#     print('Год не високосный')
# elif year%4==0:
#     print('Год високосный')
# else: print('Год не високосный')
# # №9
# a=int(input())
# b=int(input())
# c=int(input())
#
# if a>b and a<c:
#     print(f'среднее число{a}')
# elif b>a and b<c:
#     print(f'среднее число{b}')
# else:
#     print(f'среднее число{c}')
