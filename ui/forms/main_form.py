import npyscreen

from ui.events.context_event_handler import ContextEventHandler
from ui.events.cluster_event_handler import ClusterEventHandler

from ui.forms.items.context_selector import ContextSelector
from ui.forms.items.cluster_selector import ClusterSelector
from ui.forms.items.status_box import StatusBox

class MainForm(npyscreen.FormBaseNew):

    def configure_event_handler(self, event, kubernetes_api):
            if event == "change_context":
                self.add_event_hander(event,
                                      ContextEventHandler(self,
                                                          event,
                                                          kubernetes_api)
                                      .proces_event)
                return
            if event == "change_cluster":
                self.add_event_hander(event,
                                      ClusterEventHandler(self,
                                                          event,
                                                          kubernetes_api)
                                      .proces_event)
                return

            raise NotImplementedError("""
            An invalid event type was being configured: 
            """ + event)

    def read_kubernetes_data(self):
        kubernetes_api = self.parentApp.kubernetes_api

        self.current_context, self.current_context_id = (
            kubernetes_api.current_context)
        self.all_contexts = kubernetes_api.all_contexts

        self.current_cluster, self.current_cluster_id = (
            kubernetes_api.current_cluster)
        self.all_clusters = kubernetes_api.all_clusters

    def add_form_components(self):
        y, x = self.useable_space()

        self.context_selector = self.add(ContextSelector,
                                         max_height=8,
                                         value=[self.current_context_id, ],
                                         name="Context",
                                         values=self.all_contexts,
                                         scroll_exit=True)

        self.cluster_selector = self.add(ClusterSelector,
                                         max_height=8,
                                         value=[self.current_cluster_id, ],
                                         name="Cluster",
                                         values=self.all_clusters,
                                         scroll_exit=True)

        self.status_box = self.add(StatusBox,
                                   footer="No editable",
                                   editable=False)

    def create(self):

        events = ["change_context", "change_cluster"]
        for event in events:
            self.configure_event_handler(event, self.parentApp.kubernetes_api)

        self.read_kubernetes_data()
        self.add_form_components()

    def update_cluster_selector(self,
                                all_clusters,
                                current_cluster,
                                current_cluster_id):
        self.all_clusters = all_clusters
        self.current_cluster = current_cluster
        self.current_cluster_id = current_cluster_id

        self.cluster_selector.values = self.all_clusters
        self.cluster_selector.value = [self.current_cluster_id]

        self.cluster_selector.display()

    def update_status_box(self, value):
        self.status_box.value = value
        self.status_box.display()

    def exit_func(self, _input):
        exit(0)
