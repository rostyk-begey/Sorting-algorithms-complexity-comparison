from abc import ABC, abstractmethod


class SortStrategy(ABC):
    def __init__(self, array=None):
        self._array = array if array else list()

    def set_array(self, array):
        self._array = array
        return self

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def get_name():
        return 'Sort Algorithm'

    @abstractmethod
    def sort_get_count(self):
        pass
