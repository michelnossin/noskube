import npyscreen


class PodButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.queue_event(npyscreen.Event("pod_menu"))
