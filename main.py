from array import *
lists = [1,2,3], [2,3,4], [3,4,5]
k = len(lists)
def merge(*lists):#Объявим функцию
    two_dimensional_array= list(lists)#Поместим переменную в список
    sorted_list = []#Создадим пустой список, который потом осортируем
    for i in range(k):#Цикл, который преобразует двумерный массив в список
        sorted_list += list(two_dimensional_array[i])
    sorted_list.sort()#Отсортируем
    return sorted_list
print(merge(*lists)) #Я не понял, как по формуле вычислить время выполнения функции


