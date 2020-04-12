from abc import ABC, abstractmethod

class SortingAlgorithm(ABC):

    def __init__(self, data_set: list, call_on_swap):
        self.data_set = data_set
        self.call_on_swap = call_on_swap

    def get_data_set(self):
        return self.data_set

    def swap(self, index1, index2):
        self.data_set[index1], self.data_set[index2] = self.data_set[index2], self.data_set[index1]
        self.call_on_swap()
    
    @abstractmethod
    def sort(self):
        pass