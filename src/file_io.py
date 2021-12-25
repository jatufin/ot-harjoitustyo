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

    def exportJSON(self):
        """Create JSON string, which contains all the states, rules, tape
        and current state of the machine
        """
        states_dict = {}
        for state_name, state in self._machine._states.items():
            rules = state.get_rules_in_dictionary()
            states_dict[state_name] = {"rules": rules}

        machine_dict = {"alphabet": _ALPHABET,
                        "start_state": self._machine.start_state,
                        "accept_state": self._machine._accept_state,
                        "reject_state": self._machine._reject_state,
                        "tape": self._machine._tape.get_dictionary(),
                        "states": states_dict}

        return json.dumps(machine_dict)


    def importJSON(self, json_string):
        """Read the given JSON string and build the machine from it

        Args:
            json_string : String containing all the states, rules and tape of
                          the machine
        """
        self._machine.init_states()
        self._machine.clear_tape()

        import_dict = json.loads(json_string)

        self._machine._alphabet = import_dict["alphabet"]
        self._machine.start_state = import_dict["start_state"]
        self._machine.current_state = self._machine.start_state
        self._machine._accept_state = import_dict["accept_state"]
        self._machine._reject_state = import_dict["reject_state"]

        tape = import_dict["tape"]
        self._machine._tape.put_dictionary(tape)

        states = import_dict["states"]

        for state_name, rules_dict in states.items():
            rules = rules_dict["rules"]
            for character, rule in rules.items():
                self._machine.set_rule(state_name=state_name,
                                       character=character,
                                       write_char = rule["write_char"],
                                       direction = rule["direction"],
                                       next_state = rule["next_state"])

    
    def loadFile(self, filename):
        """Save file. The format is detected from the file extension

        Args:
            filename : String.
        """
        import_string = None

        with open(filename, "r") as file:
            import_string = file.read()

        extension = filename.split(".")[-1]
        type = self.getFileTypesAndExtensions()[extension]

        if import_string:
            if type == "JSON":
                self.importJSON(import_string)

    def saveFile(self, filename):
        """Save file. The format is detected from the file extension

        Args:
            filename : String.
        """     
        extension = filename.split(".")[-1]
        type = self.getFileTypesAndExtensions()[extension]

        export_string = None
        
        if type == "JSON":
            export_string = self.exportJSON()

        if export_string:
            with open(filename, "w") as file:
                file.write(export_string)

    def getFileTypesAndExtensions(self):
        """Get dictionary containing extensions and corresponding
        file format identifier

        Returns:
            A dictionary
        """

        return_dict = {}
        return_dict["json"] = "JSON"
        
        return return_dict

    def getFileformats(self):
        """Get a list of file formats and extensions with
        preceeding asterisk wildcards (e.g. ("TXT", "*.txt") ) for use
        with file dialogs. Empty wildcard ("All files", "*.*") is added

        Returns:
            A list of tuples
        """

        return_list = []

        types_and_extensions = self.getFileTypesAndExtensions()

        for extension, type in types_and_extensions.items():
            description = f"{type} files"
            filter = f"*.{extension}"

            return_list.append((description, filter))

        return_list.append(("All files", "*.*"))
        
        return return_list
