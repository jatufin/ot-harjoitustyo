import array as arr

class Tape:
    def __init__(self, negative_index=False):
        self._EMPTY = ord('.')
        self._negative_index = negative_index
        if negative_index:
            self._left_tape = arr.array('B', [self._EMPTY])
        self._right_tape = arr.array('B', [self._EMPTY])
        self._head_position=0

    def read(self):
        if head_position < 0:
            return chr(self._left_tape[abs(head_position)-1])
        else:
            return chr(self._right_tape[head_position])

    def write(self, caharacter):
        if self._is_in_alphabet(character):
            self._write(character)
            
    def _write(self, character):
        if head_position < 0:
            self._left_tape[abs(head_position)-1] = character
        else:
            self._right_tape[head_position] = character                   

    def _is_in_alphabet(self, character):
        return character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    def move_left(self):
        if self._head_position < 1:
            i = abs(self._head_position)
            if len(self._left_tape) < i:
                _left_tape.append(self._EMPTY)
        self._head_position -= 1
                
                

class Jaturing:
    def __init__():
        

def main():
    print("Foo")

if __name__ == "__main__": main()
