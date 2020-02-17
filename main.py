import random
from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
from algorithms import BubbleSort, SelectionSort, InsertionSort, QuickSort, GnomeSort


def avg(array):
    return sum(array) / len(array)


class AlgorithmComparer:
    def __init__(self, algorithms, interval=(10, 400, 10), lists_per_interval=10):
        self._algorithms = algorithms
        self._interval = interval
        self._lists_per_interval = lists_per_interval

    def _generate_random_array(self, length, interval=(0, 100)):
        for i in range(length):
            yield random.randrange(*interval)

    def _get_statistics_per_length(self, sort_algorithm, length):
        compares = []
        swaps = []
        for i in range(self._lists_per_interval):
            array = [x for x in self._generate_random_array(length)]
            a, b = sort_algorithm(array).sort_get_count()
            compares.append(a)
            swaps.append(b)
        return compares, swaps

    def _get_statistics_on_interval(self, algorithm):
        statistics = {}
        for length in range(*self._interval):
            compares, swaps = self._get_statistics_per_length(algorithm, length)
            statistics[length] = (avg(compares), avg(swaps))
        return statistics

    def get_statistics(self):
        data = {}
        for algorithm in self._algorithms:
            data[algorithm.get_name()] = self._get_statistics_on_interval(algorithm)
        return data


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
    comparer = AlgorithmComparer(algorithms)
    data = comparer.get_statistics()
    n = 1
    col = len(data.keys())
    plt.figure(figsize=(10, 5 * col))
    for title, statistics in data.items():
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
