import random
import matplotlib.pyplot as plt
from algorithms import BubbleSort, SelectionSort, InsertionSort, QuickSort


def avg(array):
    return sum(array) / len(array)


def generate_random_array(length, interval=(0, 100)):
    for i in range(length):
        yield random.randrange(*interval)


def get_statistics_per_length(sort_algorithm, length, number=10):
    data = []
    for i in range(number):
        array = [x for x in generate_random_array(length)]
        data.append(sort_algorithm(array).sort_get_count())
    return data


def get_statistics_on_interval(algorithm, start=10, stop=100, step=10, arrays_per_length=10):
    statistics = {}
    for length in range(start, stop, step):
        data = get_statistics_per_length(algorithm, length, arrays_per_length)
        statistics[length] = avg(data)
    return statistics


def draw():
    algorithms = [
        BubbleSort,
        SelectionSort,
        InsertionSort,
        QuickSort,
    ]
    for algorithm in algorithms:
        statistics = get_statistics_on_interval(algorithm, stop=400)
        x = list(statistics.keys())
        y = list(statistics.values())
        plt.plot(x, y, label=algorithm.get_name())

    plt.xlabel('array length')
    plt.ylabel('compares performed')
    plt.title("Algorithms complexity comparison")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    draw()
