import random
from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
from algorithms import BubbleSort, SelectionSort, InsertionSort, QuickSort, GnomeSort


def avg(array):
    return sum(array) / len(array)


def generate_random_array(length, interval=(0, 100)):
    for i in range(length):
        yield random.randrange(*interval)


def get_statistics_per_length(sort_algorithm, length, number=10):
    compares = []
    swaps = []
    for i in range(number):
        array = [x for x in generate_random_array(length)]
        a, b = sort_algorithm(array).sort_get_count()
        compares.append(a)
        swaps.append(b)
    return compares, swaps


def get_statistics_on_interval(algorithm, start=10, stop=100, step=10, arrays_per_length=10):
    statistics = {}
    for length in range(start, stop, step):
        compares, swaps = get_statistics_per_length(algorithm, length, arrays_per_length)
        statistics[length] = (avg(compares), avg(swaps))
    return statistics


def draw_subplot(plt, title, x, y, nrow, ncol, ind):
    plt.subplot(nrow, ncol, ind)
    plt.plot(x, y, label=title)
    plt.yscale('linear')
    plt.xlabel('array length')
    plt.ylabel('compares' if ind % 2 else 'swaps')
    plt.title(title)
    plt.grid(True)
    return ind + 1


def draw():
    algorithms = [
        BubbleSort,
        SelectionSort,
        InsertionSort,
        QuickSort,
        GnomeSort,
    ]
    n = 1
    col = len(algorithms)
    plt.figure(figsize=(10, 5 * col))
    for algorithm in algorithms:
        statistics = get_statistics_on_interval(algorithm, stop=400)
        title = algorithm.get_name()
        x = list(statistics.keys())
        y = [x for x, y in statistics.values()]
        n = draw_subplot(plt, title, x, y, col, 2, n)
        y = [y for x, y in statistics.values()]
        n = draw_subplot(plt, title, x, y, col, 2, n)
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    plt.show()


if __name__ == '__main__':
    draw()
