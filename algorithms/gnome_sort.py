from .sort_strategy import SortStrategy


class GnomeSort(SortStrategy):
    def __str__(self):
        return 'Gnome Sort'

    def get_default_compares(self, length):
        return pow(length, 2)

    def sort_get_count(self):
        array = self._array
        n = len(array)
        compares = 0
        swaps = 0
        index = 0
        while index < n:
            compares += 1
            if index == 0:
                index += 1
            if array[index] >= array[index - 1]:
                index += 1
            else:
                swaps += 1
                array[index], array[index - 1] = array[index - 1], array[index]
                index -= 1

        return compares, swaps
