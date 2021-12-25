import unittest

from rule import Rule


class TestRule(unittest.TestCase):
    def setUp(self):
        self.empty_rule = Rule()
        self.initialized_rule = Rule(next_state="q1",
                                     direction="RIGHT",
                                     write_char="A")
        
    def test_empty_rule_is_created_right(self):
        self.assertEqual(self.empty_rule._next_state, None)
        self.assertEqual(self.empty_rule._direction, None)
        self.assertEqual(self.empty_rule._write_char, None)

    def test_initialized_rule_is_created_right(self):
        self.assertEqual(self.initialized_rule.next_state, "q1")
        self.assertEqual(self.initialized_rule.direction, "RIGHT")        
        self.assertEqual(self.initialized_rule.write_char, "A")                

    def test_next_state_setter_works(self):
        self.empty_rule.next_state = "q2"
        self.assertEqual(self.empty_rule._next_state, "q2")

    def test_direction_setter_works(self):
        self.empty_rule.direction = "LEFT"
        self.assertEqual(self.empty_rule.direction, "LEFT")

    def test_write_char_setter_works(self):
        self.empty_rule.write_char = "B"
        self.assertEqual(self.empty_rule.write_char, "B")

    def test_cast_to_string_works(self):
        rule_as_string = str(self.initialized_rule)
        self.assertEqual(rule_as_string, "A;RIGHT;q1")
