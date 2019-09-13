from ui.events.event_handler import EventHandler


class PodEventHandler(EventHandler):
    def proces_event(self, event):
        self.caller.update_status_box("Changing a POD?")
