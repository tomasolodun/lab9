import numpy as np
import timeit
from SortingString import *

def BubbleSort(n, direction):
    comparisons = 0
    exchanges = 0
    len_n = len(n)
    for i in range(len_n):
        for j in range(0, len_n - 1 - i):
            comparisons += 1
            if direction and n[j] > n[j + 1]:
                exchanges += 1
                n[j], n[j + 1] = n[j + 1], n[j]
            elif not direction and n[j] < n[j + 1]:
                exchanges += 1
                n[j], n[j + 1] = n[j + 1], n[j]
    return f'Число порівнянь - {comparisons}, число обмінів - {exchanges}, Bubble sort '

def SelectionSort(n, direction):
    comparisons = 0
    exchanges = 0
    len_n = len(n)
    for i in range(len_n - 1):
        min = i
        for j in range(i + 1, len_n - 1):
            comparisons += 1
            if direction and n[j] < n[min]:
                min = j
            elif not direction and n[j] > n[min]:
                min = j
        exchanges += 1
        n[i], n[min] = n[min], n[i]
    return f'Число порівнянь - {comparisons}, число обмінів - {exchanges}, Selection sort '

def InsertionSort(n, direction):
    comparison = 0
    exchanges = 0
    len_n = len(n)
    print(n)
    for i in range(1, len_n):
        key = n[i]
        min = i - 1
        comparison += i
        comparison += min
        while direction and min >= 0 and n[min] > key:
            exchanges += 1
            n[min + 1] = n[min]
            min -= 1
        while not direction and min >= 0 and n[min] < key:
            exchanges += 1
            n[min + 1] = n[min]
            min -= 1
        n[min + 1] = key
    return f'Число порівнянь - {comparison}, число обмінів - {exchanges}, Insertion sort '

first = input("Якщо ви бажаєте заповнити масив рандомними цілими числами, натисніть 'Enter'. Якщо ж самостійно, "
             "натисніть будь-яку іншу клавішу: ")

if first == '':
    n = np.random.randint(-1000, 1000, 100)
else:
    while True:
        try:
            n = []
            for i in range(10):
                a = int(input(f'Введіть {i + 1} елемент: '))
                n.append(a)
            break
        except ValueError:
            print("Введіть ціле число,будь ласка.")

print(f'Невідсортований масив: \n {n}')

checked = input(
    'Оберіть тип сортування: \n 1 - Bubble \n 2 - Selection \n 3 - Insertion \n')
checked_next = True if input('Оберіть порядок сортування: \n 1 - За зростанням \n 2 - За спаданням \n') == "1" else False
direction = "За зростанням" if checked_next else "За спаданням"

if checked == '1':
    result, t = BubbleSort(n, checked_next), timeit.timeit(bubbleSortString, number=1)
elif checked == '2':
    result, t = SelectionSort(n, checked_next), timeit.timeit(selectionSortString, number=1)
elif checked == '3':
    result, t = InsertionSort(n, checked_next), timeit.timeit(insertionSortString, number=1)

print(f'Відсортований масив: \n {n} \n', result + direction)
print(f'Дії виконані за {t} секунд') 