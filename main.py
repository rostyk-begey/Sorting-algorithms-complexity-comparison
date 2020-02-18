from algorithms import BubbleSort, SelectionSort, InsertionSort, QuickSort, GnomeSort
from factories import CrossfadeArrayFactory
from services import AlgorithmsComparer, PlotDrawer

if __name__ == '__main__':
    algorithms = [
        BubbleSort(),
        SelectionSort(),
        InsertionSort(),
        QuickSort(),
        GnomeSort(),
    ]
    factory = CrossfadeArrayFactory()
    comparer = AlgorithmsComparer(algorithms, factory, (10, 100, 10))
    drawer = PlotDrawer(comparer)
    drawer.draw()
