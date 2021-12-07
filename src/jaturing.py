

from ui.jaturing_GUI import launch
from tape import Tape
from rule import Rule
from state import State

_ALPHABET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"



class Jaturing:
    def __init__(self):
        self._alphabet = _ALPHABET
        self._tape = Tape(self._alphabet)
        self._states = {}
        self.current_state = None

        self._accept_state = "ACCEPT"
        self.add_state(self._accept_state)

        self._reject_state = "REJECT"
        self.add_state(self._reject_state)

    @property
    def states(self):
        return self._states

    @property
    def tape(self):
        return self._tape

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


def main():
    jaturing = Jaturing()
    launch(jaturing)


if __name__ == "__main__":
    main()
