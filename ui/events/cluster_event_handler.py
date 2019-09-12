from ui.events.event_handler import EventHandler


class ClusterEventHandler(EventHandler):
    def proces_event(self, event):
        self.caller.update_status_box("Thinking about changing clusters Sir?")
