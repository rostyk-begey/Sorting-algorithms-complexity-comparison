from .sort_strategy import SortStrategy


class InsertionSort(SortStrategy):
    @staticmethod
    def get_name():
        return 'Insertion Sort'

    def sort_get_count(self):
        array = self.__array__
        counter = 0
        for i in range(1, len(array)):
            j = i - 1
            next_element = array[i]

            while (array[j] > next_element) and (j >= 0):
                array[j + 1] = array[j]
                j = j - 1
                counter += 1
            else:
                counter += 1
            array[j + 1] = next_element
        return counter

