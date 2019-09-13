from ui.events.event_handler import EventHandler


class MainMenuEventHandler(EventHandler):
    def proces_event(self, event):
        self.caller.update_status_box("Welcome to MAIN Menu Sir!!")
