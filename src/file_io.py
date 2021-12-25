import json


_ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class FileIO:
    """Contains functionality for imprting and exporting Jaturing
    object to different formats and save and load the onto a disk
    """
    def __init__(self, machine):
        """Constructor for the FileIO class

        Args:
            machine : Jaturing object
        """
        self._machine = machine

    def export_json(self):
        """Create JSON string, which contains all the states, rules, tape
        and current state of the machine
        """
        states_dict = {}
        for state_name, state in self._machine.states.items():
            rules = state.get_rules_in_dictionary()
            states_dict[state_name] = {"rules": rules}

        machine_dict = {"alphabet": _ALPHABET,
                        "start_state": self._machine.start_state,
                        "accept_state": self._machine.accept_state,
                        "reject_state": self._machine.reject_state,
                        "tape": self._machine.tape.get_dictionary(),
                        "states": states_dict}

        return json.dumps(machine_dict)

    def import_json(self, json_string):
        """Read the given JSON string and build the machine from it

        Args:
            json_string : String containing all the states, rules and tape of
                          the machine
        """
        self._machine.init_states()
        self._machine.clear_tape()

        import_dict = json.loads(json_string)

        self._machine.alphabet = import_dict["alphabet"]
        self._machine.start_state = import_dict["start_state"]
        self._machine.current_state = self._machine.start_state
        self._machine.accept_state = import_dict["accept_state"]
        self._machine.reject_state = import_dict["reject_state"]

        tape = import_dict["tape"]
        self._machine.tape.put_dictionary(tape)

        states = import_dict["states"]

        for state_name, rules_dict in states.items():
            rules = rules_dict["rules"]
            for character, rule in rules.items():
                self._machine.set_rule(state_name=state_name,
                                       character=character,
                                       write_char=rule["write_char"],
                                       direction=rule["direction"],
                                       next_state=rule["next_state"])

    def load_file(self, filename):
        """Save file. The format is detected from the file extension

        Args:
            filename : String.
        """
        import_string = None

        with open(filename, "r", encoding="utf-8") as file:
            import_string = file.read()

        extension = filename.split(".")[-1]
        file_type = self.get_file_types_and_extensions()[extension]

        if import_string:
            if file_type == "JSON":
                self.import_json(import_string)

    def save_file(self, filename):
        """Save file. The format is detected from the file extension

        Args:
            filename : String.
        """
        extension = filename.split(".")[-1]
        file_type = self.get_file_types_and_extensions()[extension]

        export_string = None

        if file_type == "JSON":
            export_string = self.export_json()

        if export_string:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(export_string)

    def get_file_types_and_extensions(self):
        """Get dictionary containing extensions and corresponding
        file format identifier

        Returns:
            A dictionary
        """

        return_dict = {}
        return_dict["json"] = "JSON"

        return return_dict

    def get_file_formats(self):
        """Get a list of file formats and extensions with
        preceeding asterisk wildcards (e.g. ("TXT", "*.txt") ) for use
        with file dialogs. Empty wildcard ("All files", "*.*") is added

        Returns:
            A list of tuples
        """

        return_list = []

        types_and_extensions = self.get_file_types_and_extensions()

        for extension, file_type in types_and_extensions.items():
            description = f"{file_type} files"
            file_filter = f"*.{extension}"

            return_list.append((description, file_filter))

        return_list.append(("All files", "*.*"))

        return return_list
