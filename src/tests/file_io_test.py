import unittest

from jaturing import Jaturing
from file_io import FileIO


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.jaturing = Jaturing()
        self.io = FileIO(self.jaturing)

        
    def test_export_json_generates_proper_json_string(self):
        correct_json = '{"alphabet": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "start_state": "ACCEPT", "accept_state": "ACCEPT", "reject_state": "REJECT", "tape": {"head_position": 0, "negative_index_allowed": false, "left_tape": [46], "right_tape": [97]}, "states": {"ACCEPT": {"rules": {}}, "REJECT": {"rules": {}}, "q0": {"rules": {"a": {"next_state": "q1", "direction": "RIGHT", "write_char": "A"}, "b": {"next_state": "q1", "direction": "RIGHT", "write_char": "B"}}}}}'

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
        self.jaturing.tape.set_value(0,'a')
        
        self.assertEqual(self.jaturing.io.exportJSON(), correct_json)

        
    def test_import_json_produces_correct_machine(self):
        json_in = '{"alphabet": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "start_state": "ACCEPT", "accept_state": "ACCEPT", "reject_state": "REJECT", "tape": {"head_position": 0, "negative_index_allowed": false, "left_tape": [46], "right_tape": [97]}, "states": {"ACCEPT": {"rules": {}}, "REJECT": {"rules": {}}, "q0": {"rules": {"a": {"next_state": "q1", "direction": "RIGHT", "write_char": "A"}, "b": {"next_state": "q1", "direction": "RIGHT", "write_char": "B"}}}}}'
        self.jaturing.io.importJSON(json_in)
        json_out = self.jaturing.io.exportJSON()
        self.assertEqual(json_in, json_out)

    def test_get_correct_file_types_and_extensions(self):
        result = self.io.getFileTypesAndExtensions()
        self.assertEqual(len(result), 1)
        self.assertEqual(result["json"], "JSON")

    def test_get_correct_file_formats(self):
        result = self.io.getFileformats()
        self.assertEqual(result[0], ("JSON files", "*.json"))

    def test_load_and_save_works(self):
        json_in = '{"alphabet": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", "start_state": "ACCEPT", "accept_state": "ACCEPT", "reject_state": "REJECT", "tape": {"head_position": 0, "negative_index_allowed": false, "left_tape": [46], "right_tape": [97]}, "states": {"ACCEPT": {"rules": {}}, "REJECT": {"rules": {}}, "q0": {"rules": {"a": {"next_state": "q1", "direction": "RIGHT", "write_char": "A"}, "b": {"next_state": "q1", "direction": "RIGHT", "write_char": "B"}}}}}'

        self.jaturing.io.importJSON(json_in)
        filename = "test.json"
        self.jaturing.io.saveFile(filename)

        second_machine = Jaturing()
        second_machine.io.loadFile(filename)
        json_out = second_machine.io.exportJSON()
        
        self.assertEqual(json_in, json_out)
        
