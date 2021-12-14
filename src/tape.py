import array as arr

_ALPHABET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Tape:
w    """ Tape object containse the actual tape arrays and head position.
    If negative head is allowed to move to the left from
    0 position, it is indicted in _negative_index_allowed propert
    Left side and right side tapes from the 0 position are stored to
    separate arrays.

    Attribute:
        alphabet : String containing all allowed characters
        init_string : String, which will be written to tape for
                      initial value
        negative_index_allowed: Boolean, which tells if head can
                                move to the left from zero
    """
    def __init__(self, alphabet="",
                 init_string="",
                 negative_index_allowed=False):
        """ Tape object containse the actual tape arrays and head position.

        Args:
            alphabet : String containing all allowed characters
            init_string : String, which will be written to tape for
                          initial value
            negative_index_allowed: Boolean, which tells if head can
                                    move to the left from zero
        """
        self._empty = ord('.')
        if alphabet == "":
            self._alphabet = _ALPHABET
        else:
            self._alphabet = alphabet
            
        self._negative_index_allowed = negative_index_allowed

        if negative_index_allowed:
            self._left_tape = arr.array('B', [self._empty])
        if init_string == "":
            init_list = [self._empty]
        else:
            init_list = list(map(ord, init_string))
        self._right_tape = arr.array('B', init_list)
        self._head_position = 0

    def get_head_position(self):
        """Returns the current position of the read/write head
        """
        return self._head_position

    def set_alphabet(self, alphabet):
        """Sets the alphabet in used

        Args:
            alphabet : String containing the caracters of the alphabet
        """
        self._alphabet = alphabet
        
    def read(self):
        """Returns the character in the tape on the current position
        of the read/write head.
        """
        if self._head_position < 0:
            return chr(self._left_tape[abs(self._head_position)-1])
        else:
            return chr(self._right_tape[self._head_position])

    def write(self, character):
        """Writes given character to the tape, on the current position
        of the read/write head

        Args:
            character : String, from which first character will be
                        written on the tape
        """
        if self._is_in_alphabet(character):
            self._write(character)

    def _write(self, character):
        """Helper function for the self.write() method
        converts a character to integer for the tape array
        of the read/write head.

        Args:
            character : String, from which first character will be
                        written on the tape
        """
        if self._head_position < 0:
            self._left_tape[abs(self._head_position)-1] = ord(character)
        else:
            self._right_tape[self._head_position] = ord(character)

    def _is_in_alphabet(self, character):
        """Returns True, if the given character is in the alphabet of
        the tape.

        Args:
            character : String, from which first character is used

        """
        return character in self._alphabet

    def _str_in_alphabet(self, string):
        """Returns True, if all characters in the given string are in
        the alphabet of the tape.

        Args:
            string : String, from which first character is used

        """
        for character in string:
            if not self._is_in_alphabet(character):
                return False
        return True

    def move_left(self):
        """Moves the write/head to the left by decreasing its value.
        The method checks if movement left from 0 is allowed.
        New empty values are added to the tape array, if needed.
        """
        if (self._head_position == 0 and
            not self._negative_index_allowed):
            return False
        if self._head_position < 1:
            if len(self._left_tape) == abs(self._head_position):
                self._left_tape.append(self._empty)
        self._head_position -= 1

        return True

    def move_right(self):
        """Moves the write/head to the left by increasing its value.
        The method checks if movement left from 0 is allowed.
        New empty values are added to the tape array, if needed.
        """
        if self._head_position > -1:
            if len(self._right_tape) - 1 == self._head_position:
                self._right_tape.append(self._empty)
        self._head_position += 1

    def _get_value(self, index):
        """Returns the value on the tape on given index

        Args:
            index : Integer for the position which should be read
                    from the tape
        """
        if index < 0:
            if self._negative_index_allowed:
                tape = self._left_tape
                index = abs(index) - 1
            else:
                return "."
        else:
            tape = self._right_tape
        if index >= len(tape):
            return "."
        return chr(tape[index])

    def get_slice(self, length):
        """ Return a 2*length long slice from the tape from both sides of the
        head_position each element in the list is a tuple containing index
        number and value. This method is meant to be used by the user interface.

        Args:
            length : Integer for the half slice length
        """
        return_list = []
        for i in range(self._head_position - length, self._head_position + length):
            value = self._get_value(i)
            return_list.append((i, value))

        return return_list

    def _go_to(self, index):
        """Moves the read/write head to the given position
        The method checks if movement left from 0 is allowed.
        
        Args:
            index : The new position of the head
        """
        if (index < 0 and
            not self._negative_index_allowed):
            return

        if index == self._head_position:
            return

        if index < self._head_position:
            self.move_left()
        else:
            self.move_right()
        self._go_to(index)

    def set_value(self, index, value):
        """Sets the value on the tape on given index
        The method checks if movement left from 0 is allowed.
        
        Args:
            index : Integer position where the value will be written
            value : Single character string, which will be written
        """
        if (index < 0 and
            not self._negative_index_allowed):
            return

        head = self._head_position
        self._go_to(index)
        self.write(value)
        self._go_to(head)

    def __str__(self):
        """String representation of the tape
        Zero position is indicated with pipe symbol '|'
        Read/write head position is indicated with greater than symbol '>'
        Empty cells are indicated with periods '.'
        Empty cells from left and right are stripped from the output.

        Returns:
            String representing the tape
        """
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

        return return_string.strip(chr(self._empty))  # Strip empty cells

    def get_dictionary(self):
        """ Generate a dictionary object from the tape.
        This is meant to be used by the exportJSON  method of the Jaturing
        main class

        Returns:
            String with JSON data
        """
        return {"head_position": self._head_position,
                "negative_index_allowed": self._negative_index_allowed,
                "left_tape": self._left_tape.tolist() if self._negative_index_allowed else None,
                "right_tape": self._right_tape.tolist()}

    def put_dictionary(self, tape_dict):
        """ Populate a tape from a dictionary object
        This is meant to be used by the exportJSON  method of the Jaturing
        main class

        Args:
            String with JSON data
        """
        self._head_position = tape_dict["head_position"]
        self.negative_index_allowed = tape_dict["negative_index_allowed"]
        if tape_dict["left_tape"]:
            self._left_tape = arr.array('B', tape_dict["left_tape"])
        self._right_tape = arr.array('B', tape_dict["right_tape"])
