from random import randrange
from .array_factory import ArrayFactory


class RandomArrayFactory(ArrayFactory):
    def generate(self, length):
        self._arrays[length] = [randrange(0, length) for _ in range(length)]
