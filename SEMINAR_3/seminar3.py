'''
import json
sp=[5,11,2,3,4,8,157,555]

def max_average(sp):
    maxx=sp[0]
    sr=0
    for i in sp:
        if i > maxx:
            maxx=i
        sr+=i
    sr=sr/len(sp)
    rez={}
    rez['максимальный элемент']=maxx
    rez['среднее арифметическое']=sr
    k=(maxx,sr,rez)
    return k

with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD = json.load(fh)  # загружаем из файла данные в словарь data
print('БД успещно загружена')
print(type(BD))


#res=max_average(sp)

#with open('data.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
    
 #           fh.write(json.dumps(res, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
#print('БД успещно сохранена')
#print(res[2])
#for x,y in res[2].items():
 #   print(x,y)


#print(len(rez))
#for x,y in rez.items():
#    print(x,y)
    
'''

'''Задайте список из n чисел ряда фибоначчи


def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input('Введите число элементов: '))

def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibo(i))
    return list
print(fibolist(x))
'''

'''сделать функцию, на вход принимающую список,
 на выходе возращающая словарь, где указаны максимальное число,
 минимальное, их индексы, и среднее арифметическое


N = 5

def inisp(N):
    sp = [];
    for i in range(1,N+1):
        sp.append(round((1+1/i)**i,2))
    return sp

def inib(sp):
    bib = {}
    max = sp[0]
    idmax = 0
    min = sp[0]
    idmin = 0
    sum = 0
    for i in range(len(sp)):
        if(max<sp[i]):
            max = sp[i]
            idmax = i
        if(min>sp[i]):
            min = sp[i]
            idmin = i
        sum += sp[i]
    sred = sum/len(sp)
    bib['max'] = max
    bib['idmax'] = idmax
    bib['min'] = min
    bib['idmin'] = idmin
    bib['sred'] = sred
    return bib

spisok = inisp(N)
bibl = {}
print(spisok)
bibl = inib(spisok)
print(bibl)
file = open('HW1.txt','a')
for a,b in bibl.items():
    file.write(f'{a} - {b} ')
file.write('\n')
file.close()
'''

'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 сохраните список в формате JSON.
'''

import json

N = int(input('Введите число: '))

def Chislo(N):
    num = []
    for i in range(-N, N + 1):
        num.append(i)
    return num

with open('data.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
    fh.write(json.dumps(Chislo(N), ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
print('БД успешно сохранена')

with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    BD = json.load(fh)  # загружаем из файла данные в словарь data
print('БД успещно загружена')
print(BD)