from ui.events.context_event_handler import ContextEventHandler
from ui.events.cluster_event_handler import ClusterEventHandler

from ui.forms.noskube_form import NosKubeForm

from ui.forms.items.context_selector import ContextSelector
from ui.forms.items.cluster_selector import ClusterSelector
from ui.forms.items.namespace_selector import NamespaceSelector

import constants as c


class MainForm(NosKubeForm):

    def configure_event_handler(self, kubernetes_api):
        event_handlers = [{"e": "change_context", "h": ContextEventHandler},
                          {"e": "change_cluster", "h": ClusterEventHandler}
                          ]
        super().configure_event_handler(kubernetes_api,
                                        event_handlers,
                                        handle_menu=True)

    def add_form_page(self):
        self.context_selector = self.add(ContextSelector,
                                         max_height=c.Y_MAX_SELECTOR,
                                         value=[self.current_context_id, ],
                                         name="Context",
                                         values=self.all_contexts,
                                         scroll_exit=True)

        self.cluster_selector = self.add(ClusterSelector,
                                         max_height=c.Y_MAX_SELECTOR,
                                         value=[self.current_cluster_id, ],
                                         name="Cluster",
                                         values=self.all_clusters,
                                         scroll_exit=True)

        self.namespace_selector = self.add(NamespaceSelector,
                                           max_height=c.Y_MAX_SELECTOR,
                                           value=[self.current_namespace_id, ],
                                           name="Namespace",
                                           values=self.all_namespaces,
                                           scroll_exit=True)

    def create(self):
        self.configure_event_handler(self.parentApp.kubernetes_api)

        self.current_namespace_id = 0
        self.current_form_id = 'MAIN CONFIGURATION'

        super().create()

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

    def update_namespace_selector(self,
                                  all_namespaces,
                                  current_namespace,
                                  current_namespace_id):
        self.all_namespaces = all_namespaces
        self.current_namespace = current_namespace
        self.current_namespace_id = current_namespace_id

        self.namespace_selector.values = self.all_namespaces
        self.namespace_selector.value = [self.current_namespace_id]

        self.namespace_selector.display()
