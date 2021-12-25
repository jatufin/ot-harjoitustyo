import unittest

from jaturing import Jaturing


class TestJaturing(unittest.TestCase):
    def setUp(self):
        self.jaturing = Jaturing()

    def test_adding_state_adds_state(self):
        self.jaturing.add_state("q1")
        self.assertEqual(len(self.jaturing.states), 3)

    def test_getting_state_gets_state(self):
        self.jaturing.add_state("q1")
        self.assertIsNotNone(self.jaturing.get_state("q1"))

    def test_init_states_initializes_states(self):
        self.jaturing.init_states()
        self.assertEqual(len(self.jaturing._states), 2)

    def test_clear_tape_clears_states(self):
        self.jaturing.clear_tape()
        self.assertEqual(str(self.jaturing._tape), "|>")
    
    def test_default_accept_state_is_recognized(self):
        self.assertTrue(self.jaturing.is_accept_or_reject("ACCEPT"))

    def test_default_reject_state_is_recognized(self):
        self.assertTrue(self.jaturing.is_accept_or_reject("REJECT"))
        
    def test_setting_rule_sets_rule(self):
        self.jaturing.add_state("q1")
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.assertEqual(str(self.jaturing.get_state("q1").rules["a"]),
                         "A;RIGHT;q2")

    def test_setting_rule_for_new_state_sets_rule(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.assertEqual(str(self.jaturing.get_state("q1").rules["a"]),
                         "A;RIGHT;q2")

    def test_tape_returns_tape(self):
        self.assertIsNotNone(self.jaturing.tape)

    def test_delete_nonexisting_state_deletes_nothing(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        before = str(self.jaturing)
        self.jaturing.delete_state('q2')
        after = str(self.jaturing)
        self.assertEqual(before, after)

    def test_deleting_state_deletes_state(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.jaturing.delete_state('q1')
        self.assertTrue("q1" not in self.jaturing._states)
        
    def test_deleting_current_state_sets_current_state_to_none(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.jaturing.current_state = "q1"
        self.jaturing.delete_state('q1')
        self.assertEqual(self.jaturing.current_state, None)

    def test_deleting_start_state_sets_start_state_to_none(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.jaturing.start_state = "q1"
        self.jaturing.delete_state('q1')
        self.assertEqual(self.jaturing.start_state, None)

    def test_setting_start_state_to_current_state_works(self):
        self.jaturing.start_state = "ACCEPT"
        self.jaturing.current_state = "REJECT"
        self.jaturing.set_start_state_to_current()
        self.assertEqual(self.jaturing.start_state, "REJECT")

    def test_deleting_existing_rule_deletes_rule(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.jaturing.delete_rule('q1', 'a')
        self.assertNotIn ("a", str(self.jaturing.get_state("q1").rules))

    def test_deleteing_rule_for_nonexistent_state_deletes_nothing(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        before = str(self.jaturing)
        self.jaturing.delete_rule('q2', 'a')
        after = str(self.jaturing)
        self.assertEqual(before, after)

    def test_step_forward_changes_state_correctlt(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.jaturing.set_rule(state_name="q2",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q2")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(0, 'a')
        self.jaturing.step_forward()
        self.assertEqual(self.jaturing.current_state, "q2")

    def test_step_forward_to_accept_state_halts(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="ACCEPT")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(0, 'a')
        self.jaturing.step_forward()
        self.jaturing.step_forward()        
        self.assertTrue(self.jaturing.halted)

    def test_step_forward_to_reject_state_halts(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="REJECT")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(0, 'a')
        self.jaturing.step_forward()
        self.jaturing.step_forward()        
        self.assertTrue(self.jaturing.halted)

    def test_step_forward_without_rule_halts(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="REJECT")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(0, 'b')
        self.jaturing.step_forward()
        self.jaturing.step_forward()        
        self.assertTrue(self.jaturing.halted)

    def test_step_forward_with_move_right_moves_right(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="REJECT")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(0, 'a')
        self.jaturing.step_forward()
        self.assertEqual(self.jaturing.tape._head_position, 1)

    def test_step_forward_with_move_left_moves_left(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="LEFT",
                               next_state="REJECT")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(1, 'a')
        self.jaturing.tape._head_position = 1
        self.jaturing.step_forward()
        self.assertEqual(self.jaturing.tape._head_position, 0)

    def test_step_forward_with_unknow_direction_rule_moves_nothing(self):
        self.jaturing.set_rule(state_name="q1",
                               character="a",
                               write_char="A",
                               direction="X",
                               next_state="REJECT")
        self.jaturing.current_state = "q1"
        self.jaturing.tape.set_value(1, 'a')
        self.jaturing.tape._head_position = 1
        self.jaturing.step_forward()
        self.assertEqual(self.jaturing.tape._head_position, 1)

    def test_return_to_start_returns_to_start(self):
        self.jaturing.start_state = "q0"
        self.jaturing.current_state = "q1"
        self.jaturing.tape._head_position = 5
        self.jaturing.return_to_start()
        self.assertEqual(self.jaturing.current_state, "q0")
        self.assertEqual(self.jaturing.tape._head_position, 0)

    def test_halt_halts(self):
        self.jaturing.halt()
        self.assertTrue(self.jaturing.halted)
        
    def test_unhalt_unhalts(self):
        self.jaturing.halt()
        self.jaturing.unhalt()
        self.assertFalse(self.jaturing.halted)        

    def print_states_and_rules(self):
        self.assertTrue(True)

