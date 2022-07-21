'''34. Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
'''

with open('file3.txt', 'r', encoding='utf-8') as f1:
    s1 = f1.readline()

with open('file4.txt', 'r', encoding='utf-8') as f2:
    s2 = f2.readline()

print(s1)
print(s2)