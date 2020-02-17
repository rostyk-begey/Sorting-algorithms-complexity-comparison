from .sort_strategy import SortStrategy


class InsertionSort(SortStrategy):
    def __str__(self):
        return 'Insertion Sort'

    def sort_get_count(self):
        array = self._array
        compares = 0
        swaps = 0
        for i in range(1, len(array)):
            j = i - 1
            next_element = array[i]

            while (array[j] > next_element) and (j >= 0):
                array[j + 1] = array[j]
                j = j - 1
                compares += 1
                swaps += 1
            else:
                compares += 1
            array[j + 1] = next_element
            swaps += 1
        return compares, swaps

