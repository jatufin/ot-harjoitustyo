import unittest

from jaturing import Tape


class TestTape(unittest.TestCase):
    def setUp(self):
        self.basic_tape = Tape()  # Only positive indexes
        self.full_tape = Tape(negative_index_allowed=True)  # Positive and negative indexes
        self.basic_tape_initialized = Tape(init_string="abc")
        self.full_tape_initialized = Tape(init_string="abc",
                                          negative_index_allowed=True)

    def test_get_head_position_returns_value(self):
        self.assertEqual(self.basic_tape.get_head_position(), 0)
    
    def test_init_with_custom_alphabet_works(self):
        tape = Tape(alphabet="1234567890")
        self.assertEqual(str(tape), "|>")
        
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

    def test_move_left_on_negative_with_full_tape_works(self):
        self.full_tape.move_left()
        self.full_tape.move_left()
        self.assertEqual(str(self.full_tape), ">..|")

    def test_move_left_and_right_in_negative_works(self):
        self.full_tape.move_left()
        self.full_tape.move_left()
        self.full_tape.move_left()
        self.full_tape.move_right()
        self.full_tape.move_left()
        self.assertEqual(str(self.full_tape), ">...|")

    def test_move_right_and_left_in_positive_works(self):
        self.full_tape.move_right()
        self.full_tape.move_right()        
        self.full_tape.move_left()
        self.full_tape.move_right()
        self.assertEqual(str(self.full_tape), "|..>")
        
    def test_read_from_empty_tape_returns_colon(self):
        self.assertEqual(self.basic_tape.read(), ".")

    def test_read_from_initialized_tape_returns_letter_a(self):
        self.assertEqual(self.basic_tape_initialized.read(), "a")

    def test_write_and_read_on_right_side_works(self):
        self.full_tape.write("A")
        self.assertEqual(self.full_tape.read(), "A")
        self.basic_tape_initialized.write("B")
        self.assertEqual(str(self.basic_tape_initialized), "|>Bbc")
        
    def test_write_and_read_on_left_side_works(self):
        self.full_tape.move_left()
        self.full_tape.write("A")
        self.assertEqual(self.full_tape.read(), "A")
        self.full_tape_initialized.move_left()
        self.full_tape_initialized.write("B")
        self.assertEqual(str(self.full_tape_initialized), ">B|abc")
        
    def test_checking_if_valid_character_is_in_aplhabet_works(self):
        self.assertTrue(self.basic_tape._is_in_alphabet("A"))

    def test_checking_if_invalid_character_is_in_aplhabet_works(self):
        self.assertFalse(self.basic_tape._is_in_alphabet("!"))                        

    def test_checking_if_valid_string_is_in_aplhabet_works(self):
        self.assertTrue(self.basic_tape._str_in_alphabet("ABC"))

    def test_checking_if_invalid_string_is_in_aplhabet_works(self):
        self.assertFalse(self.basic_tape._str_in_alphabet("A!C"))                        

    def test_write_with_invalid_character_does_not_write(self):
        self.basic_tape_initialized.write("!")
        self.assertEqual(str(self.basic_tape_initialized), "|>abc")

    def test_get_value_from_empty_returns_period(self):
        self.assertEqual(self.full_tape._get_value(-5), ".")
        self.assertEqual(self.full_tape._get_value(5), ".")                         

    def test_get_value_from_intialized_returns_correct_value(self):
        self.assertEqual(self.full_tape_initialized._get_value(1), "b")

    def test_get_value_from_intialized_returns_correct_empty_value(self):
        self.assertEqual(self.full_tape_initialized._get_value(-3), ".")

    def test_get_slice_returns_correct_list(self):
        slice = self.full_tape_initialized.get_slice(3)
        self.assertEqual(slice, [(-3, "."), (-2, "."), (-1, "."), (0, "a"), (1, "b"), (2, "c")])

    def test_go_to_goes_to_correct_positive_position(self):
        self.basic_tape._go_to(2)
        self.assertEqual(str(self.basic_tape), "|..>")

    def test_go_to_negative_does_nothing_when_not_allowed(self):
        self.basic_tape._go_to(-2)
        self.assertEqual(str(self.basic_tape), "|>")
        
    def test_go_to_goes_to_correct_negative_position(self):
        self.full_tape._go_to(-2)
        self.assertEqual(str(self.full_tape), ">..|")

    def test_set_value_sets_correct_value_with_positive_index(self):
        self.basic_tape.set_value(2, "A")
        self.assertEqual(str(self.basic_tape), "|>..A")

    def test_set_value_does_nothing_when_not_allowed(self):
        self.basic_tape.set_value(-2, "A")
        self.assertEqual(str(self.basic_tape), "|>")
    def test_set_value_sets_correct_value_with_negative_index(self):
        self.full_tape.set_value(-2, "A")
        self.assertEqual(str(self.full_tape), "A.|>")
