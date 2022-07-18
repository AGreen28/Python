'''1. Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
*Пример:*
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint
n = randint(5,10)
My_list = [randint(1,10) for i in range(n)]
print(My_list)

def number(number):    
    return [number[i] for i in range(len(number)) if i % 2 != 0]
print(f'Элементы стоящие на нечётных позициях:', number(My_list))
print(f'Cумма элементов списка =', sum(number(My_list)))
'''
'''
ls = [2, 3, 5, 9, 3]
def ls_sum(a):
    result = 0
    for i in range(len(a)):
        if i % 2 != 0:
            result += int(a[i])
    print(result)

ls_sum(ls)
'''

'''2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]


number = random.randint(3,10)
n = [random.randint(3,10) for i in range(number)]
print(n)

def par_num(n):
    return [n[-1-i] * n[i] for i in range(math.ceil(len(n)/2))]
print(par_num(n))

#def par_num(n):
#    l = []
#    result = 0
#    for i in range(math.ceil(len(n)/2)): # при math.floor получится [12, 15]
#        result = n[-1-i] * n[i]
#        l.append(result)
#    return l
'''
'''
def multiply_sp(sp):
    if (len(sp) % 2 != 0):
        print('Количество элементов списка не четное!')
        rz = int(len(sp) / 2) + 1
    else:
        rz = int(len(sp) / 2)

    mult = []
    for i in range(0, rz):
        mult.append(sp[i] * sp[len(sp)-1-i])
    return mult

if __name__ == '__main__':
#    sp = [2, 3, 4, 5, 6]
    sp = [2, 3, 5, 6]
    print(sp, ' => ', multiply_sp(sp))
'''

'''3. Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

My = random.randint(5,10)
n = [random.uniform(1,10) for i in range(My)]

def drob(n):
    return [round(i - int(i),2) for i in n]

print(drob(n))
dip = drob(n)

def max_min(dip):
    min = dip[0]
    max = dip[0]
    for i in dip:
        if i > max: max = i
        if i < min and i != 0: min = i 
    print(f'Максимальное значение дробной части: {round(max,2)}; Минимальное значение дробной части:{round(min,2)}')
    return round(max - min,2)
print(f'Разницу между max и min равна =', max_min(dip))
'''
'''
n = [1.1, 1.2, 3.1, 10.01]

def average(n):
    max = 0
    min = 1 #
    for i in n:
        temp = round(i % 1, 3) #
        if temp > max:
            max = temp
        elif temp < min:           
            min = temp
    print(f'max {max} min {min}')
    res = max - min
    return res


print(average(n))
'''
'''
a = [1.1, 1.2, 3.1, 5.10, 10.01]             
def MaxMin(list):
    for i in range(len(list)):
        list[i]=(list[i]%1)
    Result=round(max(list),3)-round(min(list),3)
    return f'Разница между остатком дробей {round(max(list),3)} и {round(min(list),3)} = {Result}'
print(MaxMin(a))
'''

'''4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10


from random import randint, random

n = randint(1,100)
print(n)
def number(n):
    l = ''
    while n > 0:
        l += str(n % 2)
        n = n // 2 
    return l[::-1]
print(number(n))
'''
'''
def DecToBin(n):
    lstBin = []
    while n > 0:
        lstBin.append(str(n%2))
        n //= 2
    return "".join(lstBin[::-1])

print(DecToBin(6))
'''

'''5. Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
*Пример:*
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
'''
import random

n = random.randint(6,10)
print(n)
def fib1(n):
    l = [1,1]  
    result = 1
    for i in range(2, n): 
       result = l[-1] + l[-2]  
       l.append(result) 
    return  l

def fib2(n):
    d = [0,1,1]
    result2 = 1
    for i in range(2, n): 
       result2 = d[-1] + d[-2] 
       d.append(result2)  
    return d

def minus(n):
    for i in range(len(n)):
        if i % 2 != 0: n[i] = - n[i] 
    return n

fibo1 = minus(fib1(n))
fibo2 = fib2(n)
print(fibo1[::-1] + fibo2)
'''

def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)
    
    for i in range(2, n+1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    
    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n-2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    return fibo_list

x = fibo(10)
print(x)
