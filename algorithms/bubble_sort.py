from .sort_strategy import SortStrategy


class BubbleSort(SortStrategy):
    def __str__(self):
        return 'Bubble Sort'

    def get_default_compares(self, length):
        return pow(length, 2)

    def sort_get_count(self):
        array = self._array
        n = len(array)
        compares = 0
        swaps = 0
        for i in range(n):
            for j in range(n):
                compares += 1
                if array[i] < array[j]:
                    swaps += 1
                    array[i], array[j] = array[j], array[i]
        return compares, swaps
