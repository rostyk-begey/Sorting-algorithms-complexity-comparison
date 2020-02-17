from .sort_strategy import SortStrategy


class SelectionSort(SortStrategy):
    @staticmethod
    def get_name():
        return 'Selection sort'

    def sort_get_count(self):
        array = self.__array__
        compares = 0
        swaps = 0
        for index in range(len(array)):
            min_index = index
            # Find the index'th smallest element
            for i in range(index + 1, len(array)):
                compares += 1
                if array[i] < array[min_index]:
                    min_index = i
            else:
                compares += 1
            if min_index != index:  # swap the elements
                swaps += 1
                array[index], array[min_index] = array[min_index], array[index]
        return compares, swaps
