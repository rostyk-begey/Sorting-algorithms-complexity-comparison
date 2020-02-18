import numpy as np


class AlgorithmsComparer:
    def __init__(self, algorithms, array_factory, interval=(10, 400, 10), lists_per_interval=10):
        self._algorithms = algorithms
        self._array_factory = array_factory
        self._interval = interval
        self._lists_per_interval = lists_per_interval

    def _get_statistics_per_length(self, sort_algorithm, length):
        compares = []
        swaps = []
        for i in range(self._lists_per_interval):
            array = self._array_factory.get_array(length)
            a, b = sort_algorithm.set_array(array).sort_get_count()
            compares.append(a)
            swaps.append(b)
        return compares, swaps

    def _get_statistics_on_interval(self, algorithm):
        statistics = {}
        for length in range(*self._interval):
            compares, swaps = self._get_statistics_per_length(algorithm, length)
            statistics[length] = (
                algorithm.get_default_compares(length),
                np.average(compares),
                np.average(swaps)
            )
        return statistics

    def get_statistics(self):
        data = {}
        for algorithm in self._algorithms:
            data[str(algorithm)] = self._get_statistics_on_interval(algorithm)
        return data
