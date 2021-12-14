from ui.jaturing_app import JaturingApp


def launch(machine):
    """Start the GUI application

    Args:
         machine : Jaturing Turing's machine
    """
    app = JaturingApp(machine)
    app.mainloop()

