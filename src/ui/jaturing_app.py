from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import simpledialog

from ui.jaturing_frame import JaturingFrame


class JaturingApp(Tk):
    def __init__(self, machine):
        super().__init__()
        self.title("Jaturing Turing's machine emulator")
        self.geometry("800x600")
        # self.resizable(False, False)

        self.set_style()

        self.machine = machine        
        self.root = JaturingFrame(self)

    def refresh(self):
        self.root.destroy()
        self.root = JaturingFrame(self)
        
    def set_style(self):
        background_color = "#ddddff"
        foreground_color = "#000000"
        self.configure(background = background_color)

        self.style = ttk.Style()
        self.style.configure("TFrame", background = background_color)
        self.style.configure("TButton", background = background_color)
        self.style.configure("TLabel", background = background_color,
                             font = ("Arial",11))
        self.style.configure("Tape.TLabel", background = background_color, foreground = foreground_color,
                             width=3, justify = "center", font = ("Helvetica", 10))
        self.style.configure("TapeHead.TLabel",
                             width=3, justify = "center", font = ("Helvetica", 12, "bold"), background = "red")
        self.style.configure("Tape.TEntry", justify = "center", font = ("Helvetica", 24))
        self.style.configure("Rule.TEntry", justify = "center", font = ("Helvetica", 24))        
