'''1. Задайте строку из набора чисел. Напишите программу, которая покажет
большее и меньшее число. В качестве символа-разделителя используйте пробел.

import random

def number(num):
    return [random.randint(1,90) for i in range(num)]   

def min_max(Stroka):   
    return [(Stroka[i]) for i in range(len(Stroka))] # функция для выделения каждого элемента из списка для 
                                                    # нахождения минимального и максимального элемента
n = random.randint(4,21)
Mu_List = number(n) # тут мы значение функции рандомного числа переписываем в будущий список
Mu_List2 = str(Mu_List).replace(',', '') #сдесь мы убираем все запятые и меняем на пробелы как просили
print(Mu_List2)
print(f'Минимальный элемент: [{min(min_max(Mu_List))}], Максимальный элемент: [{max(min_max(Mu_List))}]')
'''
'''
a = input('введите числа через пробел: ')

def num (a):
    f = [int(s) for s in a.split()]
    print(f)
    print(min(f),max(f))

num(a)
'''

'''2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
1) с помощью математических формул нахождения корней квадратного уравнения
2) с помощью дополнительных библиотек Python
'''
'''
from math import sqrt


A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

D = B**2 - 4*A*C

if D == 0:
    x = -B/(2*A)
    print(f"Уравнение имеет один корень: {x}")
elif D > 0:
    x1 = (-B + sqrt(D)) / (2 * A)
    x2 = (-B - sqrt(D)) / (2 * A)
    print(f"Уравнение имеет два корня: x1={x1}; x2={x2}")
else:
    print("Уравнение не имеет вещественных корней")
'''
'''
import math
import random
def rand(znach):
        znach = round(random.uniform(-10, 10),1) # вариант с вещественными числами
        if znach == 0: # вдруг попадается ноль мы крутим рандом по новой
            znach = round(random.uniform(1, 10),1)
        return znach 

def sqrt_dis(a,b,c):
    print(f' Находим корни квардратного уравнения: {a}x^2 + {b}x + {c} = 0')
    dis = b ** 2 - 4 * a * c
    print(f'Дискриминант: {round((dis),2)}')
    sqrt_val = math.sqrt(abs(dis)) # получаем корень и подставляем при желании его везде

    if dis < 0:
        print(f'Корней нет') 
    elif dis == 0:
        kor = round((- b / 2 * a),4)
        print(f'Один корень: {kor}')
    elif dis > 0 :
        kor1 = round(((-b + sqrt_val) / (2 * a )),4)
        kor2 = round(((-b - sqrt_val) / (2 * a )),4)
        print(f'1 корень X1: {kor1} \n2 корень X2: {kor2}')
'''

'''3. Задайте два числа. Напишите программу, которая найдёт НОК
(наименьшее общее кратное) этих двух чисел.
'''
'''
A = int(input("A="))
B = int(input("B="))


def gcd(a, b):
    if(a < b):
        (a, b) = (b, a)
    return gcd(b, a % b) if b != 0 else a


def lcm(a, b):
    return a / gcd(a, b) * b


print(lcm(A, B))
'''