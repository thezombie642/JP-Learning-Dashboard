# TODO: Implement search page that displays KANJI by keyword
import random
import json
import sys
import uuid

# Tkinter related
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import font as tkFont
from gui_page import gui_page as gui_class

name = "keyword_search"

class keyword_gui(gui_class):
    def load_rest(self):
        label = tk.Label(self, text = "Enter keyword:", font = self.controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)
        self.keyword_entry = tk.Entry(self)
        self.keyword_entry.pack()
        self.keyword_btn = tk.Button(self, text = 'Search', command = self.get_results)
        self.keyword_btn.pack()
        self.results_grid = Frame(self, pady = 25)
        self.results_grid.pack()

    def get_results(self):
        search_str = self.keyword_entry.get().lower()
        with open("kanji_by_keyword.json", '+r') as key_json:
            key_dict = json.load(key_json)
            results_list = key_dict[search_str] if search_str in key_dict else []
            i = 0
            for result in results_list:
                b1 = Button(self.results_grid, text = result, font = self.controller.results_font, padx = 10, pady = 10)
                b1.grid(row = int(i / 9), column = i % 9, sticky = E)
                i += 1
