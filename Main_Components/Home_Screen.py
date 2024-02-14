# TKInter
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import messagebox

# For interfacing with ANKI, plan to auto-create flashcards
import json
import urllib.request

# Pillow
from PIL import Image, ImageTk
import keyword_search, stroke_search, anki_create

MIKU_DIR = 'C:/Users/taunt/Downloads/JP-Learning-Dashboard/JP-Learning-Dashboard/Main_Components/miku_gif/frame_'

class JP_Learning_Main(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="Calibri", size=18, weight="bold", slant="roman")
        self.results_font = tkfont.Font(family = 'Helvetica', size = 18, weight = 'bold')
        self.title("JP-Dashboard")
        # self.iconbitmap("chiyo.ico")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.minsize(300,300)

        self.frames = {}

        for F in [StartPage, stroke_search.stroke_gui, keyword_search.keyword_gui, anki_create.create_gui]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    
    def show_frame(self, page_name):
        self.geometry("")
        frame = self.frames[page_name]
        frame.tkraise()
        return frame
        
# this is basically a template class for a window setup, or "frame" as they're called in tk
# shove your selector UI code in here
class StartPage(tk.Frame):
    # python constructor, executed on creation
    def __init__(self, parent, controller):
        # initialize the tk frame stuff
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Ask the user which feature to use
        label = tk.Label(self, text = "Select feature to use:", font = controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)
        centered_buttons = Frame(self)
        self.keyword_btn = tk.Button(centered_buttons, text="Search by keyword", command = self.show_keyword, padx = 5)
        self.stroke_btn = tk.Button(centered_buttons, text="Search by stroke", command = self.show_stroke, padx = 5)
        self.anki_create_btn = tk.Button(centered_buttons, text="Create ANKI Card", command = self.create_anki, padx = 5)
        self.webpage_btn = tk.Button(centered_buttons, text="Open LOCALHOST", command= self.launch_local, padx = 5)
        self.keyword_btn.pack(side = LEFT)
        self.stroke_btn.pack(side = LEFT)
        self.anki_create_btn.pack(side = LEFT)
        self.webpage_btn.pack(side = LEFT)
        self.miku_gif = MikuGif(self.controller)
        self.miku_gif.pack()
        self.miku_gif.load(MIKU_DIR)
        centered_buttons.pack(side=TOP)

    def show_keyword(self):
        self.miku_gif.unload()
        self.controller.show_frame("keyword_gui")

    def show_stroke(self):
        self.miku_gif.unload()
        self.controller.show_frame("stroke_gui")

    def create_anki(self):
        self.miku_gif.unload()
        self.controller.show_frame("create_gui")

    def launch_local(self):
        self.miku_gif.unload()

class MikuGif(tk.Label):
    def load(self, miku):
        self.loc = 0
        self.frames = [ImageTk.PhotoImage(Image.open(f'{miku}{i}.gif').convert('RGBA')) for i in range(4)]
        self.delay = 200
        self.next_frame()

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
    
    def unload(self):
        self.config(image="")
        self.frames = None

if __name__ == "__main__":
    app = JP_Learning_Main()
    app.mainloop()