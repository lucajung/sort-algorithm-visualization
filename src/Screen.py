import tkinter as tk
from DataPoint import DataPoint
from RGB import RGB
import random
from SortingAlgorithms.SortingAlgorithms import *


class Screen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.data_set = list()
        self.window_width = 1000
        self.window_height = 700

        self.control_width = 100

        # Setting the window title
        self.wm_title("Sorting Visualization")

        self.resizable(0, 0)

        self.minsize(width=800, height=500)

        # Init window_frame
        self.window_frame = tk.Frame(self, width=self.window_width, height=self.window_height)
        self.window_frame.grid(row=0, column=0, padx=0, pady=0)

        # Setting up the GUI frames
        self.application_status_frame = tk.Frame(self.window_frame, width=self.control_width, height=self.window_height)
        self.application_status_frame.grid(row=0, column=0, padx=0, pady=0)
        self.application_status_frame.pack_propagate(0)

        self.application_main_frame = tk.Frame(self.window_frame, width=self.window_width - self.control_width,
                                               height=self.window_height)
        self.application_main_frame.grid(row=0, column=1, padx=0, pady=0)

        # Setting up Canvas
        self.canvas = tk.Canvas(self.application_main_frame, width=self.window_width - self.control_width,
                                height=self.window_height)
        self.canvas.pack()

        self.generate_data_set(int((self.window_width - self.control_width) / 5))

        self.shuffle()

        self.sort("Bubble Sort")

        # self.after(2000, self.shuffle)

        self.mainloop()

    def shuffle(self):
        random.shuffle(self.data_set)
        self.update_canvas()

    def generate_data_set(self, length: int):
        self.data_set = list()
        for _ in range(length):
            value = random.randint(10, self.window_height)
            green_portion = int(value / self.window_height * 255)
            red_portion = 255 - green_portion
            rgb = RGB(red_portion, green_portion, 0)
            self.data_set.append(DataPoint(value, rgb))

    def update_canvas(self):
        pos = 0
        self.canvas.delete("all")
        for i in self.data_set:
            self.canvas.create_line(pos, 0, pos, i.value, fill=self.get_hex_code(i.color.r, i.color.g, i.color.b),
                                    width=3)
            pos += 5
        self.canvas.update()

    def get_hex_code(self, r, g, b):
        return "#" + '{:02x}'.format(r) + '{:02x}'.format(g) + '{:02x}'.format(b)

    def set_info(self, msg):
        pass

    def sort(self, method: str):
        self.set_info("sorting...")
        time = 0
        if method == "Bubble Sort":
            sort = BubbleSort(self.data_set, self.update_canvas)
            sort.sort()
        elif method == "Quick Sort":
            sort = QuickSort(self.data_set, self.update_canvas)
            sort.sort()
        self.set_info("Done (" + str(time) + ")")
