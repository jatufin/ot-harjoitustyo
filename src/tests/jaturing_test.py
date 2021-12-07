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
