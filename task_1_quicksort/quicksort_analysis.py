import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    same = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + same + randomized_quick_sort(greater)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    same = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + same + deterministic_quick_sort(greater)

def test_quick_sorts():
    sizes = [10_000, 50_000, 100_000, 500_000]
    r_times, d_times = [], []

    for size in sizes:
        data = [random.randint(1, 1_000_000) for _ in range(size)]
        r_total, d_total = 0, 0

        for _ in range(5):
            arr_copy = data.copy()
            start = time.perf_counter()
            randomized_quick_sort(arr_copy)
            r_total += time.perf_counter() - start

            arr_copy = data.copy()
            start = time.perf_counter()
            deterministic_quick_sort(arr_copy)
            d_total += time.perf_counter() - start

        r_avg = r_total / 5
        d_avg = d_total / 5
        r_times.append(r_avg)
        d_times.append(d_avg)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {r_avg:.4f} секунд")
        print(f"   Детермінований QuickSort: {d_avg:.4f} секунд\n")

    plt.plot(sizes, r_times, label='Randomized QuickSort')
    plt.plot(sizes, d_times, label='Deterministic QuickSort')
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час (сек)")
    plt.title("Порівняння QuickSort алгоритмів")
    plt.legend()
    plt.grid(True)
    plt.savefig("screenshots/quicksort_plot.png")
    plt.show()

if __name__ == "__main__":
    test_quick_sorts()
