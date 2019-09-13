import npyscreen


class MainButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.queue_event(npyscreen.Event("main_menu"))
