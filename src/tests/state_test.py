import unittest

from jaturing import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_empty_state_is_created(self):
        self.assertIsNotNone(self.state)

    def test_set_and_get_rule_works(self):
        self.state.set_rule("a", "q1", "RIGHT", "B")
        rule = self.state.get_rule("a")
        self.assertEqual(str(rule), "q1;RIGHT;B")

    def test_rules_returns_all_rules(self):
        self.state.set_rule("a", "q1", "RIGHT", "B")
        self.state.set_rule("b", "q1", "RIGHT", "A")
        self.assertEqual(len(self.state.rules), 2)

    def test_nonexisting_character_returns_no_rule(self):
        self.assertEqual(self.state.get_rule('a'), None)

    def test_deleting_nonexisting_rule_returns_nothing(self):
        self.assertEqual(self.state.delete_rule('a'), None)

    def test_deleting_rule_deletes_rule(self):
        self.state.set_rule("a", "q1", "RIGHT", "B")
        self.state.delete_rule("a")
        rule = self.state.get_rule("a")
        self.assertEqual(str(rule), 'None')

    def test_get_rules_in_dictionary_returns_dictionary(self):
        self.state.set_rule("a", "q1", "RIGHT", "B")
        dict = self.state.get_rules_in_dictionary()
        self.assertEqual(dict, {'a': {'direction': 'RIGHT', 'next_state': 'B', 'write_char': 'q1'}})
