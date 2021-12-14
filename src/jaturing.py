import sys
import json

from ui.jaturing_GUI import launch
from tape import Tape
from rule import Rule
from state import State

_ALPHABET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Jaturing:
    """Main class of the Turing's machine
    """
    def __init__(self):
        """ Constructor for the Jaturing class
        """
        self._alphabet = _ALPHABET
        self._tape = Tape(self._alphabet)

        self.init_states()
        self.halted = False
        
    @property
    def states(self):
        """ States of the Turing's machine

        Returns:
            Dictionary, where state names are keys, and values are State objects
        -------
        """
        return self._states

    @property
    def tape(self):
        """Returns the tape of the machine

        Returns:
             Tape object
        """
        return self._tape

    def init_states(self):
        """Initializes the machine states
        Initially the mahcine has always two halting states: ACCEPT and REJECT
        Additionally the machine has internal pointers to states, such as the
        self.current_state.
        """
        self._states = {}
        self.current_state = None
        self.start_state = None
        
        self._accept_state = "ACCEPT"
        self.add_state(self._accept_state)

        self._reject_state = "REJECT"
        self.add_state(self._reject_state)

    def add_state(self, name):
        """Add a state to the Turing's machine

        Args:
            name: String, name of the state
        """
        self._states[name] = State()
        
        if self.start_state == None:
            self.start_state = name

        if self.current_state == None:
            self.current_state = name

    def delete_state(self, name):
        """Delete the given state from the Turing's machine

        Args:
            name : String, name of the state
        """
        if not name in self._states:
            return
        if self.start_state == name:
            self.start_state = None        
        if self.current_state == name:
            self.current_state = None
        self.states.pop(name)

    def get_state(self, name):
        """Return the State object by the name of the state

        Args:
            name : String, name of the state

        Returns:
            State object
        """
        if name not in self._states:
            return None
        return self._states[name]

    def set_start_state_to_current(self):
        """Sets the current state value to the start state.
        """
        self.start_state = self.current_state
        
    def clear_tape(self):
        """Remove all characters from the tape
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

        Args:
            state_name : String, the state where the rule is applied
            character :  Single character string,. The rule is applied if this
                         character is read from the tape
            write_char : Single character string, which will be written to the
                         tape. It will overwrite the character, which had been
                         read from the tape
            direction :  String. To which direction the read/write head will be moved.
                         Allowed values are: LEFT and RIGHT
            next_state : String.The new state, the machine will be after this
                         rule has been applied
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

        Args:
            state : String, state name
            rule : Single character string
        """
        if not state in self._states:
            return
        self._states[state].delete_rule(rule)

    def is_accept_or_reject(self, state):
        """Return True if the given state is ACCEPT or REJECT state

        args:
            state : String containing the state name
        """
        return state in (self._accept_state, self._reject_state)

    def step_forward(self):
        """Perform one step of the machine applying rule from the current state
        """
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

    def return_to_start(self):
        """Return the machine to start state and read/write head
        to zero position
        """
        self.current_state = self.start_state
        self.tape.return_to_start()
        
    def halt(self):
        """Set the machine to halted state
        """
        self.halted = True

    def unhalt(self):
        """Remove the machine from halted state
        """
        self.halted = False

    def exportJSON(self):
        """Create JSON string, which contains all the states, rules, tape
        and current state of the machine
        """
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
        """Read the given JSON string and build the machine from it

        Args:
            json_string : String containing all the states, rules and tape of
                          the machine
        """
        self.init_states()
        self.clear_tape()
        
        import_dict = json.loads(json_string)
        
        self._alphabet = import_dict["alphabet"]
        self.start_state = import_dict["start_state"]
        self.current_state = self.start_state
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
