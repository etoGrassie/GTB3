import GTB3UI, GTB3Applications, GTB3Core


class Initialize:
    def __init__(self):
        self.setup_signals_slots()

    def setup_signals_slots(self):
        GTB3UI.MainWindow.signal_event_open_file.connect(GTB3Applications.Application.event_open_file)
        GTB3Applications.Application.signal_update_file_path(GTB3UI.MainWindow.set_window_file_path)