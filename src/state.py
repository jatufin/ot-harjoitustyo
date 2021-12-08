from rule import Rule


class State:
    """ State object doesn't know its own name, which is a key
    Jaturing._states dictionary
    """
    def __init__(self):
        self._rules = {}

    def set_rule(self, character, write_char, direction, next_state):
        self._rules[character] = Rule(write_char, direction, next_state)

    def get_rule(self, character):
        if not character in self._rules:
            return None
        return self._rules[character]

    def delete_rule(self, rule):
        if not rule in self._rules:
            return
        self._rules.pop(rule)

    def get_rules_in_dictionary(self):
        """ Generate dictionary object from all rules and return for use
        in the exportJSON  method of the Jaturing main class
        """
        dict = {}
        for character, rule in self._rules.items():
            dict[character] = {"next_state": rule.next_state,
                               "direction": rule.direction,
                               "write_char": rule.write_char}
        return dict
         
        
    @property
    def rules(self):
        return self._rules
