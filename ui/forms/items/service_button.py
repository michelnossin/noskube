import npyscreen


class ServiceButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.queue_event(npyscreen.Event("service_menu"))
