from ui.events.event_handler import EventHandler


class ServiceMenuEventHandler(EventHandler):
    def proces_event(self, event):
        self.caller.update_status_box("Welcome to Service Menu Sir!!")
        self.caller.current_form_id = 'SERVICE HUB'
        self.caller.refresh_menu()
