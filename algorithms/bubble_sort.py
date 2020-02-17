from .sort_strategy import SortStrategy


class BubbleSort(SortStrategy):
    @staticmethod
    def get_name():
        return 'Bubble Sort'

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
