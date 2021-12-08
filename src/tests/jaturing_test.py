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

    def test_export_json_generates_proper_json_string(self):
        correct_json = '{"alphabet": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "accept_state": "ACCEPT", "reject_state": "REJECT", "tape": {"head_position": 0, "negative_index_allowed": false, "left_tape": null, "right_tape": [46]}, "states": {"ACCEPT": {"rules": {}}, "REJECT": {"rules": {}}, "q0": {"rules": {"a": {"next_state": "q1", "direction": "RIGHT", "write_char": "A"}, "b": {"next_state": "q1", "direction": "RIGHT", "write_char": "B"}}}}}'
        
        self.jaturing.set_rule(state_name="q0",
                               character="a",
                               write_char="A",
                               direction="RIGHT",
                               next_state="q1")
        self.jaturing.set_rule(state_name="q0",
                               character="b",
                               write_char="B",
                               direction="RIGHT",
                               next_state="q1")
        self.assertEqual(self.jaturing.exportJSON(), correct_json)

    def test_import_json_produces_correct_machine(self):
        json_in = '{"alphabet": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "accept_state": "ACCEPT", "reject_state": "REJECT", "tape": {"head_position": 0, "negative_index_allowed": false, "left_tape": null, "right_tape": [46]}, "states": {"ACCEPT": {"rules": {}}, "REJECT": {"rules": {}}, "q0": {"rules": {"a": {"next_state": "q1", "direction": "RIGHT", "write_char": "A"}, "b": {"next_state": "q1", "direction": "RIGHT", "write_char": "B"}}}}}'
        self.jaturing.importJSON(json_in)
        json_out = self.jaturing.exportJSON()
        self.assertEqual(json_in, json_out)
