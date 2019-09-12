import npyscreen


class ContextSelector(npyscreen.TitleSelectOne):
    def when_value_edited(self):
        self.parent.parentApp.queue_event(npyscreen.Event("change_context"))
