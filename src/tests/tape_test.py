import unittest

from jaturing import Tape

class TestTape(unittest.TestCase):
    def setUp(self):
        self.basic_tape = Tape()
        self.full_tape = Tape(negative_index_allowed=True)

    def test_basic_tape_is_empty_after_created(self):
        self.assertEqual(str(self.basic_tape), ">")
        
    def test_full_tape_is_empty_after_created(self):
        self.assertEqual(str(self.basic_tape), ">")
