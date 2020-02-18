from .sort_strategy import SortStrategy


class SelectionSort(SortStrategy):
    def __str__(self):
        return 'Selection sort'

    def get_default_compares(self, length):
        return pow(length, 2)

    def sort_get_count(self):
        array = self._array
        n = len(array)
        compares = 0
        swaps = 0
        for index in range(n):
            min_index = index
            # Find the index'th smallest element
            for i in range(index + 1, n):
                compares += 1
                if array[i] < array[min_index]:
                    min_index = i
            else:
                compares += 1
            if min_index != index:  # swap the elements
                swaps += 1
                array[index], array[min_index] = array[min_index], array[index]
        return compares, swaps
