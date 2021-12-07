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

