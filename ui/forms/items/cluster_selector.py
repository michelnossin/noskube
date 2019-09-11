import npyscreen


class ClusterSelector(npyscreen.TitleSelectOne):
    def when_value_edited(self):
        self.parent.parentApp.queue_event(npyscreen.Event("change_cluster"))
