from .array_factory import ArrayFactory


class CrossfadeArrayFactory(ArrayFactory):
    def generate(self, length):
        array = []
        for i in range(length):
            array.append(i if i % 2 == 0 else length - i)
        self._arrays[length] = array
