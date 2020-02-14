from abc import ABC, abstractmethod


class SortStrategy(ABC):
    def __init__(self, array):
        self.__array__ = array

    @staticmethod
    def get_name():
        return 'Sort Algorithm'

    @abstractmethod
    def sort_get_count(self):
        pass
