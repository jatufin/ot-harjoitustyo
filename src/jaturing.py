import array as arr
from jaturing_GUI import launch

_ALPHABET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Tape:
    def __init__(self, alphabet="", init_string="", negative_index_allowed=False):
        self._EMPTY = ord('.')
        if alphabet == "":
            self._alphabet = _ALPHABET
        else:
            self._alphabet = alphabet
        print(f"Aakkosto: {self._alphabet}")
        self._negative_index_allowed = negative_index_allowed

        if negative_index_allowed:
            self._left_tape = arr.array('B', [self._EMPTY])
        if init_string == "":
            init_list = [self._EMPTY]
        else:
            init_list = list(map(ord, init_string))
        self._right_tape = arr.array('B', init_list)
        self._head_position=0

    def get_head_position(self):
        return self._head_position
    
    def read(self):
        if self._head_position < 0:
            return chr(self._left_tape[abs(self._head_position)-1])
        else:
            return chr(self._right_tape[self._head_position])

    def write(self, character):
        if self._is_in_alphabet(character):
            self._write(character)
            
    def _write(self, character):
        if self._head_position < 0:
            self._left_tape[abs(self._head_position)-1] = ord(character)
        else:
            self._right_tape[self._head_position] = ord(character)

    def _is_in_alphabet(self, character):
        return character in self._alphabet

    def _str_in_alphabet(self, str):
        for c in str:
            if not self._is_in_alphabet(c):
                return False
        return True
    
    def move_left(self):
        ''' Returns false, if movement to left from 0 is not allowed '''
        if self._head_position == 0 and self._negative_index_allowed == False:
            return False
        if self._head_position < 1:
            if len(self._left_tape) == abs(self._head_position):
                self._left_tape.append(self._EMPTY)
        self._head_position -= 1

        return True

    def move_right(self):
        if self._head_position > -1:
            if len(self._right_tape) - 1 == self._head_position:
                self._right_tape.append(self._EMPTY)
        self._head_position += 1

    def _get_value(self, index):
        if index < 0:
            tape = self._left_tape
            index = abs(index) - 1
        else:
            tape = self._right_tape
        if index >= len(tape):
            return "."
        return chr(tape[index])
            
        
    def get_slice(self, length):
        """ Return a 2*length long slice from the tape from both sides of the head_position
        each element in the list is a tuple containing index number and value
        """
        return_list = []
        for i in range(self._head_position - length, self._head_position + length):
            return_list.append((i, self._get_value(i)))
            
        return return_list

    def _go_to(self, index):
        if index < 0 and self._negative_index_allowed == False:
            return
        
        if index == self._head_position:
            return
        
        if index < self._head_position:
            self.move_left()
        else:
            self.move_right()
        self._go_to(index)        
            
    def set_value(self, index, value):
        if index < 0 and self._negative_index_allowed == False:
            return
        
        head = self._head_position
        self._go_to(index)
        self.write(value)
        self._go_to(head)
 
    def __str__(self):
        return_string = ""
        if self._negative_index_allowed:
            for i in range(len(self._left_tape) - 1, -1, -1):
                if (self._head_position < 0 and
                   abs(self._head_position) - 1 == i):
                    return_string += '>'
                return_string += chr(self._left_tape[i])
        return_string += '|'                   # midpoint, or 0's cell on tape
            
        for i in range(0, len(self._right_tape)):
            if self._head_position == i:
                return_string += '>'
            return_string += chr(self._right_tape[i])

        return return_string.strip(chr(self._EMPTY))  # Strip empty cells

    
class Rule:
    def __init__(self, next_state=None, direction=None, write_char=None):
        self._next_state = next_state
        self._direction = direction
        self._write_char = write_char
        
    @property
    def next_state(self):
        return self._next_state

    @next_state.setter
    def set_next_state(self, state):
        self._next_state = state
        
    @property
    def direction(self, direction):
        ''' LEFT, RIGHT or STAY '''
        return self._direction

    @direction.setter
    def set_move_to(self, direction):
        self._direction = direction

    @property
    def write_char(self):
        return self._write_char

    @write_char.setter
    def set_write_char(self, write_char):
        self._write_char = write_char
    
    def print_rule(self):
        print(f"  Write '{self.write_char}', move tape {self.direction} and change state to '{self.next_state}'")

    def __str__(self):
        return f"{self.write_char};{self.direction};{self.next_state}"


class State:        
    def set_rule(self, character, next_state, direction, write_char):
        self._rules[character] = Rule(next_state, direction, write_char)

    @property
    def rules(self):
        return self._rules
        
class Jaturing:
    def __init__(self):
        self._alphabet = _ALPHABET
        self._tape = Tape(self._alphabet)
        self._states = {}
        self._current_state = None
        self._accept_state = None
        self._reject_state = None

    def add_state(self, name):
        self._states[name] = State()

    def get_state(self, name):
        return self._states[name]

    def set_rule(self, state_name,
                 character,
                 next_state,
                 direction,
                 write_char):
        if not get_state(state_name):
            self.add_state(state_name)
        self.get_state(state_name).set_rule(character,
                                            next_state,
                                            direction,
                                            write_char)

    def print_states_and_rules(self):
        print("STATUS")
        print(f"Tape: {str(self._tape)}")
        print(f"Current state: {self._current_state}")
        print(f"Accept state: {self._accept_state}")
        print(f"Reject state: {self._reject_state}")
        print("States and rules:")
        if len(self._states) == 0:
            print("  << no states >>")
        for name, state in self._states.items():
            print(f"State: {name}")
            for character, rule in self.get_state(name).rules:
                print(f"'{character}' : ", end='')
                rule.print_rule()
        
            
def main():
    jaturing = Jaturing()
    jaturing.print_states_and_rules()
    launch(jaturing)


if __name__ == "__main__":
    main()
