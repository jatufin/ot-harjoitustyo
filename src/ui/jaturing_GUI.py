from ui.jaturing_app import JaturingApp


def launch(machine):
    machine.add_state("q0")
    machine.set_rule(state_name="q0", character="a", write_char="B", direction="RIGHT", next_state="q1")
    #machine.print_states_and_rules()
    
    app = JaturingApp(machine)
    app.mainloop()

