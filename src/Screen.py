import _tkinter
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

        # Parameter
        self.active_rgb = RGB(0, 0, 255)
        self.show_as_bars = False
        self.redraw_step_size_gui = tk.IntVar()
        self.redraw_step_size_gui.trace_add("write", self.set_redraw_step_size)
        self.redraw_step_size_gui.set(1)

        # Status
        self.is_sorting = False

        # Dimensions ==
        self.window_width = 1000
        self.window_height = 700

        self.control_width = 100

        self.canvas_data_point_width = 3
        self.canvas_data_point_space = 1
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
        toggle_view_button = ttk.Button(self.application_status_frame, text="Toggle view", command=self.toggle_view)
        toggle_view_button.grid(row=0, column=0, padx=0, pady=5)

        shuffle_button = ttk.Button(self.application_status_frame, text="Shuffle Single", command=self.shuffle_single)
        shuffle_button.grid(row=1, column=0, padx=0, pady=5)

        shuffle_button = ttk.Button(self.application_status_frame, text="Shuffle", command=self.shuffle)
        shuffle_button.grid(row=2, column=0, padx=0, pady=5)

        # Setting up Listbox
        self.sorting_algorithms_select_box = tk.Listbox(self.application_status_frame, selectmode='browse')
        self.sorting_algorithms_select_box.grid(row=3, column=0, padx=0, pady=5)
        for i in self.sorting_algorithms.algorithms:
            self.sorting_algorithms_select_box.insert('end', i.name())

        sort_button = ttk.Button(self.application_status_frame, text="Sort", command=self.button_sort_pressed)
        sort_button.grid(row=4, column=0, padx=0, pady=5)

        # Setting up status label
        self.status_label = ttk.Label(self.application_status_frame, text="")
        self.status_label.grid(row=5, column=0, padx=0, pady=5)

        redraw_step_size_label_text = tk.StringVar()
        redraw_step_size_label_text.set("Enter redraw step size:")
        redraw_step_size_label = tk.Label(self.application_status_frame, textvariable=redraw_step_size_label_text,
                                          height=1)
        redraw_step_size_label.grid(row=6, column=0, padx=0, pady=0)
        redraw_step_size_input = tk.Entry(self.application_status_frame, textvariable=self.redraw_step_size_gui)
        redraw_step_size_input.grid(row=7, column=0, padx=0, pady=0)

        # Generate random dataset
        self.generate_data_set(
            int((self.window_width - self.control_width) / (
                        self.canvas_data_point_width + self.canvas_data_point_space)))

        # Shuffle dataset
        self.shuffle()

        self.mainloop()

    def shuffle(self):
        if not self.is_sorting:
            random.shuffle(self.data_set)
            self.update_canvas()

    def shuffle_single(self):
        if not self.is_sorting:
            index1 = random.randint(0, len(self.data_set) - 1)
            index2 = random.randint(0, len(self.data_set) - 1)
            self.data_set[index1], self.data_set[index2] = self.data_set[index2], self.data_set[index1]
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
        pos = self.canvas_data_point_width
        self.canvas.delete("all")
        for i in self.data_set:
            color = i.color
            if i.active:
                color = self.active_rgb
            if self.show_as_bars:
                self.canvas.create_line(pos + (self.canvas_data_point_width / 2), self.window_height,
                                        pos + (self.canvas_data_point_width / 2), self.window_height - i.value,
                                        fill=self.get_hex_code(color.r, color.g, color.b),
                                        width=self.canvas_data_point_width)
            else:
                self.canvas.create_rectangle(pos, self.window_height - i.value, pos + self.canvas_data_point_width,
                                             self.window_height - i.value + self.canvas_data_point_width,
                                             fill=self.get_hex_code(color.r, color.g, color.b), width=0)
            pos += self.canvas_data_point_width + self.canvas_data_point_space
        self.canvas.update()

    def get_hex_code(self, r, g, b):
        return "#" + '{:02x}'.format(r) + '{:02x}'.format(g) + '{:02x}'.format(b)

    def set_info(self, msg):
        self.status_label.config(text=msg)

    def set_redraw_step_size(self, n, m, x):
        try:
            tmp = int(self.redraw_step_size_gui.get())
            if tmp < 1:
                tmp = 1
            self.redraw_step_size = tmp
            self.redraw_step_size_gui.set(tmp)

        except _tkinter.TclError:
            self.redraw_step_size = 1
            self.redraw_step_size_gui.set(1)

    def toggle_view(self):
        self.show_as_bars = not self.show_as_bars
        self.update_canvas()

    def sort(self, sorting_algorithm: SortingAlgorithm):
        self.set_info("Sorting with " + sorting_algorithm.name())
        start = time.time()
        self.is_sorting = True
        sort = sorting_algorithm(self.data_set, self.update_canvas, self.redraw_step_size)
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
