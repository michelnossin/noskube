import npyscreen

from ui.events.context_event_handler import ContextEventHandler
from ui.events.cluster_event_handler import ClusterEventHandler
from ui.events.mainmenu_event_handler import MainMenuEventHandler
from ui.events.podmenu_event_handler import PodMenuEventHandler
from ui.events.servicemenu_event_handler import ServiceMenuEventHandler

from ui.forms.items.context_selector import ContextSelector
from ui.forms.items.cluster_selector import ClusterSelector
from ui.forms.items.namespace_selector import NamespaceSelector
from ui.forms.items.main_button import MainButton
from ui.forms.items.pod_button import PodButton
from ui.forms.items.service_button import ServiceButton
from ui.forms.items.status_box import StatusBox

import constants as c


class MainForm(npyscreen.SplitForm):

    def configure_event_handler(self, kubernetes_api):
        event_handlers = [{"e": "change_context", "h": ContextEventHandler},
                          {"e": "change_cluster", "h": ClusterEventHandler},
                          {"e": "main_menu", "h": MainMenuEventHandler},
                          {"e": "pod_menu", "h": PodMenuEventHandler},
                          {"e": "service_menu", "h": ServiceMenuEventHandler}
                          ]

        for event_handler in event_handlers:
                self.add_event_hander(event_handler["e"],
                                      event_handler["h"](self,
                                                         event_handler["e"],
                                                         kubernetes_api)
                                      .proces_event)

    def read_kubernetes_data(self):
        kubernetes_api = self.parentApp.kubernetes_api

        self.current_context, self.current_context_id = (
            kubernetes_api.current_context)
        self.all_contexts = kubernetes_api.all_contexts
        self.current_cluster, self.current_cluster_id = (
            kubernetes_api.current_cluster)
        self.all_clusters = kubernetes_api.all_clusters
        self.all_pods = kubernetes_api.all_pods
        self.all_deployments = kubernetes_api.all_deployments
        self.all_namespaces = kubernetes_api.all_namespaces

    def add_horizontal_menu(self):
        def get_menu_color(button_name):
            if self.current_form_id == button_name:
                return 'VERYGOOD'
            else:
                return 'CAUTIONHL'

        x = self.nextrelx
        y = self.nextrely = self.nextrely + 2

        buttons = [{"name": "MAIN CONFIGURATION", "btn": MainButton},
                   {"name": "POD CONTROL", "btn": PodButton},
                   {"name": "SERVICE HUB", "btn": ServiceButton}]

        for button in buttons:
            bt = self.add(button["btn"],
                          name=button["name"],
                          color=get_menu_color(button["name"]))
            self.nextrely = y
            self.nextrelx = self.nextrelx + bt.width

        self.nextrelx = x
        self.nextrely = self.nextrely + 2

    def add_form_components(self):
        y, x = self.useable_space()

        self.add_horizontal_menu()

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

        self.nextrely = c.Y_POS_HALF_WAY
        self.status_box = self.add(StatusBox,
                                   max_height=c.Y_MAX_STATUSBOX,
                                   footer="By Michel Nossin",
                                   editable=False,
                                   name="NosKube output",
                                   value="""
        Use TAB and SHIFT-TAB to browse components.
        Use Cursor keys to move inside a component.
        Press ENTER to select an item""")

    def create(self):
        self.current_namespace_id = 0
        self.current_form_id = 'MAIN CONFIGURATION'

        self.configure_event_handler(self.parentApp.kubernetes_api)

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

    def update_status_box(self, value):
        self.status_box.value = value
        self.status_box.display()

    def exit_func(self, _input):
        exit(0)
