'''Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
'''

'''Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")
'''
'''Задача про программистов:
num = int(input('Введите число: '))

def progr(num):
    if (num == 1) or (num > 20 and num % 10 == 1) or (num > 99 and num % 100 ==1):
        print(f'{num} - программист')
    elif (2 <= num <= 4) or (num > 20 and 2 <= num % 10 <= 4) or (num > 99 and 2 <= num % 100 <= 4):
        print(f'{num} - программиста')
    else:
        print(f'{num} - программистов')
progr(num)

#for i in range(0,100,1):
#   progr(i)



def funk(count):
    a = count%10
    if (count == 11):
        return 'Программистов'
    elif (a==0):
        return 'Программистов'
    elif (a==1):
        return 'Программист'
    elif (2<=a)and(a<=4):
        return 'Программиста'
    elif (5<=a)and(a<=9):
        return 'Программистов'



#index = input('Введите число ')
#try:
#    x = int(index)
#except:
#    print('Введены некорректные значения')
#
#if(x<0):
#    print('Число меньше 0')
#else:
#    funk(x)

for i in range(100,111,1):
    print(f'{i}-{funk(i)}')
'''

'''Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
*Пример:*
- Для N = 5: 1, -3, 9, -27, 81


def Row(a):
    for i in range(0, a):
        b = (-3)**i
        print(b, end = ',')

Row(5)
'''

'''Калькулятор'''
'''
def Calc(arg_one, arg_two, operation):
    if operation == '+':
        return arg_one + arg_two
    if operation == '-':
        return arg_one - arg_two
    if operation == '*':
        return arg_one * arg_two
    if operation == '/':
        return arg_one / arg_two


status = True
while status != False:
    arg_one = float(input())
    operation = input()
    arg_two = float(input())
    result = Calc(arg_one, arg_two, operation)
    print(round(result))

    status = input('Введите "q", чтобы выйти из программы.')
    if status == 'q' or status == 'quit':
        status = False
'''

#дешифратор
alphabet_list = str(input("Введите пример: "))
str_a=''
str_b=''
t=0
C = ''
for i in alphabet_list: 
     if chr(ord(i))=='+' or chr(ord(i))=='-' or chr(ord(i))=='*' or chr(ord(i))=='/':
      C = chr(ord(i))
      t=1
     elif t==0:
        str_a = str_a+''.join(chr(ord(i)))
     elif t==1:
        str_b = str_b+''.join(chr(ord(i)))    
A = float(str_a)
B = float(str_b)

#тело калькулятора
if C == '/':
    if B==0:
        print ('На ноль делить нельзя')
    else:
         print (A/B)
if C == '+': 
    print (A+B)
if C == '-': 
    print (A-B)
if C == '*': 
    print (A*B)