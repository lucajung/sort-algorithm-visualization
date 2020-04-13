import tkinter as tk
from tkinter import ttk

from DataPoint import DataPoint
from RGB import RGB
import random
import time
from SortingAlgorithms.SortingAlgorithms import *


class Screen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Dataset
        self.data_set = list()

        # Status
        self.is_sorting = False

        # Dimensions ==
        self.window_width = 1000
        self.window_height = 700

        self.control_width = 100

        self.canvas_bar_width = 2
        self.canvas_bar_space = 1
        # Dimensions ==

        # Sorting Algorithms
        self.sorting_algorithms = SortingAlgorithms()

        # Setting the window title
        self.wm_title("Sorting Visualization")

        # Make window not resizable
        self.resizable(0, 0)
        self.minsize(width=self.window_width, height=self.window_height)

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

        # Setting up control elements
        sort_button = ttk.Button(self.application_status_frame, text="Sort", command=self.button_sort_pressed)
        sort_button.grid(row=1, column=0, padx=0, pady=10)

        shuffle_button = ttk.Button(self.application_status_frame, text="Shuffle", command=self.shuffle)
        shuffle_button.grid(row=0, column=0, padx=0, pady=10)

        # Setting up Listbox
        self.sorting_algorithms_select_box = tk.Listbox(self.application_status_frame, selectmode='browse')
        self.sorting_algorithms_select_box.grid(row=2, column=0, padx=0, pady=10)
        for i in self.sorting_algorithms.algorithms:
            self.sorting_algorithms_select_box.insert('end', i.name())

        # Setting up status label
        self.status_label = ttk.Label(self.application_status_frame, text="")
        self.status_label.grid(row=3, column=0, padx=0, pady=10)

        # Generate random dataset
        self.generate_data_set(
            int((self.window_width - self.control_width) / (self.canvas_bar_width + self.canvas_bar_space)))

        # Shuffle dataset
        self.shuffle()

        self.mainloop()

    def shuffle(self):
        if not self.is_sorting:
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
        pos = 1
        self.canvas.delete("all")
        for i in self.data_set:
            self.canvas.create_line(pos, 0, pos, i.value, fill=self.get_hex_code(i.color.r, i.color.g, i.color.b),
                                    width=self.canvas_bar_width)
            pos += self.canvas_bar_width + self.canvas_bar_space
        self.canvas.update()

    def get_hex_code(self, r, g, b):
        return "#" + '{:02x}'.format(r) + '{:02x}'.format(g) + '{:02x}'.format(b)

    def set_info(self, msg):
        self.status_label.config(text=msg)

    def sort(self, sorting_algorithm: SortingAlgorithm):
        self.set_info("Sorting with " + sorting_algorithm.name())
        start = time.time()
        self.is_sorting = True
        sort = sorting_algorithm(self.data_set, self.update_canvas)
        sort.sort()
        self.is_sorting = False
        self.set_info("Done in " + "{:.{}f}".format(time.time() - start, 2) + "sec")

    def get_selected_sorting_algorithm(self):
        curselection = self.sorting_algorithms_select_box.curselection()
        if len(curselection) > 0:
            selected_item = curselection[0]
            return self.sorting_algorithms_select_box.get(selected_item)
        else:
            return None

    def button_sort_pressed(self):
        if not self.is_sorting:
            selected_sorting_algorithm = self.get_selected_sorting_algorithm()
            found = False
            for sorting_algorithm in self.sorting_algorithms.algorithms:
                if selected_sorting_algorithm == sorting_algorithm.name():
                    found = True
                    self.sort(sorting_algorithm)
                    break
            if not found:
                self.set_info("Please select a valid Algorithm.")
        else:
            self.set_info("Please wait till it's sorted.")
