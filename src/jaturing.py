import sys
import json

from ui.jaturing_GUI import launch
from tape import Tape
from rule import Rule
from state import State

_ALPHABET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Jaturing:
    def __init__(self):
        self._alphabet = _ALPHABET
        self._tape = Tape(self._alphabet)

        self.init_states()
        
    @property
    def states(self):
        return self._states

    @property
    def tape(self):
        return self._tape

    def init_states(self):
        self._states = {}
        self.current_state = None

        self._accept_state = "ACCEPT"
        self.add_state(self._accept_state)

        self._reject_state = "REJECT"
        self.add_state(self._reject_state)
        
    def add_state(self, name):
        self._states[name] = State()

    def delete_state(self, name):
        if not name in self._states:
            return
        if self.current_state == name:
            self.current_state = None
        self.states.pop(name)

    def get_state(self, name):
        if not name in self._states:
            return None
        return self._states[name]

    def clear_tape(self):
        self._tape = Tape(self._alphabet)        
            
    def set_rule(self, state_name,
                 character,
                 write_char,
                 direction,
                 next_state
                 ):
        if not self.get_state(state_name):
            self.add_state(state_name)
        self.get_state(state_name).set_rule(character=character,
                                            write_char=write_char,
                                            direction=direction,
                                            next_state=next_state
                                            )

    def delete_rule(self, state, rule):
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
            print("Reject states was reached")
            return
        
        if self.current_state == self._accepm_state:
            print("Accept states was reached")
            return
        
        print(f"Current state is: {self.current_state}")
        print(f"From tape was read: {character}")
        if not rule:
            print("No rule was found for")
            return
        print(f"Write: {rule.write_char}")
        self.tape.write(rule.write_char)

        print(f"Move tape: {rule.direction}")
        if rule.direction == "RIGHT":
            self.tape.move_right()
        elif rule.direction == "LEFT":
            self.tape.move_left()

        print(f"Change state to: {rule.next_state}")
        self.current_state = rule.next_state

    def print_states_and_rules(self):
        print("STATUS")
        print(f"Tape: {str(self._tape)}")
        print(f"Current state: {self.current_state}")
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

    if(argc == 1):
        launch(jaturing)

    print(f"Command line args: {args} ")

    jaturing.set_rule(state_name="q0",
                      character="a",
                      write_char="A",
                      direction="RIGHT",
                      next_state="q1")
    jaturing.set_rule(state_name="q0",
                      character="b",
                      write_char="B",
                      direction="RIGHT",
                      next_state="q1")    



    jaturing.print_states_and_rules()

    print("EXPORT")
    json_string = jaturing.exportJSON()
    print("Exportstring:")
    print(json_string)

    print("CLEAR")
    jaturing.init_states()
    jaturing.clear_tape()
    jaturing.print_states_and_rules()

    print("IMPORT")
    jaturing.importJSON(json_string)
    jaturing.print_states_and_rules()

    print("NEW EXPORT")
    json_string = jaturing.exportJSON()
    print("Exportstring:")
    print(json_string)
    
    



if __name__ == "__main__":
    main()
