from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):

    def __init__(self, data_set: list, call_on_change):
        self.data_set = data_set
        self.call_on_change = call_on_change

    def __call__(self, data_set: list, call_on_change):
        self.__init__(data_set, call_on_change)

    def get_data_set(self):
        return self.data_set

    def swap(self, index1, index2):
        self.data_set[index1].active = True
        self.data_set[index2].active = True
        self.data_set[index1], self.data_set[index2] = self.data_set[index2], self.data_set[index1]
        self.call_on_change()
        self.data_set[index1].active = False
        self.data_set[index2].active = False

    def insert(self, index, value):
        value.active = True
        self.data_set[index] = value
        self.call_on_change()
        value.active = False

    @abstractmethod
    def sort(self):
        pass

    @staticmethod
    @abstractmethod
    def name():
        pass
