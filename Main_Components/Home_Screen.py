import tkinter as tk
from tkinter import *
from tkinter import font as tkfont

# For interfacing with ANKI, plan to auto-create flashcards
import json
import urllib.request

class JP_Learning_Main(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="Calibri", size=18, weight="bold", slant="roman")
        self.title("JP-Dashboard")
        self.iconbitmap("chiyo.ico")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in [StartPage]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
    
    def show_frame(self, page_name):
        self.geometry("")
        frame = self.frames[page_name]
        frame.tkraise()
        
# this is basically a template class for a window setup, or "frame" as they're called in tk
# shove your selector UI code in here
class StartPage(tk.Frame):
    # python constructor, executed on creation
    def __init__(self, parent, controller):
        # initialize the tk frame stuff
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Title prompt
        label = tk.Label(self, text = "Enter word to add to Anki Deck:", font = controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)

        tk.Entry().pack()

        # Search by stroke order or keyword
        keyword_text = Label(textvariable = tk.StringVar().set("Keyword"), height=4)
        keyword_text.pack(side = "left")
        tk.Entry(textvariable = tk.StringVar().set("keyword")).pack()
        tk.Entry(textvariable = tk.StringVar().set("stroke_order")).pack()

if __name__ == "__main__":
    app = JP_Learning_Main()
    app.mainloop()