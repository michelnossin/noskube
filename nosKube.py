import npyscreen

from kubernetes.kubernetes_api_factory import KubernetesApiFactory
from kubernetes.kubernetes_api import KubernetesApi

from ui.events.event_handler import EventHandler
from ui.events.context_event_handler import ContextEventHandler
from ui.events.cluster_event_handler import ClusterEventHandler

from ui.forms.main_form import MainForm
from ui.forms.items.status_box import StatusBox
from ui.forms.items.context_selector import ContextSelector
from ui.forms.items.cluster_selector import ClusterSelector

class App(npyscreen.StandardApp):
    def __init__(self, kubernetes_api):
        super().__init__()
        self.kubernetes_api = kubernetes_api

    def update_kubernetes_api(self, kubernetes_api):
        self.kubernetes_api = kubernetes_api

    def onStart(self):
        self.addForm("MAIN", MainForm, name="NosKube Professional Edition")


if __name__ == "__main__":
    kubernetes_api = KubernetesApiFactory().build_kubernetes_api()
    MyApp = App(kubernetes_api)
    MyApp.run()
