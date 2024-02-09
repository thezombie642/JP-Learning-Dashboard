# TODO: Implement search page that displays KANJI by keyword
import random
import sys
import uuid
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

from gui_page import gui_page as gui_class

name = "keyword_search"

class keyword_gui(gui_class):
    def load_rest(self):
        label = tk.Label(self, text = "Enter keyword:", font = self.controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)
