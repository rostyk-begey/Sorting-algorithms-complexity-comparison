from .array_factory import ArrayFactory


class ReversedArrayFactory(ArrayFactory):
    def generate(self, length):
        self._arrays[length] = [i for i in range(length, 0, -1)]
