import array as arr

class Tape:
    def __init__(self, negative_index_allowed=False):
        self._EMPTY = ord('.')
        self._negative_index_allowed = negative_index_allowed
        if negative_index_allowed:
            self._left_tape = arr.array('B', [self._EMPTY])
        self._right_tape = arr.array('B', [self._EMPTY])
        self._head_position=0

    def read(self):
        if self._head_position < 0:
            return chr(self._left_tape[abs(head_position)-1])
        else:
            return chr(self._right_tape[head_position])

    def write(self, character):
        if self._is_in_alphabet(character):
            self._write(character)
            
    def _write(self, character):
        if self._head_position < 0:
            self._left_tape[abs(self._head_position)-1] = ord(character)
        else:
            self._right_tape[self._head_position] = ord(character)

    def _is_in_alphabet(self, character):
        return character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    def move_left(self):
        if self._head_position == 0 and self._negative_index_allowed == False:
            return False
        if self._head_position < 1:
            if len(self._left_tape) == abs(self._head_position) - 1:
                _left_tape.append(self._EMPTY)
        self._head_position -= 1
        return True

    def move_right(self):
        if self._head_position > -1:
            if len(self._right_tape) - 1 == self._head_position:
                self._right_tape.append(self._EMPTY)
        self._head_position += 1

    def __str__(self):
        return_string = ""
        if self._negative_index_allowed:
            for i in range(len(self._left_tape) - 1, -1, -1):
                if self._head_position < 0 and abs(self._head_position) == i - 1:
                    return_string += '>'
                    s += chr(self._left_tape[i])
            return_string += '|'                   ## midpoint, or 0's cell on tape
            
        for i in range(0, len(self._right_tape)):
            if self._head_position == i:
                return_string += '>'
            return_string += chr(self._right_tape[i])

        return return_string.strip(chr(self._EMPTY)) ## Strip empty cells

class Jaturing:
    def __init__():
        pass

def main():
    tape = Tape()
    print("1:"+str(tape))
    tape.write('a')
    print("2:"+str(tape))
    tape.move_right()
    tape.write('a')
    print("3:"+str(tape))

if __name__ == "__main__": main()
