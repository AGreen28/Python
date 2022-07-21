'''32. Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
'''
'''
def find_elements(list_of_elements):
    new_list = []
    for i in list_of_elements:
        c = list_of_elements.count(i)
        if c == 1:
            new_list.append(i)
    return new_list

list1 = [1, 5, 5, 6, 6, 7, 8, 8, 9, 0]
print(find_elements(list1))
'''

numbers =[1,2,3,4,4,1,0,8,5,6,7,8,0,8,4]
def UniqueNumbers(numbers):
    result=[i for i in numbers if numbers.count(i)==1]
    return result
print(UniqueNumbers(numbers))
