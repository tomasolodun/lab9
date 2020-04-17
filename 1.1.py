import numpy as np
import timeit
from SortingString import *

def BubbleSort(n, direction): #2 аргументи - масив чисел та напрям
    comparisons = 0 # к-сть порівнянь
    exchanges = 0 # к-сть обмінів
    len_n = len(n)
    for i in range(len_n):
        for j in range(0, len_n - 1 - i): # починаємо перевірки з першого елементу, з кожним порівнянням діапазон скорочується
            comparisons += 1
            if direction and n[j] > n[j + 1]: #порівнюєио елементи за зростанням
                exchanges += 1
                n[j], n[j + 1] = n[j + 1], n[j] #перестановка
            elif not direction and n[j] < n[j + 1]: #за спаданням
                exchanges += 1
                n[j], n[j + 1] = n[j + 1], n[j] #перестановка
    return f'Число порівнянь - {comparisons}, число обмінів - {exchanges}, Bubble sort '

def SelectionSort(n, direction):
    comparisons = 0 # к-сть порівнянь
    exchanges = 0 # к-сть обмінів
    len_n = len(n)
    # Ми припускаємо, що перший елемент несортоване масива є найменшим
    for i in range(len_n - 1): # діапазон до передостаннього елементу
        min = i
        for j in range(i + 1, len_n - 1): # діапазон від наступної позиції до кінця
            comparisons += 1
            if direction and n[j] < n[min]:
                min = j # шукаємо мінімальний елемент
            elif not direction and n[j] > n[min]:
                min = j
        exchanges += 1
        n[i], n[min] = n[min], n[i] # міняємо місцями значення найменшого несортованого елемента з першим несортованим
    return f'Число порівнянь - {comparisons}, число обмінів - {exchanges}, Selection sort '

def InsertionSort(n, direction):
    comparison = 0
    exchanges = 0
    len_n = len(n)
    print(n)
    for i in range(1, len_n):
        # Почнемо з другого елементу, так як ми припускаємо, що перший елемент відсортований
        key = n[i] #Присвоєння елемента ключу,як пізніше збережеться на новому місці
        min = i - 1
        comparison += i #Порівняння з попереднім елементом і пересування вліво,
        comparison += min #поки не знайдемо його логічне місце в масиві
        while direction and min >= 0 and n[min] > key: #порівнюєио елементи за зростанням
            exchanges += 1
            n[min + 1] = n[min] #перестановка
            min -= 1
        while not direction and min >= 0 and n[min] < key: #за спаданням
            exchanges += 1
            n[min + 1] = n[min]
            min -= 1
        n[min + 1] = key # Зберігаємо посилання на індекс наступного елемента(ключ)
    return f'Число порівнянь - {comparison}, число обмінів - {exchanges}, Insertion sort '

first = input("Якщо ви бажаєте заповнити масив рандомними цілими числами, натисніть 'Enter'. Якщо ж самостійно, "
             "натисніть будь-яку іншу клавішу: ") #Вибір виконання наступних дій(самостійно/рандомно)

if first == '':
    n = np.random.randint(-1000, 1000, 100) # Діапазон рандомного масиву чисел
else:
    while True:
        try:
            n = []
            for i in range(10):
                a = int(input(f'Введіть {i + 1} елемент: ')) # Ввід 10 елементів
                n.append(a)
            break
        except ValueError:
            print("Введіть ціле число,будь ласка.") #Перевірка на правильність входження

print(f'Невідсортований масив: \n {n}')

checked = input(
    'Оберіть тип сортування: \n 1 - Bubble \n 2 - Selection \n 3 - Insertion \n')
checked_next = True if input('Оберіть порядок сортування: \n 1 - За зростанням \n 2 - За спаданням \n') == "1" else False
direction = "За зростанням" if checked_next else "За спаданням" #Вибір напрямку для виконання функції(direction/not direction)

if checked == '1':
    result, t = BubbleSort(n, checked_next), timeit.timeit(bubbleSortString, number=1) #Сортування масиву за допомогою обраної функції та визначення часу виконання
elif checked == '2':
    result, t = SelectionSort(n, checked_next), timeit.timeit(selectionSortString, number=1)
elif checked == '3':
    result, t = InsertionSort(n, checked_next), timeit.timeit(insertionSortString, number=1)

print(f'Відсортований масив: \n {n} \n', result + direction)
print(f'Дії виконані за {t} секунд') 