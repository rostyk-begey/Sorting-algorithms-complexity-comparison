from .sort_strategy import SortStrategy


class GnomeSort(SortStrategy):
    @staticmethod
    def get_name():
        return 'Gnome Sort'

    def sort_get_count(self):
        array = self.__array__
        n = len(array)
        compares = 0
        swaps = 0
        index = 0
        while index < n:
            compares += 1
            if index == 0:
                index = index + 1
            if array[index] >= array[index - 1]:
                index = index + 1
            else:
                swaps += 1
                array[index], array[index - 1] = array[index - 1], array[index]
                index = index - 1

        return compares, swaps
