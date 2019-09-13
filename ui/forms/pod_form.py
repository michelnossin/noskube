
from ui.events.context_event_handler import ContextEventHandler
from ui.events.cluster_event_handler import ClusterEventHandler
from ui.events.mainmenu_event_handler import MainMenuEventHandler
from ui.events.podmenu_event_handler import PodMenuEventHandler
from ui.events.servicemenu_event_handler import ServiceMenuEventHandler

from ui.forms.noskube_form import NosKubeForm

from ui.forms.items.pod_selector import PodSelector
from ui.events.pod_event_handler import PodEventHandler

import constants as c


class PodForm(NosKubeForm):

    def configure_event_handler(self, kubernetes_api):
        event_handlers = [{"e": "change_pod", "h": PodEventHandler}
                          ]
        super().configure_event_handler(kubernetes_api, event_handlers)

    def add_form_page(self):
        self.pod_selector = self.add(PodSelector,
                                     max_height=c.Y_MAX_SELECTOR,
                                     value=[self.current_pod_id, ],
                                     name="Pod",
                                     values=["michel", "nossin"],
                                     scroll_exit=True)

    def create(self):
        self.configure_event_handler(self.parentApp.kubernetes_api)

        self.current_pod_id = 0
        self.current_form_id = 'POD CONTROL'

        super().create()
