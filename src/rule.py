class Rule:
    """ State object contains rules for operations, which should
    be done, when certain character is read from the tape
    The _next_state property contains rule name as a string,
    which is a key in State._rules.
    """
    def __init__(self, write_char=None, direction=None, next_state=None):
        self._next_state = next_state
        self._direction = direction
        self._write_char = write_char

    @property
    def next_state(self):
        return self._next_state

    @next_state.setter
    def next_state(self, state):
        self._next_state = state

    @property
    def direction(self):
        ''' LEFT, RIGHT or STAY '''
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    @property
    def write_char(self):
        return self._write_char

    @write_char.setter
    def write_char(self, write_char):
        self._write_char = write_char

    def print_rule(self):
        print(f"  Write '{self.write_char}', move tape {self.direction} and change state to '{self.next_state}'")

    def __str__(self):
        return f"{self.write_char};{self.direction};{self.next_state}"
