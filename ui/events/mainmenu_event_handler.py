from ui.events.event_handler import EventHandler


class MainMenuEventHandler(EventHandler):
    def proces_event(self, event):
        self.caller.update_status_box("Welcome to MAIN Menu Sir!!")
        self.caller.current_form_id = 'MAIN CONFIGURATION'
        self.caller.refresh_menu()
