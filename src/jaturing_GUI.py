from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

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
        self.style.configure("Tape.TLabel", width=3, justify = "center", font = ("Helvetica", 10))
        self.style.configure("Tape.TEntry", width = 2, justify = "center", font = ("Helvetica", 24))        
        
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
        def __init__(self, master, size, head = 0):
            """ The shown tape is 2 times length of size, from 0-size to 0+size
            """
            super().__init__(master)
            self.configure(height = 200)

            self.head = head
            self.size = size
            
            self.labels = []
            self.entries = []
            self.indexes = []
            self.values = []
            for i in range(2 * size):
                index = StringVar()
                index.set(str(i - size))
                value = StringVar()
                value.set(str(i - size))
                label = ttk.Label(self, style = "Tape.TLabel", textvariable=index)
                entry = ttk.Entry(self, style = "Tape.TEntry", width = 2, textvariable = value)
                label.grid(row = 0, column = i)
                entry.grid(row = 1, column = i)

                self.labels.append(label)
                self.entries.append(entry)
                self.indexes.append(index)
                self.values.append(value)
                
        def set(self, tape_slice):
            self.head = tape.get_head_position
            i = 0
            for tape_cell  in tape_slice(self.size):
                self.indexes[i] = tape_cell[0]
                self.values[i] = tape_cell[1]

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
        self.tape = self._Tape(self.frame_top, 10)
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

