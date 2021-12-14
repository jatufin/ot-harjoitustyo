from rule import Rule


class State:
    """ State object doesn't know its own name, which is a key
    Jaturing._states dictionary. Essentially State contains
    dictionary, which has the rules which will be applied when
    the machine is in this state
    """
    def __init__(self):
        """Constructor of the class
        """
        self._rules = {}

    def set_rule(self, character, write_char, direction, next_state):
        """Create or update an existing rule for this state

        Args:
            character : Single character string. If this character
                        is read from the tape, when the machine is
                        is in this state, will this rule be applied
            write_char : This character will be written on the tape,
                         and it will overwrite the old value
            direction : Direction, where the read/write head of the
                        tape will be moved one step. LEFT and RIGHT
                        are allowed
            next_state : The new state the machine will have, after
                         this rule has been applied
        """
        self._rules[character] = Rule(write_char, direction, next_state)

    def get_rule(self, character):
        """Get the rule which will be applied if this character is read
        when the machine is in this state

        Args:
            character : Single character string

        Returns:
            Rule class object
        """
        if not character in self._rules:
            return None
        return self._rules[character]

    def delete_rule(self, rule):
        """Delete the rule which would had been applied when this character
        was read had the machine been in this state

        Args:
            character : Single character string
        """
        if not rule in self._rules:
            return
        self._rules.pop(rule)

    def get_rules_in_dictionary(self):
        """Generate dictionary object from all rules and return for use
        in the exportJSON  method of the Jaturing main class

        Returns:
            Dictionary which can be used to produce JSON for the state
        """
        dict = {}
        for character, rule in self._rules.items():
            dict[character] = {"next_state": rule.next_state,
                               "direction": rule.direction,
                               "write_char": rule.write_char}
        return dict


    @property
    def rules(self):
        """Returns all the rules this state has

        Returns:
            Dictionary, where keys are characters and values Rule objects
        """
        return self._rules
