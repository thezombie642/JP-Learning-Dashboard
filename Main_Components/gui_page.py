import random
import sys
import uuid
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

MIKU_DIR = 'C:/Users/taunt/Downloads/JP-Learning-Dashboard/JP-Learning-Dashboard/Main_Components/miku_gif/frame_'

class gui_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.backbutton = tk.Button(self, text="Back", command = self.back)
        self.backbutton.pack(side = BOTTOM)

        self.load_rest()

    def back(self):
        start_frame = self.controller.show_frame("StartPage")
        start_frame.miku_gif.load(MIKU_DIR)

    # To be implemented in children
    def load_rest(self):
        pass