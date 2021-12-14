import sys
import json

from ui.jaturing_GUI import launch
from tape import Tape
from rule import Rule
from state import State

_ALPHABET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Jaturing:
    """ Main class of the Jaturing Turing's machine
    The tape of the machine is kept in self._tape object
    and states with transition rules are in self._states dictionary
    """
    def __init__(self):
        self._alphabet = _ALPHABET
        self._tape = Tape(self._alphabet)

        self.init_states()
        self.halted = False
        
    @property
    def states(self):
        """
        The states of the machine are stored in a dictionary object, wehere
        the names of the states are keys, and State objects values.

        Parameters
        ----------
        None

        Returns
        -------
        states : { str : State }
        """
        return self._states

    @property
    def tape(self):
        """
        Tape of the machine is stored in a Tape object


        Parameters
        ----------
        None

        Returns
        -------
        tape : Tape
        """
        return self._tape

    def init_states(self):
        """ Initially the mahcine has always two halting states:
        Initialize the states of a new Turing's machine.
        Two initial actual states are ACCEPT and REJECT, an they are stored
        in the _states dictionary.
        Additionally the machine has internal pointers to states, such as the
        self.current_state.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._states = {}
        self.current_state = None
        self.start_state = None
        
        self._accept_state = "ACCEPT"
        self.add_state(self._accept_state)

        self._reject_state = "REJECT"
        self.add_state(self._reject_state)

    def add_state(self, name):
        """ Add a state to the Turing's machine

        Parameters
        ----------
        name : str
            Name of the state

        Returns
        -------
        None
        """
        self._states[name] = State()
        if self.start_state == None:
            self.start_state = name

        if self.current_state == None:
            self.current_state = name

    def delete_state(self, name):
        """
        Delete the given state from the Turing's machine

        Parameters
        ----------
        name : str
            Name of the state

        Returns
        -------
        None
        """
        if not name in self._states:
            return
        if self.start_state == name:
            self.start_state = None        
        if self.current_state == name:
            self.current_state = None
        self.states.pop(name)

    def get_state(self, name):
        """
        Return the State object by the name of the state

        Parameters
        ----------
        name : str
            Name of the state

        Returns
        -------
        state : State
            State object
        """
        if name not in self._states:
            return None
        return self._states[name]

    def clear_tape(self):
        """
        Remove all characters from the tape

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self._tape = Tape(self._alphabet)        
            
    def set_rule(self, state_name,
                 character,
                 write_char,
                 direction,
                 next_state
                 ):
        """
        Create a new rule for a state

        Parameters
        ----------
        state_name : str
            The state where the rule is applied
        character : str
            Single character. The rule is applied if this character is read from the tape,
            when the machine is in the state_name state
        write_char : str
            Single character, which will be written to the tape. It will overwrite the
            character, which had been raed from the tape
        direction : str
            To which direction the read/write head will be moved.
            Allowed values are: LEFT and RIGHT
        next_state : str
            The new state the machine will be after this rule has been applied

        Returns
        -------
        None
        """
        if not self.get_state(state_name):
            self.add_state(state_name)
        self.get_state(state_name).set_rule(character=character,
                                            write_char=write_char,
                                            direction=direction,
                                            next_state=next_state
                                            )

    def delete_rule(self, state, rule):
        """ Delete a rule from the state
        """
        if not state in self._states:
            return
        self._states[state].delete_rule(rule)

    def is_accept_or_reject(self, state):
        return state in (self._accept_state, self._reject_state)

    def step_forward(self):
        character = self.tape.read()
        state = self.get_state(self.current_state)
        rule = state.get_rule(character)

        if self.current_state == self._reject_state:
            self.halt()
            return
        
        if self.current_state == self._accept_state:
            self.halt()
            return
        
        if not rule:
            self.halt()
            return

        self.tape.write(rule.write_char)

        if rule.direction == "RIGHT":
            self.tape.move_right()
        elif rule.direction == "LEFT":
            self.tape.move_left()

        self.current_state = rule.next_state

    def halt(self):
        self.halted = True

    def unhalt(self):
        self.halted = False
        
    def print_states_and_rules(self):
        print("STATUS")
        print(f"Tape: {str(self._tape)}")
        print(f"Current state: {self.current_state}")
        print(f"Start state: {self.start_state}")
        print(f"Accept state: {self._accept_state}")
        print(f"Reject state: {self._reject_state}")
        print("States and rules:")
        if len(self._states) == 0:
            print("  << no states >>")
        for name, state in self._states.items():
            print(f"State: {name}")
            for character, rule in self.get_state(name).rules.items():
                print(f"'{character}' : ", end='')
                rule.print_rule()

    def exportJSON(self):
        states_dict = {}
        for state_name, state in self._states.items():
            rules = state.get_rules_in_dictionary()
            states_dict[state_name] = {"rules": rules}

        machine = {"alphabet": _ALPHABET,
                   "start_state": self.start_state,
                   "accept_state": self._accept_state,
                   "reject_state": self._reject_state,
                   "tape": self._tape.get_dictionary(),
                   "states": states_dict}

        return json.dumps(machine)


    def importJSON(self, json_string):
        self.init_states()
        self.clear_tape()
        
        import_dict = json.loads(json_string)
        
        self._alphabet = import_dict["alphabet"]
        self._accept_state = import_dict["start_state"]        
        self._accept_state = import_dict["accept_state"]
        self._reject_state = import_dict["reject_state"]

        tape = import_dict["tape"]
        self._tape.put_dictionary(tape)

        states = import_dict["states"]
        
        for state_name, rules_dict in states.items():
            rules = rules_dict["rules"]
            for character, rule in rules.items():
                self.set_rule(state_name=state_name,
                              character=character,
                              write_char = rule["write_char"],
                              direction = rule["direction"],
                              next_state = rule["next_state"])

                
def main():
    argc = len(sys.argv)
    args = sys.argv[1:]
    
    jaturing = Jaturing()

    # If no args, start GUI application    
    if(argc == 1):
        launch(jaturing)

if __name__ == "__main__":
    main()
