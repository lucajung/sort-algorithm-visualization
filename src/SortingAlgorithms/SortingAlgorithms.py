from .SortingAlgorithm import SortingAlgorithm


class SortingAlgorithms:
    def __init__(self):
        self.algorithms = list()
        self.algorithms.append(BubbleSort)
        self.algorithms.append(QuickSort)
        self.algorithms.append(InsertionSort)
        self.algorithms.append(SelectionSort)


class BubbleSort(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap, redraw_step_size: int):
        super().__init__(data_set, call_on_swap, redraw_step_size)

    def sort(self):
        data_set = super().get_data_set()
        length = len(data_set)
        for _ in range(length - 1):
            for i in range(length - 1):
                val1 = data_set[i].value
                val2 = data_set[i + 1].value
                if val1 > val2:
                    super().swap(i, i + 1)
            length = length - 1
        super().sorted()

    @staticmethod
    def name():
        return "Bubble Sort"


class QuickSort(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap, redraw_step_size: int):
        super().__init__(data_set, call_on_swap, redraw_step_size)

    def sort(self):
        self.sort_recursive(0, len(super().get_data_set()) - 1)
        super().sorted()

    def sort_recursive(self, index_start: int, index_end: int):
        data_set = super().get_data_set()
        if index_start < index_end:
            piv = data_set[index_end].value
            smallest = index_start - 1
            for i in range(index_start, index_end):
                if data_set[i].value < piv:
                    smallest = smallest + 1
                    super().swap(i, smallest)
            piv = smallest + 1
            super().swap(piv, index_end)
            self.sort_recursive(index_start, piv - 1)
            self.sort_recursive(piv + 1, index_end)

    @staticmethod
    def name():
        return "Quick Sort"


class InsertionSort(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap, redraw_step_size: int):
        super().__init__(data_set, call_on_swap, redraw_step_size)

    def sort(self):
        data_set = super().get_data_set()
        length = len(data_set)
        for i in range(0, length):
            val = data_set[i]
            j = i
            while j > 0 and data_set[j - 1].value > val.value:
                super().insert(j, data_set[j - 1])
                j = j - 1
            super().insert(j, val)
        super().sorted()

    @staticmethod
    def name():
        return "Insertion Sort"


class SelectionSort(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap, redraw_step_size: int):
        super().__init__(data_set, call_on_swap, redraw_step_size)

    def sort(self):
        data_set = super().get_data_set()
        length = len(data_set)
        for i in range(length - 1):
            min = i
            for j in range(i + 1, length):
                if data_set[j].value < data_set[min].value:
                    min = j
            if min != i:
                super().swap(i, min)
        super().sorted()

    @staticmethod
    def name():
        return "Selection Sort"
