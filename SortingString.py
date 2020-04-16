bubbleSortString = """import numpy as np
n = np.random.randint(-50000, 50000, 2000)
def BubbleSort(n, direction):
    if direction:
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
BubbleSort(n, True)
"""

selectionSortString ="""
import numpy as np
n = np.random.randint(-50000, 50000, 2000)
def SelectionSort(n, direction):
    comparisons = 0
    exchanges = 0
    len_n = len(n)
    for i in range(len_n - 1):
        min = i
        for j in range(i + 1, len_n - 1):
            comparisons += 1
            if direction and [j] < n[min]:
                min = j
            elif not direction and n[j] > n[min]:
                min = j
        exchanges += 1
        n[i], n[min] = n[min], n[i]
    return f'Число порівнянь - {comparisons}, число обмінів - {exchanges}, Selection sort '
SelectionSort(n, True)
"""

insertionSortString = """
import numpy as np
n = np.random.randint(-50000, 50000, 2000)
def InsertionSort(n, direction):
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
InsertionSort(n, True)
"""