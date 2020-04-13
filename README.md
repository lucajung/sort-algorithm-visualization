# sort-algorithm-visualization
The sorting algorithm visualization is a small demo application to easily compare different sorting algorithms.
It is capable of sorting a completely random dataset aswell as a nearly sorted dataset, to show of the differences in runtime.

For example:<br />
<img src="/images/quick_sort.gif" width="300"><br />
<img src="/images/selection_sort.gif" width="300"><br />
<img src="/images/bubble_sort_single.gif" width="300">

Extensibility
---
The software is build to easily extend the sorting algorihms:<br />
In order to add a new sorting algorithm, just add a new class to ([SortingAlgorithms.py](src/SortingAlgorithms/SortingAlgorithms.py)):
```python
class NewSortingAlgorithm(SortingAlgorithm):
    def __init__(self, data_set: list, call_on_swap):
        super().__init__(data_set, call_on_swap)

    def sort(self):
        pass

    @staticmethod
    def name():
        return "Name of sorting algorithm"
```
That's all!<br />
Enjoy!
