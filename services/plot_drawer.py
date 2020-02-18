from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self, algorithm_comparer):
        self._algorithm_comparer = algorithm_comparer

    def _draw_subplot(self, title, x, values, nrow, ncol, ind):
        plt.subplot(nrow, ncol, ind)
        plt.plot(x, values[0], label='current')
        if len(values) == 2:
            plt.plot(x, values[1], 'y--', label='default')
        plt.yscale('linear')
        plt.xlabel('array length')
        plt.ylabel('compares' if ind % 2 else 'swaps')
        plt.legend()
        plt.title(title)
        plt.grid(True)
        return ind + 1

    def draw(self):
        data = self._algorithm_comparer.get_statistics()
        n = 1
        col = len(data.keys())
        plt.figure(figsize=(10, 5 * col))
        for title, statistics in data.items():
            values = list(statistics.keys())
            defaults = []
            compares = []
            swaps = []
            for default, cmp, swp in statistics.values():
                defaults.append(default)
                compares.append(cmp)
                swaps.append(swp)
            n = self._draw_subplot(title, values, (compares, defaults), col, 2, n)
            n = self._draw_subplot(title, values, (swaps,), col, 2, n)
        plt.gca().yaxis.set_minor_formatter(NullFormatter())
        plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
        plt.show()
