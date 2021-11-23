import unittest

from jaturing import Tape

class TestTape(unittest.TestCase):
    def setUp(self):
        self.basic_tape = Tape()
        self.full_tape = Tape(negative_index_allowed=True)
        self.basic_tape_initialized = Tape(init_string="abc")
        self.full_tape_initialized = Tape(init_string="abc",negative_index_allowed=True)

    def test_basic_tape_is_empty_after_created(self):
        self.assertEqual(str(self.basic_tape), "|>")
        
    def test_full_tape_is_empty_after_created(self):
        self.assertEqual(str(self.full_tape), "|>")

    def test_basic_tape_is_initialized(self):
        self.assertEqual(str(self.basic_tape_initialized), "|>abc")
        
    def test_full_tape_is_initialized(self):
        self.assertEqual(str(self.full_tape_initialized), "|>abc")

    def test_move_right_works_with_empty_tape(self):
        self.basic_tape.move_right()
        self.assertEqual(str(self.basic_tape), "|.>")        

    def test_move_left_on_zero_with_basic_tape_returns_false(self):
        result = self.basic_tape.move_left()
        self.assertEqual(result, False)

    def test_move_left_on_zero_with_full_tape_returns_true(self):
        result = self.full_tape.move_left()
        self.assertEqual(result, True)

    def test_move_left_on_zero_with_full_tape_works(self):
        self.full_tape.move_left()
        self.assertEqual(str(self.full_tape), ">.|")
        
