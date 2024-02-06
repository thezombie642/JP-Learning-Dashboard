# TODO: Implement search page that displays KANJI by stroke count

import random
import sys
import uuid
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

name = "stroke_search"

class stroke_gui(tk.Frame):
    def __init__(self, parent, controller):
        # gui setup- these first two lines are required
        tk.Frame.__init__(self, parent)
        self.controller = controller