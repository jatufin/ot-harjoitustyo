from tkinter import Tk
from tkinter import ttk


class JaturingApp(Tk):
    def __init__(self, machine):
        super().__init__()
        self.title("Jaturing Turing's machine emulator")
        self.geometry("800x600")
        self.resizable(False, False)

        self.set_style()

        self.machine = machine        
        self.root = JaturingFrame(self)

        

    def set_style(self):
        background_color = "#ddddff"
        self.configure(background = background_color)

        self.style = ttk.Style()
        self.style.configure("TFrame", background = background_color)
        self.style.configure("TButton", background = background_color)
        self.style.configure("TLabel", background = background_color,
                             font = ("Arial",11))
        
class JaturingFrame(ttk.Frame):
    class _Buttons(ttk.Frame):
        def __init__(self, master, root_frame):
            super().__init__(master)

            self.configure(height = 50)
            
            self.return_to_start_button = ttk.Button(master,
                                                     text = "Return",
                                                     command = root_frame.return_to_start)
            self.play_button = ttk.Button(master,
                                          text = "PLAY",
                                          command = root_frame.play)
            self.stop_button = ttk.Button(master,
                                          text = "Stop",
                                          command = root_frame.stop)
            self.step_forward_button = ttk.Button(master,
                                                  text = "Step Forward",
                                                  command = root_frame.step_forward)        

            self.return_to_start_button.grid(row = 0, column = 0)
            self.play_button.grid(row = 0, column = 1)
            self.stop_button.grid(row = 0, column = 2)
            self.step_forward_button.grid(row = 0, column = 3)        

    class _Tape(ttk.Frame):
        def __init__(self, master, root_frame):
            super().__init__(master)
            self.configure(height = 200)

            ttk.Label(self, text="TAPE HERE!").pack()
            
    def __init__(self, container):
        super().__init__(container)

        options = { "padx": 10, "pady": 10 }

        self.frame_top = ttk.Frame(self)
        self.frame_top.grid(row = 0, column = 0, columnspan = 2)
        
        self.frame_left = ttk.Frame(self)
        self.frame_left.grid(row = 1, column = 0)
        
        self.frame_right = ttk.Frame(self)
        self.frame_right.grid(row = 1, column = 1)
        
        self.frame_bottom = ttk.Frame(self)
        self.frame_bottom.grid(row = 2, column =1, columnspan = 2)

        ttk.Label(self.frame_top, text = "Ylä").pack()
        self.tape = self._Tape(self.frame_top, self)
        self.tape.pack()
        
        ttk.Label(self.frame_left, text = "Vasen").pack()
        ttk.Label(self.frame_right, text = "Oikea").pack()

        self.buttons = self._Buttons(self.frame_bottom, self)
        self.buttons.grid()
        
        self.pack(**options)

    def play(self):
        print("Play")

    def stop(self):
        print("stop")

    def return_to_start(self):
        print("return to start")

    def step_forward(self):
        print("step forward")
        
def launch(machine):    
    app = JaturingApp(machine)
    app.mainloop()

