from .SortingAlgorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap):
        super().__init__(data_set, call_on_swap)

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


class QuickSort(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap):
        super().__init__(data_set, call_on_swap)

    def sort(self):
        self.sort_recursive(0, len(super().get_data_set()) - 1)

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
