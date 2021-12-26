from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar, BooleanVar
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import OptionMenu

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import networkx as nx


class JaturingFrame(ttk.Frame):
    class _Buttons(ttk.Frame):
        """Control buttons of the machine
        Attributes:
            master : Tkinter container containing the _Graph
            root_frame : Applications main Tkinter container
        """
        def __init__(self, master, root_frame):
            """Constructor of the class

            Args:
                master : Tkinter container containing the _Graph
                root_frame : Applications main Tkinter container
            """
            super().__init__(master)

            self.configure(height=50)

            self.return_to_start_button = ttk.Button(self,
                                                     text="Return to start",
                                                     command=root_frame.return_to_start)

            self.step_forward_button = ttk.Button(self,
                                                  text="Step Forward",
                                                  command=root_frame.step_forward,
                                                  style="Forward.TButton")

            self.new_state_button = ttk.Button(self,
                                               text="Add state",
                                               command=root_frame.new_state)
            self.delete_state_button = ttk.Button(self,
                                                  text="Delete state",
                                                  command=root_frame.delete_state)

            self.delete_rule_button = ttk.Button(self,
                                                 text="Delete rule",
                                                 command=root_frame.delete_rule)

            self.save_file_button = ttk.Button(self,
                                               text="Save file",
                                               command=root_frame.save_file)

            self.load_file_button = ttk.Button(self,
                                               text="Load file",
                                               command=root_frame.load_file)

            self.return_to_start_button.grid(row=2, column=0)
            self.step_forward_button.grid(row=2, column=1)
            self.new_state_button.grid(row=2, column=2)
            self.delete_state_button.grid(row=2, column=3)
            self.delete_rule_button.grid(row=2, column=4)
            self.save_file_button.grid(row=2, column=5)
            self.load_file_button.grid(row=2, column=6)

    class _Selections(ttk.Frame):
        """Frame containing various selections for the machine
        Attributes:
            master : Tkinter container containing the _Graph
            root_frame : Applications main Tkinter container
        """
        def __init__(self, master, root_frame):
            """Constructor of the class

            Args:
                master : Tkinter container containing the _Graph
                root_frame : Applications main Tkinter container
            """
            super().__init__(master)

            self.current_state = StringVar()
            self.start_state = StringVar()
            self.left_tape_bool = BooleanVar()

            self.current_state_label = ttk.Label(self,
                                                 textvariable=self.current_state)
            self.start_state_label = ttk.Label(self,
                                               textvariable=self.start_state)
            self.start_state_set_button = ttk.Button(self,
                                                     text="Set start state to current ",
                                                     command=root_frame.set_start_state_to_current)
            self.left_tape_checkbutton = ttk.Checkbutton(self,
                                                         text="Allow negative tape indices",
                                                         variable=self.left_tape_bool,
                                                         onvalue=True,
                                                         offvalue=False,
                                                         command=root_frame.set_negative_index_allowed)

            ttk.Label(self, text="Current state:").grid(row=0, column=0)
            self.current_state_label.grid(row=0, column=1)

            ttk.Label(self, text="Start state:").grid(row=0, column=2)
            self.start_state_label.grid(row=0, column=3)

            self.start_state_set_button.grid(row=0, column=4)
            self.left_tape_checkbutton.grid(row=0, column=5)

        def load(self, machine):
            """Load field values from given Turing's machine

            Args:
                machine : Jaturing object
            """
            self.current_state.set(machine.current_state)
            self.start_state.set(machine.start_state)
            self.left_tape_bool.set(machine.tape.negative_index_allowed)

        def reload(self, machine):
            """Load field values from given Turing's machine

            Args:
                machine : Jaturing object
            """
            self.load(machine)

    class _Rule(ttk.Frame):
        """Required fields to create a rule
        Attributes:
            master : Tkinter container containing the _Graph
            root_frame : Applications main Tkinter container
        """
        def __init__(self, master, root_frame):
            """Constructor of the class

            Args:
                master : Tkinter container containing the _Graph
                root_frame : Applications main Tkinter container
            """
            super().__init__(master)

            self.state = StringVar()
            self.character = StringVar()
            self.write_char = StringVar()
            self.direction = StringVar()
            self.new_state = StringVar()

            self.state_entry = ttk.Entry(self, textvariable=self.state, width=7)
            self.character_entry = ttk.Entry(self, textvariable=self.character, width=7)
            self.write_char_entry = ttk.Entry(self, textvariable=self.write_char, width=7)

            directions = ["RIGHT","LEFT"]
            self.direction.set(directions[0])
            self.direction_menu = OptionMenu(self, self.direction, *directions)
            self.new_state_entry = ttk.Entry(self, textvariable=self.new_state, width=7)
            self.add_rule_button = ttk.Button(self,
                                              text="Add rule",
                                              command=root_frame.add_rule)

            self.state_entry.grid(row=1, column=0)
            self.character_entry.grid(row=1, column=1)
            self.write_char_entry.grid(row=1, column=2)
            self.direction_menu.grid(row=1, column=3)
            self.new_state_entry.grid(row=1, column=4)
            self.add_rule_button.grid(row=1, column=5)

            ttk.Label(self, text="State").grid(row=0, column=0)
            ttk.Label(self, text="Read char").grid(row=0, column=1)
            ttk.Label(self, text="Write char").grid(row=0, column=2)
            ttk.Label(self, text="Move to").grid(row=0, column=3)
            ttk.Label(self, text="New state").grid(row=0, column=4)



    class _Tape(ttk.Frame):
        """_Tape object handles the graphical representation of the tape

        Attributes:
            master : Tkinter container containing the _Graph
            size : Tape is displayed from head positien size left and right
                   Displayed area is 2*size long
            head : Integer, head position
        """
        def __init__(self, master, size, head=0):
            """Constructor of the class

            Args:
                master : Tkinter container containing the _Graph
                size : Tape is displayed from head positien size left and right
                       Displayed area is 2*size long
                head : Integer, head position
            """
            super().__init__(master)
            self.configure(height=200)

            self.machine = None
            self.head = head     # Turing machine read/write head position
            self.size = size     # How many cells are shown left and right from the head

            self.labels = []  # TLabel widget showing index
            self.entries = [] # TEntry widget displaying and allowing editing of values on tape
            self.indexes = [] # StringVar object which is connected to respective TLabel
            self.values = []  # StringVar object which is connected to respective TEntry
            # Tape values, their index numbers and respective
            # StringVar objects are stored in arrays

            self.left_button = ttk.Button(self, text="<", command=self._move_left)
            self.left_button.grid(row=0, column=0)
            for i in range(2 * size):
                index = StringVar()
                index.set("1") # str(i - size))
                value = StringVar()
                value.set(str(i - size))

                label = ttk.Label(self,
                                  style="Tape.TLabel",
                                  textvariable=index)
                entry = ttk.Entry(self,
                                  width=2,
                                  textvariable=value,
                                  font=("Courier", 14, "bold"))
                label.grid(row=0, column=i+1)
                entry.grid(row=1, column=i+1)

                callback = lambda a, b, c, i=i: self._update_tape(index=i)
                value.trace_add("write", callback)

                self.labels.append(label)
                self.entries.append(entry)
                self.indexes.append(index)
                self.values.append(value)
            self.right_button = ttk.Button(self, text=">", command=self._move_right)
            self.right_button.grid(row=0, column=2*size+1)

        def load(self, machine):
            """Load the tape values from the Turing's machine

            Args:
                machine : Jaturing machine
            """
            if not machine:
                return
            self.machine = machine
            self.head = machine.tape.get_head_position()
            slice = self.machine.tape.get_slice(self.size)

            i = 0
            for cell in slice:
                tape_index = cell[0]
                self.indexes[i].set(tape_index)
                self.values[i].set(cell[1])
                if(tape_index == self.head):
                    self.labels[i].configure(style="TapeHead.TLabel")
                else:
                    self.labels[i].configure(style="Tape.TLabel")
                i += 1

        def reload(self):
            """Reload the tape values from the Turing's machine

            Args:
                machine : Jaturing machine
            """
            self.load(self.machine)

        def _update_tape(self, index):
            """Read the value from user interface and update it to
            the machine object

            Args:
                index : Index on the tape, which value will be updated
            """
            tape_index = int(self.indexes[index].get())
            value_string = self.values[index].get()
            
            if len(value_string) == 0:
                first_character = "."
            else:
                first_character = value_string[0]
                
            self.values[index].set(first_character)  # Drop rest of the string
            
            if first_character == self.machine.tape._get_value(tape_index):
                return

            self.machine.tape.set_value(tape_index, first_character)
            self.load(self.machine)

        def _move_left(self):
            """Move the read/write head to the left
            """
            if not self.machine:
                return
            self.machine.tape.move_left()
            self.reload()

        def _move_right(self):
            """Move the read/write head to the right
            """
            if not self.machine:
                return
            self.machine.tape.move_right()
            self.reload()

    class _StatesAndRules(ttk.Frame):
        """The tree view containing states and rules of the machine

        Attributes:
            master : Tkinter container containing the _Graph
            root_frame : Applications main Tkinter container
        """
        def __init__(self, master, root_frame):
            """Constructor of the class

            Args:
                master : Tkinter container containing the _Graph
                root_frame : Applications main Tkinter container
            """
            super().__init__(master)
            self.root_frame = root_frame

            self.tree = ttk.Treeview(self,
                                     selectmode="browse",
                                     columns=("ReadChar", "WriteChar", "Direction", "NextState"))
            self.tree.heading("#0", text="State")
            self.tree.column("#0", stretch="yes", width=100)
            self.tree.heading("#1", text="Read")
            self.tree.column("#1", stretch="yes", width=45)
            self.tree.heading("#2", text="Write")
            self.tree.column("#2", stretch="yes", width=45)
            self.tree.heading("#3", text="Tape")
            self.tree.column("#3", stretch="yes", width=70)
            self.tree.heading("#4", text="New state")
            self.tree.column("#4", stretch="yes", width=100)

            self.tree.pack()

            self.tree.bind("<<TreeviewSelect>>", self.tree_select)

        def tree_select(self, event):
            """Event handler for the tree. The current state is
            retrieved from the selection

            Args:
                event : Event object
            """
            all_selected_states = self.tree.focus().split(";")

            if not len(all_selected_states) > 0:
                return None
            if all_selected_states[0] == "":
                return None

            selected_state = all_selected_states[0]
            self.root_frame.set_current_state(selected_state)

        def clear_tree(self):
            """Delete all states and rules from the TreeView
            """
            for item in self.tree.get_children():
                self.tree.delete(item)

        def load(self, states):
            """Load states and rules to the TreeView

            Args:
                states : States dictionary from a Jaturing machine
            """
            for state_name, state in states.items():
                self.tree.insert(parent="",
                                 index=0,
                                 iid=state_name,
                                 text=state_name)
                if not len(state.rules) == 0:
                    for rule_name, rule in state.rules.items():
                        self.tree.insert(parent=state_name,
                                         index="end",
                                         text=rule_name,
                                         iid=f"{state_name};{rule_name}",
                                         values=(rule_name,
                                                 rule.write_char,
                                                 rule.direction,
                                                 rule.next_state))
            self._tree_expand_all()

        def reload(self, machine):
            """Reload states and rules to the TreeView

            Args:
                machine : Jaturing object of the Turing's machine
            """
            self.clear_tree()
            self.load(machine.states)

        def _tree_expand_all(self):
            """Expand all branches of the TreeView
            """
            top_branches = self.tree.get_children()
            for branch in top_branches:
                self.tree.item(branch, open=True)

    class _Graph(ttk.Frame):
        """ Graphical representation of the states

        Attributes:
            master : Tkinter container containing the _Graph
            root_frame : Applications main Tkinter container
        """
        def __init__(self, master, root_frame):
            """Constructor of the class

            Args:
                master : Tkinter container containing the _Graph
                root_frame : Applications main Tkinter container
            """
            super().__init__(master)
            self.root_frame = root_frame

            self.figure_canvas = None

        def load(self, machine):
            """Create the graph from the machine

            Args:
                machine : Jaturing object
            """
            if self.figure_canvas:
                self.figure_canvas.get_tk_widget().destroy()
            self.figure = plt.Figure(figsize=(8,6), dpi=100)
            self.axis = self.figure.add_subplot(111)
            plt.axis('off')


            # Drawing the graph using networkx library
            self.graph = nx.DiGraph()

            # Drawing area
            self.figure_canvas = FigureCanvasTkAgg(self.figure, self)
            self.figure_canvas.draw()
            self.figure_canvas.get_tk_widget().pack(side='bottom',
                                                    fill='both',
                                                    expand=1)

            color_map = []
            size_map = []
            self._add_state_nodes(machine, color_map, size_map)
            self._add_rule_edges(machine)

            #pos=nx.spring_layout(self.graph),
            pos=nx.planar_layout(self.graph)


            nx.draw_networkx(self.graph,
                             pos=pos,
                             with_labels=True,
                             node_color=color_map,
                             node_size=size_map,
                             ax=self.axis)

            edge_labels = nx.get_edge_attributes(self.graph, 'title')

            nx.draw_networkx_edge_labels(self.graph,
                                         pos=pos,
                                         edge_labels=edge_labels,
                                         font_size=1000)

            self.figure_canvas.draw()
            plt.close()

        def reload(self, machine):
            """Recreate the graph from the machine

            Args:
                machine : Jaturing object
            """
            self.load(machine)

        def _add_state_nodes(self, machine, color_map, size_map):
            """Create nodes which represent the states of the machine.

            Args:
                machine : Jaturing object
            """
            for state_name in machine.states.keys():
                if state_name == machine._accept_state:
                    color_map.append('green')
                    size_map.append(2000)
                    self.graph.add_node(state_name)
                    continue

                if state_name == machine._reject_state:
                    color_map.append('red')
                    size_map.append(2000)
                    self.graph.add_node(state_name)
                    continue

                if state_name == machine.current_state:
                    color_map.append('#ff6666')
                    size_map.append(1500)
                    self.graph.add_node(state_name)
                    continue

                color_map.append('#dddddd')
                size_map.append(1500)
                self.graph.add_node(state_name)

        def _add_rule_edges(self, machine):
            """Create edges connecting the nodes. Each edge represents
            a rule in the machine

            Args:
                machine : Jaturing object
            """

            for state_name, state in machine.states.items():
                start = state_name
                for character, rule in state.rules.items():
                    end = rule.next_state

                    # Rule has an end state, which doesn't exist
                    if end not in machine.states.keys():
                        continue
                    label = f"if '{character}' write '{rule.write_char}' move: {rule.direction}"
                    self.graph.add_edge(start, end, title=label)

    def __init__(self, container):
        """Main JaturingFrame frame initializer

        Args:
            container : Parent Tkinter container
        """
        super().__init__(container)
        self.app = container

        options = {"padx": 10, "pady": 10}

        # Top frame for the tape
        self.frame_top = ttk.Frame(self)
        self.frame_top.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.tape = self._Tape(self.frame_top, 10)
        self.tape.pack()
        self.tape.load(container.machine)

        # Left hand frame containing states and rules tree
        self.frame_left = ttk.Frame(self)
        self.frame_left.grid(row=1, column=0, sticky="w")
        self.states_and_rules_tree = self._StatesAndRules(self.frame_left, self)
        self.states_and_rules_tree.pack()
        self.states_and_rules_tree.load(container.machine.states)

        # Frame for graphical representation of the states
        self.frame_right = ttk.Frame(self)
        self.frame_right.grid(row=1, column=1)
        self.graph = self._Graph(self.frame_right, self)
        self.graph.pack()
        self.graph.load(container.machine)

        # Frame for some selections in the machine
        self.frame_bottom03 = ttk.Frame(self)
        self.frame_bottom03.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.selections = self._Selections(self.frame_bottom03, self)
        self.selections.grid(row=3, column=2, columnspan=2, sticky="w")
        self.selections.load(container.machine)

        # Frame offering fields to create rules
        self.frame_bottom02 = ttk.Frame(self)
        self.frame_bottom02.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.rulefields = self._Rule(self.frame_bottom02, self)
        self.rulefields.grid(row=4, column=2, columnspan=2, sticky="w")

        # Frame for control buttons
        self.frame_bottom01 = ttk.Frame(self)
        self.frame_bottom01.grid(row=4, column=0, columnspan=2, sticky="ew")
        self.buttons = self._Buttons(self.frame_bottom01, self)
        self.buttons.grid(row=5, column=2, columnspan=2, sticky="w")

        self.grid(**options)

        self.reload()

    def reload(self):
        """ Reload values from the machine to UI objects
        """
        machine = self.app.machine

        self.tape.reload()
        self.selections.reload(machine)
        self.graph.reload(machine)
        self.states_and_rules_tree.reload(machine)

    def return_to_start(self):
        """Return the machine to the initial state
        """
        self.app.machine.return_to_start()

        self.reload()

    def step_forward(self):
        """Performs one Turing machine step
        """
        if self.app.machine.current_state is None:
            current_state = self._selected_state()
            if not current_state:
                messagebox.showinfo(title="No state", message="No state selected")
                return
            self.app.machine.current_state = current_state

        self.app.machine.step_forward()

        self.reload()

    def new_state(self):
        """Create new state to the Turing's machine
        """
        state_name = simpledialog.askstring(title="New state",
                                            prompt="Name of the new state")
        if not state_name:
            return
        self.app.machine.add_state(state_name)

        self.reload()

    def delete_state(self):
        """Delete a state from the Turing's machine
        """
        state_name = self._selected_state()
        self.app.machine.delete_state(state_name)

        self.reload()

    def delete_rule(self):
        """Delete a rule from a state
        """
        rule = self._selected_rule()
        if rule is None:
            messagebox.showinfo(title="No rule", message="No rule to delete")
            return
        state = self._selected_state()
        self.app.machine.delete_rule(state, rule)

        self.reload()

    def add_rule(self):
        """ Add new rule for a state
        """
        state_name = self._selected_state()
        character = self.rulefields.character.get()
        write_char = self.rulefields.write_char.get()
        direction = self.rulefields.direction.get()
        new_state = self.rulefields.new_state.get()

        self.app.machine.set_rule(state_name, character, write_char, direction, new_state)

        self.reload()

    def save_file(self):
        """Convert the current machine to a JSON string and save it to a file
        """
        formats = self.app.machine.io.get_file_formats()

        filename = filedialog.asksaveasfilename(title="Save as",
                                                initialfile="Untitled.json",
                                                defaultextension=".json",
                                                filetypes=formats)

        if not filename:
            return

        self.app.machine.io.save_file(filename)

    def load_file(self):
        """Load previously saved JSON formatted Turing's machine from a file
        """
        formats = self.app.machine.io.get_file_formats()

        filename = filedialog.askopenfilename(title="Load file",
                                              defaultextension=".json",
                                              filetypes=formats)

        if not filename:
            return

        self.app.machine.io.load_file(filename)
        self.app.refresh()

    def set_current_state(self, state_name):
        """Change Turing's machine's current state

        Args:
            state_name : String, name of the state
        """
        self.app.machine.current_state = state_name
        self.rulefields.state.set(state_name)

        self.reload()

    def set_start_state_to_current(self):
        """Sets the current state value to the start state.
        """
        self.app.machine.set_start_state_to_current()

        self.reload()

    def set_negative_index_allowed(self):
        """Sets the property of the machine, which indicates if the
        read/write head of the tape can move left from zero position
        """
        if self.selections.left_tape_bool.get():
            self.app.machine.tape.allow_negative_indexes()
        else:
            self.app.machine.tape.deny_negative_indexes()

        self.reload()

    def _selected_rule(self):
        """Return the rule which is currently selected from the tree
        """
        selected_rule = self.states_and_rules_tree.tree.focus().split(";")
        if not len(selected_rule) == 2:
            return None
        return selected_rule[1]  # rule iid in the TreeView is "state;rule"

    def _selected_state(self):
        """Return the state which is currently selected from the tree
        """
        return self.rulefields.state.get()
