from .sort_strategy import SortStrategy


class BubbleSort(SortStrategy):
    @staticmethod
    def get_name():
        return 'Bubble Sort'

    def sort_get_count(self):
        array = self.__array__
        n = len(array)
        count = 0
        for i in range(n):
            for j in range(n):
                count += 1
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
        return count
