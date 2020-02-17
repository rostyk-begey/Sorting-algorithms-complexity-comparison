from .sort_strategy import SortStrategy


def _quicksort(lst, start, end):
    count = 0
    swaps = 0
    if start < end:
        pos, count, swaps = _partition(lst, start, end)

        c, s = _quicksort(lst, start, pos - 1)
        count += c
        swaps += s

        c, s = _quicksort(lst, pos + 1, end)
        count += c
        swaps += s
    return count, swaps


def _partition(lst, start, end):
    count = 0
    swaps = 0
    pos = start
    for i in range(start, end):
        count += 1
        if lst[i] < lst[end]:
            swaps += 1
            lst[i], lst[pos] = lst[pos], lst[i]
            pos += 1
    lst[pos], lst[end] = lst[end], lst[pos]
    swaps += 1
    return pos, count, swaps


class QuickSort(SortStrategy):
    @staticmethod
    def get_name():
        return 'Quick Sort'

    def sort_get_count(self):
        array = self.__array__
        return _quicksort(array, 0, len(array) - 1)
