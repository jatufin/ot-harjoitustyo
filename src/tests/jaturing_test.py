import unittest

from jaturing import Jaturing


class TestJaturing(unittest.TestCase):
    def setUp(self):
        self.jaturing = Jaturing()

    def test_adding_state_adds_state(self):
        self.jaturing.add_state("q1")
        self.assertEqual(len(self.jaturing.states), 1)

    def test_getting_state_gets_state(self):
        self.jaturing.add_state("q1")
        self.assertIsNotNone(self.jaturing.get_state("q1"))

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
