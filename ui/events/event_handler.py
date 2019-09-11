import abc

class EventHandler():
    def __init__(self, caller, event, kubernetes_api):
        self.event = event
        self.kubernetes_api = kubernetes_api
        self.caller = caller

    @abc.abstractmethod
    def proces_event(self, event):
        raise NotImplementedError("""
        users must define proces_event to use this base class
        """)
