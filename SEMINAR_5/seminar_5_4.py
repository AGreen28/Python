'''35. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
Найдите это число.
'''

with open('text1111.txt', 'r') as f:
    text = f.read()

list = text.split()

def Nuck(list):
    for i in range(len(list)):
        if int(list[i]) - 1 != int(list[i - 1]):
            print(int(list[i]) - 1)

Nuck(list)