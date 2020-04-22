from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):

    def __init__(self, data_set: list, call_on_change, redraw_step_size: int):
        self.data_set = data_set
        self.call_on_change = call_on_change
        self.redraw_step_size = redraw_step_size
        self.count = 0

    def __call__(self, data_set: list, call_on_change, redraw_step_size: int):
        self.__init__(data_set, call_on_change, redraw_step_size)

    def get_data_set(self):
        return self.data_set

    def swap(self, index1, index2):
        self.data_set[index1].active = True
        self.data_set[index2].active = True
        self.data_set[index1], self.data_set[index2] = self.data_set[index2], self.data_set[index1]
        self._value_changed()
        self.data_set[index1].active = False
        self.data_set[index2].active = False

    def insert(self, index, value):
        value.active = True
        self.data_set[index] = value
        self._value_changed()
        value.active = False

    def _value_changed(self):
        self.count = self.count + 1
        if self.redraw_step_size <= self.count:
            self.call_on_change()
            self.count = 0

    def sorted(self):
        self.call_on_change()
        self.count = 0


    @abstractmethod
    def sort(self):
        pass

    @staticmethod
    @abstractmethod
    def name():
        pass
