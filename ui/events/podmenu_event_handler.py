from ui.events.event_handler import EventHandler


class PodMenuEventHandler(EventHandler):
    def proces_event(self, event):
        self.caller.update_status_box("Welcome to Pod Menu Sir!!")
        self.caller.current_form_id = 'POD CONTROL'
        self.caller.refresh_menu()
