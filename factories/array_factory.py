from abc import ABC, abstractmethod


class ArrayFactory(ABC):
    def __init__(self):
        self._arrays = {}

    def get_array(self, length):
        if length not in self._arrays.keys():
            self.generate(length)
        return self._arrays[length][::]

    @abstractmethod
    def generate(self, length):
        self._arrays[length] = [0 for _ in range(length)]

    def reset(self):
        self._arrays = {}
