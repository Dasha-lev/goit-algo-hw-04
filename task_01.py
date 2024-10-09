import random
import timeit
import matplotlib.pyplot as plt

#Реалізація алгоритмів
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

#Генерація масивів різного типу
def generate_array(size, kind='random'):
    if kind == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif kind == 'sorted':
        return list(range(size))
    elif kind == 'reversed':
        return list(range(size))[::-1]
    else:
        raise ValueError("Unknown array kind")

#Функція для заміру часу виконання алгоритму
def time_algorithm(algorithm, array):
    return timeit.timeit(lambda: algorithm(array.copy()), number=10)

# Параметри експерименту
sizes = [100, 1000, 10000]
kinds = ['random', 'sorted', 'reversed']

#Збереження результатів
results = {}
algorithms = [insertion_sort, merge_sort, sorted]  
for algorithm in algorithms:
    results[algorithm.__name__] = {}
    for kind in kinds:
        results[algorithm.__name__][kind] = []
        for size in sizes:
            array = generate_array(size, kind)
            # Заміру часу виконання алгоритму
            time = time_algorithm(algorithm, array)
            results[algorithm.__name__][kind].append(time)

#Візуалізація результатів
for kind in kinds:
    plt.figure(figsize=(10, 6))
    for algorithm, data in results.items():
        plt.plot(sizes, data[kind], label=algorithm)
    plt.xlabel("Розмір масиву")
    plt.ylabel("Час виконання (с)")
    plt.title(f"Порівняння алгоритмів для {kind} масивів")
    plt.legend()
    plt.show()
